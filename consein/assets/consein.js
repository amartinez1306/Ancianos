/* Consein · Servicios
   Interacciones: menú móvil, sub-navegación activa, animaciones de entrada,
   subpantallas «Ver servicio» y formulario de contacto. */
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

  // ---- Desplegables del menú (clic / teclado; en escritorio también hover por CSS) ----
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

  // ---- Subpantallas «Ver servicio» ----
  // Se abren con cualquier elemento data-service="<id>" o al entrar con #<id>
  // en la URL (p. ej. index.html#etapa-03). El contenido está en servicios-data.js.
  var SERVICIOS = window.CONSEIN_SERVICIOS || [];
  var byService = {};
  SERVICIOS.forEach(function (s) { byService[s.id] = s; });

  function esc(t) {
    return String(t).replace(/[&<>"]/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c];
    });
  }

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
        row("En una frase", "<strong><em>" + esc(s.frase) + "</em></strong>") +
        row("Ideal para", esc(s.ideal)) +
        row("Qué resuelve", esc(s.resuelve)) +
        row("Incluye", incluye) +
        row("Cómo lo hacemos", esc(s.como), "svc__row--hl") +
        row("Entregables", esc(s.entregables), "svc__row--hl") +
        row("Resultado", "<strong>" + esc(s.resultado) + "</strong>") +
        row("Cómo medimos el éxito", esc(s.exito), "svc__row--kpi") +
      "</tbody></table></div>" +
      '<footer class="svc__foot">' +
        '<a class="svc__cta" href="#contacto" data-cta="' + esc(s.id) + '">' + esc(s.cta) + "</a>" +
      "</footer>"
    );
  }

  var dialog = null;
  var lastTrigger = null;

  function closeService() {
    if (dialog && dialog.open) dialog.close();
  }

  function selectService(svc) {
    var form = document.querySelector("#contacto form");
    if (!form) return;
    var hidden = form.querySelector('input[name="servicio"]');
    if (hidden) hidden.value = svc.titulo;
    var note = form.querySelector(".form-service");
    if (note) { note.hidden = false; note.textContent = "Servicio seleccionado: " + svc.titulo; }
    document.getElementById("contacto").scrollIntoView();
    var first = form.querySelector("input:not([type=hidden])");
    if (first) first.focus({ preventScroll: true });
  }

  function openService(id, trigger) {
    var s = byService[id];
    if (!s || !window.HTMLDialogElement) return false;
    if (!dialog) {
      dialog = document.createElement("dialog");
      dialog.className = "svc";
      dialog.setAttribute("aria-labelledby", "svc-title");
      document.body.appendChild(dialog);
      dialog.addEventListener("click", function (e) {
        if (e.target === dialog || e.target.closest("[data-close]")) { closeService(); return; }
        var cta = e.target.closest("[data-cta]");
        if (cta) {
          e.preventDefault();
          lastTrigger = null;
          closeService();
          selectService(byService[cta.dataset.cta]);
        }
      });
      dialog.addEventListener("close", function () {
        if (byService[location.hash.slice(1)]) history.replaceState(null, "", location.pathname + location.search);
        if (lastTrigger) lastTrigger.focus();
      });
    }
    dialog.innerHTML = renderService(s);
    lastTrigger = trigger || null;
    if (!dialog.open) dialog.showModal();
    if (location.hash !== "#" + id) history.replaceState(null, "", "#" + id);
    dialog.querySelector(".svc__body").scrollTop = 0;
    return true;
  }

  document.addEventListener("click", function (e) {
    var link = e.target.closest("[data-service]");
    if (link && openService(link.dataset.service, link)) e.preventDefault();
  });
  function fromHash() {
    var id = location.hash.slice(1);
    if (byService[id]) openService(id);
  }
  window.addEventListener("hashchange", fromHash);
  fromHash();

  // ---- Formulario de contacto ----
  // Si el formulario tiene data-endpoint="https://…", los datos se envían por POST
  // (FormData) a ese endpoint. Sin endpoint, solo se valida y se muestra la
  // confirmación (útil en el ambiente de desarrollo).
  document.querySelectorAll("form[data-contact-form]").forEach(function (form) {
    var status = form.querySelector(".form-status");
    var submit = form.querySelector('[type="submit"]');

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

      var okMsg = "¡Gracias! Un especialista te contactará muy pronto.";
      var endpoint = form.dataset.endpoint;
      if (!endpoint) { done(true, okMsg); return; }

      if (submit) submit.disabled = true;
      status.dataset.state = "ok";
      status.textContent = "Enviando…";
      fetch(endpoint, { method: "POST", body: new FormData(form), headers: { Accept: "application/json" } })
        .then(function (res) {
          done(res.ok, res.ok ? okMsg : "No pudimos enviar tu mensaje. Inténtalo de nuevo o escríbenos por correo.");
        })
        .catch(function () {
          done(false, "No pudimos enviar tu mensaje. Revisa tu conexión e inténtalo de nuevo.");
        });
    });
  });
})();
