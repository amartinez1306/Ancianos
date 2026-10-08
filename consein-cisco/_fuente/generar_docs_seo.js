// Genera Manual_SEO_Consein_Cisco.docx y Palabras_clave_SEO_Consein_Cisco.docx desde _fuente/palabras_clave.json
// Uso (requiere Node y el paquete docx: npm install docx):  node _fuente/generar_docs_seo.js .
const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType, ShadingType,
  HeadingLevel, AlignmentType, LevelFormat, BorderStyle, Footer, PageNumber, TableOfContents,
} = require("docx");

const SITIO = process.argv[2];           // carpeta consein-cisco
const KW = JSON.parse(fs.readFileSync(SITIO + "/_fuente/palabras_clave.json", "utf8"));
// Metadatos vigentes, leídos de las páginas generadas
const limpio = t => t.replace(/<[^>]+>/g, " ").replace(/&amp;/g, "&").replace(/\s+/g, " ").trim();
const META = { h2: {} };
for (const f of ["index.html", "soluciones.html", "productos.html"]) {
  const t = fs.readFileSync(SITIO + "/" + f, "utf8");
  META[f] = { title: limpio(t.match(/<title>(.*?)<\/title>/)[1]), desc: limpio(t.match(/name="description" content="([^"]*)"/)[1]),
              h1: limpio(t.match(/<h1[^>]*>([\s\S]*?)<\/h1>/)[1]) };
}
for (const m of fs.readFileSync(SITIO + "/soluciones.html", "utf8").matchAll(/<section class="area" id="([^"]+)">[\s\S]*?<h2>([\s\S]*?)<\/h2>/g))
  META.h2[m[1]] = limpio(m[2]);

const NAVY = "000F76", MUTED = "5D6278", LINE = "D9DCE6";
const W = 9360;

const p = (text, opts = {}) => new Paragraph({ spacing: { after: 120 }, ...opts, children: [new TextRun({ text, ...(opts.run || {}) })] });
const rich = (runs, opts = {}) => new Paragraph({ spacing: { after: 120 }, ...opts, children: runs.map(r => new TextRun(r)) });
const h1 = (t, brk = true) => new Paragraph({ heading: HeadingLevel.HEADING_1, pageBreakBefore: brk, children: [new TextRun(t)] });
const h2 = t => new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun(t)] });
const bullet = (t, bold) => new Paragraph({ numbering: { reference: "bul", level: 0 }, spacing: { after: 60 },
  children: bold ? [new TextRun({ text: bold, bold: true }), new TextRun(t)] : [new TextRun(t)] });
const num = (t, ref = "num") => new Paragraph({ numbering: { reference: ref, level: 0 }, spacing: { after: 60 }, children: [new TextRun(t)] });
const check = t => new Paragraph({ numbering: { reference: "chk", level: 0 }, spacing: { after: 60 }, children: [new TextRun(t)] });
const gap = () => new Paragraph({ spacing: { after: 60 }, children: [] });

const border = { style: BorderStyle.SINGLE, size: 4, color: LINE };
const borders = { top: border, bottom: border, left: border, right: border };
function table(headers, rows, widths) {
  const cell = (text, i, head) => new TableCell({
    width: { size: widths[i], type: WidthType.DXA }, borders,
    shading: head ? { fill: NAVY, type: ShadingType.CLEAR, color: "auto" } : undefined,
    margins: { top: 70, bottom: 70, left: 110, right: 110 },
    children: String(text).split("\n").map(line => new Paragraph({ children: [new TextRun({ text: line, bold: head || (i === 0), color: head ? "FFFFFF" : undefined, size: 19 })] })),
  });
  return new Table({
    width: { size: widths.reduce((a, b) => a + b, 0), type: WidthType.DXA }, columnWidths: widths,
    rows: [new TableRow({ tableHeader: true, children: headers.map((h, i) => cell(h, i, true)) }),
      ...rows.map(r => new TableRow({ children: r.map((c, i) => cell(c, i, false)) }))],
  });
}
const KW_W = [2900, 1250, 1300, 900, 3010];
const kwRows = g => g.kw.map(k => [k[0] + (k[5] === false ? " *" : ""), k[1], k[2], k[3], k[4]]);
const kwTable = g => table(["Palabra clave", "Tipo", "Intención", "Prioridad", "Dónde está en el sitio"], kwRows(g), KW_W);
const total = KW.grupos.reduce((a, g) => a + g.kw.length, 0);
const totalA = KW.grupos.reduce((a, g) => a + g.kw.filter(k => k[3] === "A").length, 0);
const M = META;

