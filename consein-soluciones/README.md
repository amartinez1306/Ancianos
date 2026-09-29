# Consein · Soluciones (modelo para desarrollo y producción)

Modelo HTML/CSS/JS estático, sin dependencias ni build. Abrir `index.html` en el navegador
o servir la carpeta con cualquier servidor web (`npx serve .`, `python3 -m http.server`).

## Estructura

```
index.html                 Estructura de la página (header, hero, NortIA, 7 especialidades, contacto, footer)
assets/css/styles.css      Estilos (colores de marca del logo: #000F76 y #61FC22)
assets/js/data.js          Contenido: NortIA + 7 especialidades y sus fichas (offerings)
assets/js/app.js           Presentación: tarjetas, subpantalla con fichas, rutas y formulario
assets/img/                Logo oficial (color y blanco, PNG transparente)
```

## Funcionamiento

- Cada tarjeta de especialidad tiene su botón **Ver …** que abre una **subpantalla** con sus fichas.
- La subpantalla muestra la lista de offerings de la especialidad y la ficha seleccionada con:
  En una frase · Ideal para · Qué resuelve · Incluye · Núcleo Microsoft · Puente NortIA ·
  Resultado · Prueba · Respaldo · botón de CTA.
- Enlaces directos: `index.html#/infraestructura`, `#/seguridad`, `#/colaboracion`,
  `#/servicios-empresariales`, `#/data`, `#/automatizacion`, `#/inteligencia-artificial`, `#/nortia`.
  Con ficha: `#/infraestructura/INF-04`.
- Cerrar: botón ×, clic fuera o tecla Esc.
- El CTA de cada ficha lleva al formulario de contacto con la solución preseleccionada.

## Para producción

- Conectar el formulario (`#contact-form` en `app.js`) al CRM o endpoint del sitio.
- Validar con los líderes de cada práctica los nombres y alcances de los offerings de `data.js`.
- Reemplazar los PNG del logo por la versión SVG oficial, si existe.

Contenido basado en `Consein_Soluciones_DISD_Offerings_NortIA_ver_1.docx` (DISD, septiembre 2026).
