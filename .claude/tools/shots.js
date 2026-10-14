const { chromium } = require("playwright-core");
const SP = process.env.SP; const base = "http://localhost:8765";
(async () => {
  const browser = await chromium.launch({ executablePath: "/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell", args: ["--no-sandbox"] });
  const jobs = [
    ["home-mobile", "/", { width: 390, height: 844, isMobile: true, deviceScaleFactor: 2 }],
    ["septic-mobile", "/septic-inspection/", { width: 390, height: 844, isMobile: true, deviceScaleFactor: 2 }],
    ["morganton-mobile", "/septic-inspection-morganton-nc/", { width: 390, height: 844, isMobile: true, deviceScaleFactor: 2 }],
    ["septic-desktop", "/septic-inspection/", { width: 1366, height: 900 }],
    ["agents-desktop", "/for-agents/", { width: 1366, height: 900 }],
    ["records-desktop", "/septic-records/", { width: 1366, height: 900 }],
  ];
  for (const [name, path, vp] of jobs) {
    const ctx = await browser.newContext({ viewport: { width: vp.width, height: vp.height }, isMobile: !!vp.isMobile, deviceScaleFactor: vp.deviceScaleFactor || 1, hasTouch: !!vp.isMobile });
    const page = await ctx.newPage();
    await page.goto(base + path, { waitUntil: "networkidle" });
    const sw = await page.evaluate(() => [document.documentElement.scrollWidth, document.documentElement.clientWidth]);
    console.log(name, "scrollWidth/clientWidth", sw.join("/"));
    await page.screenshot({ path: `${SP}/shots/${name}.png`, fullPage: true });
    await ctx.close();
  }
  await browser.close();
})();
