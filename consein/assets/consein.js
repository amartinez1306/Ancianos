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
    });
  });
})();
