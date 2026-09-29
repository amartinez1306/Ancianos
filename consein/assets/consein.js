/* Consein · Dirección de Innovación y Servicios Digitales
   Interacciones compartidas: menú móvil, sub-navegación activa,
   animaciones de entrada y formularios de muestra. */
(function () {
  "use strict";

  // ---- Menú móvil ----
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.querySelector(".main-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", String(open));
    });
  }

  // ---- Desplegables (clic / teclado; en escritorio también hover por CSS) ----
  document.querySelectorAll(".main-nav__item > button").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var item = btn.parentElement;
      var open = item.classList.toggle("is-open");
      btn.setAttribute("aria-expanded", String(open));
    });
  });
  document.addEventListener("keydown", function (e) {
    if (e.key !== "Escape") return;
    document.querySelectorAll(".main-nav__item.is-open").forEach(function (item) {
      item.classList.remove("is-open");
      item.querySelector("button").setAttribute("aria-expanded", "false");
    });
  });

  // ---- Sub-navegación: resalta la sección visible ----
  var subLinks = document.querySelectorAll(".subnav__link");
  if (subLinks.length && "IntersectionObserver" in window) {
    var byId = {};
    subLinks.forEach(function (a) { byId[a.getAttribute("href").slice(1)] = a; });
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        subLinks.forEach(function (a) { a.classList.remove("is-active"); a.removeAttribute("aria-current"); });
        var link = byId[entry.target.id];
        if (link) { link.classList.add("is-active"); link.setAttribute("aria-current", "true"); }
      });
    }, { rootMargin: "-45% 0px -50% 0px" });
    Object.keys(byId).forEach(function (id) {
      var el = document.getElementById(id);
      if (el) spy.observe(el);
    });
  }

  // ---- Animaciones de entrada ----
  var reveals = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) { entry.target.classList.add("is-visible"); io.unobserve(entry.target); }
      });
    }, { threshold: 0.12 });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add("is-visible"); });
  }

  // ---- Subpantallas de servicio ("Ver servicio") ----
  // Se abren al hacer clic en cualquier enlace con data-service="<id>" o al
  // entrar con #<id> en la URL (p. ej. innovacion-y-servicios-digitales.html#csc-03).
  // CONSEIN_BASE permite usar las fichas desde páginas fuera de /servicios (p. ej. el índice).
  var BASE = window.CONSEIN_BASE || "";
  var SERVICIOS = window.CONSEIN_SERVICIOS || [];
  var byService = {};
  SERVICIOS.forEach(function (s) { byService[s.id] = s; });

  function esc(t) {
    return String(t).replace(/[&<>"]/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c];
    });
  }

  var dialog = null;
  var lastTrigger = null;

  function row(label, value, cls) {
    return '<tr class="' + (cls || "") + '"><th scope="row">' + label + "</th><td>" + value + "</td></tr>";
  }

  function renderService(s) {
    var incluye = "<ul>" + s.incluye.map(function (i) { return "<li>" + esc(i) + "</li>"; }).join("") + "</ul>";
    return (
      '<header class="svc__head">' +
        '<p class="svc__code">' + esc(s.codigo) + (s.etiqueta ? ' <span class="svc__tag">' + esc(s.etiqueta) + "</span>" : "") + "</p>" +
        '<h2 class="svc__title" id="svc-title">' + esc(s.titulo) + "</h2>" +
        '<p class="svc__format">' + esc(s.formato) + "</p>" +
        '<button class="svc__close" type="button" data-close aria-label="Cerrar">&times;</button>' +
      "</header>" +
      '<div class="svc__body"><table class="svc__table"><tbody>' +
        row("En una frase", "<strong><em>" + esc(s.frase) + "</em></strong>", "svc__row--lead") +
        row("Ideal para", esc(s.ideal)) +
        row("Qué resuelve", esc(s.resuelve)) +
        row("Incluye", incluye) +
        row("Aporte Cisco", esc(s.cisco), "svc__row--cisco") +
        row("Núcleo Microsoft", esc(s.microsoft), "svc__row--ms") +
        row("Resultado", "<strong>" + esc(s.resultado) + "</strong>") +
        row("Prueba", "<em>" + esc(s.prueba) + "</em>", "svc__row--proof") +
      "</tbody></table></div>" +
      '<footer class="svc__foot">' +
        (s.pagina ? '<a class="svc__more" href="' + esc(BASE + s.pagina) + '">Ver página completa del servicio</a>' : "<span></span>") +
        '<a class="svc__cta" href="#contacto" data-cta="' + esc(s.id) + '">' + esc(s.cta) + "</a>" +
      "</footer>"
    );
  }

  function openService(id, trigger) {
    var s = byService[id];
    if (!s) return false;
    if (!dialog) {
      dialog = document.createElement("dialog");
      dialog.className = "svc";
      dialog.setAttribute("aria-labelledby", "svc-title");
      document.body.appendChild(dialog);
      dialog.addEventListener("click", function (e) {
        if (e.target === dialog || e.target.closest("[data-close]")) closeService();
        var cta = e.target.closest("[data-cta]");
        if (cta) {
          var form = document.querySelector("#contacto form");
          lastTrigger = null;
          if (!form) { cta.setAttribute("href", BASE + "innovacion-y-servicios-digitales.html#contacto"); closeService(); return; }
          e.preventDefault();
          closeService();
          var svc = byService[cta.dataset.cta];
          var hidden = form.querySelector('input[name="servicio"]');
          if (hidden) hidden.value = svc.titulo;
          var note = form.querySelector(".form-service");
          if (note) { note.hidden = false; note.textContent = "Servicio seleccionado: " + svc.titulo; }
          document.getElementById("contacto").scrollIntoView();
          var first = form.querySelector("input:not([type=hidden])");
          if (first) first.focus({ preventScroll: true });
        }
      });
      dialog.addEventListener("close", function () {
        if (/^#(csc-|nortia)/.test(location.hash)) history.replaceState(null, "", location.pathname + location.search);
        if (lastTrigger) lastTrigger.focus();
      });
    }
    dialog.innerHTML = renderService(s);
    lastTrigger = trigger || null;
    if (dialog.showModal) { if (!dialog.open) dialog.showModal(); } else { dialog.setAttribute("open", ""); }
    if (location.hash !== "#" + id) history.replaceState(null, "", "#" + id);
    dialog.querySelector(".svc__body").scrollTop = 0;
    return true;
  }

  function closeService() {
    if (!dialog) return;
    if (dialog.close) dialog.close(); else dialog.removeAttribute("open");
  }

  document.addEventListener("click", function (e) {
    var link = e.target.closest("[data-service]");
    if (!link) return;
    if (openService(link.dataset.service, link)) e.preventDefault();
  });
  function fromHash() {
    var id = location.hash.slice(1);
    if (byService[id]) openService(id);
  }
  window.addEventListener("hashchange", fromHash);
  fromHash();

  // ---- Formularios (modelo: sin backend conectado) ----
  // Para producción, sustituir el bloque "demo" por el envío al CRM / endpoint de Consein.
  document.querySelectorAll("form[data-demo-form]").forEach(function (form) {
    var status = form.querySelector(".form-status");
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var firstInvalid = null;
      form.querySelectorAll("[required]").forEach(function (field) {
        var ok = field.checkValidity();
        field.setAttribute("aria-invalid", ok ? "false" : "true");
        if (!ok && !firstInvalid) firstInvalid = field;
      });
      if (firstInvalid) {
        status.dataset.state = "error";
        status.textContent = "Revisa los campos marcados: son obligatorios y el correo debe ser válido.";
        firstInvalid.focus();
        return;
      }
      status.dataset.state = "ok";
      status.textContent = "¡Gracias! Un especialista de la Dirección te contactará muy pronto.";
      form.reset();
      var note = form.querySelector(".form-service");
      if (note) note.hidden = true;
    });
  });
})();
