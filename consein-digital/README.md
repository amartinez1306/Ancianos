# Consein · Página de Servicios — Versión digital

Variante con diseño gráfico moderno y tecnológico de la página de Servicios. Mismo contenido,
textos SEO y estructura que la versión minimalista (`../consein/`).

**Paleta:** Azul oscuro `#1b245b` (principal) · Verde `#58bb47` (principal).
**Tipografías:** títulos en Haltto (archivos con licencia en `assets/fonts/`), textos en Poppins.

## Recursos gráficos por sección

| Sección | Recurso |
|---|---|
| Portada | Fondo azul con retícula y halo verde; órbita animada de las 7 etapas (cada número abre su ficha); barra de datos. |
| Propuesta de valor | Ciclo Escuchamos → Aprendemos → Ejecutamos → Acompañamos y tarjetas con íconos. |
| Servicio en 7 etapas | Sección oscura con retícula; una fila por fase y tarjetas translúcidas con ícono y número. |
| Oficina de Proyectos | Línea de pasos y panel de control (alcance, tiempo, costo y valor). |
| Preguntas frecuentes | Acordeón sobre fondo de puntos. |
| Contacto | Banda azul con formulario destacado. |
| Fichas «Ver servicio» | Cabecera azul con código de etapa y fila de resultado resaltada en verde. |

Las animaciones se desactivan si el usuario lo pide en su sistema (`prefers-reduced-motion`).

## Estructura

```
consein-digital/
├── index.html            Página completa (fichas y datos estructurados incluidos)
└── assets/
    ├── digital.css
    ├── digital.js
    ├── logo-consein.png / logo-consein-blanco.png
    └── fonts/            Haltto (ver LEEME.txt)
```

El formulario, las fichas y el SEO funcionan igual que en la versión minimalista (ver `../consein/README.md`).
