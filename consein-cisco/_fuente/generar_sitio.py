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
  <text x="{cx}" y="{cy + 38}" text-anchor="middle" class="core-sub">núcleo</text>
</svg></div>"""


ARTE_CAPAS = """<div class="stack" aria-hidden="true">
  <div class="layer l1"><span class="tag">Núcleo</span><b>Microsoft</b><small>Identidad · Microsoft 365 · Azure · Dynamics 365 · IA</small></div>
  <div class="layer l2"><span class="tag">Acelerador</span><b>Cisco</b><small>Red · Seguridad perimetral · Salas · Observabilidad</small></div>
  <div class="layer l3"><span class="tag">Integrador</span><b>Consein</b><small>Diseñamos, implementamos y operamos con un solo responsable</small></div>
</div>"""

# ---------------------------------------------------------------------------
# Especialidades (7) — cada una apunta a un grupo de palabras clave SEO
# ---------------------------------------------------------------------------
ESPECIALIDADES = [
    {"id": "infraestructura", "nombre": "Infraestructura",
     "h2": "Infraestructura de red y SD-WAN para Azure",
     "intro": "Conectamos sus sedes, su campus y su datacenter con Azure y Microsoft 365 mediante redes Cisco Catalyst, Nexus y Meraki SD-WAN, gestionadas desde la nube.",
     "cisco": "Catalyst, Nexus, ACI, Meraki SD-WAN, Catalyst 8000V, ThousandEyes, Intersight",
     "microsoft": "Azure Virtual WAN, Azure Arc, Azure Monitor, ExpressRoute"},
    {"id": "seguridad", "nombre": "Seguridad",
     "h2": "Ciberseguridad y Zero Trust de red",
     "intro": "Extendemos Zero Trust desde la identidad Microsoft hasta cada puerto de red y concentramos todos los eventos en Microsoft Sentinel.",
     "cisco": "Cisco ISE, TrustSec, Secure Firewall, Secure Network Analytics",
     "microsoft": "Entra ID, Intune, Defender, Microsoft Sentinel, Azure Firewall"},
    {"id": "colaboracion", "nombre": "Colaboración",
     "h2": "Colaboración y salas Microsoft Teams Rooms",
     "intro": "Diseñamos salas Microsoft Teams Rooms en hardware Cisco certificado y medimos la calidad real de cada llamada.",
     "cisco": "Room Kit, Board, Desk, Control Hub, ThousandEyes",
     "microsoft": "Microsoft Teams, Teams Rooms, Teams Phone, Microsoft 365 Copilot"},
    {"id": "data-analitica", "nombre": "Data y Analítica",
     "h2": "Data, analítica y observabilidad de aplicaciones",
     "intro": "Medimos el rendimiento de sus aplicaciones de punta a punta y publicamos los indicadores de disponibilidad en Power BI.",
     "cisco": "AppDynamics, ThousandEyes Cloud Insights, Splunk Observability",
     "microsoft": "Azure Monitor, Application Insights, Power BI, Microsoft Fabric"},
    {"id": "servicios-empresariales", "nombre": "Servicios Empresariales",
     "h2": "Acceso seguro a Dynamics 365 y Business Central",
     "intro": "Conectamos a usuarios remotos, sedes y terceros con sus aplicaciones de negocio mediante acceso basado en identidad.",
     "cisco": "Cisco Secure Access, Catalyst, Meraki, AppDynamics",
     "microsoft": "Dynamics 365, Business Central, Entra ID"},
    {"id": "automatizacion", "nombre": "Automatización",
     "h2": "Automatización de redes con Power Platform",
     "intro": "Automatizamos la operación de la red con flujos de Power Automate que orquestan las APIs de Cisco.",
     "cisco": "Meraki Dashboard API, Catalyst Center API, Cisco NSO",
     "microsoft": "Power Automate, Logic Apps, Azure Automation, Copilot Studio"},
    {"id": "inteligencia-artificial", "nombre": "Inteligencia Artificial",
     "h2": "Infraestructura y seguridad para inteligencia artificial",
     "intro": "Preparamos la red y protegemos los modelos y agentes de IA que usted lleva a producción en Azure.",
     "cisco": "Cisco AI Defense, Hypershield, Secure AI Factory, ThousandEyes",
     "microsoft": "Microsoft Foundry, Azure OpenAI, Copilot Studio, Defender for Cloud, Purview"},
]

# ---------------------------------------------------------------------------
# Soluciones (15 offerings)
# ---------------------------------------------------------------------------
SOLUCIONES = [
    {"code": "CSC-01", "esp": "infraestructura", "titulo": "Diagnóstico Red + Nube",
     "valor": "Evaluamos de forma gratuita, en 8 horas y en remoto, si su red y su conexión a Azure acompañan a su plataforma Microsoft.",
     "ideal": "Empresas que usan Microsoft 365 y Azure y perciben lentitud o cortes en sus sedes.",
     "resuelve": "Alineamos la red, las sedes y el acceso con la inversión que usted ya hizo en la nube.",
     "incluye": ["Revisamos la red de campus, las sucursales y la conexión a Azure y Microsoft 365.",
                 "Medimos la experiencia de los usuarios en Teams, Dynamics 365 y Copilot.",
                 "Mapeamos los riesgos de seguridad en la capa de red.",
                 "Entregamos una hoja de ruta Cisco + Microsoft priorizada."],
     "resultado": "Le entregamos un diagnóstico integral y un plan priorizado que protege su inversión Microsoft.",
     "tec": ("ThousandEyes, análisis de red, WiFi y SD-WAN", "Azure, Microsoft 365 y su licenciamiento"),
     "dato": "Las fallas digitales inesperadas cuestan a las empresas Global 2000 cerca de 9% de sus utilidades (Splunk y Oxford Economics, 2024).",
     "cta": "Diagnostiquemos su red"},
    {"code": "CSC-02", "esp": "infraestructura", "titulo": "Red híbrida para Azure",
     "valor": "Conectamos todas sus sucursales a Azure con SD-WAN Cisco y Azure Virtual WAN, con rendimiento estable y control central.",
     "ideal": "Organizaciones con varias sucursales que trabajan en Azure y Microsoft 365.",
     "resuelve": "Reducimos el costo de los enlaces y unificamos la experiencia de acceso a la nube en todas las sedes.",
     "incluye": ["Diseñamos la red híbrida con Meraki SD-WAN o Catalyst 8000V en Azure.",
                 "Integramos Azure Virtual WAN como red troncal.",
                 "Priorizamos el tráfico de Teams, Microsoft 365 y Dynamics 365.",
                 "Monitoreamos todas las sucursales desde un solo lugar."],
     "resultado": "Logramos sucursales estables, conectadas a Azure y gestionadas de forma central.",
     "tec": ("Meraki SD-WAN, Catalyst 8000V", "Azure Virtual WAN"),
     "dato": "Con Meraki, las organizaciones reducen 40% el tiempo de inactividad de la red y 80% los tickets de soporte (Forrester TEI de Cisco Meraki, 2025).",
     "cta": "Conectemos sus sedes a Azure"},
    {"code": "CSC-03", "esp": "infraestructura", "titulo": "Campus y datacenter modernos",
     "valor": "Modernizamos la red de campus y datacenter con Cisco Catalyst y Nexus para sostener su operación híbrida con Azure.",
     "ideal": "Empresas con redes de campus o datacenter al final de su vida útil que operan cargas híbridas con Azure.",
     "resuelve": "Eliminamos cuellos de botella y fallas de conectividad en la base física de su plataforma.",
     "incluye": ["Diseñamos el campus con Cisco Catalyst y el datacenter con Nexus / ACI.",
                 "Conectamos con Azure mediante ExpressRoute o VPN.",
                 "Implementamos segmentación y alta disponibilidad.",
                 "Documentamos y transferimos el conocimiento a su equipo."],
     "resultado": "Le entregamos una red física confiable, gobernada en la capa cloud por Azure Arc.",
     "tec": ("Catalyst, Nexus, ACI", "Azure networking, Azure Arc"),
     "cta": "Modernicemos su red"},
    {"code": "CSC-04", "esp": "infraestructura", "titulo": "Red gestionada Meraki",
     "valor": "Operamos su red de sedes desde la nube con especialistas Consein y Cisco Meraki.",
     "ideal": "Empresas distribuidas con equipos de TI pequeños.",
     "resuelve": "Centralizamos los cambios, detectamos fallas a tiempo y reducimos las visitas técnicas.",
     "incluye": ["Operamos switches, WiFi y SD-WAN Meraki.",
                 "Aplicamos actualizaciones de firmware y cambios de configuración de forma centralizada.",
                 "Enviamos las alertas a Microsoft Teams.",
                 "Reportamos la disponibilidad cada mes en Power BI."],
     "resultado": "Logramos una red estable y liberamos a su equipo interno para el negocio.",
     "tec": ("Cisco Meraki", "Microsoft Teams, Power BI"),
     "dato": "Forrester reporta 90% menos tiempo en actualizaciones y cambios de configuración, y 75% menos visitas técnicas con Meraki (TEI de Cisco Meraki, 2025).",
     "cta": "Operemos su red"},
    {"code": "CSC-05", "esp": "infraestructura", "titulo": "Operación híbrida unificada",
     "valor": "Unificamos la gestión de su infraestructura híbrida en Azure Arc con la telemetría experta de Cisco Intersight.",
     "ideal": "Organizaciones con servidores Cisco UCS que usan Azure Arc como plano de gestión.",
     "resuelve": "Anticipamos fallas de hardware y concentramos el monitoreo en una sola consola.",
     "incluye": ["Integramos la telemetría de Cisco Intersight.",
                 "Gobernamos los recursos híbridos con Azure Arc.",
                 "Configuramos alertas proactivas de hardware.",
                 "Definimos los procedimientos de operación."],
     "resultado": "Reducimos los incidentes y aceleramos la respuesta desde una sola consola.",
     "tec": ("Cisco Intersight", "Azure Arc"),
     "dato": "Intersight: 192% de ROI y 50% menos tiempo medio de resolución (Forrester TEI, 2025). Azure Arc: 30% más productividad de TI (Forrester TEI, 2025).",
     "cta": "Unifiquemos su operación"},
    {"code": "CSC-06", "esp": "seguridad", "titulo": "Zero Trust de red",
     "valor": "Damos acceso a su red solo a las personas y los dispositivos que cumplen sus políticas, con Cisco ISE y Microsoft Intune.",
     "ideal": "Empresas con dispositivos corporativos, invitados y equipos IoT en la misma red.",
     "resuelve": "Segmentamos la red y bloqueamos los dispositivos no conformes en la LAN.",
     "incluye": ["Implementamos control de acceso a la red (NAC) y segmentación con Cisco ISE y TrustSec.",
                 "Integramos el cumplimiento de dispositivos de Microsoft Intune.",
                 "Definimos políticas por usuario, dispositivo y ubicación.",
                 "Acompañamos las pruebas y la adopción."],
     "resultado": "Logramos Zero Trust de extremo a extremo: identidad Microsoft y red Cisco trabajando juntas.",
     "tec": ("Cisco ISE, TrustSec", "Microsoft Intune, Entra ID"),
     "dato": "Solo 4% de las organizaciones tiene un nivel de ciberseguridad maduro (Cisco Cybersecurity Readiness Index, 2025).",
     "cta": "Llevemos Zero Trust a su red"},
    {"code": "CSC-07", "esp": "seguridad", "titulo": "Perímetro protegido",
     "valor": "Protegemos el borde de su red con Cisco Secure Firewall y lo hacemos visible en Microsoft Sentinel.",
     "ideal": "Organizaciones con sedes, plantas o datacenter propios además de la nube.",
     "resuelve": "Modernizamos la protección del borde local e integramos sus eventos en el SIEM.",
     "incluye": ["Diseñamos e implementamos Cisco Secure Firewall en el perímetro local.",
                 "Enviamos los eventos a Microsoft Sentinel.",
                 "Alineamos las políticas con Azure Firewall en la nube.",
                 "Configuramos tableros y procedimientos de respuesta."],
     "resultado": "Le entregamos protección en cada borde y una sola vista de seguridad.",
     "tec": ("Cisco Secure Firewall", "Microsoft Sentinel, Azure Firewall, Defender"),
     "dato": "Secure Firewall: 195% de ROI y recuperación en 10 meses (Forrester TEI, 2022). Defender: 242% de ROI (Forrester TEI, 2025).",
     "cta": "Protejamos su perímetro"},
    {"code": "CSC-08", "esp": "seguridad", "titulo": "Detección de amenazas en la red",
     "valor": "Llevamos la telemetría de su red a Microsoft Sentinel para detectar movimientos laterales y amenazas internas (NDR).",
     "ideal": "Equipos de seguridad que operan Microsoft Sentinel.",
     "resuelve": "Damos al SIEM visibilidad completa de lo que ocurre dentro de la red.",
     "incluye": ["Desplegamos Cisco Secure Network Analytics.",
                 "Enviamos a Sentinel la telemetría de red (NetFlow y comportamiento).",
                 "Enriquecemos las reglas de detección.",
                 "Ajustamos y operamos la solución."],
     "resultado": "Detectamos amenazas antes y fortalecemos su SIEM actual.",
     "tec": ("Cisco Secure Network Analytics", "Microsoft Sentinel"),
     "dato": "77% de las organizaciones afirma que tener más de diez soluciones de seguridad aisladas frena su respuesta (Cisco Cybersecurity Readiness Index, 2025).",
     "cta": "Demos visibilidad a Sentinel"},
    {"code": "CSC-09", "esp": "servicios-empresariales", "titulo": "Acceso seguro a aplicaciones",
     "valor": "Conectamos a usuarios remotos y terceros con Dynamics 365 mediante acceso basado en identidad y trazabilidad completa.",
     "ideal": "Empresas con equipos remotos, proveedores o socios que usan aplicaciones de negocio.",
     "resuelve": "Reemplazamos las VPN tradicionales por accesos mínimos y trazables.",
     "incluye": ["Evaluamos los accesos remotos actuales.",
                 "Implementamos Cisco Secure Access con identidad de Microsoft Entra.",
                 "Definimos políticas por aplicación (Dynamics 365, Business Central).",
                 "Monitoreamos y reportamos cada acceso."],
     "resultado": "Logramos un acceso mínimo, necesario y trazable a sus aplicaciones críticas.",
     "tec": ("Cisco Secure Access", "Entra ID, Dynamics 365, Business Central"),
     "cta": "Controlemos el acceso"},
    {"code": "CSC-10", "esp": "colaboracion", "titulo": "Salas Microsoft Teams Rooms",
     "valor": "Implementamos salas Microsoft Teams Rooms en hardware Cisco certificado, listas para Copilot.",
     "ideal": "Empresas que usan Microsoft Teams y quieren salas híbridas de primer nivel.",
     "resuelve": "Hacemos que cada reunión inicie a tiempo, con audio claro y participación equitativa de los asistentes remotos.",
     "incluye": ["Diseñamos cada sala según su tamaño y uso.",
                 "Instalamos Cisco Room Kit, Board y Desk certificados para Teams Rooms.",
                 "Configuramos Teams Admin Center y gestionamos el hardware en Control Hub.",
                 "Capacitamos a los usuarios y damos soporte."],
     "resultado": "Le entregamos reuniones híbridas equitativas que inician con un toque.",
     "tec": ("Room Kit, Board, Desk, Control Hub", "Microsoft Teams Rooms, Microsoft 365 Copilot"),
     "dato": "Teams Rooms: 342% de ROI (Forrester TEI). Las reuniones híbridas en Teams Rooms se proyectan más de 30% más productivas con Microsoft 365 Copilot (Forrester, 2025).",
     "nortia": "Preparamos las salas para Copilot como parte de la fase Norte de NortIA.",
     "cta": "Diseñemos sus salas"},
    {"code": "CSC-11", "esp": "colaboracion", "titulo": "Experiencia Teams garantizada",
     "valor": "Monitoreamos la calidad de Teams y Microsoft 365 con Cisco ThousandEyes e identificamos la causa de cada falla antes que el usuario.",
     "ideal": "Organizaciones con trabajo remoto, sucursales o centros de atención que dependen de Teams.",
     "resuelve": "Identificamos con precisión la causa de los cortes de audio y video.",
     "incluye": ["Monitoreamos con ThousandEyes la experiencia hacia Teams y Microsoft 365.",
                 "Visualizamos rutas, proveedores de internet y redes no administradas.",
                 "Emitimos alertas y diagnósticos proactivos.",
                 "Reportamos la experiencia cada mes."],
     "resultado": "Reducimos el tiempo de diagnóstico y aumentamos la confianza de los usuarios en Teams.",
     "tec": ("Cisco ThousandEyes", "Microsoft Teams, Teams Admin Center, Microsoft 365"),
     "dato": "ThousandEyes: 50% a 80% menos tiempo para identificar incidentes que afectan a trabajadores remotos y 173% de ROI (Forrester TEI).",
     "cta": "Garanticemos su experiencia Teams"},
    {"code": "CSC-12", "esp": "data-analitica", "titulo": "Observabilidad de aplicaciones",
     "valor": "Medimos el rendimiento de Dynamics 365 y de sus aplicaciones en Azure de punta a punta, con indicadores ejecutivos en Power BI.",
     "ideal": "Empresas que dependen de Dynamics 365, Business Central o aplicaciones en Azure.",
     "resuelve": "Identificamos en minutos si la lentitud está en la red o en la aplicación.",
     "incluye": ["Monitoreamos transacciones con Cisco AppDynamics.",
                 "Visualizamos la red y las sedes con ThousandEyes.",
                 "Integramos Azure Monitor y Application Insights.",
                 "Publicamos los indicadores de disponibilidad en Power BI."],
     "resultado": "Logramos menos interrupciones y una sola fuente de verdad sobre el rendimiento.",
     "tec": ("AppDynamics, ThousandEyes", "Azure Monitor, Application Insights, Power BI, Fabric"),
     "dato": "La observabilidad de Cisco (AppDynamics + ThousandEyes) alcanza 358% de ROI (Forrester TEI, 2024).",
     "cta": "Aseguremos su ERP y CRM"},
    {"code": "CSC-13", "esp": "automatizacion", "titulo": "NetOps automatizado",
     "valor": "Automatizamos la operación de su red con Power Automate y las APIs de Cisco Meraki y Catalyst Center.",
     "ideal": "Empresas con altas y cambios frecuentes de sedes, usuarios o dispositivos.",
     "resuelve": "Convertimos tareas manuales y tickets repetitivos en flujos automáticos.",
     "incluye": ["Integramos las APIs de Meraki y Catalyst Center.",
                 "Construimos flujos en Power Automate y Logic Apps.",
                 "Gestionamos alertas y aprobaciones en Microsoft Teams.",
                 "Orquestamos con Cisco NSO cuando aplica."],
     "resultado": "Aceleramos los cambios de red y los hacemos trazables.",
     "tec": ("Meraki API, Catalyst Center API, Cisco NSO", "Power Automate, Logic Apps, Azure Automation"),
     "dato": "Con Meraki, los cambios de configuración toman 90% menos tiempo (Forrester TEI de Cisco Meraki, 2025).",
     "nortia": "Conectamos los agentes y automatizaciones de la fase Vector de NortIA con su infraestructura.",
     "cta": "Automaticemos su red"},
    {"code": "CSC-14", "esp": "inteligencia-artificial", "titulo": "Red y seguridad para IA",
     "valor": "Protegemos sus agentes y modelos de IA en Azure con Cisco AI Defense, Hypershield y ThousandEyes.",
     "ideal": "Empresas que llevan agentes, Copilot Studio o Azure OpenAI a producción.",
     "resuelve": "Mitigamos la inyección de instrucciones y la fuga de datos, y preparamos la red para escalar la IA.",
     "incluye": ["Protegemos el tráfico de inferencia y los agentes con Cisco AI Defense.",
                 "Microsegmentamos las cargas de IA con Cisco Hypershield.",
                 "Monitoreamos con ThousandEyes el acceso a Copilot y Azure OpenAI.",
                 "Alineamos la protección con Defender for Cloud y Purview."],
     "resultado": "Llevamos su IA a producción con más control y mejor experiencia.",
     "tec": ("AI Defense, Hypershield, ThousandEyes", "Microsoft Foundry, Copilot Studio, Defender for Cloud, Purview"),
     "dato": "Solo 15% de las organizaciones tiene redes listas para la IA y menos de una de cada tres puede detectar amenazas específicas de IA (Cisco AI Readiness Index, 2025).",
     "nortia": "Reforzamos el pilar Trust de la fase Brújula de NortIA.",
     "cta": "Preparemos su red para la IA"},
    {"code": "CSC-15", "esp": "integral", "titulo": "Consein Connected",
     "valor": "Operamos su plataforma Microsoft y su red Cisco como un solo servicio gestionado, con un solo responsable.",
     "ideal": "Empresas que prefieren un único socio para su plataforma Microsoft y su red Cisco.",
     "resuelve": "Integramos a todos sus proveedores bajo un solo responsable y mantenemos los costos bajo control.",
     "incluye": ["Operamos la red Cisco (Meraki / Catalyst) y la plataforma Microsoft.",
                 "Monitoreamos la experiencia con ThousandEyes.",
                 "Integramos la seguridad con Sentinel y Defender.",
                 "Entregamos un reporte ejecutivo mensual único."],
     "resultado": "Operamos su ecosistema de extremo a extremo.",
     "tec": ("Red, seguridad perimetral, salas y observabilidad", "Identidad, productividad, datos, aplicaciones de negocio e IA"),
     "cta": "Hablemos"},
]

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
     "valor": "Financiamos su renovación en cuotas previsibles con Cisco Capital.",
     "ideal": "Empresas que necesitan renovar y cuidan su flujo de caja.",
     "resuelve": "Convertimos la renovación en un gasto programado.",
     "incluye": ["Estructuramos planes de pago con Cisco Capital, según disponibilidad en cada país.",
                 "Gestionamos incentivos por entrega de equipos antiguos cuando el programa está vigente.",
                 "Ofrecemos equipos Cisco Refresh, remanufacturados y certificados.",
                 "Retiramos los equipos reemplazados de forma responsable."],
     "resultado": "Renovamos su infraestructura con un desembolso inicial reducido.",
     "tec": ("Todo el proyecto en un esquema de pagos", "Combinable con la planificación de licencias Microsoft"),
     "dato": "Cisco Lifecycle Pay with Trade-In ofrece hasta 10% de incentivo por reemplazo al entregar equipos existentes (Cisco, condiciones por país).",
     "cta": "Revisemos sus opciones de pago"},
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

def nombre_esp(esp_id):
    for e in ESPECIALIDADES:
        if e["id"] == esp_id:
            return e["nombre"]
    return "Servicio integral"

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
    especialidades += '<li><a href="soluciones.html#integral">Consein Connected</a></li>'
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
              <a class="mega-l2" href="soluciones.html"><b>Soluciones de Valor</b><small>15 soluciones en 7 especialidades</small></a>
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
        <li><a href="index.html?interes=CSC-01#contacto">Diagnóstico Red + Nube</a></li>
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
        "texto": "Le entregamos el mapa de obsolescencia de su base instalada y un plan de renovación priorizado, con costo total y opciones de pago.",
        "cifra": "<small>hasta</small>10%", "cifra_txt": "de incentivo por reemplazo al entregar sus equipos antiguos con Cisco Lifecycle Pay with Trade-In.", "fuente": "Cisco · sujeto a disponibilidad en cada país",
        "lista_tipo": "ol",
        "lista": ["Inventariamos su base instalada y sus fechas de fin de soporte", "Priorizamos por riesgo, criticidad y costo total", "Renovamos por fases, con planes de pago previsibles"],
        "cta2": ("Autodiagnóstico", "#autodiagnostico"),
    },
}


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
        <div class="aviso-stat"><b>{a['cifra']}</b><p>{E(a['cifra_txt'])}<cite>{E(a['fuente'])}</cite></p></div>
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
        n = sum(1 for o in SOLUCIONES if o["esp"] == e["id"])
        tiles += f"""<a class="tile" href="soluciones.html#{e['id']}">{D(icono(e['id']) + f'<span class="idx">0{i}</span>')}
  <h3>{E(e['h2'])}</h3><p>{E(e['intro'])}</p><span class="count">{n} {'solución' if n == 1 else 'soluciones'}</span></a>"""
    tiles += f"""<a class="tile featured" href="soluciones.html#integral" style="border-color:var(--navy)">{D(icono('integral'))}
  <h3>Consein Connected</h3><p>Operamos su plataforma Microsoft y su red Cisco como un solo servicio gestionado.</p><span class="count">Servicio integral</span></a>"""

    faq = "".join(f"<details><summary>{E(q)}</summary><p>{E(a)}</p></details>" for q, a in FAQ)

    opciones = '<option value="">Quiero hablar con un especialista</option><optgroup label="Soluciones">'
    opciones += "".join(f'<option value="{o["code"]}">{E(o["titulo"])}</option>' for o in SOLUCIONES)
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
      <a class="btn btn-primary" href="index.html?interes=CSC-01#contacto">Solicitar diagnóstico gratuito</a>
      <a class="btn btn-line" href="soluciones.html">Ver soluciones</a>
    </div>
    <div class="figures">
      <div><b>15</b><span>soluciones</span></div>
      <div><b>7</b><span>especialidades</span></div>
      <div><b>8</b><span>productos de renovación</span></div>
      <div><b>26</b><span>productos Cisco integrados</span></div>
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
      <p class="lead">Cada especialidad combina tecnología Cisco con su núcleo Microsoft.</p>
    </div>
    <div class="grid g4">{tiles}</div>
  </div>
</section>

<section id="metodo">
  <div class="wrap">
    <div class="section-head"><p class="eyebrow">Cómo trabajamos</p><h2>Un modelo de punta a punta</h2></div>
    <ol class="steps">
      <li><b>Evaluamos</b><span>Diagnóstico Red + Nube gratuito, de 8 horas y remoto.</span></li>
      <li><b>Diseñamos</b><span>Arquitecturas Cisco + Microsoft bajo CAF/WAF y Zero Trust.</span></li>
      <li><b>Ejecutamos</b><span>Implementamos con mínima interrupción.</span></li>
      <li><b>Acompañamos</b><span>Servicio gestionado y reporte ejecutivo mensual.</span></li>
      <li><b>Optimizamos</b><span>Mejora continua de red, seguridad y experiencia.</span></li>
    </ol>
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
def soluciones():
    chips = "".join(f'<a href="#{e["id"]}">{E(e["nombre"])}</a>' for e in ESPECIALIDADES) + '<a href="#integral">Servicio integral</a>'
    areas = ""
    for e in ESPECIALIDADES:
        cards = "".join(tarjeta(o, e["nombre"]) for o in SOLUCIONES if o["esp"] == e["id"])
        areas += f"""<section class="area" id="{e['id']}">
  <div class="wrap">
    <div class="area-head">
      <div>{D(icono(e['id']))}<p class="eyebrow">{E(e['nombre'])}</p><h2>{E(e['h2'])}</h2></div>
      <div><p>{E(e['intro'])}</p><p class="tech"><b>Cisco:</b> {E(e['cisco'])} · <b>Microsoft:</b> {E(e['microsoft'])}</p></div>
    </div>
    <div class="grid g3">{cards}</div>
  </div>
