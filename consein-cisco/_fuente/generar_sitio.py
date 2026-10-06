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
    "conectividad": '<rect x="3" y="3" width="7" height="5" rx="1"/><rect x="14" y="3" width="7" height="5" rx="1"/><rect x="8.5" y="16" width="7" height="5" rx="1"/><path d="M6.5 8v3h11V8M12 11v5"/>',
    "secaas": '<path d="M7 18a4.5 4.5 0 0 1-.6-8.96A6 6 0 0 1 18 9a4 4 0 0 1 0 9z"/><path d="M9.5 13.5l2 2 3.5-3.5"/>',
    "proteccion-red": '<path d="M12 3l7 3v5c0 4.5-3 8.3-7 10-4-1.7-7-5.5-7-10V6z"/><path d="M9 11h6M9 14h6M12 8v8"/>',
    "usuarios-remotos": '<rect x="4" y="5" width="16" height="11" rx="1.5"/><path d="M2 19h20"/><path d="M10 10.5v-1a2 2 0 0 1 4 0v1M9.5 10.5h5v3h-5z"/>',
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
    nodos = ["SD&#45;WAN", "SECaaS", "Teams Rooms", "Cisco ISE", "AI Defense", "Meraki"]
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
  <text x="{cx}" y="{cy + 38}" text-anchor="middle" class="core-sub">BASE</text>
</svg></div>"""


ARTE_CAPAS = """<div class="stack" aria-hidden="true">
  <div class="layer l1"><span class="tag">BASE</span><b>Microsoft</b><small>Identidad · Microsoft 365 · Azure · Dynamics 365 · IA</small></div>
  <div class="layer l2"><span class="tag">Acelerador</span><b>Cisco</b><small>Red · Seguridad · Salas</small></div>
  <div class="layer l3"><span class="tag">Integrador</span><b>Consein</b><small>Diseñamos, implementamos y operamos con un solo responsable</small></div>
