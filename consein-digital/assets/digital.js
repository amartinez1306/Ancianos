/* Consein · Servicios — Versión digital
   Interacciones: encabezado al hacer scroll, menú móvil, animaciones de entrada,
   fichas «Ver servicio» y formulario de contacto. */
(function () {
  "use strict";

  // ---- Encabezado: fondo sólido al hacer scroll ----
  var header = document.querySelector(".site-header");
  function onScroll() { header.classList.toggle("is-scrolled", window.scrollY > 24); }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  // ---- Menú móvil y desplegables ----
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.querySelector(".main-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", String(open));
    });
  }
  document.querySelectorAll(".main-nav__item > button").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var open = btn.parentElement.classList.toggle("is-open");
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

  // ---- Animaciones de entrada (incluye el panel de la PMO) ----
  var reveals = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-visible");
        io.unobserve(entry.target);
      });
    }, { threshold: 0.15 });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add("is-visible"); });
  }

  // ---- Fichas «Ver servicio» ----
  // Cada ficha es un <dialog class="svc" id="etapa-0X"> en el HTML (indexable).
  var lastTrigger = null;

  function getDialog(id) {
    var el = id && document.getElementById(id);
    return el && el.tagName === "DIALOG" ? el : null;
  }

  function openService(id, trigger) {
    var dialog = getDialog(id);
    if (!dialog || typeof dialog.showModal !== "function") return false;
    document.querySelectorAll("dialog.svc[open]").forEach(function (d) { d.close(); });
    lastTrigger = trigger || null;
    dialog.showModal();
    dialog.querySelector(".svc__body").scrollTop = 0;
    if (location.hash !== "#" + id) history.replaceState(null, "", "#" + id);
    return true;
  }

  function selectService(dialog) {
    var form = document.querySelector("#contacto form");
    if (!form) return;
    var name = dialog.querySelector("h2").textContent;
    var hidden = form.querySelector('input[name="servicio"]');
    if (hidden) hidden.value = name;
    var note = form.querySelector(".form-service");
    if (note) { note.hidden = false; note.textContent = "Servicio seleccionado: " + name; }
    document.getElementById("contacto").scrollIntoView();
    var first = form.querySelector("input:not([type=hidden])");
    if (first) first.focus({ preventScroll: true });
  }

  document.querySelectorAll("dialog.svc").forEach(function (dialog) {
    dialog.addEventListener("click", function (e) {
      if (e.target === dialog || e.target.closest("[data-close]")) { dialog.close(); return; }
      if (e.target.closest("[data-cta]")) {
        e.preventDefault();
        lastTrigger = null;
        dialog.close();
        selectService(dialog);
      }
    });
    dialog.addEventListener("close", function () {
      if (location.hash === "#" + dialog.id) history.replaceState(null, "", location.pathname + location.search);
      if (lastTrigger) lastTrigger.focus();
    });
  });

  document.addEventListener("click", function (e) {
    var link = e.target.closest("[data-service]");
    if (link && openService(link.dataset.service, link)) e.preventDefault();
  });
  function fromHash() { openService(location.hash.slice(1)); }
  window.addEventListener("hashchange", fromHash);
  fromHash();

  // ---- Formulario de contacto ----
  // Con data-endpoint="https://…" los datos se envían por POST (FormData).
  // Sin endpoint solo se valida y se muestra la confirmación (ambiente de desarrollo).
  document.querySelectorAll("form[data-contact-form]").forEach(function (form) {
    var status = form.querySelector(".form-status");
    var submit = form.querySelector('[type="submit"]');
    var okMsg = "Gracias. Un especialista de nuestro equipo te contactará muy pronto.";
    var errMsg = "No pudimos enviar tu mensaje. Inténtalo de nuevo o escríbenos a ventas@consein.com.";

    function done(ok, msg) {
      status.dataset.state = ok ? "ok" : "error";
      status.textContent = msg;
      if (submit) submit.disabled = false;
      if (ok) {
        form.reset();
        var note = form.querySelector(".form-service");
        if (note) note.hidden = true;
      }
    }

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var firstInvalid = null;
      form.querySelectorAll("[required]").forEach(function (field) {
        var ok = field.checkValidity();
        field.setAttribute("aria-invalid", ok ? "false" : "true");
        if (!ok && !firstInvalid) firstInvalid = field;
      });
      if (firstInvalid) {
        done(false, "Revisa los campos marcados: son obligatorios y el correo debe ser válido.");
        firstInvalid.focus();
        return;
      }
      var endpoint = form.dataset.endpoint;
      if (!endpoint) { done(true, okMsg); return; }
      if (submit) submit.disabled = true;
      status.dataset.state = "ok";
      status.textContent = "Enviando…";
      fetch(endpoint, { method: "POST", body: new FormData(form), headers: { Accept: "application/json" } })
        .then(function (res) { done(res.ok, res.ok ? okMsg : errMsg); })
        .catch(function () { done(false, errMsg); });
    });
  });
})();
