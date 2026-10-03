#!/usr/bin/env python3
"""Genera el sitio Consein · Soluciones Cisco (index.html, soluciones.html, productos.html).

Todo el contenido vive en este archivo. Para editar un texto:
  1. Cambie el texto aquí.
  2. Ejecute:  python3 _fuente/generar_sitio.py
  3. Abra index.html en el navegador.
"""
import html
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
URL_BASE = "https://www.consein.com/cisco/"  # ajustar a la URL definitiva
E = html.escape
TEMA = "minimal"   # "minimal" o "digital" (ver __main__)
GEN = {}           # páginas generadas en memoria para la versión de un solo archivo


def D(fragmento):
    """Devuelve el fragmento solo en el tema digital."""
    return fragmento if TEMA == "digital" else ""


_ICONOS = {
    "infraestructura": '<rect x="3" y="3" width="7" height="5" rx="1"/><rect x="14" y="3" width="7" height="5" rx="1"/><rect x="8.5" y="16" width="7" height="5" rx="1"/><path d="M6.5 8v3h11V8M12 11v5"/>',
    "seguridad": '<path d="M12 3l7 3v5c0 4.5-3 8.3-7 10-4-1.7-7-5.5-7-10V6z"/><path d="M9 12l2 2 4-4"/>',
    "colaboracion": '<rect x="3" y="6" width="13" height="12" rx="2"/><path d="M16 10l5-3v10l-5-3"/>',
    "data-analitica": '<path d="M4 20h16"/><path d="M7 16v-4M11 16V8M15 16v-6M19 16V5"/>',
    "servicios-empresariales": '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5a1 1 0 011-1h4a1 1 0 011 1v2M3 13h18"/>',
    "automatizacion": '<path d="M20 12a8 8 0 01-14.3 4.9M4 12a8 8 0 0114.3-4.9"/><path d="M18.5 3v4.3h-4.3M5.5 21v-4.3h4.3"/>',
    "inteligencia-artificial": '<rect x="6" y="6" width="12" height="12" rx="2"/><path d="M9 2v4M15 2v4M9 18v4M15 18v4M2 9h4M2 15h4M18 9h4M18 15h4"/><path d="M10 10h4v4h-4z"/>',
    "integral": '<path d="M12 12c-2-2.7-3.6-4-5.3-4C4.6 8 3 9.8 3 12s1.6 4 3.7 4c1.7 0 3.3-1.3 5.3-4zm0 0c2 2.7 3.6 4 5.3 4 2.1 0 3.7-1.8 3.7-4s-1.6-4-3.7-4c-1.7 0-3.3 1.3-5.3 4z"/>',
    "calendario": '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
    "certificado": '<circle cx="12" cy="9" r="5"/><path d="M9 13.5L8 21l4-2 4 2-1-7.5"/>',
    "trofeo": '<path d="M8 4h8v5a4 4 0 01-8 0zM8 6H5a3 3 0 003 4M16 6h3a3 3 0 01-3 4M12 13v4M9 21h6M10 17h4v4h-4z"/>',
    "objetivo": '<circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="4"/><circle cx="12" cy="12" r="1"/>',
}


def icono(nombre):
    return ('<span class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{_ICONOS[nombre]}</svg></span>')


def arte_hero():
    """Diagrama de red animado: Microsoft al centro, nodos Cisco y el anillo integrador de Consein."""
    import math
    cx, cy, r = 280, 260, 160
    nodos = ["SD&#45;WAN", "Zero Trust", "Teams Rooms", "ThousandEyes", "AI Defense", "Meraki"]
    lineas, paquetes, puntos = [], [], []
    for i, n in enumerate(nodos):
        a = math.radians(-90 + 60 * i)
        x, y = cx + r * math.cos(a), cy + r * math.sin(a)
        lineas.append(f'<path class="flow" d="M{cx} {cy} L{x:.1f} {y:.1f}"/>')
        paquetes.append(f'<circle r="3.2" class="packet"><animateMotion dur="{2.2 + i * 0.35:.2f}s" repeatCount="indefinite" '
                        f'path="M{cx} {cy} L{x:.1f} {y:.1f}"/></circle>')
        lx, ly = cx + (r + 50) * math.cos(a), cy + (r + 50) * math.sin(a) + 4
        anchor = "middle" if abs(math.cos(a)) < 0.2 else ("start" if math.cos(a) > 0 else "end")
        if anchor != "middle":
            lx = x + (42 if anchor == "start" else -42)
            ly = y + 4
        puntos.append(f'<circle class="pulse" cx="{x:.1f}" cy="{y:.1f}" r="22"/>'
                      f'<circle class="node" cx="{x:.1f}" cy="{y:.1f}" r="22"/>'
                      f'<circle class="node-dot" cx="{x:.1f}" cy="{y:.1f}" r="5"/>'
                      f'<text class="node-label" x="{lx:.1f}" y="{ly:.1f}" text-anchor="{anchor}">{n}</text>')
    return f"""<div class="hero-art" aria-hidden="true">
<svg viewBox="0 0 560 520" role="img">
  <defs>
    <radialGradient id="g-core" cx="50%" cy="40%" r="60%"><stop offset="0" stop-color="#2d3a8c"/><stop offset="1" stop-color="#1b245b"/></radialGradient>
    <radialGradient id="g-glow"><stop offset="0" stop-color="#58bb47" stop-opacity=".35"/><stop offset="1" stop-color="#58bb47" stop-opacity="0"/></radialGradient>
    <path id="arco" d="M{cx} {cy} m-232 0 a232 232 0 1 1 464 0 a232 232 0 1 1 -464 0"/>
  </defs>
  <circle cx="{cx}" cy="{cy}" r="200" fill="url(#g-glow)"/>
  <g class="orbit"><circle cx="{cx}" cy="{cy}" r="232" class="ring-outer"/>
    <text class="ring-text"><textPath href="#arco" startOffset="2%">CONSEIN · INTEGRAMOS Y OPERAMOS · UN SOLO RESPONSABLE · CONSEIN · INTEGRAMOS Y OPERAMOS · UN SOLO RESPONSABLE ·</textPath></text></g>
  <circle cx="{cx}" cy="{cy}" r="{r}" class="ring-mid"/>
  {''.join(lineas)}
  {''.join(paquetes)}
  {''.join(puntos)}
  <circle cx="{cx}" cy="{cy}" r="78" class="core-halo"/>
  <circle cx="{cx}" cy="{cy}" r="66" fill="url(#g-core)" class="core"/>
  <path d="M258 262a14 14 0 0 1 3-27.6 19 19 0 0 1 36.5 4.6 12 12 0 0 1 2.5 23z" class="cloud" transform="translate(0 -12)"/>
  <text x="{cx}" y="{cy + 22}" text-anchor="middle" class="core-label">MICROSOFT</text>
  <text x="{cx}" y="{cy + 38}" text-anchor="middle" class="core-sub">base</text>
</svg></div>"""


ARTE_CAPAS = """<div class="stack" aria-hidden="true">
  <div class="layer l1"><span class="tag">Base</span><b>Microsoft</b><small>Identidad · Microsoft 365 · Azure · Dynamics 365 · IA</small></div>
  <div class="layer l2"><span class="tag">Acelerador</span><b>Cisco</b><small>Red · Seguridad perimetral · Salas · Observabilidad</small></div>
  <div class="layer l3"><span class="tag">Integrador</span><b>Consein</b><small>Diseñamos, implementamos y operamos con un solo responsable</small></div>
</div>"""

# ---------------------------------------------------------------------------
# Especialidades (7) — cada una apunta a un grupo de palabras clave SEO
# ---------------------------------------------------------------------------
ESPECIALIDADES = [
    # Fuente única: Nueva Matriz de Valor Cisco + Microsoft (Consein, ver. 1). Sección A y B.
    {"id": "infraestructura", "nombre": "Infraestructura",
     "h2": "Conectividad de sedes, WAN y red local",
     "intro": "Conectamos sedes, WAN y red local: la base sobre la que operan Microsoft 365 y Azure."},
    {"id": "seguridad", "nombre": "Seguridad",
     "h2": "Seguridad de red para el stack Microsoft",
     "intro": "Sumamos controles de red y telemetría que refuerzan su seguridad Microsoft, con una sola consola."},
    {"id": "colaboracion", "nombre": "Colaboración",
     "h2": "Hardware certificado para Microsoft Teams Rooms",
     "intro": "Implementamos hardware Cisco certificado para la experiencia Microsoft Teams Rooms."},
    {"id": "data-analitica", "nombre": "Data y Analítica",
     "h2": "Datos físicos y operativos para Power BI y Fabric",
     "intro": "Aportamos datos físicos y operativos que enriquecen la analítica de Power BI y Microsoft Fabric."},
    {"id": "servicios-empresariales", "nombre": "Servicios Empresariales",
     "h2": "Conectividad y acceso seguro para Dynamics 365",
     "intro": "Conectamos y protegemos el acceso a sus aplicaciones de negocio en Dynamics 365."},
    {"id": "automatizacion", "nombre": "Automatización",
     "h2": "Automatización de red con Power Platform",
     "intro": "Orquestamos eventos y acciones de red desde Power Platform."},
    {"id": "inteligencia-artificial", "nombre": "Inteligencia Artificial",
     "h2": "Seguridad del ciclo de vida de modelos y agentes de IA",
     "intro": "Aportamos seguridad especializada para el ciclo de vida de sus modelos y agentes de IA."},
]