</div>"""

# ---------------------------------------------------------------------------
# Especialidades (7) — cada una apunta a un grupo de palabras clave SEO
# ---------------------------------------------------------------------------
ESPECIALIDADES = [
    # "linea": línea de soluciones Consein a la que pertenece cada área (título visible en el sitio).
    # Productos: Nueva Matriz de Valor v2 (secciones A y B) + Iniciativa SECaaS de Consein.
    {"id": "conectividad", "linea": "Infraestructura", "nombre": "Conectividad LAN y WAN",
     "h2": "Conectividad e interconexión de redes LAN y WAN",
     "intro": "Conectamos sus sedes según el destino del tráfico: aplicaciones SaaS como Microsoft 365 o cargas IaaS en Azure."},
    {"id": "secaas", "linea": "Seguridad", "nombre": "SECaaS",
     "h2": "SECaaS: seguridad como servicio, del endpoint al firewall en la nube",
     "intro": "Convertimos la ciberseguridad en un servicio por consumo: paquetes todo en uno basados en Cisco, administrados por Consein desde Cisco Security Cloud Control."},
    {"id": "proteccion-red", "linea": "Seguridad", "nombre": "Red local y perímetro",
     "h2": "Control de la red local y protección del perímetro",
     "intro": "Ofrecemos por separado Cisco ISE, para controlar quién entra a su red local, y Cisco Secure Firewall, para proteger el borde on-premise y la conectividad híbrida."},
    {"id": "colaboracion", "linea": "Colaboración", "nombre": "Colaboración",
     "h2": "Hardware certificado para Microsoft Teams Rooms",
     "intro": "Implementamos hardware Cisco certificado para la experiencia Microsoft Teams Rooms."},
    {"id": "inteligencia-artificial", "linea": "IA", "nombre": "Inteligencia Artificial",
     "h2": "Adopción responsable de IA",
     "intro": "Acompañamos la adopción de IA en Azure AI Foundry y Copilot Studio, empezando por el inventario y la validación."},
]

# Diferenciadores de SECaaS (Iniciativa SECaaS)
SECAAS_DIF = [
    ("Agnóstico y universal", "Protegemos a sus usuarios sin importar si su empresa usa AWS, Google, servidores locales o aplicaciones a la medida."),
    ("Un solo servicio", "Consolidamos VPN, antivirus y filtrado web en un servicio unificado, con un menor costo total de propiedad."),
    ("Valor inmediato", "Al ser 100% nativo de la nube, activamos las políticas de seguridad en horas o días."),
]

# Criterio de la matriz (v2, Better Together)
CRITERIOS = [
    ("Se integra con Microsoft", "Cisco trabaja junto a su plataforma Microsoft como acelerador: red, seguridad y salas."),
    ("Cubre brechas de red y seguridad", "Posicionamos cada solución donde aporta valor real a su red y a su seguridad."),
    ("Evita duplicar lo que ya paga", "Proponemos solo lo que complementa su inversión Microsoft actual."),
]

S1 = "S1 · Protección Avanzada M365"
S2 = "S2 · Secure Access como Servicio"
S3 = "S3 · Meraki Cloud Managed"
S4 = "S4 · Cisco Rooms para Teams"
S5 = "S5 · SD-WAN Seguro"
S6 = "S6 · Azure + Cisco Secure Firewall"
S7 = "S7 · Cisco AI Defense"

# Productos Cisco por área (Matriz v2, sección B, e Iniciativa SECaaS).
# mensaje = mensaje comercial (visible en la tarjeta); valor = cómo agrega valor (en el detalle).
MATRIZ = [
    {"area": "conectividad", "id": "meraki-mx-secure-access", "nombre": "Meraki MX + Cisco Secure Access",
     "origen": [S3, S5, S2], "mensaje": "Arquitectura SASE: SD-WAN + seguridad en la nube.",
     "ms": "Microsoft 365 / Teams",
     "valor": "Protegemos la red de cada sede y priorizamos el tráfico hacia aplicaciones SaaS como Microsoft 365 y Teams. Meraki MX aporta el SD-WAN y Cisco Secure Access, la seguridad en la nube: juntos forman una arquitectura SASE."},
    {"area": "conectividad", "id": "catalyst-sdwan", "nombre": "Cisco Catalyst SD-WAN",
     "origen": [S5], "mensaje": "Conectividad ágil y resiliente hacia IaaS.",
     "ms": "Azure Virtual WAN / ExpressRoute",
     "valor": "Conectamos de forma segura sus sedes y su centro de datos con las cargas de trabajo en Azure, AWS o GCP, con failover automático y políticas por aplicación."},
    {"area": "conectividad", "id": "meraki-ms-mr", "nombre": "Meraki MS (Switching) y Meraki MR (Wireless)",
     "origen": [S3], "mensaje": "Experiencia digital impecable en sus oficinas.",
     "ms": "Microsoft Teams / Microsoft 365",
     "valor": "Optimizamos la infraestructura Wi-Fi y cableada para que la colaboración, la voz y el video funcionen de forma continua, con gestión 100% en la nube."},
    {"area": "conectividad", "id": "meraki-mg", "nombre": "Meraki MG (Cellular Gateways)",
     "origen": [S3], "mensaje": "Respaldo para que su operación continúe.",
     "ms": "Microsoft 365 / Azure",
     "valor": "Integramos enlaces celulares 4G/5G de respaldo que mantienen el acceso a sus aplicaciones críticas y a Azure cuando falla su proveedor de internet principal, sujeto a la cobertura celular de la sede."},

    {"area": "secaas", "id": "secaas-essential", "nombre": "SECaaS Essential",
     "origen": ["Servicio administrado por Consein desde Cisco Security Cloud Control"],
     "mensaje": "Base sólida para la seguridad moderna: identidad, acceso web y cimientos de Zero Trust.",
     "ms": "Active Directory / Entra ID",
     "ideal": "Medianas empresas y corporaciones que buscan modernizar su seguridad y prefieren delegar su gestión a Consein.",
     "componentes": "Duo Essentials · Cisco Secure Access (SWG/DNS)",
     "incluye": ["MFA avanzado con Cisco Duo (push y OTP).",
                 "Integración con Active Directory / Entra ID.",
                 "Seguridad DNS: bloqueo de malware y phishing.",
                 "SWG (Secure Web Gateway): filtrado web completo.",
                 "Controles de acceso ZTNA (Zero Trust Network Access).",
                 "Gestión operativa de altas y bajas.",
                 "Monitoreo continuo NOC/SOC 24/7."],
     "valor": "Protegemos la identidad y el acceso web de sus usuarios y establecemos los cimientos de Zero Trust para su organización, como un servicio administrado por Consein."},
    {"area": "secaas", "id": "secaas-advantage", "nombre": "SECaaS Advantage",
     "origen": ["Servicio administrado por Consein desde Cisco Security Cloud Control"],
     "mensaje": "Seguridad avanzada y visibilidad total para entornos híbridos y distribuidos.",
     "ms": "Active Directory / Entra ID",
     "ideal": "Organizaciones con entornos híbridos y distribuidos que necesitan protección integral del endpoint y control de la nube.",
     "componentes": "Duo Advantage · Cisco Secure Access (FWaaS/CASB) · Cisco Secure Endpoint (EDR)",
     "incluye": ["Todo lo incluido en SECaaS Essential.",
                 "Autenticación basada en riesgo (MFA avanzado).",
                 "FWaaS (Firewall as a Service) en la nube.",
                 "CASB (Cloud Access Security Broker) para aplicaciones SaaS.",
                 "Inspección avanzada del tráfico web.",
                 "EDR (Endpoint Detection and Response) en el endpoint.",
                 "Bloqueo avanzado de malware en el dispositivo.",
                 "Mayor visibilidad y control de aplicaciones."],
     "valor": "Sumamos a todo lo incluido en Essential la protección integral del endpoint, el firewall en la nube y el control de las aplicaciones SaaS, como un servicio administrado por Consein."},
    {"area": "proteccion-red", "id": "cisco-ise", "nombre": "Cisco ISE (Identity Services Engine)",
     "origen": [S1], "mensaje": "Control de acceso a la red (NAC).",
     "ms": "Microsoft Intune (integración complementaria)",
     "valor": "Controlamos qué usuario y qué dispositivo entra a la red cableada e inalámbrica, y segmentamos el acceso. Evaluamos la postura con Cisco Secure Client y la complementamos con la integración con Intune. Aporta el control de acceso a la red (NAC), una capa que complementa a Microsoft."},
    {"area": "proteccion-red", "id": "secure-firewall", "nombre": "Cisco Secure Firewall",
     "origen": [S6], "mensaje": "Gobierno único de la conectividad híbrida.",
     "ms": "Azure Firewall / Microsoft Sentinel",
     "valor": "Protegemos el borde on-premise y la conectividad entre Azure, sedes y centro de datos con un gobierno único de reglas. Sus registros llegan a Microsoft Sentinel."},
    {"area": "colaboracion", "id": "room-bar", "nombre": "Cisco Room Bar / Room Bar Pro",
     "origen": [S4], "mensaje": "Salas híbridas simples y consistentes.",
     "ms": "Microsoft Teams Rooms",
     "valor": "Instalamos un dispositivo certificado que ejecuta Microsoft Teams Rooms de forma nativa. En Consein sumamos el hardware de sala, la instalación y el soporte."},
    {"area": "colaboracion", "id": "board-pro", "nombre": "Cisco Board Pro Series",
     "origen": [S4], "mensaje": "Colaboración visual en sala.",
     "ms": "Microsoft Teams Rooms / Whiteboard",
     "valor": "Llevamos la reunión híbrida y la pizarra de Teams a una pantalla táctil certificada para salas medianas."},

    {"area": "inteligencia-artificial", "id": "ai-defense", "nombre": "Cisco AI Defense",
     "origen": [S7], "mensaje": "Adopción responsable de IA.",
     "ms": "Azure AI Foundry / Copilot Studio",
     "valor": "Empezamos por el inventario de sus activos de IA y la validación de modelos y aplicaciones. Definimos el alcance de la protección en tiempo real junto a Prompt Shields y Defender for AI."},
]

NUMEROS = {1: "un", 2: "dos", 3: "tres", 4: "cuatro", 5: "cinco", 6: "seis", 7: "siete", 8: "ocho", 9: "nueve", 10: "diez"}


def productos_area(area_id):
    return [m for m in MATRIZ if m["area"] == area_id]


def tecnologias_area(area_id):
    """Cisco y Microsoft de un área, derivados de la propia matriz."""
    import re
    ms = []
    for m in productos_area(area_id):
        for x in re.sub(r"\s*\([^)]*\)", "", m["ms"]).split(" / "):
            if x and x not in ms:
                ms.append(x)
    cisco = []
    for m in productos_area(area_id):
        partes = re.sub(r"\s*\([^)]*\)", "", m["componentes"]).split(" · ") if m.get("componentes") else [m["nombre"]]
        for x in partes:
            if x not in cisco:
                cisco.append(x)
    return ", ".join(cisco), ", ".join(ms)

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
     "valor": "Renovamos switches y access points legados por Meraki MS y Meraki MR, con QoS para la voz y el video de Teams.",
     "ideal": "Oficinas y sedes con switches o WiFi de generaciones anteriores.",
     "resuelve": "Aceleramos la red local y el Wi-Fi y habilitamos el acceso según el cumplimiento de Intune.",
     "incluye": ["Diseñamos la red LAN/WLAN gestionada en la nube con Meraki MS (switching) y Meraki MR (wireless).",
                 "Migramos por oleadas mientras su operación sigue activa.",
                 "Controlamos el acceso a la red con Cisco ISE y Cisco Secure Client, con integración complementaria con Intune.",
                 "Retiramos los equipos antiguos de forma responsable."],
     "resultado": "Le entregamos una red local y un Wi-Fi gestionados en la nube, listos para Teams y Microsoft 365.",
     "tec": ("Switches y access points legados → Meraki MS y Meraki MR", "Microsoft Teams, Microsoft 365, Intune y Entra ID"),
     "dato": "Con Meraki, 40% menos tiempo de inactividad y 80% menos tickets de red (Forrester TEI, 2025).",
     "cta": "Renovemos su campus"},
    {"code": "REN-03", "titulo": "Sucursales con SD-WAN",
     "valor": "Reemplazamos routers legados y enlaces MPLS por Meraki MX con SD-WAN y, junto a Cisco Secure Access, formamos una arquitectura SASE.",
     "ideal": "Empresas con routers de sucursal antiguos o enlaces MPLS.",
     "resuelve": "Protegemos el borde de cada sucursal y priorizamos el tráfico de Microsoft 365 y Teams.",
     "incluye": ["Instalamos Meraki MX con SD-WAN en cada sucursal y sumamos la seguridad en la nube de Cisco Secure Access.",
                 "Conectamos cada sede con Azure Virtual WAN.",
                 "Priorizamos el tráfico de Microsoft 365, Teams y Dynamics 365.",
                 "Agregamos respaldo celular 4G/5G con Meraki MG, sujeto a la cobertura celular de la sede."],
     "resultado": "Logramos sucursales estables, gestionadas en la nube y conectadas a Azure.",
     "tec": ("Routers legados y MPLS → Meraki MX + Cisco Secure Access (SASE) y Meraki MG", "Azure Virtual WAN, Microsoft 365, Teams y Dynamics 365"),
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
    {"code": "REN-05", "titulo": "Conectividad de datacenter y nube",
     "valor": "Renovamos la WAN entre su centro de datos, la sede central y Azure con Cisco Catalyst SD-WAN.",
     "ideal": "Empresas con routers WAN de centro de datos o sede central de generaciones anteriores.",
     "resuelve": "Extendemos las políticas por aplicación hasta Azure IaaS, con failover y visibilidad del desempeño.",
     "incluye": ["Conectamos de forma segura sedes y centro de datos con las cargas en Azure, AWS o GCP mediante Cisco Catalyst SD-WAN.",
                 "Conectamos con Azure mediante Azure Virtual WAN o ExpressRoute.",
                 "Configuramos políticas por aplicación y failover.",
                 "Damos visibilidad del desempeño de la WAN de punta a punta."],
     "resultado": "Le entregamos una WAN de centro de datos y sede central lista para operar con Azure.",
     "tec": ("Routers WAN de datacenter y sede central → Cisco Catalyst SD-WAN", "Azure Virtual WAN y ExpressRoute"),
     "cta": "Planifiquemos su WAN"},
    {"code": "REN-06", "titulo": "Salas para Teams",
     "valor": "Convertimos sus salas de video legadas en salas Microsoft Teams Rooms con Cisco Room Bar y Board Pro Series.",
     "ideal": "Empresas con equipos de videoconferencia de generaciones anteriores.",
     "resuelve": "Unificamos la colaboración en Microsoft Teams Rooms, con hardware certificado.",
     "incluye": ["Instalamos Cisco Room Bar o Room Bar Pro, certificados para Teams Rooms, en salas pequeñas y medianas.",
                 "Llevamos la reunión híbrida y la pizarra de Teams a Cisco Board Pro Series.",
                 "Configuramos Microsoft Teams Rooms y el soporte del hardware de sala.",
                 "Capacitamos a los usuarios y damos soporte."],
     "resultado": "Le entregamos salas Microsoft Teams Rooms con hardware Cisco certificado.",
     "tec": ("Video legado → Cisco Room Bar / Room Bar Pro y Board Pro Series", "Microsoft Teams Rooms y Whiteboard"),
     "dato": "Teams Rooms: 342% de ROI (Forrester TEI).",
     "cta": "Renovemos sus salas"},
    {"code": "REN-07", "titulo": "Renovación financiada",
     "valor": "Gestionamos ante bancos locales el financiamiento de su renovación, para distribuir la inversión en el tiempo.",
     "ideal": "Empresas que necesitan renovar su hardware Cisco y prefieren financiar la inversión.",
     "resuelve": "Abrimos una vía de financiamiento bancario cuando el presupuesto de capital del año no alcanza.",
     "incluye": ["Ayudamos a preparar el expediente técnico y económico del proyecto: alcance, equipos, costo total y plan por fases.",
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
                 "Administramos la base instalada como servicio recurrente."],
     "resultado": "Le aseguramos una infraestructura siempre soportada y un presupuesto predecible.",
     "tec": ("Renovación planificada y continua", "Alineada con el ciclo de vida de su plataforma Microsoft"),
     "cta": "Planifiquemos su ciclo de vida"},
]

FAQ = [
    ("¿Cómo conectan las sedes a Microsoft 365 y Azure?",
     "Según el destino del tráfico. Para aplicaciones SaaS como Microsoft 365 y Teams combinamos Meraki MX con Cisco Secure Access en una arquitectura SASE; para cargas en Azure usamos Cisco Catalyst SD-WAN con Azure Virtual WAN o ExpressRoute. Meraki MG agrega respaldo 4G/5G, sujeto a la cobertura celular de la sede."),
    ("¿Qué es SECaaS de Consein?",
     "Es seguridad como servicio: paquetes todo en uno basados en Cisco Duo, Secure Access y Secure Endpoint, administrados por Consein desde Cisco Security Cloud Control. SECaaS Essential protege la identidad y el acceso web con Zero Trust; SECaaS Advantage suma firewall en la nube, CASB y EDR."),
    ("¿Cómo controlan el acceso a la red local?",
     "Con Cisco ISE controlamos qué usuario y qué dispositivo entra a la red cableada e inalámbrica, evaluamos la postura con Cisco Secure Client y la complementamos con Microsoft Intune. Para el borde on-premise ofrecemos, por separado, Cisco Secure Firewall, que envía sus registros a Microsoft Sentinel."),
    ("¿Qué equipos usan para las salas Microsoft Teams Rooms?",
     "Instalamos Cisco Room Bar, Room Bar Pro y Board Pro Series, dispositivos certificados que ejecutan Microsoft Teams Rooms de forma nativa. En Consein sumamos el hardware de sala, la instalación y el soporte."),
    ("¿Cómo protegen a los usuarios remotos?",
     "Con SECaaS: acceso ZTNA, filtrado web y seguridad DNS con Cisco Secure Access, MFA con Cisco Duo y, en SECaaS Advantage, EDR con Cisco Secure Endpoint, todo administrado por Consein."),
    ("¿Cómo acompañan la adopción de inteligencia artificial?",
     "Con Cisco AI Defense empezamos por el inventario de sus activos de IA y la validación de modelos y aplicaciones en Azure AI Foundry y Copilot Studio."),
]

FUENTES = [
    "Forrester Total Economic Impact™, encargados por Cisco: Cisco Meraki (2025) y Cisco Secure Firewall (2022).",
    "Forrester Total Economic Impact™, encargado por Microsoft: Microsoft Teams Rooms.",
    "NTT DATA, Lifecycle Management Report, 2024 · VulnCheck, 2025 · Verizon, Data Breach Investigations Report, 2026.",
    "CISA, Binding Operational Directive 26-02, febrero 2026.",
    "Los estudios TEI modelan organizaciones compuestas; los publicamos como referencia de la industria. Estimamos el resultado de cada empresa en el paso Evaluamos.",
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
              <a class="mega-l2" href="soluciones.html"><b>Soluciones de Valor</b><small>{len(MATRIZ)} productos Cisco en {len(ESPECIALIDADES)} áreas de práctica</small></a>
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
      <span>Cisco, Meraki y Duo son marcas de Cisco Systems, Inc. Microsoft, Azure, Teams y Dynamics 365 son marcas de Microsoft Corporation.</span>
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


def sticker_renueva(sufijo=""):
    """Sticker discreto (Inicio, Soluciones de Valor y Ofertas de Productos): lleva al aviso completo en Ofertas de Productos.
    El sufijo evita ids repetidos cuando todas las páginas conviven en la versión de un solo archivo."""
    return f"""<a class="sticker" href="productos.html#renovacion-hardware" aria-label="Programa Renueva: renovación de hardware Cisco con inventario gratuito">
  <svg viewBox="0 0 160 160" aria-hidden="true">
    <defs><path id="st-c{sufijo}" d="M80 80 m-61 0 a61 61 0 1 1 122 0 a61 61 0 1 1 -122 0"/></defs>
    <circle class="st-bg" cx="80" cy="80" r="78"/>
    <circle class="st-in" cx="80" cy="80" r="47"/>
    <g class="st-ring"><text class="st-t"><textPath href="#st-c{sufijo}" textLength="378" lengthAdjust="spacing">RENOVACIÓN DE HARDWARE · PROGRAMA RENUEVA ·</textPath></text></g>
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
  <span class="linea">{E(e['linea'])}</span><h3>{E(e['h2'])}</h3><p>{E(e['intro'])}</p><span class="count">{n} {'producto Cisco' if n == 1 else 'productos Cisco'}</span></a>"""
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
    <p class="lead">Integramos redes, seguridad y salas de reunión Cisco con Microsoft 365, Entra ID, Azure y Teams, en un solo servicio gestionado y con un solo responsable.</p>
    <div class="actions">
      <a class="btn btn-primary" href="index.html#contacto">Hablar con un especialista</a>
      <a class="btn btn-line" href="soluciones.html">Ver soluciones</a>
    </div>
    <div class="figures">
      <div><b>{len(MATRIZ)}</b><span>productos Cisco</span></div>
      <div><b>{len(ESPECIALIDADES)}</b><span>áreas de práctica</span></div>
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
    <p class="statement-text">Construimos cada proyecto sobre su plataforma Microsoft e incorporamos Cisco como acelerador en las capas que la potencian: la red, la seguridad y las salas.</p>
   </div>
   {D(ARTE_CAPAS)}
  </div>
</section>

<section id="especialidades">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">Soluciones de Valor</p>
      <h2>{NUMEROS[len(ESPECIALIDADES)].capitalize()} áreas de práctica</h2>
      <p class="lead">Cada área combina tecnología Cisco con su BASE Microsoft.</p>
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
      <div class="stat"><b>90%</b><p>menos tiempo en actualizaciones y cambios de configuración con Cisco Meraki.</p><cite>Forrester TEI, 2025</cite></div>
      <div class="stat"><b>195%</b><p>de ROI con Cisco Secure Firewall.</p><cite>Forrester TEI, 2022</cite></div>
      <div class="stat"><b>342%</b><p>de ROI con Microsoft Teams Rooms.</p><cite>Forrester TEI</cite></div>
    </div>
    <p class="note" style="margin-top:40px">Citamos estudios por componente, encargados por cada fabricante, como referencia de la industria. Estimamos el resultado para su empresa en el paso Evaluamos.</p>
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

<section id="contacto">
  <div class="wrap contact">
    <div>
      <p class="eyebrow">Contacto</p>
      <h2>Un ecosistema, un solo responsable</h2>
      <p class="lead">Conversemos sobre su red y su plataforma Microsoft. Comenzamos por el paso Evaluamos: inventario, postura actual, brechas, riesgos y objetivos del negocio.</p>
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
</section>

<section class="soft faq" id="preguntas">
  <div class="wrap">
    <div class="section-head"><p class="eyebrow">Preguntas frecuentes</p><h2>Respondemos sus dudas</h2></div>
    {faq}
  </div>
</section>"""
    ld = [{"@type": "WebPage", "name": "Soluciones Cisco + Microsoft", "url": URL_BASE, "inLanguage": "es"},
          {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}]
    pagina("index.html", "index",
           "Soluciones Cisco y Microsoft: redes, ciberseguridad e IA | Consein",
           "Integramos redes, seguridad y salas Cisco con su plataforma Microsoft: SASE y SD-WAN, seguridad como servicio (SECaaS), Cisco ISE, Microsoft Teams Rooms e IA responsable. Venezuela, Panamá, República Dominicana y EE. UU.",
           cuerpo, ld)

