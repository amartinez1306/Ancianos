"""Genera las versiones de un solo archivo (CSS, JS, logo y, si existe en
assets/fonts/, la fuente Haltto incrustados):
  index.html          -> consein-hardware-standalone.html
  index-grafico.html  -> consein-hardware-grafico-standalone.html

Uso: python3 build.py
"""
import base64
import pathlib
import re

ROOT = pathlib.Path(__file__).parent
MIME = {'.woff2': 'font/woff2', '.woff': 'font/woff', '.otf': 'font/otf', '.ttf': 'font/ttf'}


def data_uri(path, mime):
    return f'data:{mime};base64,' + base64.b64encode(path.read_bytes()).decode()


PAGES = {
    'index.html': 'consein-hardware-standalone.html',
    'index-grafico.html': 'consein-hardware-grafico-standalone.html',
}


def font_src(match):
    path = ROOT / 'assets/fonts' / match.group(1)
    if path.exists():
        return f'url("{data_uri(path, MIME[path.suffix])}")'
    return ''


def inline_css(name):
    css = (ROOT / 'assets/css' / name).read_text(encoding='utf-8')
    # Incrusta los archivos de fuente presentes y descarta los que no existen
    css = re.sub(r'url\("\.\./fonts/([^"]+)"\) format\("[^"]+"\)', font_src, css)
    css = re.sub(r',\s*(?=,|;)', '', css)
    return css


js = (ROOT / 'assets/js/main.js').read_text(encoding='utf-8')
logo = data_uri(ROOT / 'assets/img/logo-consein.jpg', 'image/jpeg')

for source, target in PAGES.items():
    html = (ROOT / source).read_text(encoding='utf-8')
    html = re.sub(r'<link rel="stylesheet" href="assets/css/([\w-]+\.css)">',
                  lambda m: '<style>\n' + inline_css(m.group(1)) + '</style>', html)
    html = html.replace('<script src="assets/js/main.js" defer></script>', '<script>\n' + js + '</script>')
    html = html.replace('src="assets/img/logo-consein.jpg"', 'src="' + logo + '"')
    (ROOT / target).write_text(html, encoding='utf-8')
    print(f'{target}: {len(html) // 1024} KB')