function documento(titulo, pie, children) {
  return new Document({
    creator: "Consein", title: titulo, features: { updateFields: true },
    styles: {
      default: { document: { run: { font: "Arial", size: 21 } } },
      paragraphStyles: [
        { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
          run: { size: 32, bold: true, font: "Arial", color: NAVY }, paragraph: { spacing: { before: 240, after: 160 }, outlineLevel: 0 } },
        { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
          run: { size: 25, bold: true, font: "Arial", color: NAVY }, paragraph: { spacing: { before: 240, after: 120 }, outlineLevel: 1 } },
      ],
    },
    numbering: { config: [
      { reference: "bul", levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 540, hanging: 270 } } } }] },
      { reference: "chk", levels: [{ level: 0, format: LevelFormat.BULLET, text: "☐", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 540, hanging: 300 } } } }] },
      { reference: "num", levels: [{ level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 540, hanging: 300 } } } }] },
      { reference: "num2", levels: [{ level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 540, hanging: 300 } } } }] },
    ] },
    sections: [{
      properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 } } },
      footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.RIGHT, children: [
        new TextRun({ text: pie + "   ·   Página ", color: MUTED, size: 16 }),
        new TextRun({ children: [PageNumber.CURRENT], color: MUTED, size: 16 })] })] }) },
      children,
    }],
  });
}
const portada = (titulo, sub, nota) => [
  new Paragraph({ spacing: { before: 1800, after: 120 }, children: [new TextRun({ text: "CONSEIN", bold: true, color: MUTED, size: 20 })] }),
  new Paragraph({ spacing: { after: 160 }, children: [new TextRun({ text: titulo, bold: true, color: NAVY, size: 56 })] }),
  new Paragraph({ spacing: { after: 400 }, children: [new TextRun({ text: sub, color: NAVY, size: 30 })] }),
  p(nota, { run: { color: MUTED } }),
];

// =====================================================================================
// MANUAL SEO
// =====================================================================================
const c = [];
c.push(...portada("Manual SEO", "Soluciones Cisco de Consein · consein.com/cisco",
  "Documento editable para el equipo de marketing y contenidos · Versión 2 · Octubre 2026"));
c.push(p(`Este manual reúne la estrategia de posicionamiento del sitio Soluciones Cisco, los ajustes que ya aplicamos, las ${total} palabras clave objetivo y el plan de trabajo para llegar a las cinco primeras posiciones de Google en nuestro ámbito.`));
c.push(new Paragraph({ pageBreakBefore: true, heading: HeadingLevel.HEADING_1, children: [new TextRun("Contenido")] }),
  new TableOfContents("Contenido", { hyperlink: true, headingStyleRange: "1-1" }),
  p("Si el índice aparece vacío, haga clic derecho sobre él y elija “Actualizar campo”.", { run: { color: MUTED, size: 18 } }));

// 1. Objetivo
c.push(h1("1. Objetivo y alcance"),
  p("Queremos que Consein aparezca entre los cinco primeros resultados cuando una empresa de Venezuela, Panamá, República Dominicana o el mercado hispano de Estados Unidos busque soluciones Cisco integradas con Microsoft: conectividad SD-WAN y SASE, seguridad como servicio, control de acceso a la red, salas Teams Rooms, seguridad para IA y renovación de equipos Cisco."),
  h2("Lo que es alcanzable"),
  bullet(" búsquedas con intención comercial y modificador geográfico (por ejemplo, “integrador Cisco en Venezuela”, “seguridad como servicio Panamá”) y frases long tail (“migración de Cisco ASA a Secure Firewall”). Aquí competimos con integradores locales y el top 5 es realista en 3 a 6 meses.", "Top 5 alcanzable:"),
  bullet(" términos genéricos como “Cisco ISE”, “SD-WAN” o “Microsoft Teams Rooms”. Los dominan cisco.com, microsoft.com y medios globales. Trabajamos sus variantes locales y comerciales, que son las que convierten.", "Top 5 difícil:"),
  bullet(" ningún proveedor serio puede garantizar posiciones: las decide Google y cambian con cada actualización. Este manual maximiza la probabilidad con buenas prácticas medibles.", "Sin garantías:"),
  h2("Indicadores de éxito"),
  table(["Indicador", "Meta a 6 meses", "Herramienta"], [
    ["Palabras clave A en el top 5 (con modificador geográfico)", "60% de las prioridad A", "Google Search Console · Semrush o Ahrefs"],
    ["Palabras clave B en el top 10", "50% de las prioridad B", "Google Search Console"],
    ["Clics orgánicos al mes", "Crecimiento mensual sostenido", "Google Search Console"],
    ["CTR medio en resultados", "3% o más", "Google Search Console"],
    ["Solicitudes del formulario desde orgánico", "Medir línea base el mes 1 y crecer cada trimestre", "Google Analytics 4 (evento de envío)"],
    ["Core Web Vitals", "LCP < 2,5 s · INP < 200 ms · CLS < 0,1", "PageSpeed Insights · Search Console"],
  ], [3600, 2900, 2860]));

