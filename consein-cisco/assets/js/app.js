/* Consein · Soluciones Cisco · comportamiento del sitio */
(function () {
  "use strict";

  // Menú móvil
  var toggle = document.querySelector(".menu-toggle");
  var nav = document.getElementById("nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", String(open));
    });
  }

  // Submenús Soluciones y Productos
  var menus = document.querySelectorAll(".has-menu");
  var hoverable = window.matchMedia("(hover:hover) and (min-width:1001px)");
  function closeAll(except) {
    menus.forEach(function (m) {
      if (m !== except) {
        m.classList.remove("open");
        m.querySelector(".nav-link").setAttribute("aria-expanded", "false");
      }
    });
  }
  menus.forEach(function (m) {
    var btn = m.querySelector(".nav-link");
    btn.addEventListener("click", function (e) {
      e.preventDefault();
      // Con ratón el menú ya se abrió al pasar por encima: el clic lo mantiene abierto
      var open = hoverable.matches ? true : !m.classList.contains("open");
      closeAll(m);
      m.classList.toggle("open", open);
      btn.setAttribute("aria-expanded", String(open));
    });
    m.addEventListener("mouseenter", function () {
      if (hoverable.matches) { closeAll(m); m.classList.add("open"); btn.setAttribute("aria-expanded", "true"); }
    });
    m.addEventListener("mouseleave", function () {
      if (hoverable.matches) { m.classList.remove("open"); btn.setAttribute("aria-expanded", "false"); }
    });
  });
  document.addEventListener("click", function (e) {
    if (!e.target.closest(".has-menu")) closeAll();
    if (e.target.closest("#nav a") && nav) { closeAll(); nav.classList.remove("open"); }
  });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") closeAll(); });

  // Subpantalla "Seguir leyendo…"
  var dialog = document.getElementById("detalle");
  var dialogBody = dialog ? dialog.querySelector(".detail-body") : null;
  var lastHash = "";
  var single = document.body.hasAttribute("data-single");
  var currentPage = "inicio";

  function openDetail(id) {
    var src = document.getElementById("detalle-" + id);
    if (!src || !dialog) return false;
    dialogBody.innerHTML = src.innerHTML;
    if (!dialog.open) dialog.showModal();
    dialog.scrollTop = 0;
    return true;
  }
  function fromHash() {
    var id = decodeURIComponent(location.hash.slice(1));
    if (id && document.getElementById("detalle-" + id)) {
      lastHash = id;
      openDetail(id);
    }
  }
  if (dialog) {
    dialog.querySelector(".detail-close").addEventListener("click", function () { dialog.close(); });
    dialog.addEventListener("click", function (e) { if (e.target === dialog) dialog.close(); });
    dialog.addEventListener("close", function () {
      if (single) {
        if (lastHash) history.replaceState(null, "", "#" + currentPage);
      } else if (lastHash && location.hash.slice(1) === lastHash) {
        history.replaceState(null, "", location.pathname + location.search);
      }
      lastHash = "";
    });
    if (!single) {
      window.addEventListener("hashchange", fromHash);
      fromHash();
    }
  }

  // Versión de un solo archivo: navegación entre Inicio, Soluciones y Productos
  // Enlaces con la forma  #pagina  ·  #pagina:seccion  ·  #pagina:seccion?interes=CSC-01
  if (single) {
    var meta = JSON.parse(document.getElementById("paginas").textContent);
    var route = function () {
      var h = decodeURIComponent(location.hash.slice(1)), q = "", i = h.indexOf("?");
      if (i >= 0) { q = h.slice(i + 1); h = h.slice(0, i); }
      var parts = h.split(":"), page = parts[0] || "inicio", target = parts[1] || "";
      if (!meta[page]) return; // anclas internas, por ejemplo #contenido
      var changed = page !== currentPage;
      currentPage = page;
      document.querySelectorAll(".page").forEach(function (el) { el.hidden = el.getAttribute("data-page") !== page; });
      document.title = meta[page].title;
      document.querySelector('meta[name="description"]').setAttribute("content", meta[page].description);
      document.querySelectorAll("[data-nav]").forEach(function (a) {
        if (a.getAttribute("data-nav") === page) a.setAttribute("aria-current", "page");
        else a.removeAttribute("aria-current");
      });
      var interes = new URLSearchParams(q).get("interes");
      var sel = document.getElementById("f-interes");
      if (interes && sel) sel.value = interes;
      if (dialog && dialog.open) { lastHash = ""; dialog.close(); }
      var pageEl = document.querySelector('.page[data-page="' + page + '"]');
      var el = target ? pageEl.querySelector("#" + CSS.escape(target)) : null;
      if (el) el.scrollIntoView();
      else if (changed || !target) window.scrollTo(0, 0);
      if (target && document.getElementById("detalle-" + target)) { lastHash = target; openDetail(target); }
    };
    window.addEventListener("hashchange", route);
    route();
  }

  // Autodiagnóstico Programa Renueva
  var checks = document.querySelectorAll("#autodiagnostico input[type=checkbox]");
  if (checks.length) {
    var bar = document.getElementById("meter");
    var verdict = document.getElementById("verdict");
    checks.forEach(function (c) {
      c.addEventListener("change", function () {
        var n = Array.prototype.filter.call(checks, function (x) { return x.checked; }).length;
        bar.style.width = (n / checks.length * 100) + "%";
        verdict.textContent =
          n === 0 ? "Marque las señales que reconoce en su empresa." :
          n <= 2 ? "Le recomendamos inventariar su base instalada para planificar a tiempo." :
          n <= 4 ? "Su red ya limita su plataforma Microsoft. Le proponemos un inventario de obsolescencia." :
                   "Riesgo alto. Le proponemos iniciar el inventario de obsolescencia esta semana.";
      });
    });
  }

  // Formulario de contacto (maqueta): preselecciona la solución desde ?interes=CSC-01
  var form = document.getElementById("form-contacto");
  if (form) {
    var interes = new URLSearchParams(location.search).get("interes");
    var sel = document.getElementById("f-interes");
    if (interes && sel) sel.value = interes;
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      document.getElementById("form-ok").style.display = "block";
    });
  }

  var y = document.getElementById("year");
  if (y) y.textContent = new Date().getFullYear();
})();
