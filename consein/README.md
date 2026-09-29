# Consein · Servicios › Innovación y Servicios Digitales (modelo)

Modelo de página web para la opción **Servicios** de www.consein.com, basado en el documento
"Consein · Servicios · Innovación y Servicios Digitales / PMO".

| Archivo | Contenido |
|---|---|
| `index.html` | Índice para el comité: recorrido sugerido, las 8 fichas (se abren ahí mismo), páginas y puntos a validar. |
| `servicios/index.html` | Redirige a la página de la Dirección (para abrir `/servicios/`). |
| `servicios/innovacion-y-servicios-digitales.html` | Página de la Dirección: portada, quiénes somos, 7 pasos en 3 fases, PMO, líneas de especialidad, innovación y reconocimientos, contacto. |
| `servicios/evaluamos.html` | Subpágina del servicio **01 · Evaluamos** (plantilla para los servicios 02–07). |
| `assets/consein.css` | Estilos compartidos (paleta, tipografía, componentes, responsive). |
| `assets/consein.js` | Menú móvil, sub-navegación activa, animaciones, subpantallas de servicio y formularios. |
| `assets/servicios-data.js` | Contenido de las 8 fichas «Ver servicio» (7 servicios de valor + NortIA). |
| `assets/logo-consein*.png` | Logo original Consein (fondo claro y versión blanca para fondos oscuros). |

**Política de forma aplicada:** navy `#0a2540`, azul `#0b5cad` / `#2e7fd1`, verde `#2bb673`,
fondos `#f4f8fb` / `#e8f0fb`; títulos en *Bricolage Grotesque* y texto en *Nunito Sans* (Google Fonts).

**Subpantallas «Ver servicio»:** cada botón *Ver servicio* abre la ficha del servicio (modelo
«Consein 360 · Diagnóstico Red + Nube»). También se abren por URL: `innovacion-y-servicios-digitales.html#csc-01` … `#csc-07` y `#nortia`.
El botón de la ficha lleva al formulario de contacto con el servicio ya seleccionado.

**Pendiente para producción:** conectar los formularios al CRM/endpoint (hoy solo validan y muestran
confirmación), validar con el comité los nombres, formatos, alcance de NortIA y cifras de las fichas, y ajustar las URL del menú
del sitio real.