# Criterio de selección (Nueva Matriz de Valor)
CRITERIOS = [
    ("Operan en otra capa", "Productos que trabajan en una capa distinta a la de Microsoft."),
    ("Se integran de forma nativa", "Productos que se conectan con la plataforma Microsoft de forma nativa."),
    ("Extienden una capacidad", "Productos que amplían una capacidad con una sola función, consola y licencia por necesidad."),
]

# Productos Cisco por área (Nueva Matriz de Valor, sección B). 19 entradas.
# Campos: area, id, nombre, origen (servicio del Modelo de Servicios Cisco de Consein), capa,
# ms (producto Microsoft asociado), valor (visible en la tarjeta) y extra (se suma en el detalle).
MATRIZ = [
    {"area": "infraestructura", "id": "meraki-mx", "nombre": "Meraki MX Security & SD-WAN",
     "origen": ["S3 · Meraki Cloud Managed", "S5 · SD-WAN Seguro"], "capa": "Seguridad perimetral y SD-WAN de sucursal",
     "ms": "Azure Virtual WAN / Microsoft 365",
     "valor": "Conectamos sus sucursales a Azure Virtual WAN con gestión en la nube y priorizamos el tráfico de Microsoft 365 y Teams.",
     "extra": "Aporta el equipo de borde de cada sede, una capa que complementa a Microsoft."},
    {"area": "infraestructura", "id": "cisco-sdwan-catalyst", "nombre": "Cisco SD-WAN (Catalyst) para DC/HQ e IaaS",
     "origen": ["S5 · SD-WAN Seguro"], "capa": "Overlay WAN entre centro de datos, sedes y nube",
     "ms": "Azure Virtual WAN / ExpressRoute",
     "valor": "Extendemos las políticas por aplicación hasta Azure IaaS, con failover y visibilidad del desempeño.",
     "extra": "Azure aporta el destino cloud y Cisco, el transporte."},
    {"area": "infraestructura", "id": "meraki-ms-mr", "nombre": "Meraki MS (switching) y MR (wireless)",
     "origen": ["S3 · Meraki Cloud Managed"], "capa": "Red LAN/WLAN gestionada en la nube",
     "ms": "Microsoft Teams / Microsoft 365",
     "valor": "Entregamos la red física y el Wi-Fi con QoS para la voz y el video de Teams.",
     "extra": "Es una capa de red que complementa a Microsoft."},
    {"area": "infraestructura", "id": "meraki-mg", "nombre": "Meraki MG (cellular gateways)",
     "origen": ["S3 · Meraki Cloud Managed"], "capa": "Enlace celular 4G/5G de respaldo",
     "ms": "Microsoft 365 / Azure",
     "valor": "Mantenemos el acceso a Microsoft 365 y Azure cuando falla el enlace principal de la sede."},

    {"area": "seguridad", "id": "secure-firewall", "nombre": "Cisco Secure Firewall",
     "origen": ["S6 · Azure + Cisco Secure Firewall"], "capa": "Firewall NGFW/IPS on-premise y virtual en Azure",
     "ms": "Azure Firewall / Microsoft Sentinel",
     "valor": "Protegemos el borde on-premise y la conectividad híbrida con Azure, con un gobierno único de reglas.",
     "extra": "Sus registros llegan a Microsoft Sentinel."},
    {"area": "seguridad", "id": "cisco-ise", "nombre": "Cisco ISE (Premier)",
     "origen": ["S1 · Protección Avanzada M365 (suite User Protection Advantage)"], "capa": "Control de acceso a la red (NAC) y segmentación",
     "ms": "Microsoft Intune (cumplimiento) / Entra ID",
     "valor": "Decidimos qué usuario y qué dispositivo entra a la LAN y al Wi-Fi según el estado de cumplimiento de Intune.",
     "extra": "Aporta el control de acceso a la red (NAC), una capa que complementa a Microsoft."},
    {"area": "seguridad", "id": "secure-network-analytics", "nombre": "Cisco Secure Network Analytics (NDR)",
     "origen": ["S1 · Protección Avanzada M365 (suite Breach Protection Advantage)"], "capa": "Detección por comportamiento en flujos de red",
     "ms": "Microsoft Sentinel",
     "valor": "Enviamos a Sentinel la telemetría de red (NetFlow y comportamiento) para mejorar las detecciones.",
     "extra": "Complementa a su SIEM actual."},
    {"area": "seguridad", "id": "telemetry-broker", "nombre": "Cisco Telemetry Broker",
     "origen": ["S1 · Protección Avanzada M365 (suite Breach Protection Advantage)"], "capa": "Filtrado y enrutamiento de pipelines de telemetría",
     "ms": "Microsoft Sentinel / Azure Monitor",
     "valor": "Filtramos y enrutamos la telemetría antes de que llegue a Sentinel: menor costo de ingesta y datos de mejor calidad."},
    {"area": "seguridad", "id": "secure-access-sse", "nombre": "Cisco Secure Access (SSE)",
     "origen": ["S2 · Secure Access como Servicio", "S1 · Protección Avanzada M365"], "capa": "Acceso seguro: ZTNA, SWG, DNS y VPNaaS",
     "ms": "Entra ID (proveedor de identidad)",
     "valor": "Ofrecemos acceso Zero Trust a aplicaciones privadas e internet con la identidad de Entra ID."},

    {"area": "colaboracion", "id": "room-bar", "nombre": "Cisco Room Bar / Room Bar Pro",
     "origen": ["S4 · Espacios Cisco Rooms para Teams"], "capa": "Dispositivo todo en uno para salas pequeñas y medianas",
     "ms": "Microsoft Teams Rooms",
     "valor": "Instalamos un dispositivo certificado que ejecuta Microsoft Teams Rooms de forma nativa.",
     "extra": "En Consein sumamos el hardware de sala, la instalación y el soporte."},
    {"area": "colaboracion", "id": "board-pro", "nombre": "Cisco Board Pro Series",
     "origen": ["S4 · Espacios Cisco Rooms para Teams"], "capa": "Pantalla colaborativa y pizarra interactiva",
     "ms": "Microsoft Teams Rooms / Whiteboard",
     "valor": "Llevamos la reunión híbrida y la pizarra de Teams a una pantalla táctil certificada para salas medianas."},

    {"area": "data-analitica", "id": "meraki-mv", "nombre": "Meraki MV (cámaras inteligentes)",
     "origen": ["S3 · Meraki Cloud Managed"], "capa": "Video y analítica de ocupación en el borde",
     "ms": "Power BI / Microsoft Fabric",
     "valor": "Enviamos por API el conteo de personas y la ocupación a sus tableros ejecutivos en Power BI.",
     "extra": "Aporta la capa de video, que complementa a Microsoft."},
    {"area": "data-analitica", "id": "meraki-mt", "nombre": "Meraki MT (sensores IoT)",
     "origen": ["S3 · Meraki Cloud Managed"], "capa": "Sensores ambientales: temperatura, humedad, puertas y energía",
     "ms": "Microsoft Fabric / Power BI / Azure IoT",
     "valor": "Aportamos datos de las condiciones físicas de sedes y centros de datos para análisis y alertas operativas."},

    {"area": "servicios-empresariales", "id": "secure-access-ztna", "nombre": "Cisco Secure Access (ZTNA)",
     "origen": ["S2 · Secure Access como Servicio"], "capa": "Acceso seguro a aplicaciones privadas y de negocio",
     "ms": "Dynamics 365 / Business Central",
     "valor": "Damos acceso basado en identidad y postura a usuarios remotos y terceros que operan Dynamics 365 y sus sistemas relacionados."},
    {"area": "servicios-empresariales", "id": "sdwan-multisede", "nombre": "Meraki / Cisco SD-WAN multisede",
     "origen": ["S3 · Meraki Cloud Managed", "S5 · SD-WAN Seguro"], "capa": "Conectividad de sucursales y última milla",
     "ms": "Dynamics 365 / Azure ExpressRoute",
     "valor": "Aseguramos un desempeño estable de Dynamics 365 en todas las sedes.",
     "extra": "Microsoft aloja la aplicación y Cisco transporta el tráfico."},

    {"area": "automatizacion", "id": "meraki-api", "nombre": "Meraki Dashboard API y webhooks",
     "origen": ["S3 · Meraki Cloud Managed"], "capa": "Automatización de red, alertas y configuración",
     "ms": "Power Automate / Logic Apps",
     "valor": "Exponemos alertas y acciones de red (altas, cambios e incidentes de sede) para orquestarlas con Power Automate y Logic Apps."},

    {"area": "inteligencia-artificial", "id": "ai-defense-inventory", "nombre": "Cisco AI Defense: AI Inventory y AI Supply Chain Risk Management",
     "origen": ["S7 · Cisco AI Defense"], "capa": "Inventario de modelos, agentes, servidores MCP y cadena de suministro",
     "ms": "Azure AI Foundry / Copilot Studio",
     "valor": "Inventariamos sus activos de IA y evaluamos el riesgo de modelos y componentes de terceros antes de desplegarlos en Azure AI Foundry."},
    {"area": "inteligencia-artificial", "id": "ai-defense-validation", "nombre": "Cisco AI Defense: AI Model & App Validation",
     "origen": ["S7 · Cisco AI Defense"], "capa": "Pruebas algorítmicas de seguridad de modelos y aplicaciones",
     "ms": "Azure AI Foundry / Azure OpenAI",
     "valor": "Validamos modelos y aplicaciones frente a prompt injection, jailbreak y fuga de datos antes de pasarlos a producción."},
    {"area": "inteligencia-artificial", "id": "ai-defense-runtime", "nombre": "Cisco AI Defense: AI Runtime Protection",
     "origen": ["S7 · Cisco AI Defense"], "capa": "Protección en tiempo real de agentes y respuestas",
     "ms": "Copilot Studio / Azure OpenAI",
     "valor": "Agregamos una capa de protección de red sobre el tráfico de inferencia.",
     "extra": "Definimos su alcance junto a Prompt Shields y Defender for AI."},
]