// 2. Ajustes aplicados
c.push(h1("2. Ajustes que aplicamos en el sitio"),
  p("Auditamos las tres páginas con la lista de palabras clave. Antes de los ajustes, la mayoría de las frases objetivo no aparecía de forma literal: de 52 frases revisadas, solo 5 estaban en el texto. Hoy las " + (total - 1) + " frases publicables aparecen en la página que les corresponde (la frase “partner Cisco Venezuela” queda pendiente hasta confirmar el nivel de partnership)."),
  table(["Elemento", "Ajuste"], [
    ["Títulos (title)", "Reescritos con la palabra clave principal al inicio y máximo 60 caracteres. Inicio incluye “Integrador Cisco y Microsoft” y los países principales."],
    ["Meta descriptions", "Reescritas en 140 a 155 caracteres, con beneficio, productos y países."],
    ["H1", "Soluciones de Valor: “Soluciones Cisco que suman valor…”. Ofertas de Productos: “renovación de equipos Cisco”. Inicio mantiene “Sinergia exponencial” y suma la palabra clave en el texto superior."],
    ["H2 por área", "Cada área lleva su palabra clave principal: SD-WAN para empresas, seguridad como servicio, control de acceso a la red (NAC), Microsoft Teams Rooms y seguridad para inteligencia artificial."],
    ["Textos", "Introducciones, fichas de producto y ofertas Renueva incluyen las frases objetivo de forma natural, en primera persona y sin relleno."],
    ["Preguntas frecuentes", "Tres preguntas nuevas: trabajo con otras nubes, equipos Cisco en fin de soporte y países donde atendemos. Están marcadas como FAQPage para resultados enriquecidos."],
    ["Jerarquía de encabezados", "Un solo H1 por página; las fichas de detalle pasan a H3 para respetar el orden H1 › H2 › H3."],
    ["Canonical y Open Graph", "Apuntan a la URL real de cada archivo (soluciones.html, productos.html)."],
    ["Robots y hreflang", "Meta robots index, follow y hreflang es / x-default en cada página."],
    ["sitemap.xml y robots.txt", "Se generan automáticamente con el sitio."],
    ["Datos estructurados", "Organization con descripción y temas de especialidad (knowsAbout), WebPage, BreadcrumbList, ItemList de Service (11 + 8) con categoría y FAQPage (9 preguntas)."],
    ["Mensaje multinube", "Microsoft sigue como BASE en todos los titulares. Cada ficha suma la fila “También en otras plataformas” (AWS, Google Cloud, Google Workspace, Webex, otras MDM y SIEM), cada área muestra “También en:” y hay una pregunta frecuente nueva: “¿Trabajan solo con Microsoft?”."],
    ["Verificador", "Script _fuente/verificar_seo.py: confirma que cada palabra clave aparece en su página después de cualquier cambio de texto."],
  ], [2400, 6960]));

