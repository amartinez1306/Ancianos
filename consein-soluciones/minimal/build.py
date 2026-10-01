"""Genera ../consein-soluciones-minimal.html (un solo archivo: contenido, estilos, lógica y logo).
Uso: python3 build.py
Para editar textos: content.json. Para editar diseño: template.html."""
import base64
import json
from pathlib import Path

root = Path(__file__).parent
data = json.loads((root / 'content.json').read_text(encoding='utf8'))
logo = 'data:image/png;base64,' + base64.b64encode((root / 'logo-consein.png').read_bytes()).decode()
html = (root / 'template.html').read_text(encoding='utf8')
html = html.replace('__LOGO__', logo)
html = html.replace('__DATA__', json.dumps(data, ensure_ascii=False).replace('</', '<\\/'))
out = root.parent / 'consein-soluciones-minimal.html'
out.write_text(html, encoding='utf8')
print('OK', out.name, len(html), 'bytes')
