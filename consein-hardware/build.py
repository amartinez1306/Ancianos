"""Genera consein-hardware-standalone.html: un solo archivo con CSS, JS, logo
y (si existe en assets/fonts/) la fuente Haltto incrustados.

Uso: python3 build.py
"""
import base64
import pathlib
import re

ROOT = pathlib.Path(__file__).parent
MIME = {'.woff2': 'font/woff2', '.woff': 'font/woff', '.otf': 'font/otf', '.ttf': 'font/ttf'}


def data_uri(path, mime):
    return f'data:{mime};base64,' + base64.b64encode(path.read_bytes()).decode()


html = (ROOT / 'index.html').read_text(encoding='utf-8')
css = (ROOT / 'assets/css/styles.css').read_text(encoding='utf-8')
js = (ROOT / 'assets/js/main.js').read_text(encoding='utf-8')


def font_src(match):
    path = ROOT / 'assets/fonts' / match.group(1)
    if path.exists():
        return f'url("{data_uri(path, MIME[path.suffix])}")'
    return ''


# Incrusta los archivos de fuente presentes y descarta los que no existen
css = re.sub(r'url\("\.\./fonts/([^"]+)"\) format\("[^"]+"\)', font_src, css)
css = re.sub(r',\s*(?=,|;)', '', css)
css = re.sub(r',(\s*\n\s*)+;', ';', css)

html = html.replace('<link rel="stylesheet" href="assets/css/styles.css">', '<style>\n' + css + '</style>')
html = html.replace('<script src="assets/js/main.js" defer></script>', '<script>\n' + js + '</script>')
html = html.replace('src="assets/img/logo-consein.jpg"', 'src="' + data_uri(ROOT / 'assets/img/logo-consein.jpg', 'image/jpeg') + '"')

out = ROOT / 'consein-hardware-standalone.html'
out.write_text(html, encoding='utf-8')
print(f'{out.name}: {len(html) // 1024} KB')
