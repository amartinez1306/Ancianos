# Modelo web · Consein › Soluciones

Modelo de página para el menú **Soluciones** de www.consein.com, construido a partir de
`Consein_Soluciones_DISD_Offerings_NortIA_ver_1.docx` (DISD, septiembre 2026).

Abrir `index.html` en el navegador (archivo único, sin dependencias salvo Google Fonts).

## Páginas

Una página por cada una de las 7 prácticas, más la portada y NortIA.

| Ruta | Página | Offerings | Personalidad |
|---|---|---|---|
| `#/soluciones` | Portada del menú Soluciones | — | Institucional |
| `#/nortia` | NortIA (solución insignia) | NRT-00 a 05 | Cobre / brújula |
| `#/infraestructura` | Infraestructura | INF-01 a 07 | Azul · cuadrícula · Resiliencia, Escala, Costo justo |
| `#/ciberseguridad` | Seguridad | SEG-01 a 06 | Verde · hexágonos · Zero Trust, Detección, Respuesta |
| `#/colaboracion` | Colaboración | COL-01 a 06 | Turquesa · red de personas · Personas, Conocimiento, Copilot |
| `#/servicios-empresariales` | Servicios Empresariales | EMP-01 a 06 | Naranja · barras · Control, Visibilidad, Decisión |
| `#/data` | Data | DAT-01 a 06 | Celeste · puntos · Unificar, Gobernar, Activar |
| `#/automatizacion` | Automatización de procesos | AUT-01 a 06 | Violeta · flujos · Menos manual, Más velocidad, Trazabilidad |
| `#/inteligencia-artificial` | Inteligencia Artificial | IA-02 a 06 (+ banner NortIA) | Índigo · red neuronal · Activar, Escalar, Gobernar |

Cada práctica tiene su propio color, fondo, patrón gráfico, ilustración, pregunta gancho, tono de voz,
palabras clave, dato destacado y llamado a la acción (tomado de sus "Mensajes listos para publicar").

Estructura de cada página: Hero · Personalidad y dato destacado · Problemas (como preguntas) · Soluciones ·
Offerings · Evidencia (con fuente y año) · Respaldo · Puente NortIA · Otras prácticas · Cierre con un único CTA.

> Nota: el documento proponía agrupar prácticas en las páginas actuales del sitio
> (p. ej. /infraestructura-y-colaboracion). Este modelo separa las 7 prácticas en páginas propias.

## Editar contenido

Todos los textos están en el objeto `DATA` dentro de `index.html`. La configuración de páginas,
colores y personalidad por práctica están en `PAGES`, `COLORS`, `PERSONA` y `ART`.

## Pendiente antes de publicar (notas internas del documento)

- Validar nombres y alcances de los 43 offerings con los líderes de cada práctica.
- Confirmar con cada cliente los testimonios asociados a offerings (Digitel, Banco Plaza, Aiwa Latam).
- Sustituir el logotipo provisional por el oficial y conectar el formulario al CRM del sitio.
- Ajustar tipografía y colores a la guía de marca vigente del sitio si difiere de la del documento.
