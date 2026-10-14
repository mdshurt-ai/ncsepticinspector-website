#!/usr/bin/env node
/*
  NC Septic Inspector site generator (Node port of the Inspect-All build.ps1).
  Run from anywhere:   node .claude/build.js
  Reads:  .claude/site.json (business facts, towns, page order)
          .claude/reviews.json (Google rating numbers + featured reviews)
          .claude/photos.json (septic gallery)
          .claude/pages-src/<name>.main.html + <name>.meta.json (one pair per content page)
          _template.html, _home.html, _icons.html, _404.html, _thanks.html, _schedule.html
  Writes: index.html, <path>/index.html for every page, schedule/, 404.html, thanks.html, sitemap.xml, robots.txt
  Exits non-zero and prints a PROBLEMS list if anything is off: unfilled {{TOKENS}}, missing images, bad JSON-LD,
  broken internal links, wrong rating-badge count, banned wording (wrong septic number, "licensed septic", prices,
  referral-perk wording on the agents page).
*/
"use strict";
const fs = require("fs");
const path = require("path");

const root = path.resolve(__dirname, "..");
const read = (p) => fs.readFileSync(path.join(root, p), "utf8");
const exists = (p) => fs.existsSync(path.join(root, p));
const write = (p, s) => { fs.mkdirSync(path.dirname(path.join(root, p)), { recursive: true }); fs.writeFileSync(path.join(root, p), s, "utf8"); };
const esc = (s) => String(s).replace(/&(?!(amp|lt|gt|quot|#\d+);)/g, "&amp;").replace(/"/g, "&quot;").replace(/</g, "&lt;").replace(/>/g, "&gt;");

const site = JSON.parse(read(".claude/site.json"));
const reviews = JSON.parse(read(".claude/reviews.json"));
const photos = JSON.parse(read(".claude/photos.json")).photos;
const problems = [];

// ---- shared pieces -------------------------------------------------------
const icons = read("_icons.html").trim();
const contact = read("_contact.html");

const business = {
  "@context": "https://schema.org",
  "@type": "HomeAndConstructionBusiness",
  "@id": site.site + "/#business",
  "name": site.brand,
  "alternateName": site.legal_name,
  "legalName": site.legal_name,
  "url": site.site + "/",
  "logo": site.site + "/images/logo.svg",
  "image": site.site + "/images/drainfield-marked.jpg",
  "telephone": "+1-" + site.phone,
  "email": site.email,
  "founder": { "@type": "Person", "name": site.person },
  "address": { "@type": "PostalAddress", "addressLocality": "Morganton", "addressRegion": "NC", "addressCountry": "US" },
  "areaServed": site.towns.map((t) => ({ "@type": "City", "name": t.name + ", NC" })),
  "sameAs": [site.sister_site + "/", site.google_profile],
  "description": "Independent septic system inspections for home buyers, sellers, owners and real estate agents in the foothills and mountains of Western North Carolina, by an NC On-Site Wastewater Inspector who does not pump or repair systems."
};
const businessJson = JSON.stringify(business, null, 2);

const areaLinks = site.towns.map((t) => `          <li><a href="/septic-inspection-${t.slug}/">${t.name}</a></li>`).join("\n");

const gRating = Number(reviews.google_rating).toFixed(1);
const gCount = String(parseInt(reviews.google_review_count, 10));
const gUrl = reviews.google_reviews_url;
const star = '<svg aria-hidden="true" focusable="false"><use href="#i-star"/></svg>';
const ratingBadge = '<div class="g-rating"><a href="' + gUrl + '" target="_blank" rel="noopener">' +
  '<span class="g-rating-mark" aria-hidden="true"><svg focusable="false"><use href="#s-google"/></svg></span>' +
  '<span class="g-rating-stars" role="img" aria-label="Rated ' + gRating + ' out of 5 on Google from ' + gCount + ' reviews of Inspect-All Home Inspections">' + star.repeat(5) + '</span>' +
  '<span class="g-rating-text" aria-hidden="true"><b>' + gRating + '</b><span class="g-rating-dot">&middot;</span>' + gCount + ' Google reviews</span></a></div>';
if (gRating !== "5.0") problems.push("Google rating is " + gRating + ": the five full stars and the 'every one of them five stars' wording on the home page need changing");

const heroBtnsRx = /<section class="page-hero"(?:(?!<\/section>)[\s\S])*?<div class="btns">(?:(?!<\/div>)[\s\S])*<\/div>/;
function addHeroRating(html, where) {
  if (!heroBtnsRx.test(html)) { problems.push("no page-hero buttons for the Google rating badge on " + where); return html; }
  return html.replace(heroBtnsRx, (m) => m + "\n  " + ratingBadge);
}

const common = {
  SITE: site.site, PHONE: site.phone, TEL: site.tel, EMAIL: site.email, PERSON: site.person, CITY: site.city,
  SISTER_SITE: site.sister_site, SPECTORA_SAMPLE: site.spectora_sample_report, SPECTORA_SCHEDULE: site.spectora_schedule,
  GOOGLE_REVIEWS_URL: gUrl, GOOGLE_RATING: gRating, GOOGLE_REVIEW_COUNT: gCount, GOOGLE_RATING_BADGE: ratingBadge,
  BUSINESS_JSON: businessJson, AREA_LINKS: areaLinks, ICONS: icons, CONTACT: contact,
  REVIEWS_JSON: JSON.stringify(reviews.featured.map((r) => [r.name, r.text])),
  PHOTOS_JSON: JSON.stringify(photos.map((p) => [p.file, p.caption, p.alt]))
};
function fill(html, vars) {
  const all = Object.assign({}, common, vars);
  let out = html, passes = 0;
  while (/\{\{[A-Z_]+\}\}/.test(out) && passes++ < 4) out = out.replace(/\{\{([A-Z_]+)\}\}/g, (m, k) => (k in all ? all[k] : m));
  return out;
}

const tpl = read("_template.html");
function render(meta, main) {
  return fill(tpl, {
    TITLE: esc(meta.title), DESCRIPTION: esc(meta.description), PATH: meta.path, OG_IMAGE: meta.og_image,
    SCHEMA_JSON: typeof meta.schema === "string" ? meta.schema : JSON.stringify(meta.schema, null, 2), MAIN: main
  });
}

// ---- content pages -------------------------------------------------------
const paths = ["/"];
const builtPages = [];
for (const name of site.pages) {
  const mainFile = `.claude/pages-src/${name}.main.html`, metaFile = `.claude/pages-src/${name}.meta.json`;
  if (!exists(mainFile) || !exists(metaFile)) { problems.push("missing source for page " + name); continue; }
  let main = read(mainFile);
  const meta = JSON.parse(read(metaFile));
  if (typeof meta.schema === "string") { try { JSON.parse(meta.schema); } catch (e) { problems.push("bad JSON-LD on " + meta.path); } }
  if (meta.title.length > 65) problems.push(`title is ${meta.title.length} chars on ${meta.path} (keep under 65)`);
  if (meta.description.length > 165) problems.push(`description is ${meta.description.length} chars on ${meta.path} (keep under 165)`);
  if (!exists(`images/${meta.og_image}.jpg`)) problems.push(`og image ${meta.og_image} missing on ${meta.path}`);
  main = addHeroRating(main, meta.path);
  let html = render(meta, main);
  if (meta.path === "/schedule/") {
    html = html.replace('<h2 id="contact-title">Schedule a septic inspection</h2>', '<h2 id="contact-title">Prefer to send a request?</h2>');
    const lead = "Book online in a couple of minutes, call or text for the fastest response, or send a request and I'll get back to you with availability.";
    if (!html.includes(lead)) problems.push("contact lead not found on /schedule/");
    html = html.replace(lead, "Send a request and I'll get back to you with availability, or call or text for the fastest response.");
    html = html.replace(/\s*<a href="\/schedule\/" class="btn btn-primary">Book Online<\/a>/, "");
  }
  write(meta.path.replace(/^\//, "") + "index.html", html);
  paths.push(meta.path);
  builtPages.push({ path: meta.path, file: meta.path.replace(/^\//, "") + "index.html" });
}

// ---- home ----------------------------------------------------------------
write("index.html", fill(read("_home.html"), { PATH: "/" }));
builtPages.push({ path: "/", file: "index.html" });

// ---- 404 + thanks --------------------------------------------------------
{
  const main404 = addHeroRating(read("_404.html"), "/404.html");
  let h = render({ title: "Page Not Found | NC Septic Inspector", description: "The page you were looking for could not be found.", path: "/404.html", og_image: "drainfield-marked",
    schema: '{"@context":"https://schema.org","@type":"WebPage","name":"Page not found"}' }, main404);
  h = h.replace('<meta name="viewport"', '<meta name="robots" content="noindex"><meta name="viewport"');
  write("404.html", h);
  builtPages.push({ path: "/404.html", file: "404.html", badges: 3 });
  write("thanks.html", fill(read("_thanks.html"), { PATH: "/thanks.html" }));
}

// ---- sitemap + robots ----------------------------------------------------
{
  let sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n';
  for (const u of paths) sm += `  <url><loc>${site.site}${u}</loc><lastmod>${site.sitemap_lastmod}</lastmod></url>\n`;
  sm += "</urlset>\n";
  write("sitemap.xml", sm);
  write("robots.txt", `User-agent: *\nAllow: /\nDisallow: /thanks.html\n\nSitemap: ${site.site}/sitemap.xml\n`);
}

// ---- checks --------------------------------------------------------------
const bannedEverywhere = [
  [/60071/, "wrong septic number 60071 (it is 6007I)"],
  [/licensed septic|septic license|licensed on-site wastewater|wastewater contractor(?!s and inspectors)/i, "septic credential wording (never 'licensed' or 'contractor')"],
  [/\$\s?\d/, "a price"],
  [/preferred (inspector|provider|vendor|partner)|recommended inspector/i, "referral-list wording (11 NCAC 08 .1116(e))"]
];
const bannedAgents = /(?:\bfree\b|gift|discount|perk|reward|kickback|exclusive|\bvip\b|priority scheduling)/i;
for (const p of builtPages) {
  const t = read(p.file);
  const m = t.match(/\{\{[A-Z_]+\}\}/);
  if (m) problems.push(`unfilled ${m[0]} on ${p.path}`);
  const words = t.replace(/<script[\s\S]*?<\/script>|<!--[\s\S]*?-->/g, "");
  for (const [rx, why] of bannedEverywhere) { const mm = words.match(rx); if (mm) problems.push(`${why} on ${p.path}: '${mm[0]}'`); }
  if (p.path === "/for-agents/") { const mm = words.match(bannedAgents); if (mm) problems.push(`wording to avoid on /for-agents/: '${mm[0]}'`); }
  const badges = (t.match(/class="g-rating"/g) || []).length;
  const want = 3; // hero or page-hero + contact + footer
  if (badges !== want) problems.push(`Google rating badge appears ${badges} times on ${p.path} (expected ${want})`);
  // internal links and images
  const refs = [...words.matchAll(/(?:href|src)="(\/[^"#?]*)/g)].map((x) => x[1]);
  for (const r of new Set(refs)) {
    const f = r.endsWith("/") ? r + "index.html" : r;
    if (!exists(f.replace(/^\//, ""))) problems.push(`broken internal link ${r} on ${p.path}`);
  }
  for (const r of new Set([...words.matchAll(/\/images\/(?:thumbs\/)?([a-z0-9-]+)\.jpg/g)].map((x) => x[1]))) {
    if (!exists(`images/${r}.jpg`) || !exists(`images/thumbs/${r}.jpg`)) problems.push(`missing image (full or thumb) ${r} on ${p.path}`);
  }
}
if (problems.length) { console.error("PROBLEMS:\n - " + problems.join("\n - ")); process.exit(1); }
console.log(`built ${paths.length} pages + 404 + thanks + sitemap + robots, no problems`);