// 3. Mapa por página
c.push(h1("3. Mapa de palabras clave por página"),
  p("Cada página compite por un grupo de búsquedas. Así evitamos que dos páginas propias compitan entre sí (canibalización)."),
  table(["Página", "Palabra clave principal", "Title vigente", "H1 vigente"], [
    ["Inicio\nindex.html", "integrador Cisco y Microsoft", M["index.html"].title, M["index.html"].h1],
    ["Soluciones de Valor\nsoluciones.html", "soluciones Cisco · SD-WAN · SECaaS", M["soluciones.html"].title, M["soluciones.html"].h1],
    ["Ofertas de Productos\nproductos.html", "renovación de equipos Cisco", M["productos.html"].title, M["productos.html"].h1],
  ], [1900, 2200, 2700, 2560]),
  gap(), h2("Meta descriptions vigentes"),
  table(["Página", "Meta description", "Caracteres"],
    ["index.html", "soluciones.html", "productos.html"].map(f => [f, M[f].desc, String(M[f].desc.length)]), [1900, 6260, 1200]),
  gap(), h2("H2 de cada área de práctica"),
  table(["Área", "H2 vigente", "Línea Consein"], [
    ["Conectividad LAN y WAN", M.h2.conectividad, "Infraestructura"],
    ["SECaaS", M.h2.secaas, "Seguridad"],
    ["Red local y perímetro", M.h2["proteccion-red"], "Seguridad"],
    ["Colaboración", M.h2.colaboracion, "Colaboración"],
    ["Inteligencia Artificial", M.h2["inteligencia-artificial"], "IA"],
  ], [2400, 5160, 1800]));

// 4. Palabras clave
c.push(h1("4. Palabras clave objetivo"),
  p(`${total} palabras clave en ${KW.grupos.length} grupos; ${totalA} son de prioridad A. La lista maestra está en _fuente/palabras_clave.json: edite ese archivo y vuelva a generar este manual para mantener todo alineado.`),
  bullet(" término central del grupo; va en el title, el H1 o el H2.", "Principal:"),
  bullet(" término de apoyo con volumen relevante.", "Secundaria:"),
  bullet(" frase específica, con menos competencia y mayor conversión.", "Long tail:"),
  bullet(" nombre exacto de producto o paquete.", "Producto:"),
  bullet(" A = meta top 5 en 6 meses; B = top 10; C = soporte semántico.", "Prioridad:"),
  rich([{ text: "* ", bold: true }, "No se publica hasta confirmar el nivel de partnership vigente de Consein con Cisco."]),
  rich([{ text: "Validación pendiente: ", bold: true }, "confirme volúmenes y dificultad por país con Google Keyword Planner, Semrush o Ahrefs antes de fijar metas definitivas. Ajuste la prioridad de los términos sin volumen."]),
  h2("Modificadores geográficos"),
  p("Combine las palabras clave de prioridad A con estos modificadores en títulos de artículos, perfiles de Google Business y páginas por país:"),
  table(["País", "Modificadores"], KW.paises, [2600, 6760]));
KW.grupos.forEach(g => {
  c.push(h2(g.titulo),
    rich([{ text: "Página: ", bold: true }, { text: g.pagina }, { text: "   ·   Objetivo: ", bold: true }, { text: g.objetivo }]),
    kwTable(g), gap());
});

// 5. Redacción
c.push(h1("5. Reglas de redacción SEO"),
  p("Estas reglas combinan las buenas prácticas de SEO con los lineamientos de forma de Consein."),
  h2("Lineamientos Consein"),
  bullet("Escribimos en primera persona del plural: “Conectamos”, “Protegemos”, “Renovamos”."),
  bullet("Títulos cortos y directos. Evitamos dobles negaciones y fórmulas como “no es esto, es aquello”."),
  bullet("Estilo minimalista: una idea por frase y sin redundancias."),
  bullet("Microsoft es nuestra BASE y va primero en titulares y argumentos. En cada área decimos también qué aportamos en AWS, Google Cloud y otras plataformas, para no perder a las empresas que operan en varias nubes."),
  bullet("Tipografías: Haltto en títulos y Poppins en párrafos. Paleta digital #1b245b y #58bb47."),
  h2("Buenas prácticas SEO"),
  num("La palabra clave principal va en el title, el H1 (o H2 del área), el primer párrafo y, cuando exista, la URL."),
  num("Usamos cada frase objetivo una o dos veces por sección, de forma natural. Repetirla de más perjudica el posicionamiento."),
  num("Escribimos los nombres de producto exactos: Cisco Meraki, Cisco Catalyst SD-WAN, Cisco ISE, Cisco Secure Firewall, Microsoft Teams Rooms. Escribimos “Wi-Fi” con guion."),
  num("Incluimos el país o la ciudad cuando el contexto lo permite (“para empresas en Venezuela, Panamá…”)."),
  num("Cada ficha responde qué es, para quién es, qué incluye y qué resultado entrega: así cubrimos la intención de búsqueda completa."),
  num("Los enlaces internos usan texto descriptivo (“seguridad como servicio”), nunca “haga clic aquí”."),
  num("Toda imagen nueva lleva texto alternativo que describe su contenido."),
  num("Las preguntas frecuentes repiten la forma en que el cliente pregunta (“¿Qué hacemos con los equipos Cisco en fin de soporte?”)."),
  h2("Contenido que no se publica"),
  p("Por decisión comercial, estos temas no aparecen en el sitio ni en artículos: “Better Together” y “Microsoft primero”, el posicionamiento por licencia Microsoft 365, los paquetes User Protection y Breach Protection, Cisco XDR, NDR y Telemetry Broker, la parte de negocio de SECaaS (ingresos recurrentes, plazos, multi-tenant) y las secciones internas de la matriz de valor."));

