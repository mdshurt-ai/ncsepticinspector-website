(function () {
  "use strict";

  // Mobile menu ---------------------------------------------------
  var btn = document.querySelector(".menu-btn"),
      menu = document.querySelector(".nav-links") || document.querySelector(".nav ul");
  function setMenu(open) {
    menu.classList.toggle("open", open);
    btn.setAttribute("aria-expanded", open ? "true" : "false");
    btn.setAttribute("aria-label", open ? "Close menu" : "Menu");
  }
  if (btn && menu) {
    // onclick (not addEventListener) so a page that still carries its own
    // inline menu handler ends up with exactly one toggle.
    btn.onclick = function () { setMenu(!menu.classList.contains("open")); };
    menu.addEventListener("click", function (e) { if (e.target.closest("a")) setMenu(false); });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && menu.classList.contains("open")) { setMenu(false); btn.focus(); }
    });
    document.addEventListener("click", function (e) {
      if (menu.classList.contains("open") && !e.target.closest("header")) setMenu(false);
    });
    window.addEventListener("resize", function () { if (window.innerWidth >= 1024 && menu.classList.contains("open")) setMenu(false); });
  }

  // Phone call / book bar: shows once the hero buttons scroll off the top,
  // hides only while the request form (which has its own submit button) is on screen.
  var bar = document.getElementById("cta-bar"),
      heroActions = document.querySelector(".hero-actions, .page-hero .btns, .hero .btns"),
      contactSec = document.querySelector("#contact form");
  if (bar && heroActions && contactSec && "IntersectionObserver" in window) {
    var heroGone = false, contactSeen = false;
    var updateBar = function () {
      var on = heroGone && !contactSeen;
      bar.classList.toggle("show", on);
      document.body.classList.toggle("bar-on", on);
    };
    new IntersectionObserver(function (entries) {
      var en = entries[0];
      heroGone = !en.isIntersecting && en.boundingClientRect.top < 0;
      updateBar();
    }, { threshold: 0 }).observe(heroActions);
    new IntersectionObserver(function (entries) {
      contactSeen = entries[0].isIntersecting;
      updateBar();
    }, { threshold: 0 }).observe(contactSec);
  }

  // Social links not set yet: keep "#" placeholders from jumping to the top
  document.querySelectorAll('a[data-social][href="#"]').forEach(function (a) {
    a.addEventListener("click", function (e) { e.preventDefault(); });
  });

  // Footer year
  var yr = document.getElementById("yr");
  if (yr) yr.textContent = new Date().getFullYear();
})();
