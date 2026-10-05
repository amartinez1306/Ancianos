# Consein · Asesoría Licenciamiento Microsoft

Modelo de página para la opción **Asesoría Licenciamiento** del menú principal de www.consein.com.
Misma imagen que `consein.com/servicios` (azul `#1b245b`, verde `#58bb47`, Poppins/Haltto, fondos en cuadrícula).

## Cómo ejecutarlo
- Abrir `index.html` directamente en el navegador (archivo autocontenido, sin dependencias de compilación), o
- servirlo localmente: `python3 -m http.server 8000` y visitar `http://localhost:8000/consein-licenciamiento/`.

## Para producción
- URL sugerida: `https://www.consein.com/asesoria-licenciamiento`.
- Formulario: definir `data-endpoint="https://…"` en el `<form>` para enviar por POST; vacío solo valida.
- Fuente Haltto: colocar `assets/fonts/Haltto-Bold.woff2` / `.woff` junto a la página (igual que en Servicios).
- Uso del logotipo Microsoft sujeto a las guías de marca del programa Microsoft Partner.