# ---------------------------------------------------------------------------
# Soluciones
# ---------------------------------------------------------------------------
def tarjeta_producto(m, area):
    """Tarjeta: producto y mensaje visibles; el resto en la subpantalla "Seguir leyendo…"."""
    filas = []
    if m.get("ideal"):
        filas.append(("Ideal para", E(m["ideal"])))
    if m.get("incluye"):
        filas.append(("Qué incluye", "<ul>" + "".join(f"<li>{E(x)}</li>" for x in m["incluye"]) + "</ul>"))
    if m.get("componentes"):
        filas.append(("Componentes Cisco", E(m["componentes"])))
    filas += [("Se integra con" if m.get("incluye") else "Producto Microsoft asociado", E(m["ms"])),
              ("Cómo agrega valor", E(m["valor"])),
              ("Servicio Consein", "<br>".join(E(o) for o in m["origen"]))]
    dl = "".join(f"<dt>{a}</dt><dd>{b}</dd>" for a, b in filas)
    return f"""<article class="card" id="{m['id']}">
  <h3>{E(m['nombre'])}</h3>
  <p>{E(m['mensaje'])}</p>
  <a class="more" href="#{m['id']}" aria-label="Seguir leyendo: {E(m['nombre'])}">Seguir leyendo…</a>
  <div class="detalle-src" id="detalle-{m['id']}">
    <p class="code">{E(area['nombre'])} · Producto Cisco</p>
    <h2>{E(m['nombre'])}</h2>
    <p class="value">{E(m['mensaje'])}</p>
    <dl>{dl}</dl>
    <a class="btn btn-primary" href="index.html?interes={area['id']}#contacto">Solicitar información</a>
  </div>
</article>"""


