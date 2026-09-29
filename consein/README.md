# Consein · Página de Servicios

Página estática (HTML, CSS y JavaScript sin dependencias ni compilación) para la opción
**Servicios** de www.consein.com. Lista para desplegar en los ambientes de desarrollo y producción.

## Estructura

```
consein/
├── index.html                  Página de Servicios (punto de entrada)
└── assets/
    ├── consein.css             Estilos
    ├── consein.js              Interacciones (menú, subpantallas, formulario)
    ├── servicios-data.js       Contenido de las 7 subpantallas «Ver servicio»
    ├── logo-consein.png        Logo original (fondo claro)
    └── logo-consein-blanco.png Logo original (fondo oscuro)
```

## Secciones de la página

1. **Portada** – mensaje principal y escudo con las 7 etapas (cada número abre su subpantalla).
2. **Propuesta de valor** – compromiso de Consein y los pilares Escuchamos, Aprendemos, Ejecutamos y Acompañamos.
3. **Servicio en 7 etapas** – 3 fases (Solución, Transformación, Gobernanza) y el escudo transversal de ciberseguridad.
4. **Oficina de Proyectos (PMO)** – cómo se garantiza el resultado.
5. **Contacto** – formulario y canales directos.

## Subpantallas «Ver servicio»

Cada botón *Ver servicio* abre la ficha de su etapa en una ventana modal. Estructura de la ficha:
En una frase · Ideal para · Qué resuelve · Incluye · Cómo lo hacemos · Entregables · Resultado · Cómo medimos el éxito.

- El contenido se edita en `assets/servicios-data.js` (un objeto por etapa, sin tocar el HTML).
- Cada ficha tiene enlace directo: `index.html#etapa-01` … `index.html#etapa-07`.
- El botón de la ficha lleva al formulario de contacto con el servicio ya seleccionado (campo oculto `servicio`).

## Formulario de contacto

En `index.html`, el formulario tiene el atributo `data-endpoint`:

```html
<form class="form-card reveal" data-contact-form data-endpoint="" novalidate>
```

- **Vacío (desarrollo):** valida los campos y muestra la confirmación, sin enviar datos.
- **Con URL (producción):** envía los datos por `POST` como `FormData` a esa URL y muestra éxito o error
  según la respuesta HTTP.

Campos enviados: `nombre`, `empresa`, `cargo`, `correo`, `pais`, `reto`, `servicio`.

## Despliegue

- Copiar la carpeta `consein/` completa al servidor web (o a la ruta `/servicios` del sitio).
- No requiere compilación ni instalación de paquetes.
- Recursos externos: tipografías de Google Fonts (*Bricolage Grotesque* y *Nunito Sans*).
- Para probar en local: `python3 -m http.server 8000` desde la carpeta y abrir `http://localhost:8000`.

## Pendiente antes de producción

- Definir la URL del `data-endpoint` del formulario.
- Reemplazar los enlaces `#` del menú y pie «Soluciones» por las URL reales del sitio.