// 6. Metadatos
c.push(h1("6. Plantillas de metadatos"),
  table(["Elemento", "Regla", "Plantilla / ejemplo"], [
    ["Title", "Máximo 60 caracteres. Palabra clave al inicio y marca al final.", "[Palabra clave principal] [en País] | Consein\nEj.: Seguridad como servicio en Panamá | Consein"],
    ["Meta description", "140 a 155 caracteres. Beneficio + productos + país. Sin comillas dobles.", "[Qué hacemos] con [productos]. [Beneficio]. [Países]."],
    ["H1", "Uno por página. Puede ser de marca si el title y el primer párrafo llevan la palabra clave.", "Programa Renueva: renovación de equipos Cisco"],
    ["URL", "Corta, en minúsculas, con guiones y sin acentos.", "/cisco/seguridad-como-servicio/"],
    ["Open Graph", "Mismo title y description; imagen de 1200 × 630 px.", "Pendiente: diseñar imagen para redes sociales"],
  ], [1700, 3600, 4060]));

// 7. Técnico
c.push(h1("7. SEO técnico"),
  h2("Antes de publicar"),
  check("Ajustar URL_BASE en _fuente/generar_sitio.py a la URL definitiva y regenerar el sitio."),
  check("Publicar con HTTPS y redirigir http → https y la versión sin www → con www (o al revés, pero siempre la misma)."),
  check("Copiar las reglas de robots.txt en el robots.txt de la raíz del dominio: los buscadores solo leen ese archivo."),
  check("Subir sitemap.xml y enviarlo en Google Search Console y en Bing Webmaster Tools."),
  check("Verificar la propiedad del dominio en Search Console (registro DNS) y en Bing."),
  check("Validar los datos estructurados con la Prueba de resultados enriquecidos de Google y con validator.schema.org."),
  check("Medir Core Web Vitals con PageSpeed Insights en móvil y escritorio."),
  check("Si el sitio reemplaza páginas anteriores de consein.com, crear redirecciones 301 desde cada URL antigua a la nueva equivalente."),
  check("Instalar Google Analytics 4 con un evento de conversión en el envío del formulario y conectar el formulario al CRM."),
  h2("Recomendaciones de arquitectura"),
  bullet(" hoy las URLs terminan en .html. Si el servidor lo permite, use URLs limpias (/cisco/soluciones/) con redirección 301 desde la versión .html y actualice el canonical.", "URLs limpias:"),
  bullet(" la mayor oportunidad es crear una página propia por área (por ejemplo, /cisco/seguridad-como-servicio/) con 600 a 900 palabras, su propio title y H1. SECaaS y Renueva son las prioridades.", "Una URL por área:"),
  bullet(" si se crean versiones por país, declarar hreflang es-VE, es-PA, es-DO y es-US entre ellas.", "Páginas por país:"),
  bullet(" el contenido de “Seguir leyendo…” ya está en el HTML y es indexable. Mantenga ese patrón: no cargue textos importantes solo con JavaScript.", "Contenido indexable:"),
  bullet(" las versiones de un solo archivo (Consein_Cisco_sitio_completo.html y diseño digital) son para presentaciones. No las publique: duplicarían el contenido.", "Versiones de presentación:"));

