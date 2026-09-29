# Consein · Página de Hardware

Subpágina de **www.consein.com** que se abre al hacer clic en la opción **Hardware** del menú.
Es un sitio estático (HTML + CSS + JS), sin dependencias ni proceso de compilación.

```
consein-hardware/
├── index.html              # Página
├── assets/css/styles.css   # Estilos (colores del logo: #000F76 / #61FC22)
├── assets/js/main.js       # Menú móvil, pestañas, navegación por secciones
├── assets/img/logo-consein.jpg
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

## Antes de publicar

- Revisar los enlaces a `https://www.consein.com/#contacto`, `#servicios` y `#nosotros`
  y ajustarlos a las URLs reales del sitio.
- Ajustar el menú superior (`<nav class="main-nav">`) para que coincida con el del sitio principal.
