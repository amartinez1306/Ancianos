# Consein · Asesoría Licenciamiento Microsoft

Modelo de página para la opción **Asesoría Licenciamiento** del menú principal de www.consein.com.
Misma imagen que `consein.com/servicios` (azul `#1b245b`, verde `#58bb47`, Poppins/Haltto, fondos en cuadrícula).

## Cómo ejecutarlo
- Abrir `index.html` directamente en el navegador (archivo autocontenido, sin dependencias de compilación), o
- servirlo localmente: `python3 -m http.server 8000` y visitar `http://localhost:8000/consein-licenciamiento/`.

## Para producción
- URL de publicación: `https://www.consein.com/licenciamiento-microsoft` (es la URL canónica declarada en la página; si se publica en otra, actualizar `canonical`, `og:url` y los datos estructurados).
- Formulario: definir `data-endpoint="https://…"` en el `<form>` para enviar por POST; vacío solo valida.
- Fuente Haltto: colocar `assets/fonts/Haltto-Bold.woff2` / `.woff` junto a la página (igual que en Servicios).
- Uso del logotipo Microsoft sujeto a las guías de marca del programa Microsoft Partner.
