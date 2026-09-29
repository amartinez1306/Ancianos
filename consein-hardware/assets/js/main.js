/* Consein · Hardware — interacciones de la página */
(function () {
  'use strict';

  // Año en el pie
  var year = document.getElementById('year');
  if (year) year.textContent = new Date().getFullYear();

  // Menú móvil
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('main-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', String(open));
      toggle.setAttribute('aria-label', open ? 'Cerrar menú' : 'Abrir menú');
    });
    nav.addEventListener('click', function (e) {
      if (e.target.closest('a')) {
        nav.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
      }
    });
  }

  // Tabs de soluciones (accesibles con teclado)
  var tabs = Array.prototype.slice.call(document.querySelectorAll('[role="tab"]'));
  function selectTab(tab, focus) {
    tabs.forEach(function (t) {
      var selected = t === tab;
      t.setAttribute('aria-selected', String(selected));
      t.tabIndex = selected ? 0 : -1;
      document.getElementById(t.getAttribute('aria-controls')).hidden = !selected;
    });
    if (focus) tab.focus();
  }
  tabs.forEach(function (tab, i) {
    tab.addEventListener('click', function () { selectTab(tab); });
    tab.addEventListener('keydown', function (e) {
      var next = null;
      if (e.key === 'ArrowRight') next = tabs[(i + 1) % tabs.length];
      if (e.key === 'ArrowLeft') next = tabs[(i - 1 + tabs.length) % tabs.length];
      if (e.key === 'Home') next = tabs[0];
      if (e.key === 'End') next = tabs[tabs.length - 1];
      if (next) { e.preventDefault(); selectTab(next, true); }
    });
  });

  // Botón "volver arriba"
  var toTop = document.querySelector('.to-top');
  function onScroll() {
    if (toTop) toTop.classList.toggle('show', window.scrollY > 600);
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  if (!('IntersectionObserver' in window)) return;

  // Resaltar la sección actual en el sub-menú
  var links = {};
  document.querySelectorAll('.subnav a').forEach(function (a) {
    links[a.getAttribute('href').slice(1)] = a;
  });
  var spy = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      var link = links[entry.target.id];
      if (link && entry.isIntersecting) {
        Object.keys(links).forEach(function (k) { links[k].classList.remove('is-current'); });
        link.classList.add('is-current');
      }
    });
  }, { rootMargin: '-45% 0px -50% 0px' });
  Object.keys(links).forEach(function (id) {
    var el = document.getElementById(id);
    if (el) spy.observe(el);
  });

  // Animación de entrada
  var items = document.querySelectorAll('.pillar, .card, .services li, .when li, .timeline li');
  var reveal = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add('in');
        reveal.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });
  items.forEach(function (el) { el.classList.add('reveal'); reveal.observe(el); });
})();
