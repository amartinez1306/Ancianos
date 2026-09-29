/* Consein · Fichas de servicio (subpantallas "Ver servicio")
   Una ficha por cada uno de los 7 servicios de valor y NortIA.
   Estructura según el modelo "Consein 360 · Diagnóstico Red + Nube". */
window.CONSEIN_SERVICIOS = [
  {
    id: "csc-01",
    paso: "01 · Evaluamos",
    codigo: "CSC-01 · Infraestructura",
    titulo: "Consein 360 · Diagnóstico Red + Nube",
    formato: "Assessment · gratuito, 8 horas, 100% remoto",
    frase: "Descubra si su red está a la altura de su plataforma Microsoft.",
    ideal: "Empresas que usan Microsoft 365 y Azure y sienten lentitud, cortes o incertidumbre en sus sedes.",
    resuelve: "Inversiones en nube que no rinden porque la red, las sedes o el acceso no acompañan.",
    incluye: [
      "Revisión de la red de campus, sucursales y conexión a Azure y Microsoft 365.",
      "Medición de experiencia de usuario hacia Teams, Dynamics 365 y Copilot.",
      "Mapa de riesgos de seguridad en la capa de red.",
      "Hoja de ruta Cisco + Microsoft sin duplicar herramientas."
    ],
    cisco: "Análisis de red, WiFi, SD-WAN y observabilidad con ThousandEyes.",
    microsoft: "Evaluación de Azure, Microsoft 365 y su licenciamiento actual.",
    resultado: "Un diagnóstico integral y un plan priorizado que protege su inversión Microsoft.",
    prueba: "El tiempo de inactividad cuesta a las empresas Global 2000 cerca de USD 400.000 millones al año, 9% de sus utilidades (Splunk y Oxford Economics, 2024).",
    cta: "Solicite su Diagnóstico Red + Nube",
    pagina: "evaluamos.html"
  },
  {
    id: "csc-02",
    paso: "02 · Diseñamos",
    codigo: "CSC-02 · Arquitectura",
    titulo: "Consein 360 · Arquitectura Híbrida Segura",
    formato: "Taller de diseño · 3 semanas, remoto + 1 sesión presencial",
    frase: "Diseñe una vez y crezca sin tener que rehacer.",
    ideal: "Empresas que planean abrir sedes, llevar cargas a Azure o integrar sistemas, y no quieren comprar piezas que luego no encajen.",
    resuelve: "Soluciones compradas por catálogo que no se integran, se duplican o hay que rehacer al crecer.",
    incluye: [
      "Arquitectura de referencia en Azure (landing zone) alineada al Cloud Adoption Framework.",
      "Diseño de conectividad sede–nube con SD-WAN y acceso seguro.",
      "Modelo de identidad y acceso con Entra ID bajo principios Zero Trust.",
      "Estimación de costos y plan de implementación por etapas."
    ],
    cisco: "Diseño de red de campus, SD-WAN y acceso seguro (SSE) con Cisco Secure Access.",
    microsoft: "Azure Landing Zone, Entra ID e integración con Microsoft 365.",
    resultado: "Una arquitectura documentada, costeada y lista para implementar, que escala con su negocio.",
    prueba: "Gartner proyectó que, hasta 2025, el 99% de las fallas de seguridad en la nube serían responsabilidad del cliente, principalmente por errores de configuración (Gartner, 2019).",
    cta: "Solicite su Taller de Arquitectura"
  },
  {
    id: "csc-03",
    paso: "03 · Actualizamos",
    codigo: "CSC-03 · Modernización",
    titulo: "Consein 360 · Migración sin Pausa",
    formato: "Proyecto · por olas, con ventanas fuera de horario",
    frase: "Modernice su infraestructura sin detener su operación.",
    ideal: "Empresas con servidores, equipos o aplicaciones al final de su soporte, o centros de datos costosos de mantener.",
    resuelve: "Sistemas viejos, caros y riesgosos que nadie se atreve a migrar.",
    incluye: [
      "Inventario y evaluación de cargas con Azure Migrate.",
      "Plan de migración por olas, con pruebas y plan de reversa.",
      "Migración de servidores, bases de datos y escritorios a Azure y Windows 11.",
      "Renovación de la red de sedes para soportar la nube."
    ],
    cisco: "Renovación de switching y WiFi con Cisco Catalyst y Meraki, gestionados desde la nube.",
    microsoft: "Azure Migrate, Azure Virtual Desktop, Windows 11 y Azure Arc.",
    resultado: "Una infraestructura moderna y con soporte, migrada sin interrumpir el negocio.",
    prueba: "Windows 10 llegó al fin de su soporte el 14 de octubre de 2025: sin actualizaciones de seguridad, cada equipo que no migra es un riesgo abierto (Microsoft, 2025).",
    cta: "Solicite su Plan de Migración"
  },
  {
    id: "csc-04",
    paso: "04 · Transformamos",
    codigo: "CSC-04 · Adopción",
    titulo: "Consein 360 · Adopción Productiva",
    formato: "Programa · 90 días, acompañamiento por área",
    etiqueta: "Nuestro diferenciador",
    frase: "Convierta licencias en hábitos, y hábitos en productividad.",
    ideal: "Empresas que pagan Microsoft 365 o Copilot y ven poco uso más allá del correo.",
    resuelve: "Licencias pagadas que nadie usa y herramientas instaladas que no cambian la forma de trabajar.",
    incluye: [
      "Línea base de uso con los informes de Microsoft 365 y Copilot.",
      "Casos de uso por área y red de campeones internos.",
      "Capacitación práctica en Teams, SharePoint y Copilot.",
      "Tablero de adopción y retorno de la inversión."
    ],
    cisco: "Salas de reunión con dispositivos Cisco certificados para Microsoft Teams Rooms.",
    microsoft: "Microsoft 365, Teams, SharePoint, Viva y Microsoft 365 Copilot.",
    resultado: "Adopción medible y licencias que pagan su propio costo.",
    prueba: "Los proyectos con una excelente gestión del cambio tienen 7 veces más probabilidades de cumplir sus objetivos (Prosci, Best Practices in Change Management).",
    cta: "Solicite su Programa de Adopción"
  },
  {
    id: "csc-05",
    paso: "05 · Optimizamos",
    codigo: "CSC-05 · FinOps y rendimiento",
    titulo: "Consein 360 · Optimización Continua",
    formato: "Servicio recurrente · revisión mensual",
    frase: "Pague por lo que usa y obtenga más de lo que paga.",
    ideal: "Empresas cuya factura de Azure crece cada mes sin que el rendimiento mejore.",
    resuelve: "Costos de nube en aumento, recursos sobredimensionados y soluciones que se quedaron estancadas.",
    incluye: [
      "Análisis de consumo con Azure Cost Management y Azure Advisor.",
      "Ajuste de tamaños, reservas y apagado programado de recursos.",
      "Optimización del rendimiento de aplicaciones y red.",
      "Automatización de procesos repetitivos con Power Platform."
    ],
    cisco: "Visibilidad del rendimiento de aplicaciones y red con ThousandEyes y Splunk.",
    microsoft: "Azure Cost Management, Azure Advisor, Power Automate y licenciamiento optimizado.",
    resultado: "Una factura de nube bajo control y una plataforma que mejora mes a mes.",
    prueba: "Las organizaciones estiman que cerca del 27% de su gasto en nube se desperdicia (Flexera, State of the Cloud Report 2024).",
    cta: "Solicite su Revisión de Costos"
  },
  {
    id: "csc-06",
    paso: "06 · Administramos",
    codigo: "CSC-06 · Servicios gestionados",
    titulo: "Consein 360 · Operación Gestionada 24/7",
    formato: "Servicio gestionado · 24/7, con niveles de servicio acordados",
    frase: "Deje de apagar incendios: nosotros vigilamos su plataforma.",
    ideal: "Empresas donde TI depende de una o dos personas y los incidentes se descubren cuando llama el usuario.",
    resuelve: "Soporte reactivo, conocimiento concentrado en pocas personas y caídas que se detectan tarde.",
    incluye: [
      "Monitoreo proactivo de servidores, nube, red y Microsoft 365.",
      "Mesa de servicio especializada con niveles de servicio (SLA).",
      "Gestión de parches, respaldos y cambios.",
      "Informe mensual de salud de la plataforma y recomendaciones."
    ],
    cisco: "Monitoreo de red y experiencia digital con Meraki Dashboard y ThousandEyes.",
    microsoft: "Azure Monitor, Microsoft Intune, Azure Backup y Azure Arc.",
    resultado: "Una operación estable y predecible, que no depende de una sola persona.",
    prueba: "Gartner estimó el costo promedio de la inactividad de TI en USD 5.600 por minuto (Gartner, 2014).",
    cta: "Solicite su Propuesta de Operación 24/7"
  },
  {
    id: "csc-07",
    paso: "07 · Aseguramos",
    codigo: "CSC-07 · Ciberseguridad",
    titulo: "Consein 360 · Escudo Zero Trust",
    formato: "Evaluación + protección continua · monitoreo 24/7",
    frase: "Proteja identidades, datos y red antes de necesitarlo.",
    ideal: "Empresas preocupadas por ransomware, robo de credenciales o fuga de información, o sujetas a regulación.",
    resuelve: "Ataques y fugas que se detectan tarde, y protecciones aisladas que no se hablan entre sí.",
    incluye: [
      "Evaluación de postura Zero Trust con Microsoft Secure Score.",
      "Protección de identidades, equipos y correo con Entra ID, Intune y Defender.",
      "Clasificación y prevención de fuga de datos con Purview.",
      "Detección y respuesta 24/7 con Microsoft Sentinel."
    ],
    cisco: "Seguridad de red y acceso con Cisco Secure Firewall, Duo y Cisco XDR.",
    microsoft: "Microsoft Defender XDR, Entra ID, Intune, Purview y Sentinel.",
    resultado: "Una postura de seguridad medible, que protege cada etapa de su transformación.",
    prueba: "El costo promedio global de una filtración de datos alcanzó USD 4,88 millones (IBM, Cost of a Data Breach Report 2024).",
    cta: "Solicite su Evaluación Zero Trust"
  },
  {
    id: "nortia",
    paso: "NortIA",
    codigo: "CSC-IA · IA y automatización",
    titulo: "NortIA · Agentes de IA para su negocio",
    formato: "Piloto · 6 semanas, de prototipo a producto mínimo viable",
    frase: "Ponga la IA a trabajar sobre sus datos, con seguridad y resultados medibles.",
    ideal: "Empresas que quieren usar IA generativa en atención al cliente, operaciones o análisis, pero no saben por dónde empezar ni cómo proteger sus datos.",
    resuelve: "Iniciativas de IA que se quedan en pruebas aisladas, sin datos confiables, sin gobierno y sin retorno claro.",
    incluye: [
      "Identificación y priorización de casos de uso de IA con retorno medible.",
      "Asistente o agente construido con Copilot Studio y Azure AI Foundry sobre sus datos.",
      "Gobierno y seguridad de datos con Purview y controles de IA responsable.",
      "Ruta de prototipo → MVP → lanzamiento, como en el caso BanIA / Aria."
    ],
    cisco: "Red y seguridad preparadas para cargas de IA, con protección de aplicaciones de IA mediante Cisco AI Defense.",
    microsoft: "Copilot Studio, Azure OpenAI en Azure AI Foundry, Microsoft Fabric y Power Platform.",
    resultado: "Un agente de IA en producción que resuelve un problema real del negocio, con sus datos protegidos.",
    prueba: "El 65% de las organizaciones ya usa IA generativa de forma regular, casi el doble que diez meses antes (McKinsey, The State of AI, 2024).",
    cta: "Solicite su Piloto NortIA"
  }
];
