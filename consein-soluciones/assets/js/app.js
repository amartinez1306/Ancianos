/* =========================================================
   Consein · Soluciones — lógica de presentación
   - Tarjetas de las 7 especialidades + NortIA
   - Subpantalla por especialidad con fichas de offerings
   - Enlaces directos: index.html#/infraestructura, #/seguridad, ... #/nortia
   ========================================================= */
(function () {
  'use strict';

  const DATA = window.CONSEIN_DATA;
  const AREAS = [DATA.nortia].concat(DATA.areas);

  const ICONS = {
    '01': '<path d="M7 18a4.5 4.5 0 0 1-.5-9A6 6 0 0 1 18 9a4 4 0 0 1-.5 9z"/>',
    '02': '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/>',
    '03': '<circle cx="9" cy="8" r="3"/><circle cx="17" cy="10" r="2.5"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6M14 20c0-2.5 1.5-4.5 3-4.5s4 1 4 4.5"/>',
    '04': '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',
    '05': '<ellipse cx="12" cy="5" rx="8" ry="3"/><path d="M4 5v14c0 1.7 3.6 3 8 3s8-1.3 8-3V5M4 12c0 1.7 3.6 3 8 3s8-1.3 8-3"/>',
    '06': '<circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M4.2 4.2l2.1 2.1M17.7 17.7l2.1 2.1M2 12h3M19 12h3M4.2 19.8l2.1-2.1M17.7 6.3l2.1-2.1"/>',
    '07': '<rect x="5" y="7" width="14" height="12" rx="3"/><path d="M12 3v4M9 12h.01M15 12h.01M9 16h6"/>'
  };

  const $ = (sel, root = document) => root.querySelector(sel);
  const esc = (s) => String(s ?? '').replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const noDot = (s) => String(s).replace(/\.\s*$/, '');
  const bySlug = (slug) => AREAS.find((a) => a.slug === slug);

  function setAreaColors(el, area) {
    el.style.setProperty('--area', area.color);
    el.style.setProperty('--area-dark', area.bg);
  }

  /* ---------- Tarjetas ---------- */
  function renderCards() {
    const grid = $('#areas-grid');
    grid.innerHTML = DATA.areas.map((a) => `
      <article class="area-card" style="--area:${a.color}">
        <div class="area-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">${ICONS[a.num]}</svg></div>
        <span class="area-num">${a.num}</span>
        <h3>${esc(a.short)}</h3>
        <p class="area-promesa">${esc(a.promesa)}</p>
        <p class="area-hook">${esc(a.hook)}</p>
        <div class="tags">${a.keywords.map((k) => `<span>${esc(k)}</span>`).join('')}</div>
        <a class="btn btn-area" href="#/${a.slug}">Ver ${esc(a.short)}</a>
      </article>`).join('');
  }

  /* ---------- Información 1: mapa del menú ---------- */
  const MAP_LABEL = { nortia: 'NortIA', seguridad: 'Ciberseguridad', automatizacion: 'Automatización de procesos' };
  function renderMap() {
    $('#map-body').innerHTML = AREAS.map((a) => {
      const first = a.offerings[0].code, last = a.offerings[a.offerings.length - 1].code;
      const promesa = a.slug === 'nortia' ? 'Solución insignia transversal' : a.promesa;
      return `<tr style="--area:${a.color}"><td><a href="#/${a.slug}">${esc(MAP_LABEL[a.slug] || a.short)}</a></td><td>${esc(promesa)}</td><td><code>${esc(first)} a ${esc(last)}</code></td></tr>`;
    }).join('');
  }

  /* ---------- Selector de interés del formulario ---------- */
  function renderInterestOptions() {
    const sel = $('#interes');
    sel.innerHTML = '<option>Diagnóstico Consein 360</option>' + AREAS.map((a) =>
      `<optgroup label="${esc(a.short)}">${a.offerings.map((o) => `<option>${esc(o.code + ' · ' + o.name)}</option>`).join('')}</optgroup>`
    ).join('');
  }

  /* ---------- Ficha ---------- */
  function fichaHTML(area, o) {
    const hlLabel = area.slug === 'nortia' ? 'Fase NortIA' : 'Puente NortIA';
    return `
      <header class="ficha-head">
        <p class="ficha-code">${esc(o.code)} · ${esc(area.short)}</p>
        <h3>${esc(o.name)}</h3>
        <p class="ficha-type">${esc(o.tipo)}</p>${o.tipo.includes('*') ? '<small class="cond">*Condiciones aplican.</small>' : ''}
      </header>
      <table class="ficha-table">
        <tbody>
          <tr class="frase"><th scope="row">En una frase</th><td>${esc(o.frase)}</td></tr>
          <tr><th scope="row">Ideal para</th><td>${esc(o.ideal)}</td></tr>
          <tr><th scope="row">Qué resuelve</th><td>${esc(o.resuelve)}</td></tr>
          <tr><th scope="row">Incluye</th><td><ul>${o.incluye.map((i) => `<li>${esc(i)}</li>`).join('')}</ul></td></tr>
          <tr class="hl"><th scope="row">Núcleo Microsoft</th><td>${esc(o.microsoft)}</td></tr>
          <tr class="hl"><th scope="row">${hlLabel}</th><td>${esc(o.puente)}</td></tr>
          <tr class="resultado"><th scope="row">Resultado</th><td>${esc(o.resultado)}</td></tr>
          <tr class="prueba"><th scope="row">Prueba</th><td>${esc(o.prueba)}</td></tr>
          <tr><th scope="row">Respaldo</th><td>${esc(area.respaldo)}</td></tr>
        </tbody>
      </table>
      <footer class="ficha-foot">
        <a class="btn btn-area" href="#contacto" data-interest="${esc(o.code + ' · ' + o.name)}">${esc(noDot(o.cta))}</a>${o.cta.includes('*') ? '<small class="cond">*Condiciones aplican.</small>' : ''}
      </footer>`;
  }

  /* ---------- Subpantalla ---------- */
  const panel = $('#area-panel');
  let lastFocus = null;

  function openPanel(area, code) {
    setAreaColors(panel, area);
    $('#panel-kicker').textContent = area.slug === 'nortia' ? 'Solución insignia' : `Especialidad ${area.num} · ${area.promesa}`;
    $('#panel-title').textContent = area.h1;
    $('#panel-sub').textContent = area.sub;
    $('#panel-tags').innerHTML = area.keywords.map((k) => `<span>${esc(k)}</span>`).join('');
    $('#offer-tabs').innerHTML = area.offerings.map((o) =>
      `<button class="offer-tab" role="tab" data-code="${esc(o.code)}" aria-selected="false"><small>${esc(o.code)}</small><span>${esc(o.name)}</span></button>`
    ).join('');
    showOffer(area, code || area.offerings[0].code);

    if (panel.hidden) {
      lastFocus = document.activeElement;
      panel.hidden = false;
      document.body.classList.add('no-scroll');
      $('.icon-btn', panel).focus();
    }
    $('.panel-sheet', panel).scrollTop = 0;
  }

  function showOffer(area, code) {
    const o = area.offerings.find((x) => x.code === code) || area.offerings[0];
    panel.querySelectorAll('.offer-tab').forEach((t) => t.setAttribute('aria-selected', String(t.dataset.code === o.code)));
    $('#ficha').innerHTML = fichaHTML(area, o);
  }

  function closePanel() {
    if (panel.hidden) return;
    panel.hidden = true;
    document.body.classList.remove('no-scroll');
    if (location.hash.startsWith('#/')) history.pushState('', document.title, location.pathname + location.search + '#soluciones');
    if (lastFocus) lastFocus.focus();
  }

  /* ---------- Rutas: #/slug o #/slug/CODIGO ---------- */
  function route() {
    const m = location.hash.match(/^#\/([\w-]+)(?:\/([\w-]+))?/);
    const area = m && bySlug(m[1]);
    if (area) openPanel(area, m[2]);
    else if (!panel.hidden) { panel.hidden = true; document.body.classList.remove('no-scroll'); }
  }

  /* ---------- Eventos ---------- */
  function bindEvents() {
    panel.addEventListener('click', (e) => {
      if (e.target.closest('[data-close]')) return closePanel();
      const tab = e.target.closest('.offer-tab');
      if (tab) {
        const slug = location.hash.match(/^#\/([\w-]+)/)[1];
        history.replaceState(null, '', `#/${slug}/${tab.dataset.code}`);
        showOffer(bySlug(slug), tab.dataset.code);
      }
      const cta = e.target.closest('[data-interest]');
      if (cta) {
        e.preventDefault();
        closePanel();
        $('#interes').value = cta.dataset.interest;
        $('#contacto').scrollIntoView({ behavior: 'smooth' });
      }
    });

    document.addEventListener('keydown', (e) => { if (e.key === 'Escape') closePanel(); });

    $('.nav-toggle').addEventListener('click', (e) => {
      const nav = $('#main-nav');
      const open = nav.classList.toggle('open');
      e.currentTarget.setAttribute('aria-expanded', String(open));
    });

    // Formulario de muestra: conectar aquí al CRM / endpoint de producción.
    $('#contact-form').addEventListener('submit', (e) => {
      e.preventDefault();
      const form = e.currentTarget;
      if (!form.checkValidity()) { form.reportValidity(); return; }
      $('.form-ok', form).hidden = false;
      form.reset();
    });

    window.addEventListener('hashchange', route);
  }

  renderCards();
  renderMap();
  renderInterestOptions();
  bindEvents();
  route();
})();
