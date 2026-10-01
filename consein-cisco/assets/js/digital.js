/* Consein · Tema digital: animaciones de entrada y contadores */
(function () {
  "use strict";
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var art = document.querySelector(".hero-art svg");
  if (reduce && art && art.pauseAnimations) art.pauseAnimations();
  if (reduce || !("IntersectionObserver" in window)) return;

  document.documentElement.classList.add("js-anim");

  // Contadores para cifras enteras (15, 7, 71%, 342%…)
  function contar(el) {
    var m = el.textContent.trim().match(/^(\d+)(%?)$/);
    if (!m || el.dataset.contado) return;
    el.dataset.contado = "1";
    var fin = parseInt(m[1], 10), suf = m[2], t0 = null, dur = 1100;
    function paso(t) {
      if (!t0) t0 = t;
      var k = Math.min(1, (t - t0) / dur);
      el.textContent = Math.round(fin * (1 - Math.pow(1 - k, 3))) + suf;
      if (k < 1) requestAnimationFrame(paso);
    }
    requestAnimationFrame(paso);
  }

  var sel = ".section-head, .tile, .card, .stat, .steps li, .proof > div, .area-head, .integral, .check, .faq details, .table.routes tbody tr, .stack .layer, .figures > div";
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (!e.isIntersecting) return;
      var el = e.target;
      el.classList.add("in");
      io.unobserve(el);
      el.querySelectorAll(".figures b, b").forEach(function (b) {
        if (b.closest(".stat, .figures")) contar(b);
      });
      // Al terminar la entrada se retira la clase para que funcionen los efectos al pasar el ratón
      setTimeout(function () { el.classList.remove("reveal", "in"); el.style.transitionDelay = ""; }, 900);
    });
  }, { threshold: 0.12 });

  document.querySelectorAll(sel).forEach(function (el) {
    var hermanos = el.parentElement ? Array.prototype.indexOf.call(el.parentElement.children, el) : 0;
    el.classList.add("reveal");
    el.style.transitionDelay = Math.min(hermanos, 6) * 70 + "ms";
    io.observe(el);
  });
})();