def soluciones():
    chips = "".join(f'<a href="#{e["id"]}">{E(e["nombre"])}</a>' for e in ESPECIALIDADES)
    criterios = "".join(f"<div>{D(icono(ic))}<b>{E(t)}</b><p>{E(d)}</p></div>"
                        for (t, d), ic in zip(CRITERIOS, ("integral", "secaas", "objetivo")))
    vista = ""
    for i, e in enumerate(ESPECIALIDADES, 1):
        n = len(productos_area(e["id"]))
        vista += f"""<a class="tile" href="#{e['id']}">{D(icono(e['id']) + f'<span class="idx">0{i}</span>')}
  <span class="linea">{E(e['linea'])}</span><h3>{i}. {E(e['nombre'])}</h3><p>{E(e['intro'])}</p><span class="count">{n} {'producto' if n == 1 else 'productos'}</span></a>"""
    vista += f"""<div class="tile featured">{D(icono('integral'))}
  <h3>Total: {len(MATRIZ)} productos</h3><p>Productos y paquetes Cisco que integramos con su plataforma Microsoft.</p></div>"""
    dif = '<div class="grid g3 proof secaas-dif">' + "".join(
        f"<div>{D(icono(ic))}<b>{E(t)}</b><p>{E(d)}</p></div>" for (t, d), ic in zip(SECAAS_DIF, ("conectividad", "integral", "objetivo"))) + "</div>"
    areas = ""
    for e in ESPECIALIDADES:
        cisco, ms = tecnologias_area(e["id"])
        cards = "".join(tarjeta_producto(m, e) for m in productos_area(e["id"]))
        areas += f"""<section class="area" id="{e['id']}">
  <div class="wrap">
    <div class="area-head">
      <div>{D(icono(e['id']))}<p class="linea">Soluciones Consein · {E(e['linea'])}</p><p class="eyebrow">{E(e['nombre'])}</p><h2>{E(e['h2'])}</h2></div>
      <div><p>{E(e['intro'])}</p><p class="tech"><b>Cisco:</b> {E(cisco)} · <b>Microsoft:</b> {E(ms)}</p></div>
    </div>
    <div class="grid g3">{cards}</div>{dif if e["id"] == "secaas" else ""}
  </div>
</section>"""
    cuerpo = f"""
<section class="page-head">
  <div class="wrap">
    <p class="crumbs"><a href="index.html">Inicio</a> › Soluciones Cisco › Soluciones de Valor</p>
    <p class="eyebrow">Acelerador Cisco: Red · Seguridad · Salas</p>
    <h1>Cisco suma valor a su plataforma Microsoft</h1>
    <p class="lead">Integramos conectividad, seguridad como servicio y colaboración Cisco con su plataforma Microsoft, en {NUMEROS[len(ESPECIALIDADES)]} áreas de práctica.</p>
    <nav class="chips" aria-label="Áreas de práctica">{chips}</nav>
    {sticker_renueva("-sol")}
  </div>
</section>

<section id="criterio">
  <div class="wrap">
    <div class="section-head"><p class="eyebrow">Nuestro criterio</p><h2>Cisco como acelerador de su plataforma Microsoft</h2>
      <p class="lead">Integramos Cisco con Microsoft para cubrir brechas de red y seguridad: posicionamos cada solución donde aporta valor real y evitamos duplicar lo que usted ya paga.</p></div>
    <div class="grid g3 proof">{criterios}</div>
    <p class="note" style="margin-top:32px">Cada producto indica el servicio del Modelo de Servicios Cisco de Consein del que proviene, y cada servicio sigue nuestros siete pasos, de Evaluamos a Aseguramos.</p>
  </div>
</section>

<section class="soft" id="vista">
  <div class="wrap">
    <div class="section-head"><p class="eyebrow">Vista consolidada</p><h2>Valor agregado por área de práctica</h2></div>
    <div class="grid g3">{vista}</div>
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
               "@type": "Service", "name": m["nombre"], "description": m["mensaje"] + " " + m["valor"],
               "serviceType": next(e["nombre"] for e in ESPECIALIDADES if e["id"] == m["area"]),
               "category": next(e["linea"] for e in ESPECIALIDADES if e["id"] == m["area"]),
               "provider": {"@id": URL_BASE + "#consein"}, "url": URL_BASE + "soluciones#" + m["id"],
               "areaServed": [{"@type": "Country", "name": p} for p in PAISES]}} for i, m in enumerate(MATRIZ)]}]
    pagina("soluciones.html", "soluciones",
           "Soluciones Cisco: SASE, SD-WAN, SECaaS, ISE y Teams Rooms | Consein",
           "Seguridad como servicio (SECaaS) con Cisco Duo, Secure Access y Secure Endpoint; SASE y SD-WAN con Meraki y Catalyst; Cisco ISE, Secure Firewall, Room Bar, Board Pro y AI Defense, integrados con su plataforma Microsoft.",
           cuerpo, ld)

# ---------------------------------------------------------------------------
# Productos · Programa Renueva
# ---------------------------------------------------------------------------
def productos():
    cards = "".join(tarjeta(p, "Programa Renueva", renovacion=True) for p in PRODUCTOS)
    rutas = [
        ("Switches de campus legados", "Meraki MS (Switching)", "Red cableada para la colaboración, la voz y el video de Teams; control de acceso a la red con Cisco ISE."),
        ("WiFi de generaciones anteriores", "Meraki MR (Wireless)", "Wi-Fi gestionado en la nube para Microsoft Teams y Microsoft 365."),
        ("Routers de sucursal y MPLS", "Meraki MX + Cisco Secure Access (SASE)", "Prioridad para el tráfico hacia Microsoft 365 y Teams, con seguridad en la nube."),
        ("Sedes sin enlace de respaldo", "Meraki MG (Cellular Gateways)", "Acceso a Microsoft 365 y Azure cuando falla el enlace principal, sujeto a cobertura celular."),
        ("Firewalls legados", "Cisco Secure Firewall", "Gobierno único de reglas con Azure Firewall y registros en Microsoft Sentinel."),
        ("Routers WAN de datacenter y sede central", "Cisco Catalyst SD-WAN", "Conectividad segura hacia Azure, con failover automático y políticas por aplicación."),
        ("Video legado", "Cisco Room Bar / Room Bar Pro y Board Pro Series", "Microsoft Teams Rooms y la pizarra de Teams en hardware certificado."),
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
    {sticker_renueva("-prod")}
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
           "Renovamos switches, WiFi, routers, firewalls y salas Cisco en fin de soporte con Meraki, Cisco SD-WAN, Secure Firewall, Room Bar y Board Pro. Inventario gratuito, migración por fases y financiamiento con bancos locales.",
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