</section>"""
    integral = next(o for o in SOLUCIONES if o["esp"] == "integral")
    cuerpo = f"""
<section class="page-head">
  <div class="wrap">
    <p class="crumbs"><a href="index.html">Inicio</a> › Soluciones de Valor</p>
    <h1>Soluciones Cisco para su plataforma Microsoft</h1>
    <p class="lead">Quince soluciones en siete especialidades. Cada una suma tecnología Cisco a Azure, Microsoft 365, Teams o Dynamics 365.</p>
    <nav class="chips" aria-label="Especialidades">{chips}</nav>
  </div>
</section>
{areas}
<section class="area" id="integral">
  <div class="wrap">
    <div class="integral" id="{slug(integral['code'])}">
      <div>{D(icono('integral'))}<p class="eyebrow">Servicio integral</p><h2>{E(integral['titulo'])}</h2><p class="lead" style="margin:0">{E(integral['valor'])}</p></div>
      <div><a class="more" href="#{slug(integral['code'])}">Seguir leyendo…</a>{detalle(integral, 'Servicio integral')}</div>
    </div>
  </div>
</section>
{banda('Comencemos con un Diagnóstico Red + Nube gratuito', 'Solicitar diagnóstico', 'index.html?interes=CSC-01#contacto')}"""
    ld = [{"@type": "WebPage", "name": "Soluciones Cisco para su plataforma Microsoft", "url": URL_BASE + "soluciones", "inLanguage": "es",
           "breadcrumb": {"@type": "BreadcrumbList", "itemListElement": [
               {"@type": "ListItem", "position": 1, "name": "Inicio", "item": URL_BASE},
               {"@type": "ListItem", "position": 2, "name": "Soluciones de Valor", "item": URL_BASE + "soluciones"}]}},
          {"@type": "ItemList", "name": "Soluciones Cisco + Microsoft",
           "itemListElement": [{"@type": "ListItem", "position": i + 1, "item": servicio_ld(o, nombre_esp(o["esp"]))} for i, o in enumerate(SOLUCIONES)]}]
    pagina("soluciones.html", "soluciones",
           "Soluciones Cisco para Azure, Microsoft 365 y Teams | Consein",
           "SD-WAN para Azure, Zero Trust con Cisco ISE e Intune, Microsoft Teams Rooms, observabilidad de aplicaciones, automatización de redes y seguridad para IA. 15 soluciones Consein.",
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
    <p class="lead">Renovamos sus equipos Cisco obsoletos por una red segura, gestionable y conectada a Teams, Azure e Intune. Inventariamos, priorizamos por riesgo y migramos por fases, con planes de pago.</p>
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