def productos_area(area_id):
    return [m for m in MATRIZ if m["area"] == area_id]


def tecnologias_area(area_id):
    """Cisco y Microsoft de un área, derivados de la propia matriz."""
    ms = []
    for m in productos_area(area_id):
        for x in m["ms"].replace(" (cumplimiento)", "").replace(" (proveedor de identidad)", "").split(" / "):
            if x not in ms:
                ms.append(x)
    return ", ".join(m["nombre"] for m in productos_area(area_id)), ", ".join(ms)

# ---------------------------------------------------------------------------
# Productos · Programa Renueva (8)
# ---------------------------------------------------------------------------
PRODUCTOS = [
    {"code": "REN-01", "titulo": "Inventario de obsolescencia",
     "valor": "Identificamos de forma gratuita qué equipos Cisco perdieron soporte y cuánto riesgo representan.",
     "ideal": "Cualquier empresa con switches, routers, firewalls, servidores o salas Cisco de más de cinco años.",
     "resuelve": "Basamos cada decisión de renovación en datos de riesgo y soporte.",
     "incluye": ["Inventariamos su base instalada Cisco.",
                 "Cruzamos cada equipo con las fechas oficiales de fin de venta y de soporte.",
                 "Calculamos el riesgo por equipo: vulnerabilidades, soporte y criticidad.",
                 "Entregamos un plan priorizado con costo total y opciones de financiamiento."],
     "resultado": "Le entregamos un mapa de obsolescencia y una hoja de ruta de renovación por fases.",
     "tec": ("Toda la base instalada, clasificada en renovar ya, planificar o mantener", "Identificamos qué equipos limitan la integración con Azure, Intune, Sentinel o Teams Rooms"),
     "dato": "69% del hardware activo con fecha de fin de soporte programada quedará sin soporte en 2027 (NTT DATA, 2024).",
     "cta": "Inventariemos su red"},
    {"code": "REN-02", "titulo": "Campus y WiFi renovados",
     "valor": "Renovamos switches y WiFi con Cisco Catalyst 9000 o Meraki, listos para Zero Trust, Teams y Copilot.",
     "ideal": "Oficinas y sedes con switches o WiFi de generaciones anteriores.",
     "resuelve": "Aceleramos el WiFi, segmentamos los puertos y habilitamos las políticas modernas de acceso.",
     "incluye": ["Diseñamos con Catalyst 9000 o Meraki MS y WiFi de nueva generación.",
                 "Migramos por oleadas mientras su operación sigue activa.",
                 "Segmentamos con Cisco ISE e integramos Intune.",
                 "Retiramos los equipos antiguos de forma responsable."],
     "resultado": "Le entregamos una red de campus segura, gestionable y lista para la IA.",
     "tec": ("Switches y access points legados → Catalyst 9000 / Meraki", "Teams, Microsoft 365, Copilot e Intune"),
     "dato": "Con Meraki, 40% menos tiempo de inactividad y 80% menos tickets de red (Forrester TEI, 2025).",
     "cta": "Renovemos su campus"},
    {"code": "REN-03", "titulo": "Sucursales con SD-WAN",
     "valor": "Reemplazamos routers legados y enlaces MPLS por SD-WAN Cisco conectada a Azure Virtual WAN.",
     "ideal": "Empresas con routers de sucursal antiguos o enlaces MPLS.",
     "resuelve": "Protegemos el borde de internet de cada sucursal y reducimos el costo de los enlaces.",
     "incluye": ["Instalamos Catalyst 8000 o Meraki MX con SD-WAN.",
                 "Conectamos cada sede con Azure Virtual WAN.",
                 "Priorizamos Teams, Microsoft 365 y Dynamics 365.",
                 "Configuramos respaldo por enlace celular cuando aplica."],
     "resultado": "Logramos sucursales estables y más económicas de operar.",
     "tec": ("Routers legados y MPLS → Catalyst 8000 / Meraki MX", "Azure Virtual WAN, Microsoft 365"),
     "dato": "En el estudio de Forrester sobre Meraki, una organización redujo en más de dos tercios su costo mensual de conectividad por sede al migrar desde MPLS (TEI, 2025).",
     "cta": "Modernicemos sus sucursales"},
    {"code": "REN-04", "titulo": "Renovación de firewalls",
     "valor": "Migramos sus firewalls legados a Cisco Secure Firewall, con soporte vigente y eventos en Microsoft Sentinel.",
     "ideal": "Empresas con firewalls Cisco de generaciones anteriores, como familias ASA legadas.",
     "resuelve": "Actualizamos la protección de la puerta más atacada: el borde de internet.",
     "incluye": ["Migramos las políticas a Cisco Secure Firewall.",
                 "Validamos y probamos las reglas.",
                 "Enviamos los eventos a Microsoft Sentinel.",
                 "Operamos y ajustamos la solución."],
     "resultado": "Le entregamos un perímetro actualizado, con soporte y visible en su SIEM.",
     "tec": ("Firewalls legados → Cisco Secure Firewall", "Microsoft Sentinel, Azure Firewall"),
     "dato": "42,5% de las vulnerabilidades explotadas en equipos de borde durante 2025 afectó a dispositivos en fin de vida o cerca de él (VulnCheck, 2025).",
     "cta": "Renovemos su perímetro"},
    {"code": "REN-05", "titulo": "Datacenter híbrido",
     "valor": "Renovamos su datacenter con Nexus 9000 y Cisco UCS, integrado con Azure Arc y Azure Local.",
     "ideal": "Empresas con switching de datacenter o servidores Cisco UCS de generaciones anteriores.",
     "resuelve": "Ampliamos la capacidad, renovamos el soporte y habilitamos la operación híbrida.",
     "incluye": ["Renovamos el switching con Nexus 9000 o ACI.",
                 "Instalamos servidores Cisco UCS gestionados con Intersight.",
                 "Integramos Azure Arc y, cuando aplica, Azure Local sobre hardware validado.",
                 "Planificamos en conjunto la renovación de Windows Server."],
     "resultado": "Le entregamos un datacenter moderno que opera en conjunto con Azure.",
     "tec": ("Nexus y UCS legados → Nexus 9000 / ACI y UCS actuales", "Azure Arc, Azure Local, Windows Server"),
     "dato": "Intersight: 192% de ROI y 50% menos tiempo de resolución (Forrester TEI, 2025).",
     "cta": "Planifiquemos su datacenter"},
    {"code": "REN-06", "titulo": "Salas y voz para Teams",
     "valor": "Convertimos sus salas y teléfonos legados en experiencias Microsoft Teams con hardware Cisco certificado.",
     "ideal": "Empresas con videoconferencia o telefonía IP de generaciones anteriores.",
     "resuelve": "Unificamos la colaboración en una sola plataforma.",
     "incluye": ["Instalamos Cisco Room Kit, Board y Desk certificados para Teams Rooms.",
                 "Incorporamos teléfonos Cisco compatibles con Teams Phone.",
                 "Migramos la telefonía a Teams Phone.",
                 "Capacitamos a los usuarios y damos soporte."],
     "resultado": "Le entregamos una sola plataforma de colaboración con el mejor hardware.",
     "tec": ("Video y telefonía legada → hardware Cisco certificado", "Microsoft Teams Rooms, Teams Phone"),
     "dato": "Teams Rooms: 342% de ROI (Forrester TEI).",
     "cta": "Renovemos sus salas"},
    {"code": "REN-07", "titulo": "Renovación financiada",
     "valor": "Gestionamos ante bancos locales el financiamiento de su renovación, para distribuir la inversión en el tiempo.",
     "ideal": "Empresas que necesitan renovar su hardware Cisco y prefieren financiar la inversión.",
     "resuelve": "Abrimos una vía de financiamiento bancario cuando el presupuesto de capital del año no alcanza.",
     "incluye": ["Preparamos el expediente técnico y económico del proyecto: alcance, equipos, costo total y plan por fases.",
                 "Presentamos el proyecto a bancos locales y acompañamos sus solicitudes de información.",
                 "Cada banco estudia el caso y decide la factibilidad, el monto y las condiciones del financiamiento.",
                 "Ajustamos el plan de renovación por fases a las condiciones que apruebe el banco."],
     "resultado": "Le facilitamos el acceso a financiamiento bancario local para renovar por fases.",
     "tec": ("Todo el proyecto de renovación, presentado a bancos locales", "Combinable con la planificación de licencias Microsoft"),
     "nota": "Consein realiza las gestiones con los bancos; la aprobación, el monto y las condiciones dependen de la evaluación de cada banco.",
     "cta": "Exploremos su financiamiento"},
    {"code": "REN-08", "titulo": "Ciclo de vida gestionado",
     "valor": "Mantenemos su red siempre vigente con un inventario vivo y un plan anual de renovación.",
     "ideal": "Empresas que prefieren planificar la renovación con anticipación.",
     "resuelve": "Anticipamos la obsolescencia antes de que se convierta en una emergencia.",
     "incluye": ["Mantenemos un inventario vivo de la base instalada.",
                 "Emitimos alertas de fin de venta y de soporte.",
                 "Elaboramos el plan anual de renovación y su presupuesto.",
                 "Operamos con Consein Connected."],
     "resultado": "Le aseguramos una infraestructura siempre soportada y un presupuesto predecible.",
     "tec": ("Renovación planificada y continua", "Alineada con el ciclo de vida de su plataforma Microsoft"),
     "cta": "Planifiquemos su ciclo de vida"},
]

