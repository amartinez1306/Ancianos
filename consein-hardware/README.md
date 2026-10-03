# Consein · Página de Hardware

Subpágina de **www.consein.com** que se abre al hacer clic en la opción **Hardware** del menú.
Es un sitio estático (HTML + CSS + JS), sin dependencias ni proceso de compilación.

```
consein-hardware/
├── index.html              # Página (iconos e ilustraciones por sección)
├── index-digital.html      # Variante moderna y tecnológica (ejemplo)
├── assets/css/styles.css   # Estilos base (paleta: azul oscuro #1B245B / verde #58BB47)
├── assets/css/grafico.css  # Estilos de iconos, ilustraciones y bloques gráficos
├── assets/css/digital.css  # Estilos de la variante digital
├── assets/js/main.js       # Menú móvil y botón "volver arriba"
├── assets/img/logo-consein.jpg
├── assets/img/brands/      # Logos de marcas (Dell, HP, Lenovo); falta Logitech
├── assets/fonts/           # Colocar aquí Haltto.woff2 (fuente de títulos)
├── build.py                # Genera las versiones de un solo archivo
├── seo/                    # Palabras clave SEO (docx) para el equipo de SEO
├── Dockerfile + nginx.conf # Opción contenedor (sirve en /hardware/)
└── README.md
```

Todas las rutas son **relativas**, así que la carpeta funciona en cualquier ruta del servidor.

## 1. Desarrollo (local)

```bash
cd consein-hardware
python3 -m http.server 8080
# abrir http://localhost:8080
```

O con Docker, igual que en producción:

```bash
docker build -t consein-hardware .
docker run --rm -p 8080:80 consein-hardware
# abrir http://localhost:8080/hardware/
```

## 2. Producción

**Opción A — Hosting actual de consein.com (recomendada)**
1. Subir el contenido de `consein-hardware/` (solo `index.html` y `assets/`) a la carpeta
   `/hardware/` del sitio (FTP / cPanel / panel del hosting).
   Resultado: `https://www.consein.com/hardware/`.
2. En el menú principal del sitio, apuntar la opción **Hardware** a `/hardware/`.
3. Si el sitio es WordPress: crear la carpeta `hardware` en la raíz pública
   (junto a `wp-content`); el servidor entrega la página estática antes que WordPress.

**Opción B — Contenedor** (Docker / Kubernetes / Cloud Run / App Service)
Construir la imagen con el `Dockerfile` y publicar el puerto 80. La página queda en `/hardware/`.

## Tipografías

- **Títulos: Haltto.** No es una fuente pública de Google Fonts: copie el archivo licenciado
  (`Haltto.woff2`, `.woff`, `.otf` o `.ttf`) en `assets/fonts/` y ejecute `python3 build.py`
  para incrustarla también en la versión de un solo archivo. Mientras no esté, los títulos usan Poppins.
- **Párrafos: Poppins**, cargada desde Google Fonts.

## Versión de un solo archivo

`python3 build.py` regenera `consein-hardware-standalone.html` y `consein-hardware-digital-standalone.html`
(CSS, JS, logo y fuente incrustados).
Ejecútelo después de cada cambio en `index.html` o `assets/`.

## Logos de marcas

- **Dell, HP y Lenovo:** SVG vectoriales de [Simple Icons](https://simpleicons.org) (licencia CC0),
  con el color oficial de cada marca. Las marcas siguen siendo propiedad de sus dueños: su uso en la web
  debe cumplir las guías de cada fabricante y el acuerdo de canal/partner vigente.
  Recomendado: reemplazarlos por los archivos oficiales del portal de partners de cada marca
  (Dell Brand, HP Brand Central, Lenovo Partner Hub) conservando el mismo nombre de archivo.
- **Logitech:** no está disponible como logo libre. Mientras tanto se muestra el nombre en texto.
  Para usar el logo oficial, copie el archivo en `assets/img/brands/logitech.svg` y reemplace en
  `index-digital.html` el elemento `<li class="brand-word">Logitech</li>` por
  `<li><img src="assets/img/brands/logitech.svg" alt="Logitech" width="120" height="40"></li>`.

## Antes de publicar

- Revisar los enlaces a `https://www.consein.com/#contacto` y `#nosotros`
  y ajustarlos a las URLs reales del sitio.
- Ajustar el menú superior (`<nav class="main-nav">`) para que coincida con el del sitio principal.
