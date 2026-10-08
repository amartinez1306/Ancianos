# Consein · Soluciones Cisco (sitio)

Sitio de la sección Cisco de consein.com: Microsoft como BASE, Cisco como acelerador.

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
| `index.html` | Inicio | Sinergia exponencial con sticker "Inventario gratis", enfoque, 5 áreas de práctica (incluida SECaaS), Cómo trabajamos (los siete pasos aplicados a Cisco), resultados, nosotros, contacto (llamado a la acción) y preguntas frecuentes |
| `soluciones.html` | Soluciones Cisco › Soluciones de Valor | Criterio, vista consolidada y 11 soluciones en 5 áreas: Conectividad LAN y WAN, SECaaS (Essential y Advantage), Red local y perímetro (ISE y Secure Firewall, por separado), Colaboración e IA |
| `productos.html` | Soluciones Cisco › Ofertas de Productos | Aviso "Inventariamos gratis su hardware Cisco", por qué renovar, autodiagnóstico, rutas, método y 8 ofertas |

Menú: **Inicio · Soluciones Cisco · Nosotros · Contacto**. Soluciones Cisco despliega dos opciones de segundo nivel,
Soluciones de Valor (5 áreas de práctica) y Ofertas de Productos (8 ofertas del Programa Renueva).

**Soluciones de Valor** se construye con la parte de productos (secciones A y B) de
`Nueva_Matriz_Valor_Cisco_Microsoft_Consein_v2.docx` y con `Iniciativa_SECaaS.docx` (paquetes Essential y Advantage,
en `MATRIZ` y `SECAAS_DIF`). No se publican: "Better Together", el posicionamiento por licencia, los paquetes
User Protection / Breach Protection, las secciones internas de la matriz (reglas de uso, C, D, E, F, Estado) ni
la parte de negocio de SECaaS (ingresos recurrentes, plazos, multi-tenant). Datos en `ESPECIALIDADES`, `CRITERIOS` y `MATRIZ`. Cada área muestra su línea de Soluciones Consein
(campo `linea`: Infraestructura, Seguridad, Colaboración, IA) como título sobre el encabezado y en las tarjetas. Cada producto muestra su
**nombre y mensaje comercial**; "Seguir leyendo…" abre En Microsoft (nuestra BASE), También en otras plataformas
(AWS, Google Cloud y otras; campo `otras`), Cómo agrega valor y Servicio Consein (por ejemplo `soluciones.html#cisco-ise`).
En **Ofertas de Productos**, la subpantalla muestra Ideal para, Qué resolvemos, Qué incluye y Resultado.

## Aviso de renovación de hardware
- **Inicio, Soluciones de Valor y Ofertas de Productos:** sticker circular discreto en el encabezado ("Inventario gratis", con el texto giratorio
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

## Matriz de valor (uso interno)
`Nueva_Matriz_Valor_Cisco_Microsoft_Consein_v3.docx` consolida lo incorporado: SECaaS, ISE y Secure Firewall por
separado, venta directa de User/Breach Protection, Programa Renueva, los siete pasos, decisiones pendientes y cambios.
No se publica en el sitio.

## SEO
- **`Manual_SEO_Consein_Cisco.docx`** (editable): objetivo y alcance, ajustes aplicados, mapa de palabras clave por página,
  reglas de redacción, plantillas de metadatos, SEO técnico y local, plan de contenidos, plan de 90 días y pendientes.
- **`Palabras_clave_SEO_Consein_Cisco.docx`** (v3): la lista de palabras clave por área y para el Programa Renueva.
- **Lista maestra:** `_fuente/palabras_clave.json`. Los dos documentos se generan desde ahí:
  `node _fuente/generar_docs_seo.js .` (requiere `npm install docx`).
- **Verificación:** `python3 _fuente/verificar_seo.py` confirma que cada palabra clave aparece en su página.
- El sitio genera `sitemap.xml` y `robots.txt` (copie sus reglas en el robots.txt de la raíz del dominio), e incluye
  title y description por página, canonical, hreflang, Open Graph y datos estructurados schema.org
  (Organization, WebPage, BreadcrumbList, Service, FAQPage).

## Antes de publicar
- Confirmar el nivel de partnership y las certificaciones Cisco vigentes de Consein.
- Validar la capacidad de entrega de cada oferta (en especial AI Defense, Hypershield y Secure AI Factory).
- Revisar CSC-09 frente a Microsoft Entra Global Secure Access.
- Acordar con los bancos locales de cada país el proceso de evaluación para la Renovación financiada (REN-07).
- Conectar el formulario de contacto al CRM (hoy es una maqueta).
