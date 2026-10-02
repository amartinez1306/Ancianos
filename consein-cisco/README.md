# Consein · Soluciones Cisco (sitio)

Sitio de la sección Cisco de consein.com: Microsoft como núcleo, Cisco como acelerador.

## Cómo verlo
- **Versión de un solo archivo (recomendada para presentar):** abra `Consein_Cisco_sitio_completo.html` con doble clic.
  Incluye las tres páginas, las fuentes y el logotipo; funciona sin internet y puede enviarse por correo.
- **Diseño digital (ejemplo):** abra `Consein_Cisco_diseno_digital.html`. Mismo contenido con un diseño moderno y
  tecnológico en la paleta Consein: azul oscuro `#1b245b` y verde `#58bb47`. Un solo archivo, sin internet.
- **Versión de sitio (para publicar):** abra `index.html`. Usa la carpeta `assets/` y tiene una página por sección para SEO.
Para publicarlo, suba la carpeta a cualquier servidor web (ajuste `URL_BASE` en `_fuente/generar_sitio.py`).

## Páginas
| Archivo | Menú | Contenido |
|---|---|---|
| `index.html` | Inicio | Sinergia exponencial con sticker "Inventario gratis", enfoque, 7 especialidades, método, resultados, nosotros, preguntas frecuentes, contacto |
| `soluciones.html` | Soluciones Cisco › Soluciones de Valor | 15 soluciones agrupadas en 7 especialidades |
| `productos.html` | Soluciones Cisco › Ofertas de Productos | Aviso "Inventariamos gratis su hardware Cisco", por qué renovar, autodiagnóstico, rutas, método y 8 ofertas |

Menú: **Inicio · Soluciones Cisco · Nosotros · Contacto**. Soluciones Cisco despliega dos opciones de segundo nivel,
Soluciones de Valor (7 especialidades y Consein Connected) y Ofertas de Productos (8 ofertas del Programa Renueva).

Cada oferta muestra solo **título y valor**. "Seguir leyendo…" abre la subpantalla con Ideal para, Qué resolvemos,
Qué incluye y Resultado. Los submenús enlazan directo a cada oferta (por ejemplo `soluciones.html#csc-06`).

## Aviso de renovación de hardware
- **Inicio:** sticker circular discreto en la portada ("Inventario gratis", con el texto giratorio
  "Renovación de hardware · Programa Renueva") que lleva al aviso completo. Se edita en `sticker_renueva()`.
- **Ofertas de Productos:** aviso completo "Inventariamos gratis su hardware Cisco", después del encabezado.
  Textos en `AVISOS` e ilustración en `arte_hardware()`.
Estilos al final de `estilos.css` (y ajustes en `digital.css`). El menú
muestra la etiqueta "Destacado · Renovación de hardware" en Ofertas de Productos.

## Tipografías
- **Párrafos: Poppins**, incluida en `assets/fonts/` (licencia SIL OFL 1.1).
- **Títulos: Haltto.** Es una fuente comercial que no está incluida. Copie los archivos con licencia como
  `assets/fonts/Haltto-Bold.woff2` y `assets/fonts/Haltto-Regular.woff2`: el sitio los toma automáticamente.
  Mientras no estén, los títulos se muestran en Poppins.

## Editar textos
Todo el contenido está en `_fuente/generar_sitio.py`. Después de editar:
```
python3 _fuente/generar_sitio.py
```
El comando regenera las tres páginas, la versión de un solo archivo y el diseño digital.

## Diseño digital
- Estilos: `assets/css/digital.css` (se aplica sobre `estilos.css`); animaciones: `assets/js/digital.js`.
- Recursos gráficos (diagrama de red, capas, iconos) en `_fuente/generar_sitio.py` (`arte_hero`, `ARTE_CAPAS`, `_ICONOS`).
- Texto azul oscuro sobre verde; nunca texto blanco sobre verde (contraste insuficiente).
- Respeta la preferencia del sistema "reducir movimiento".

## SEO
`Palabras_clave_SEO_Consein_Cisco.docx` lista 93 palabras clave por especialidad para el equipo SEO.
El sitio ya incluye títulos y descripciones por página, un H2 por especialidad, canonical, Open Graph
y datos estructurados schema.org (Organization, Service, BreadcrumbList, FAQPage).

## Antes de publicar
- Confirmar el nivel de partnership y las certificaciones Cisco vigentes de Consein.
- Validar la capacidad de entrega de cada oferta (en especial AI Defense, Hypershield y Secure AI Factory).
- Revisar CSC-09 frente a Microsoft Entra Global Secure Access.
- Confirmar con Cisco Capital los programas de financiamiento por país.
- Conectar el formulario de contacto al CRM (hoy es una maqueta).