FAQ = [
    ("¿Cómo conectan las sucursales de una empresa a Azure?",
     "Implementamos SD-WAN Cisco (Meraki o Catalyst 8000V) integrada con Azure Virtual WAN. Priorizamos Teams, Microsoft 365 y Dynamics 365 y gestionamos todas las sedes desde un solo lugar."),
    ("¿Cómo extienden Zero Trust hasta la red corporativa?",
     "Integramos Cisco ISE con Microsoft Intune y Entra ID: la red solo admite a usuarios y dispositivos que cumplen las políticas, y todos los eventos llegan a Microsoft Sentinel."),
    ("¿Qué equipos usan para las salas Microsoft Teams Rooms?",
     "Instalamos Cisco Room Kit, Board y Desk certificados para Microsoft Teams Rooms, configurados en Teams Admin Center y listos para Microsoft 365 Copilot."),
    ("¿Cómo miden el rendimiento de las aplicaciones de negocio?",
     "Combinamos Cisco AppDynamics y ThousandEyes con Azure Monitor y publicamos los indicadores de disponibilidad en Power BI."),
    ("¿Cómo protegen el acceso remoto a Dynamics 365?",
     "Implementamos Cisco Secure Access con identidad de Microsoft Entra y políticas por aplicación para Dynamics 365 y Business Central."),
    ("¿Qué tareas de red pueden automatizar?",
     "Automatizamos altas de sedes, cambios de configuración, alertas y aprobaciones con Power Automate y Logic Apps conectados a las APIs de Meraki y Catalyst Center."),
    ("¿Cómo protegen la inteligencia artificial en Azure?",
     "Protegemos modelos y agentes con Cisco AI Defense, segmentamos las cargas con Hypershield y monitoreamos Copilot y Azure OpenAI con ThousandEyes, alineados con Defender for Cloud y Purview."),
]

FUENTES = [
    "Forrester Total Economic Impact™, encargados por Cisco: Meraki (2025), Intersight (2025), ThousandEyes End User Monitoring, ThousandEyes for Enterprise Networks (2023), Full-Stack Observability (2024), Secure Firewall (2022).",
    "Forrester Total Economic Impact™, encargados por Microsoft: Teams Rooms, Projected TEI of Microsoft Teams with Microsoft 365 Copilot (2025), Microsoft Defender (2025), Azure Arc (2025).",
    "NTT DATA, Lifecycle Management Report, 2024 · NTT, Global Network Insights Report, 2020 · VulnCheck, 2025 · Verizon, Data Breach Investigations Report, 2026.",
    "CISA, Binding Operational Directive 26-02, febrero 2026.",
    "Cisco Cybersecurity Readiness Index 2025 · Cisco AI Readiness Index 2025 · Splunk y Oxford Economics, The Hidden Costs of Downtime, 2024.",
    "Los estudios TEI modelan organizaciones compuestas; los publicamos como referencia de la industria. Estimamos el resultado de cada empresa en el Diagnóstico Red + Nube.",
]

PAISES = ["Venezuela", "Panamá", "República Dominicana", "Estados Unidos"]

# ---------------------------------------------------------------------------
# Plantillas
# ---------------------------------------------------------------------------
def slug(code):
    return code.lower()


def detalle(o, etiqueta, renovacion=False):
    filas = [("Ideal para", E(o["ideal"])),
             ("Qué resolvemos", E(o["resuelve"])),
             ("Qué incluye", "<ul>" + "".join(f"<li>{E(i)}</li>" for i in o["incluye"]) + "</ul>"),
             ("Resultado", f"<strong>{E(o['resultado'])}</strong>")]
    dl = "".join(f"<dt>{a}</dt><dd>{b}</dd>" for a, b in filas)
    t1, t2 = o["tec"]
    extra = (f"<p><b>Renovamos:</b> {E(t1)}</p><p><b>Valor Microsoft:</b> {E(t2)}</p>" if renovacion
             else f"<p><b>Cisco:</b> {E(t1)} · <b>Microsoft:</b> {E(t2)}</p>")
    if o.get("dato"):
        extra += f"<p><b>Dato:</b> {E(o['dato'])}</p>"
    if o.get("nota"):
        extra += f"<p><b>Importante:</b> {E(o['nota'])}</p>"
    if o.get("nortia"):
        extra += f"<p><b>NortIA:</b> {E(o['nortia'])}</p>"
    return f"""<div class="detalle-src" id="detalle-{slug(o['code'])}">
  <p class="code">{o['code']} · {E(etiqueta)}</p>
  <h2>{E(o['titulo'])}</h2>
  <p class="value">{E(o['valor'])}</p>
  <dl>{dl}</dl>
  <div class="extra">{extra}</div>
  <a class="btn btn-primary" href="index.html?interes={o['code']}#contacto">{E(o['cta'])}</a>
</div>"""

def tarjeta(o, etiqueta, renovacion=False):
    s = slug(o["code"])
    return f"""<article class="card" id="{s}">
  <h3>{E(o['titulo'])}</h3>
  <p>{E(o['valor'])}</p>
  <a class="more" href="#{s}" aria-label="Seguir leyendo: {E(o['titulo'])}">Seguir leyendo…</a>
  {detalle(o, etiqueta, renovacion)}
</article>"""

def menu(actual):
    def cur(*paginas):
        return ' aria-current="page"' if actual in paginas else ""
    especialidades = "".join(f'<li><a href="soluciones.html#{e["id"]}">{E(e["nombre"])}</a></li>' for e in ESPECIALIDADES)
    productos_menu = "".join(f'<li><a href="productos.html#{slug(p["code"])}">{E(p["titulo"])}</a></li>' for p in PRODUCTOS)
    return f"""<header class="site-header">
  <div class="wrap">
    <a class="logo" href="index.html" aria-label="Consein, inicio"><img src="assets/img/{'logo-consein-blanco.png' if TEMA == 'digital' else 'logo-consein.png'}" alt="Consein" width="166" height="28"></a>
    <button class="menu-toggle" aria-label="Abrir menú" aria-expanded="false" aria-controls="nav">☰</button>
    <nav class="nav" id="nav" aria-label="Principal">
      <ul>
        <li><a class="nav-link" href="index.html"{cur('index')}>Inicio</a></li>
        <li class="has-menu">
          <button class="nav-link" aria-expanded="false" aria-haspopup="true"{cur('soluciones', 'productos')}>Soluciones Cisco<span class="caret">▾</span></button>
          <div class="mega mega-cisco">
            <div class="mega-group">
              <a class="mega-l2" href="soluciones.html"><b>Soluciones de Valor</b><small>19 productos Cisco en 7 áreas de práctica</small></a>
              <ul>{especialidades}</ul>
            </div>
            <div class="mega-group">
              <a class="mega-l2" href="productos.html"><b>Ofertas de Productos</b><small>Programa Renueva · 8 ofertas de renovación</small><em class="badge">Destacado · Renovación de hardware</em></a>
              <ul>{productos_menu}</ul>
            </div>
          </div>
        </li>
        <li><a class="nav-link" href="index.html#nosotros">Nosotros</a></li>
      </ul>
      <a class="btn btn-primary" href="index.html#contacto">Contacto</a>
    </nav>
  </div>
</header>"""

def pie():
    esp = "".join(f'<li><a href="soluciones.html#{e["id"]}">{E(e["nombre"])}</a></li>' for e in ESPECIALIDADES)
    fuentes = "".join(f"<li>{E(f)}</li>" for f in FUENTES)
    return f"""<footer class="site-footer">
  <div class="wrap">
    <div class="foot">
      <div>
        <a class="logo" href="index.html"><img src="assets/img/logo-consein-blanco.png" alt="Consein" width="154" height="26"></a>
        <p>Integramos Cisco y Microsoft para empresas en {', '.join(PAISES[:-1])} y {PAISES[-1]} desde 1987.</p>
      </div>
      <div><h4>Soluciones de Valor</h4><ul>{esp}</ul></div>
      <div><h4>Ofertas de Productos</h4><ul>
        <li><a href="productos.html">Programa Renueva</a></li>
        <li><a href="productos.html#autodiagnostico">Autodiagnóstico</a></li>
        <li><a href="productos.html#ofertas">Ofertas de renovación</a></li>
      </ul></div>
      <div><h4>Contacto</h4><ul>
        <li><a href="soluciones.html">Soluciones de Valor</a></li>
        <li><a href="index.html?interes=REN-01#contacto">Inventario de obsolescencia</a></li>
        <li><a href="index.html#contacto">Hable con un especialista</a></li>
      </ul></div>
    </div>
    <details class="sources"><summary>Fuentes</summary><ul>{fuentes}</ul></details>
    <div class="foot-legal">
      <span>© <span id="year">2026</span> Consein. Todos los derechos reservados.</span>
      <span>Cisco, Meraki y ThousandEyes son marcas de Cisco Systems, Inc. Microsoft, Azure, Teams y Dynamics 365 son marcas de Microsoft Corporation.</span>
    </div>
  </div>
</footer>
<dialog class="detail" id="detalle" aria-label="Detalle">
  <div class="detail-in"><button class="detail-close" aria-label="Cerrar">×</button><div class="detail-body"></div></div>
</dialog>
<script src="assets/js/app.js"></script>"""

