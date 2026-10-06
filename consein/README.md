# Consein · Página de Servicios

Página estática (HTML, CSS y JavaScript, sin dependencias ni compilación) para la opción
**Servicios** de www.consein.com. Lista para los ambientes de desarrollo y producción.

## Estructura

```
consein/
├── index.html               Página de Servicios (incluye las 7 fichas y los datos estructurados SEO)
└── assets/
    ├── consein.css          Estilos (look minimalista)
    ├── consein.js           Menú, fichas «Ver servicio» y formulario
    ├── logo-consein.png     Logo original
    └── fonts/               Archivos de la tipografía Haltto (ver LEEME.txt)
```

## Tipografías

- **Títulos: Haltto.** Tipografía con licencia comercial. Copiar `Haltto-Bold.woff2` y `Haltto-Bold.woff`
  en `assets/fonts/`. Mientras no estén, los títulos se muestran con Poppins.
- **Párrafos: Poppins** (Google Fonts, pesos 300, 400 y 500).

## Secciones

1. **Portada** – H1 principal y gráfico de las 7 etapas (cada número abre su ficha).
2. **Propuesta de valor** – Escuchamos, Aprendemos, Ejecutamos y Acompañamos.
3. **Servicio en 7 etapas** – tres fases; cada etapa enlaza a su especialidad.
4. **Oficina de Proyectos (PMO)** – cómo garantizamos el resultado.
5. **Preguntas frecuentes** – contenido para búsquedas de tipo pregunta.
6. **Contacto** – formulario y canales directos.

## Fichas «Ver servicio»

Cada ficha es un `<dialog class="svc" id="etapa-0X">` dentro de `index.html`, por lo que los buscadores
leen su contenido. Se abren con *Ver servicio* o con enlace directo: `index.html#etapa-01` … `#etapa-07`.
El botón de la ficha lleva al formulario con el servicio ya seleccionado (campo oculto `servicio`).

## SEO incluido

- `title`, `meta description`, `canonical`, Open Graph y un solo H1.
- Encabezados con las palabras clave de cada especialidad.
- `hreflang`, Twitter Card y encabezados H1/H2/H3 con las palabras clave de cada especialidad.
- Datos estructurados JSON-LD: `Organization`, `WebPage`, `ProfessionalService` (Caracas y Panamá),
  `BreadcrumbList`, `ItemList` de `Service` y `FAQPage`.
- Guías en `docs/`: *Consein_Manual_SEO.docx* (reglas, SEO técnico, local, contenidos y medición) y
  *Consein_Palabras_Clave_SEO.docx* (palabras clave por especialidad, mercado y ciudad).
- Plantillas `docs/seo/robots.txt` y `docs/seo/sitemap.xml` para la raíz del dominio.

Antes de publicar, confirmar que la URL definitiva sea `https://www.consein.com/servicios`
(se usa en `canonical`, Open Graph y JSON-LD).

## Formulario de contacto

```html
<form data-contact-form data-endpoint="" novalidate>
```

- **Vacío (desarrollo):** valida los campos y muestra la confirmación, sin enviar datos.
- **Con URL (producción):** envía los datos por `POST` (`FormData`) y muestra éxito o error según la respuesta.

Campos: `nombre`, `empresa`, `cargo`, `correo`, `pais`, `reto`, `servicio`.

## Despliegue

Copiar la carpeta `consein/` al servidor. Para probar en local:
`python3 -m http.server 8000` desde la carpeta y abrir `http://localhost:8000`.

## Pendiente antes de producción

- Archivos de la tipografía Haltto con licencia.
- URL del `data-endpoint` del formulario.
- Enlaces reales del menú «Soluciones» (hoy apuntan a `#`).
