"""Genera consein-soluciones.html: una versión de un solo archivo (CSS, JS, datos y logos incluidos).
Uso: python3 build_single.py"""
import base64
from pathlib import Path

root = Path(__file__).parent
read = lambda p: (root / p).read_text(encoding='utf8')
b64 = lambda p: 'data:image/png;base64,' + base64.b64encode((root / p).read_bytes()).decode()

html = read('index.html')
html = html.replace('<link rel="stylesheet" href="assets/css/styles.css">', '<style>\n' + read('assets/css/styles.css') + '\n</style>')
html = html.replace('<script src="assets/js/data.js"></script>', '<script>\n' + read('assets/js/data.js').replace('</', '<\\/') + '\n</script>')
html = html.replace('<script src="assets/js/app.js"></script>', '<script>\n' + read('assets/js/app.js') + '\n</script>')
html = html.replace('assets/img/logo-consein-blanco.png', b64('assets/img/logo-consein-blanco.png'))
html = html.replace('assets/img/logo-consein.png', b64('assets/img/logo-consein.png'))
assert 'assets/' not in html
(root / 'consein-soluciones.html').write_text(html, encoding='utf8')
print('OK consein-soluciones.html', len(html), 'bytes')