ORG = {
    "@type": "Organization", "@id": URL_BASE + "#consein", "name": "Consein",
    "url": "https://www.consein.com/", "logo": URL_BASE + "assets/img/logo-consein.png",
    "foundingDate": "1987",
    "areaServed": [{"@type": "Country", "name": p} for p in PAISES],
}

def pagina(archivo, actual, titulo, descripcion, cuerpo, jsonld):
    url = URL_BASE + ("" if archivo == "index.html" else archivo.replace(".html", ""))
    ld = json.dumps({"@context": "https://schema.org", "@graph": [ORG] + jsonld}, ensure_ascii=False, indent=1)
    doc = f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(titulo)}</title>
<meta name="description" content="{E(descripcion)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_LA">
<meta property="og:site_name" content="Consein">
<meta property="og:title" content="{E(titulo)}">
<meta property="og:description" content="{E(descripcion)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{URL_BASE}assets/img/logo-consein.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="stylesheet" href="assets/css/estilos.css">
<script type="application/ld+json">
{ld}
</script>
</head>
<body>
<a class="skip" href="#contenido">Saltar al contenido</a>
{menu(actual)}
<main id="contenido">
{cuerpo}
</main>
{pie()}
</body>
</html>
"""
    # Evita que "SD-WAN" se parta en dos renglones (solo en texto visible, no en atributos)
    import re
    cabeza, cuerpo_html = doc.split("<body>", 1)
    cuerpo_html = re.sub(r">([^<]*)<", lambda m: ">" + m.group(1).replace("SD-WAN", '<span class="nw">SD-WAN</span>') + "<", cuerpo_html)
    doc = cabeza + "<body>" + cuerpo_html
    GEN[archivo] = doc
    if TEMA == "minimal":
        (RAIZ / archivo).write_text(doc, encoding="utf-8")
        print("✔", archivo)

def banda(titulo, cta, href):
    return f"""<section class="band"><div class="wrap">
  <h2>{E(titulo)}</h2>
  <a class="btn btn-primary" href="{href}">{E(cta)}</a>
</div></section>"""

def servicio_ld(o, cat):
    return {"@type": "Service", "name": o["titulo"], "description": o["valor"], "serviceType": cat,
            "provider": {"@id": URL_BASE + "#consein"}, "url": URL_BASE + ("soluciones" if o["code"].startswith("CSC") else "productos") + "#" + slug(o["code"]),
            "areaServed": [{"@type": "Country", "name": p} for p in PAISES]}


# ---------------------------------------------------------------------------
# Aviso destacado: renovación de hardware (Inicio y Ofertas de Productos)
# ---------------------------------------------------------------------------
def arte_hardware():
    """Equipo legado → equipo nuevo listo para Microsoft, sobre una línea de tiempo hasta 2027."""
    def equipo(x, y, nuevo):
        clase = "hw-new" if nuevo else "hw-old"
        puertos = "".join(f'<rect class="port" x="{x + 14 + i * 13}" y="{y + 18}" width="9" height="9" rx="1.5"/>' for i in range(7))
        leds = "".join(f'<circle class="led{" led-on" if nuevo else ""}" style="animation-delay:{i * .35:.2f}s" cx="{x + 118 + i * 9}" cy="{y + 22}" r="2.6"/>' for i in range(3))
        return f'<g class="{clase}"><rect class="chassis" x="{x}" y="{y}" width="150" height="46" rx="7"/>{puertos}{leds}</g>'
    return f"""<div class="aviso-art" aria-hidden="true">
<svg viewBox="0 0 440 290" role="img">
  <text class="hw-label" x="95" y="40" text-anchor="middle">Equipo legado</text>
  <g transform="translate(70 26)"><rect class="eos" x="-2" y="20" width="54" height="18" rx="9"/><text class="eos-t" x="25" y="33" text-anchor="middle">EoS</text></g>
  {equipo(20, 70, False)}{equipo(20, 126, False)}
  <path class="hw-flow" d="M186 125 H252"/><path class="hw-arrow" d="M248 117 l10 8 -10 8"/>
  <text class="hw-label hw-label-new" x="345" y="40" text-anchor="middle">Cisco actual</text>
  {equipo(270, 70, True)}{equipo(270, 126, True)}
  <g transform="translate(412 64)"><circle class="ok" r="15"/><path class="ok-t" d="M-6 0 l4 4 8-8"/></g>
  <text class="hw-ms" x="345" y="196" text-anchor="middle">Teams · Azure · Intune · Sentinel</text>
  <line class="tl" x1="20" y1="246" x2="420" y2="246"/>
  <line class="tl-run" x1="20" y1="246" x2="420" y2="246"/>
  <circle class="tl-dot" cx="20" cy="246" r="6"/><text class="tl-t" x="20" y="272">Hoy</text>
  <text class="tl-t tl-mid" x="220" y="236" text-anchor="middle">Renovación por fases</text>
  <circle class="tl-end" cx="420" cy="246" r="8"/><text class="tl-t tl-year" x="420" y="276" text-anchor="end">2027</text>
</svg></div>"""


AVISOS = {
    "productos": {
        "tag": "Oferta destacada · Renovación de hardware",
        "titulo": "Inventariamos gratis su hardware Cisco",
        "texto": "Le entregamos el mapa de obsolescencia de su base instalada y un plan de renovación priorizado, con costo total y alternativas de financiamiento bancario.",
        "cifra": "<small>financiamiento</small>local", "cifra_txt": "Gestionamos su solicitud ante bancos locales. Cada banco estudia el caso y decide la factibilidad del financiamiento.", "fuente": "",
        "lista_tipo": "ol",
        "lista": ["Inventariamos su base instalada y sus fechas de fin de soporte", "Priorizamos por riesgo, criticidad y costo total", "Renovamos por fases y gestionamos el financiamiento con bancos locales"],
        "cta2": ("Autodiagnóstico", "#autodiagnostico"),
    },
}


PASOS = [
    ("Evaluamos", "Inventario, postura actual, dependencias, brechas, riesgos y objetivos del negocio."),
    ("Diseñamos", "Arquitectura objetivo, políticas, integraciones, dimensionamiento, transición y gobierno."),
    ("Actualizamos", "Implementación, migración, configuración, pruebas, documentación y puesta en producción."),
    ("Transformamos", "Adopción, formación, comunicación, cambio operativo y transferencia de conocimiento."),
    ("Optimizamos", "Telemetría, revisión periódica, ajustes, capacidad, experiencia, costo y roadmap."),
    ("Administramos", "Monitoreo, soporte, incidentes, cambios, reportes y continuidad bajo un servicio recurrente."),
]
PASO_TRANSVERSAL = ("Aseguramos", ["Zero Trust", "Hardening", "Control de acceso", "Protección de datos", "Respuesta", "Cumplimiento"])


def pasos_consein():
    """Los siete pasos aplicados a Cisco: 1–6 en secuencia y 7 como capa transversal."""
    items = ""
    for i, (t, d) in enumerate(PASOS, 1):
        tag = '<small>Servicio recurrente</small>' if i == len(PASOS) else ""
        items += f"<li><b>{E(t)}</b><span>{E(d)}</span>{tag}</li>"
    nombre, temas = PASO_TRANSVERSAL
    chips = "".join(f"<li>{E(x)}</li>" for x in temas)
    return f"""<div class="pasos7">
      <ol class="steps steps-6">{items}</ol>
      <div class="capa-transversal">
        <div class="ct-head"><span class="ct-num">07</span><div><b>{E(nombre)}</b><em>Capa transversal a los seis pasos</em></div></div>
        <ul class="ct-temas">{chips}</ul>
      </div>
    </div>"""


def sticker_renueva():
    """Sticker discreto para Inicio: lleva al aviso completo en Ofertas de Productos."""
    return """<a class="sticker" href="productos.html#renovacion-hardware" aria-label="Programa Renueva: renovación de hardware Cisco con inventario gratuito">
  <svg viewBox="0 0 160 160" aria-hidden="true">
    <defs><path id="st-c" d="M80 80 m-61 0 a61 61 0 1 1 122 0 a61 61 0 1 1 -122 0"/></defs>
    <circle class="st-bg" cx="80" cy="80" r="78"/>
    <circle class="st-in" cx="80" cy="80" r="47"/>
    <g class="st-ring"><text class="st-t"><textPath href="#st-c" textLength="378" lengthAdjust="spacing">RENOVACIÓN DE HARDWARE · PROGRAMA RENUEVA ·</textPath></text></g>
  </svg>
  <span class="st-core"><b>Inventario gratis</b><i>→</i></span>