// 8. Local
c.push(h1("8. SEO local"),
  p("Para búsquedas con país o ciudad, Google pondera la relevancia local. Estos pasos suelen tener el mayor impacto en el corto plazo:"),
  num("Crear o completar un perfil de Google Business por cada oficina (Venezuela, Panamá, República Dominicana, Estados Unidos), con categoría principal “Consultor de informática” o “Servicio de redes informáticas”, horario, fotos y enlace a /cisco/.", "num2"),
  num("Mantener nombre, dirección y teléfono (NAP) idénticos en el sitio, los perfiles y los directorios.", "num2"),
  num("Pedir reseñas a clientes satisfechos que mencionen el servicio (“implementación de Teams Rooms”, “SD-WAN”).", "num2"),
  num("Registrarnos en el localizador de partners de Cisco y en el directorio de partners de Microsoft, con enlace al sitio.", "num2"),
  num("Aparecer en cámaras de comercio y gremios TIC de cada país, con enlace al sitio.", "num2"),
  num("Agregar al pie del sitio la dirección y el teléfono de cada oficina y marcarlos con schema.org PostalAddress (pendiente: datos de oficinas).", "num2"));

// 9. Autoridad
c.push(h1("9. Autoridad y enlaces"),
  bullet(" un caso por área con datos medidos del cliente (tiempo de activación, reducción de incidentes, ahorro). Son el contenido que más enlaces y confianza genera.", "Casos de éxito:"),
  bullet(" difundir hitos como el reconocimiento WITSA 2026 a ARIA IA Generativa, con enlace a la página correspondiente.", "Notas de prensa:"),
  bullet(" contenidos conjuntos y eventos con Cisco y Microsoft que enlacen a nuestras páginas.", "Co-marketing:"),
  bullet(" artículos de opinión en medios de tecnología y negocios de cada país.", "Medios locales:"),
  bullet(" publicar cada artículo en la página de LinkedIn de Consein y en los perfiles de los especialistas.", "LinkedIn:"),
  p("Evite comprar enlaces o participar en redes de enlaces: Google lo penaliza."));

// 10. Plan de contenidos
c.push(h1("10. Plan de contenidos"),
  p("Un artículo pilar por área y artículos satélite de long tail que enlacen al pilar y a la sección del sitio. Ritmo sugerido: dos artículos al mes."),
  table(["Área", "Artículos sugeridos", "Palabra clave objetivo"], [
    ["SECaaS", "Qué es SECaaS y cuándo conviene a una empresa\nZTNA o VPN: cómo dar acceso seguro a usuarios remotos\nCómo elegir un proveedor de ciberseguridad administrada", "seguridad como servicio · alternativa a la VPN tradicional · ciberseguridad administrada para empresas"],
    ["Conectividad", "SD-WAN o MPLS: qué conviene a sus sucursales\nQué es SASE y cómo se implementa con Cisco Meraki\nCómo conectar sucursales a Azure", "SD-WAN para empresas · arquitectura SASE · conectividad de sucursales a Azure"],
    ["Red local y perímetro", "Qué es NAC y cómo controla el acceso a su red\nCómo migrar de Cisco ASA a Secure Firewall", "control de acceso a la red (NAC) · migración de Cisco ASA a Secure Firewall"],
    ["Colaboración", "Cómo equipar una sala Microsoft Teams Rooms\nCisco Room Bar o Board Pro: cuál elegir según la sala", "Microsoft Teams Rooms · salas de reuniones para Teams"],
    ["Multinube", "Cisco con Microsoft, AWS y Google Cloud: una red y una seguridad para varias nubes\nCómo conectar sus sedes a AWS y Google Cloud con SD-WAN", "SD-WAN multinube · seguridad multinube · conectividad a AWS y Google Cloud"],
    ["IA", "Seguridad para IA generativa en la empresa\nCómo hacer un inventario de activos de IA", "seguridad para inteligencia artificial · inventario de activos de IA"],
    ["Programa Renueva", "Cómo saber si sus equipos Cisco están en end of life\nQué implica la directiva BOD 26-02 para su red\nCómo financiar la renovación tecnológica", "equipos Cisco en fin de soporte · end of life · financiamiento para renovación tecnológica"],
  ], [1700, 4360, 3300]),
  gap(),
  p("Cada artículo: 900 a 1.500 palabras, palabra clave en el title, H1, URL y primer párrafo; dos o tres enlaces internos; un llamado a la acción al formulario de contacto con el interés preseleccionado (por ejemplo, index.html?interes=secaas#contacto)."));

