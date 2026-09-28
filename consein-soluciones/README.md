# Modelo web · Consein › Soluciones

Modelo de página para el menú **Soluciones** de www.consein.com, construido a partir de
`Consein_Soluciones_DISD_Offerings_NortIA_ver_1.docx` (DISD, septiembre 2026).

Abrir `index.html` en el navegador (archivo único, sin dependencias salvo Google Fonts).

## Páginas (según la sección 06 del documento)

| Ruta | Contenido |
|---|---|
| `#/soluciones` | Portada del menú Soluciones: cifras, NortIA destacado, 7 prácticas, "Por qué Consein" |
| `#/nortia` | Nueva página insignia NortIA (NRT-00 a NRT-05) |
| `#/infraestructura-y-colaboracion` | Infraestructura (INF-01 a 07) + Colaboración (COL-01 a 06) |
| `#/ciberseguridad` | Seguridad (SEG-01 a 06), SEG-03 destacado como puente a NortIA |
| `#/ia-y-automatizacion-de-procesos` | Banner NortIA + IA (IA-02 a 06) + Automatización (AUT-01 a 06) |
| `#/financieras-y-gobierno-corporativo` | Data (DAT-01 a 06) + Servicios Empresariales (EMP-01 a 06) |

Cada página de solución sigue los 8 bloques recomendados: Hero · Problemas (como preguntas) ·
Soluciones · Offerings · Evidencia (con fuente y año) · Respaldo · Puente NortIA · Cierre con un único CTA
(Diagnóstico Consein 360).

## Editar contenido

Todos los textos están en el objeto `DATA` dentro de `index.html`. La configuración de páginas,
colores por práctica y menú está en `PAGES`, `COLORS` y `SHORT`.

## Pendiente antes de publicar (notas internas del documento)

- Validar nombres y alcances de los 43 offerings con los líderes de cada práctica.
- Confirmar con cada cliente los testimonios asociados a offerings (Digitel, Banco Plaza, Aiwa Latam).
- Sustituir el logotipo provisional por el oficial y conectar el formulario al CRM del sitio.
- Ajustar tipografía y colores a la guía de marca vigente del sitio si difiere de la del documento.