</a>"""


def aviso(variante):
    a = AVISOS[variante]
    items = "".join(f"<li>{E(i)}</li>" for i in a["lista"])
    return f"""<section class="aviso-wrap aviso-{variante}" id="renovacion-hardware" aria-label="Renovación de hardware Cisco">
  <div class="wrap">
    <div class="aviso">
      <div class="aviso-copy">
        <p class="aviso-tag"><span class="aviso-dot"></span>{E(a['tag'])}</p>
        <h2>{E(a['titulo'])}</h2>
        <p class="aviso-text">{E(a['texto'])}</p>
        <div class="aviso-stat"><b>{a['cifra']}</b><p>{E(a['cifra_txt'])}{f"<cite>{E(a['fuente'])}</cite>" if a['fuente'] else ""}</p></div>
        <{a['lista_tipo']} class="aviso-list">{items}</{a['lista_tipo']}>
        <div class="actions">
          <a class="btn btn-primary" href="index.html?interes=REN-01#contacto">Solicitar inventario gratuito</a>
          <a class="btn btn-line" href="{a['cta2'][1]}">{E(a['cta2'][0])}</a>
        </div>
      </div>
      {arte_hardware()}
    </div>
  </div>
</section>"""

# ---------------------------------------------------------------------------
# Inicio
# ---------------------------------------------------------------------------
def inicio():
    tiles = ""
    for i, e in enumerate(ESPECIALIDADES, 1):
        n = len(productos_area(e["id"]))
        tiles += f"""<a class="tile" href="soluciones.html#{e['id']}">{D(icono(e['id']) + f'<span class="idx">0{i}</span>')}
  <h3>{E(e['h2'])}</h3><p>{E(e['intro'])}</p><span class="count">{n} {'producto Cisco' if n == 1 else 'productos Cisco'}</span></a>"""
    tiles += f"""<a class="tile featured" href="soluciones.html#criterio" style="border-color:var(--navy)">{D(icono('integral'))}
  <h3>Matriz de valor</h3><p>{len(MATRIZ)} productos Cisco que suman valor a su plataforma Microsoft, seleccionados con un mismo criterio.</p><span class="count">Ver el criterio</span></a>"""

    faq = "".join(f"<details><summary>{E(q)}</summary><p>{E(a)}</p></details>" for q, a in FAQ)

    opciones = '<option value="">Quiero hablar con un especialista</option><optgroup label="Soluciones de Valor">'
    opciones += "".join(f'<option value="{e["id"]}">{E(e["nombre"])}</option>' for e in ESPECIALIDADES)
    opciones += '</optgroup><optgroup label="Programa Renueva">'
    opciones += "".join(f'<option value="{o["code"]}">{E(o["titulo"])}</option>' for o in PRODUCTOS)
    opciones += "</optgroup>"
    paises = "".join(f"<option>{p}</option>" for p in PAISES + ["Otro"])

    cuerpo = f"""
<section class="hero">
  <div class="wrap hero-grid">
   <div class="hero-copy">
    <p class="eyebrow">Soluciones Cisco · Consein</p>
    <h1><em>Sinergia exponencial:</em><span>su plataforma Microsoft, potenciada por una red Cisco</span></h1>
    <p class="lead">Integramos redes, ciberseguridad, salas de reunión y observabilidad Cisco con Microsoft 365, Azure y Dynamics 365, en un solo servicio gestionado y con un solo responsable.</p>
    <div class="actions">
      <a class="btn btn-primary" href="index.html#contacto">Hablar con un especialista</a>
      <a class="btn btn-line" href="soluciones.html">Ver soluciones</a>
    </div>
    <div class="figures">
      <div><b>19</b><span>productos Cisco</span></div>
      <div><b>7</b><span>áreas de práctica</span></div>
      <div><b>8</b><span>ofertas de renovación</span></div>
    </div>
   </div>
   {sticker_renueva()}
   {D(arte_hero())}
  </div>
</section>

<section class="soft" id="enfoque">
  <div class="wrap enfoque-grid">
   <div>
    <p class="eyebrow">Nuestro enfoque</p>
    <p class="statement">Microsoft es donde trabaja su negocio. Cisco es por donde viaja. En Consein los hacemos funcionar como uno solo.</p>
    <p class="statement-text">Construimos cada proyecto sobre su plataforma Microsoft e incorporamos Cisco en las capas que la potencian: la red, las salas, la observabilidad y la seguridad especializada.</p>
   </div>
   {D(ARTE_CAPAS)}
  </div>
</section>

<section id="especialidades">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">Soluciones de Valor</p>
      <h2>Siete especialidades</h2>
      <p class="lead">Cada especialidad combina tecnología Cisco con su base Microsoft.</p>
    </div>
    <div class="grid g4">{tiles}</div>
  </div>
</section>

<section id="metodo">
  <div class="wrap">
    <div class="section-head"><p class="eyebrow">Cómo trabajamos</p><h2>Los siete pasos aplicados a Cisco</h2>
      <p class="lead">Seis pasos acompañan el ciclo de vida de su red Cisco y un séptimo la protege de principio a fin.</p></div>
    {pasos_consein()}
  </div>
</section>

<section class="soft" id="resultados">
  <div class="wrap">
    <div class="section-head"><p class="eyebrow">Resultados medidos</p><h2>Lo que muestran los estudios</h2></div>
    <div class="grid g4">
      <div class="stat"><b>40%</b><p>menos inactividad de red con Cisco Meraki.</p><cite>Forrester TEI, 2025</cite></div>
      <div class="stat"><b>50–80%</b><p>menos tiempo para identificar incidentes con ThousandEyes.</p><cite>Forrester TEI</cite></div>
      <div class="stat"><b>342%</b><p>de ROI con Microsoft Teams Rooms.</p><cite>Forrester TEI</cite></div>
      <div class="stat"><b>358%</b><p>de ROI con la observabilidad de Cisco.</p><cite>Forrester TEI, 2024</cite></div>
    </div>
    <p class="note" style="margin-top:40px">Citamos estudios por componente, encargados por cada fabricante, como referencia de la industria. Estimamos el resultado para su empresa en el Diagnóstico Red + Nube.</p>
  </div>
</section>

<section id="nosotros">
  <div class="wrap">
    <div class="section-head"><p class="eyebrow">Nosotros</p><h2>Por qué Consein</h2></div>
    <div class="grid g4 proof">
      <div>{D(icono('calendario'))}<b>Desde 1987</b><p>Operamos en Venezuela, Panamá, República Dominicana y Estados Unidos.</p></div>
      <div>{D(icono('certificado'))}<b>82 certificaciones</b><p>Somos Microsoft Solutions Partner en Infrastructure, Modern Work, Data &amp; AI y Digital &amp; App Innovation.</p></div>
      <div>{D(icono('trofeo'))}<b>WITSA 2026</b><p>ARIA IA Generativa, que desarrollamos con Bancaribe, recibió el reconocimiento de los Global AI Awards.</p></div>
      <div>{D(icono('objetivo'))}<b>Un responsable</b><p>Operamos ambos mundos y validamos cada producto Cisco contra su plataforma Microsoft.</p></div>
    </div>
  </div>
</section>

<section class="soft faq" id="preguntas">
  <div class="wrap">
    <div class="section-head"><p class="eyebrow">Preguntas frecuentes</p><h2>Respondemos sus dudas</h2></div>
    {faq}
  </div>
</section>

<section id="contacto">
  <div class="wrap contact">
    <div>
      <p class="eyebrow">Contacto</p>
      <h2>Un ecosistema, un solo responsable</h2>
      <p class="lead">Conversemos sobre su red y su plataforma Microsoft. Comenzamos con un Diagnóstico Red + Nube gratuito.</p>
    </div>
    <form class="form" id="form-contacto">
      <div class="row">
        <div><label for="f-nombre">Nombre y apellido</label><input id="f-nombre" autocomplete="name" required></div>
        <div><label for="f-empresa">Empresa</label><input id="f-empresa" autocomplete="organization" required></div>
      </div>
      <div class="row">
        <div><label for="f-correo">Correo corporativo</label><input id="f-correo" type="email" autocomplete="email" required></div>
        <div><label for="f-pais">País</label><select id="f-pais">{paises}</select></div>
      </div>
      <label for="f-interes">Solución de interés</label>
      <select id="f-interes">{opciones}</select>
      <label for="f-mensaje">Mensaje</label>
      <textarea id="f-mensaje" rows="3"></textarea>
      <button class="btn btn-primary" type="submit">Enviar</button>
      <p class="ok" id="form-ok">Gracias. Le contactaremos en breve. (Maqueta: en producción conectamos este formulario al CRM).</p>
    </form>
  </div>
</section>"""
    ld = [{"@type": "WebPage", "name": "Soluciones Cisco + Microsoft", "url": URL_BASE, "inLanguage": "es"},
          {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}]
    pagina("index.html", "index",
           "Soluciones Cisco y Microsoft: redes, ciberseguridad e IA | Consein",
           "Integramos redes Cisco con su plataforma Microsoft: SD-WAN para Azure, Zero Trust, Microsoft Teams Rooms, observabilidad e IA segura. Venezuela, Panamá, República Dominicana y EE. UU.",
           cuerpo, ld)

# ---------------------------------------------------------------------------
# Soluciones
# ---------------------------------------------------------------------------
def tarjeta_producto(m, area):
    """Tarjeta: título y valor visibles; el resto en la subpantalla "Seguir leyendo…"."""
    texto = m["valor"] + (" " + m["extra"] if m.get("extra") else "")
    filas = [("Capa / función", E(m["capa"])),
             ("Producto Microsoft asociado", E(m["ms"])),
             ("Cómo agrega valor", E(texto)),
             ("Servicio Consein", "<br>".join(E(o) for o in m["origen"]))]
    dl = "".join(f"<dt>{a}</dt><dd>{b}</dd>" for a, b in filas)
    return f"""<article class="card" id="{m['id']}">
  <h3>{E(m['nombre'])}</h3>
  <p>{E(m['valor'])}</p>
  <a class="more" href="#{m['id']}" aria-label="Seguir leyendo: {E(m['nombre'])}">Seguir leyendo…</a>
  <div class="detalle-src" id="detalle-{m['id']}">
    <p class="code">{E(area['nombre'])} · Producto Cisco</p>
    <h2>{E(m['nombre'])}</h2>
    <p class="value">{E(m['valor'])}</p>
    <dl>{dl}</dl>
    <a class="btn btn-primary" href="index.html?interes={area['id']}#contacto">Solicitar información</a>
  </div>
