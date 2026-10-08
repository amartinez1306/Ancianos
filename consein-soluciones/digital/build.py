"""Genera ../consein-soluciones-digital.html (un solo archivo).
Usa los textos de ../minimal/content.json y el diseño de template.html.
Uso: python3 build.py"""
import base64
import json
from pathlib import Path

root = Path(__file__).parent
data = json.loads((root.parent / 'minimal' / 'content.json').read_text(encoding='utf8'))
logo_w = 'data:image/png;base64,' + base64.b64encode((root / 'logo-blanco.png').read_bytes()).decode()
html = (root / 'template.html').read_text(encoding='utf8')
html = html.replace('__LOGO_W__', logo_w)
html = html.replace('__WITSA__', 'data:image/png;base64,' + base64.b64encode((root.parent / 'minimal' / 'witsa-award.png').read_bytes()).decode())
html = html.replace('__DATA__', json.dumps(data, ensure_ascii=False).replace('</', '<\\/'))
out = root.parent / 'consein-soluciones-digital.html'
out.write_text(html, encoding='utf8')
print('OK', out.name, len(html), 'bytes')