// 11. Plan 90 días
c.push(h1("11. Plan de 90 días"),
  table(["Periodo", "Acciones", "Responsable"], [
    ["Semanas 1 y 2", "Publicar el sitio. Robots, sitemap, Search Console, Bing, GA4 y conversión del formulario. Validar datos estructurados.", "Desarrollo web"],
    ["Semanas 3 y 4", "Perfiles de Google Business por país. Directorios de partners Cisco y Microsoft. Validar volúmenes de palabras clave.", "Marketing"],
    ["Mes 2", "Página propia para SECaaS y para Programa Renueva. Primeros cuatro artículos (SECaaS y Renueva). Primer caso de éxito.", "Marketing + especialistas"],
    ["Mes 3", "Cuatro artículos más (Conectividad y Red local). Revisión de posiciones y CTR; ajustar titles y descriptions con CTR bajo.", "Marketing"],
    ["Cada mes", "Informe de posiciones, clics, CTR y solicitudes. Ejecutar verificar_seo.py tras cada cambio de texto.", "Marketing"],
  ], [1700, 5660, 2000]));

// 12. Cómo editar
c.push(h1("12. Cómo editar y verificar"),
  table(["Qué quiere cambiar", "Dónde se edita"], [
    ["Textos de áreas, fichas y ofertas", "_fuente/generar_sitio.py: ESPECIALIDADES, MATRIZ, SECAAS_DIF, PRODUCTOS"],
    ["Preguntas frecuentes", "_fuente/generar_sitio.py: FAQ"],
    ["Title y meta description", "_fuente/generar_sitio.py: llamadas a pagina(...) al final de inicio(), soluciones() y productos()"],
    ["URL definitiva", "_fuente/generar_sitio.py: URL_BASE"],
    ["Lista de palabras clave", "_fuente/palabras_clave.json"],
  ], [3200, 6160]),
  gap(),
  p("Después de editar, ejecute en la carpeta consein-cisco:"),
  p("python3 _fuente/generar_sitio.py", { run: { font: "Consolas" } }),
  p("python3 _fuente/verificar_seo.py", { run: { font: "Consolas" } }),
  p("El primer comando regenera las páginas, sitemap.xml y robots.txt. El segundo lista cada palabra clave con OK o FALTA según aparezca en su página; corrija los FALTA antes de publicar."));

// 13. Pendientes
c.push(h1("13. Pendientes de validación"),
  check("Confirmar el nivel de partnership con Cisco para usar “partner Cisco” en el sitio."),
  check("Definir la URL definitiva del sitio (URL_BASE)."),
  check("Validar volúmenes de búsqueda por país y ajustar prioridades."),
  check("Datos de oficinas (dirección y teléfono) para el pie y los perfiles de Google Business."),
  check("Imagen Open Graph de 1200 × 630 px."),
  check("Decidir si Cisco AI Defense sigue publicado mientras está en validación."),
  check("Decidir si se agrega Datacenter al acelerador y una oferta de renovación de datacenter."));

// =====================================================================================
// LISTA DE PALABRAS CLAVE (v3)
// =====================================================================================
const k = [];
k.push(...portada("Palabras clave SEO", "Soluciones Cisco de Consein · 5 áreas de práctica y Programa Renueva",
  "Documento editable para el equipo SEO · Versión 4 · Octubre 2026"));
k.push(p(`${total} palabras clave en ${KW.grupos.length} grupos (${totalA} de prioridad A). La estrategia, las reglas de uso y el plan de trabajo están en el Manual SEO. Esta lista se genera desde _fuente/palabras_clave.json.`),
  rich([{ text: "Prioridad: ", bold: true }, "A = meta top 5 en 6 meses; B = top 10; C = soporte semántico.   ", { text: "* ", bold: true }, "Pendiente de confirmar el nivel de partnership."]),
  h2("Modificadores geográficos"), table(["País", "Modificadores"], KW.paises, [2600, 6760]));
KW.grupos.forEach((g, i) => {
  k.push(h1(g.titulo, i === 0), rich([{ text: "Página: ", bold: true }, { text: g.pagina }]),
    rich([{ text: "Objetivo: ", bold: true }, { text: g.objetivo }]), kwTable(g));
});

Promise.all([
  Packer.toBuffer(documento("Manual SEO · Soluciones Cisco de Consein", "Consein · Manual SEO · Soluciones Cisco", c))
    .then(b => fs.writeFileSync(SITIO + "/Manual_SEO_Consein_Cisco.docx", b)),
  Packer.toBuffer(documento("Palabras clave SEO · Soluciones Cisco de Consein · v3", "Consein · Palabras clave SEO · Soluciones Cisco", k))
    .then(b => fs.writeFileSync(SITIO + "/Palabras_clave_SEO_Consein_Cisco.docx", b)),
]).then(() => console.log("ok", total, totalA));