</article>"""


def soluciones():
    chips = "".join(f'<a href="#{e["id"]}">{E(e["nombre"])}</a>' for e in ESPECIALIDADES)
    criterios = "".join(f"<div>{D(icono(ic))}<b>{E(t)}</b><p>{E(d)}</p></div>"
                        for (t, d), ic in zip(CRITERIOS, ("infraestructura", "integral", "objetivo")))
    vista = ""
    for i, e in enumerate(ESPECIALIDADES, 1):
        n = len(productos_area(e["id"]))
        vista += f"""<a class="tile" href="#{e['id']}">{D(icono(e['id']) + f'<span class="idx">0{i}</span>')}
  <h3>{i}. {E(e['nombre'])}</h3><p>{E(e['intro'])}</p><span class="count">{n} {'producto' if n == 1 else 'productos'}</span></a>"""
    vista += f"""<div class="tile featured">{D(icono('integral'))}
  <h3>Total: {len(MATRIZ)} productos</h3><p>Entradas de producto Cisco sin colisión relevante con la plataforma Microsoft. Algunos productos aparecen en más de un área.</p></div>"""
    areas = ""
    for e in ESPECIALIDADES:
        cisco, ms = tecnologias_area(e["id"])
        cards = "".join(tarjeta_producto(m, e) for m in productos_area(e["id"]))
        areas += f"""<section class="area" id="{e['id']}">
  <div class="wrap">
    <div class="area-head">
      <div>{D(icono(e['id']))}<p class="eyebrow">{E(e['nombre'])}</p><h2>{E(e['h2'])}</h2></div>
      <div><p>{E(e['intro'])}</p><p class="tech"><b>Cisco:</b> {E(cisco)} · <b>Microsoft:</b> {E(ms)}</p></div>
    </div>
    <div class="grid g3">{cards}</div>
  </div>
</section>"""
    cuerpo = f"""
<section class="page-head">
  <div class="wrap">
    <p class="crumbs"><a href="index.html">Inicio</a> › Soluciones Cisco › Soluciones de Valor</p>
    <h1>Cisco suma valor a su plataforma Microsoft</h1>
    <p class="lead">Seleccionamos productos Cisco del Modelo de Servicios Cisco de Consein, filtrados por colisión con los servicios Microsoft y organizados en nuestras 7 áreas de práctica.</p>
    <nav class="chips" aria-label="Áreas de práctica">{chips}</nav>
  </div>
</section>

<section id="criterio">
  <div class="wrap">
    <div class="section-head"><p class="eyebrow">Criterio de selección</p><h2>Solo productos que suman valor</h2>
      <p class="lead">Incluimos productos del Modelo de Servicios (servicios 1 a 7) que cumplen al menos una de estas condiciones y respetan su inversión Microsoft: una sola función, una sola consola y una sola licencia por necesidad.</p></div>
    <div class="grid g3 proof">{criterios}</div>
    <p class="note" style="margin-top:32px">Excluimos los productos con colisión alta o media frente a Microsoft, como Cisco Duo y Cisco XDR. Cada producto indica el servicio Consein del que proviene.</p>
  </div>
</section>

<section class="soft" id="vista">
  <div class="wrap">
    <div class="section-head"><p class="eyebrow">Vista consolidada</p><h2>Valor agregado por área de práctica</h2></div>
    <div class="grid g4">{vista}</div>
  </div>
</section>
{areas}
{banda('Conversemos sobre el valor que Cisco suma a su plataforma Microsoft', 'Hablar con un especialista', 'index.html#contacto')}"""
    ld = [{"@type": "WebPage", "name": "Cisco suma valor a su plataforma Microsoft", "url": URL_BASE + "soluciones", "inLanguage": "es",
           "breadcrumb": {"@type": "BreadcrumbList", "itemListElement": [
               {"@type": "ListItem", "position": 1, "name": "Inicio", "item": URL_BASE},
               {"@type": "ListItem", "position": 2, "name": "Soluciones de Valor", "item": URL_BASE + "soluciones"}]}},
          {"@type": "ItemList", "name": "Matriz de valor Cisco + Microsoft",
           "itemListElement": [{"@type": "ListItem", "position": i + 1, "item": {
               "@type": "Service", "name": m["nombre"], "description": m["valor"],
               "serviceType": next(e["nombre"] for e in ESPECIALIDADES if e["id"] == m["area"]),
               "provider": {"@id": URL_BASE + "#consein"}, "url": URL_BASE + "soluciones#" + m["id"],
               "areaServed": [{"@type": "Country", "name": p} for p in PAISES]}} for i, m in enumerate(MATRIZ)]}]
    pagina("soluciones.html", "soluciones",
           "Matriz de valor Cisco + Microsoft: 19 productos en 7 áreas | Consein",
           "Productos Cisco que suman valor a Microsoft 365, Azure, Teams, Dynamics 365, Power BI y Copilot Studio: Meraki, Cisco SD-WAN, Secure Firewall, ISE, Secure Access, Room Bar, Board Pro y AI Defense.",
           cuerpo, ld)

# ---------------------------------------------------------------------------
# Productos · Programa Renueva
# ---------------------------------------------------------------------------
def productos():
    cards = "".join(tarjeta(p, "Programa Renueva", renovacion=True) for p in PRODUCTOS)
    rutas = [
        ("Switches de campus legados", "Cisco Catalyst 9000 o Meraki MS", "Segmentación Zero Trust con ISE e Intune y PoE para salas y teléfonos Teams."),
        ("WiFi de generaciones anteriores", "WiFi de nueva generación Catalyst o Meraki", "Mejor experiencia en Teams, Microsoft 365 y Copilot."),
        ("Routers de sucursal y MPLS", "Catalyst 8000 o Meraki MX con SD-WAN", "Conexión directa con Azure Virtual WAN."),
        ("Firewalls legados", "Cisco Secure Firewall", "Eventos en Microsoft Sentinel y complemento de Azure Firewall."),
        ("Switching de datacenter legado", "Nexus 9000 o ACI", "Base para la operación híbrida con Azure Arc."),
        ("Servidores UCS antiguos", "UCS actuales con Intersight", "Azure Arc y Azure Local sobre hardware validado."),
        ("Video y telefonía legada", "Room Kit, Board, Desk y teléfonos Cisco", "Microsoft Teams Rooms y Teams Phone como plataforma única."),
    ]
    filas = "".join(f"<tr><td>{E(a)}</td><td>{E(b)}</td><td>{E(c)}</td></tr>" for a, b, c in rutas)
    senales = [
        "Sus equipos Cisco tienen más de cinco años o ya recibieron un anuncio de fin de venta o de soporte.",
        "El WiFi se satura en reuniones de Teams o en horas pico.",
        "Sus firewalls o routers de sucursal llevan tiempo sin actualizaciones.",
        "Cada cambio de configuración exige visitar sede por sede.",
        "Su red todavía aplica políticas de acceso independientes del cumplimiento de Intune.",
        "Sus salas de video funcionan fuera de Microsoft Teams.",
        "Su auditor o su aseguradora preguntó por equipos sin soporte.",
    ]
    checks = "".join(f'<label><input type="checkbox"> {E(s)}</label>' for s in senales)
    cuerpo = f"""
<section class="page-head">
  <div class="wrap">
    <p class="crumbs"><a href="index.html">Inicio</a> › Ofertas de Productos</p>
    <h1>Programa Renueva: renovación de redes Cisco</h1>
    <p class="lead">Renovamos sus equipos Cisco obsoletos por una red segura, gestionable y conectada a Teams, Azure e Intune. Inventariamos, priorizamos por riesgo, migramos por fases y gestionamos el financiamiento con bancos locales.</p>
    <div class="actions"><a class="btn btn-primary" href="index.html?interes=REN-01#contacto">Solicitar inventario gratuito</a><a class="btn btn-line" href="#ofertas">Ver ofertas</a></div>
  </div>
</section>
{aviso('productos')}

<section id="por-que-renovar">
  <div class="wrap">
    <div class="section-head"><p class="eyebrow">Por qué renovar ahora</p><h2>La red define el ritmo de su plataforma</h2>
      <p class="lead">Mientras Microsoft evoluciona cada trimestre, los equipos desactualizados frenan la experiencia, limitan las integraciones y elevan el riesgo.</p></div>
    <div class="grid g4">
      <div class="stat" style="--p:71"><b>71%</b><p>de las organizaciones tiene activos de red mayormente envejecidos u obsoletos.</p><cite>NTT DATA, 2024</cite></div>
      <div class="stat" style="--p:69"><b>69%</b><p>del hardware con fin de soporte programado quedará sin soporte en 2027.</p><cite>NTT DATA, 2024</cite></div>
      <div class="stat" style="--p:42.5"><b>42,5%</b><p>de las vulnerabilidades explotadas en equipos de borde afectó a dispositivos en fin de vida.</p><cite>VulnCheck, 2025</cite></div>
      <div class="stat" style="--p:31"><b>31%</b><p>de las brechas comenzó por la explotación de vulnerabilidades.</p><cite>Verizon DBIR, 2026</cite></div>
    </div>
    <p class="note" style="margin-top:40px">En febrero de 2026, la CISA de Estados Unidos emitió la directiva BOD 26-02, que ordena reemplazar los equipos de borde sin soporte del fabricante. Auditorías, contratos y pólizas de ciberseguro ya la toman como referencia.</p>
  </div>
</section>

<section class="soft" id="autodiagnostico">
  <div class="wrap">
    <div class="grid g2" style="gap:64px;align-items:start">
      <div><p class="eyebrow">Autodiagnóstico</p><h2>¿Su red necesita renovación?</h2>
        <p class="lead">Marque las señales que reconoce. Con dos o más, le recomendamos un inventario de obsolescencia.</p></div>
      <form class="check" onsubmit="return false">
        {checks}
        <div class="meter" aria-hidden="true"><i id="meter"></i></div>
        <p class="verdict" id="verdict" aria-live="polite">Marque las señales que reconoce en su empresa.</p>
        <a class="btn btn-primary" href="index.html?interes=REN-01#contacto">Solicitar inventario</a>
      </form>
    </div>
  </div>
</section>

<section id="rutas">
  <div class="wrap">
    <div class="section-head"><p class="eyebrow">Rutas de renovación</p><h2>De lo obsoleto a lo que potencia Microsoft</h2></div>
    <div class="table-scroll"><table class="table routes">
      <thead><tr><th>Renovamos</th><th>Hacia</th><th>Beneficio en Microsoft</th></tr></thead>
      <tbody>{filas}</tbody></table></div>
    <p class="small" style="margin-top:16px">Validamos las fechas de fin de venta y de soporte de cada modelo contra los anuncios oficiales de Cisco durante el inventario.</p>
  </div>
</section>

<section class="soft" id="como-renovamos">
  <div class="wrap">
    <div class="section-head"><p class="eyebrow">Cómo renovamos</p><h2>Cinco pasos, con su operación activa</h2></div>
    <ol class="steps">
      <li><b>Inventario</b><span>Base instalada y fechas oficiales de fin de soporte.</span></li>
      <li><b>Priorización</b><span>Riesgo, criticidad y costo total.</span></li>
      <li><b>Diseño</b><span>Arquitectura Cisco + Microsoft y financiamiento.</span></li>
      <li><b>Migración</b><span>Por oleadas, en ventanas acordadas.</span></li>
      <li><b>Operación</b><span>Servicio gestionado y retiro responsable.</span></li>
    </ol>
  </div>
</section>

<section id="ofertas">
  <div class="wrap">
    <div class="section-head"><p class="eyebrow">Ofertas de renovación</p><h2>Ocho productos del Programa Renueva</h2></div>
    <div class="grid g4">{cards}</div>
  </div>
</section>
{banda('Inventariemos su red gratis', 'Solicitar inventario', 'index.html?interes=REN-01#contacto')}"""
    ld = [{"@type": "WebPage", "name": "Programa Renueva: renovación de redes Cisco", "url": URL_BASE + "productos", "inLanguage": "es",
           "breadcrumb": {"@type": "BreadcrumbList", "itemListElement": [
               {"@type": "ListItem", "position": 1, "name": "Inicio", "item": URL_BASE},
               {"@type": "ListItem", "position": 2, "name": "Ofertas de Productos", "item": URL_BASE + "productos"}]}},
          {"@type": "ItemList", "name": "Programa Renueva",
           "itemListElement": [{"@type": "ListItem", "position": i + 1, "item": servicio_ld(p, "Renovación de infraestructura Cisco")} for i, p in enumerate(PRODUCTOS)]}]
    pagina("productos.html", "productos",
           "Programa Renueva: renovación de equipos Cisco obsoletos | Consein",
           "Renovamos switches, WiFi, routers, firewalls, servidores UCS y salas Cisco en fin de soporte. Inventario de obsolescencia sin costo, migración por fases y financiamiento.",
           cuerpo, ld)


# ---------------------------------------------------------------------------
# Versión de un solo archivo (para abrir con doble clic o enviar por correo)
# ---------------------------------------------------------------------------
def version_unica(nombre="Consein_Cisco_sitio_completo.html", digital=False):
    import base64
    import re

    def data_uri(ruta, tipo):
        return f"data:{tipo};base64," + base64.b64encode((RAIZ / ruta).read_bytes()).decode()

    paginas = {"index": "inicio", "soluciones": "soluciones", "productos": "productos"}
    fuentes = {}
    for archivo, pag in paginas.items():
        fuentes[pag] = GEN[f"{archivo}.html"]

    def reescribir(fragmento, actual):
        def rw(m):
            pre, href = m.group(1), m.group(2)
            a = re.match(r"(index|soluciones|productos)\.html(?:\?interes=([\w-]+))?(?:#([\w-]+))?$", href)
            if a:
                destino = "#" + paginas[a.group(1)]
                if a.group(3):
                    destino += ":" + a.group(3)
                if a.group(2):
                    destino += "?interes=" + a.group(2)
                return f'{pre}href="{destino}"'
            if href.startswith("#") and actual:
                return f'{pre}href="#{actual}:{href[1:]}"'
            return m.group(0)
        # Solo enlaces <a>: las referencias internas de SVG (textPath) no se tocan
        return re.sub(r'(<a\b[^>]*?)href="([^"]*)"', rw, fragmento)

    meta, cuerpos = {}, []
    for pag, doc in fuentes.items():
        meta[pag] = {"title": html.unescape(re.search(r"<title>(.*?)</title>", doc).group(1)),
                     "description": html.unescape(re.search(r'<meta name="description" content="(.*?)">', doc).group(1))}
        main = re.search(r'<main id="contenido">(.*?)</main>', doc, re.S).group(1)
        oculto = "" if pag == "inicio" else " hidden"
        cuerpos.append(f'<div class="page" data-page="{pag}"{oculto}>{reescribir(main, pag)}</div>')

    base = fuentes["inicio"]
    cabecera = re.search(r'<header class="site-header">.*?</header>', base, re.S).group(0)
    cabecera = cabecera.replace(' aria-current="page"', "")
    cabecera = cabecera.replace('<a class="nav-link" href="index.html"', '<a class="nav-link" data-nav="inicio" href="index.html"')
    cabecera = cabecera.replace('aria-haspopup="true">Soluciones Cisco', 'aria-haspopup="true" data-nav="soluciones productos">Soluciones Cisco')
    cabecera = reescribir(cabecera, None)
    pie_html = reescribir(re.search(r"<footer.*?</dialog>", base, re.S).group(0), None)

    css = (RAIZ / "assets/css/estilos.css").read_text(encoding="utf-8")
    if digital:
        css += "\n" + (RAIZ / "assets/css/digital.css").read_text(encoding="utf-8")
    css = re.sub(r'url\("\.\./fonts/(poppins-[\w-]+\.woff2)"\)',
                 lambda m: 'url("' + data_uri("assets/fonts/" + m.group(1), "font/woff2") + '")', css)
    css = re.sub(r',url\("\.\./fonts/Haltto[^)]*\) format\("woff2"\)', "", css)  # Haltto: solo si está instalada
    js = (RAIZ / "assets/js/app.js").read_text(encoding="utf-8")
    if digital:
        js += "\n" + (RAIZ / "assets/js/digital.js").read_text(encoding="utf-8")
    logo = data_uri("assets/img/logo-consein.png", "image/png")
    logo_blanco = data_uri("assets/img/logo-consein-blanco.png", "image/png")

    doc = f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(meta['inicio']['title'])}</title>
<meta name="description" content="{E(meta['inicio']['description'])}">
<style>
{css}
</style>
<script type="application/json" id="paginas">{json.dumps(meta, ensure_ascii=False)}</script>
</head>
<body data-single{' class="theme-digital"' if digital else ''}>
<a class="skip" href="#contenido">Saltar al contenido</a>
{cabecera}
<main id="contenido">
{''.join(cuerpos)}
</main>
{pie_html.replace('<script src="assets/js/app.js"></script>', '')}
<script>
{js}
</script>
</body>
</html>
"""
    doc = doc.replace('src="assets/img/logo-consein.png"', f'src="{logo}"')
    doc = doc.replace('src="assets/img/logo-consein-blanco.png"', f'src="{logo_blanco}"')
    assert "assets/" not in doc.replace("assets/fonts/", ""), "quedó una referencia externa"
    (RAIZ / nombre).write_text(doc, encoding="utf-8")
    print("✔", nombre, f"({len(doc) // 1024} KB, un solo archivo)")


if __name__ == "__main__":
    # Tema minimal: sitio de 3 páginas + versión de un solo archivo
    inicio()
    soluciones()
    productos()
    version_unica()
    # Tema digital: versión de ejemplo en un solo archivo (paleta #1b245b / #58bb47)
    TEMA = "digital"
    GEN.clear()
    inicio()
    soluciones()
    productos()
    version_unica("Consein_Cisco_diseno_digital.html", digital=True)
