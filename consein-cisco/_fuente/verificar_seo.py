"""Verifica que cada palabra clave de palabras_clave.json aparezca en la página asignada.

Uso:  python3 _fuente/verificar_seo.py
Revisa texto visible, title, meta description y encabezados H1/H2 del sitio de tres páginas.
"""
import html
import json
import re
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent


def normal(t):
    t = unicodedata.normalize("NFD", html.unescape(t).lower())
    return re.sub(r"\s+", " ", "".join(c for c in t if unicodedata.category(c) != "Mn"))


def leer(archivo):
    doc = (RAIZ / archivo).read_text(encoding="utf-8")
    meta = " ".join(re.findall(r"<title>(.*?)</title>", doc) + re.findall(r'name="description" content="([^"]*)"', doc))
    enc = " ".join(re.sub(r"<[^>]+>", " ", h) for h in re.findall(r"<h[12][^>]*>(.*?)</h[12]>", doc, re.S))
    cuerpo = re.sub(r"<script.*?</script>|<style.*?</style>", " ", doc.split("<body>", 1)[1], flags=re.S)
    return {"meta": normal(meta), "h": normal(enc), "texto": normal(re.sub(r"<[^>]+>", " ", cuerpo))}


def main():
    datos = json.loads((RAIZ / "_fuente" / "palabras_clave.json").read_text(encoding="utf-8"))
    paginas = {a: leer(a) for a in ("index.html", "soluciones.html", "productos.html")}
    faltan = 0
    for g in datos["grupos"]:
        archivo = g["pagina"].split("#")[0]
        print(f"\n{g['titulo']}  ({archivo})")
        for kw in g["kw"]:
            frase, prioridad = kw[0], kw[3]
            if len(kw) > 5 and kw[5] is False:
                print(f"  ·  {prioridad}  {frase:45s} pendiente (no se publica aún)")
                continue
            p = paginas[archivo]
            n = normal(frase)
            donde = [k for k in ("meta", "h", "texto") if n in p[k]]
            if not donde and all(t in p["meta"] for t in n.split() if len(t) > 2):
                donde = ["términos en title/description"]
            if not donde:
                faltan += 1
            marca = "OK" if donde else "FALTA"
            print(f"  {marca:5s} {prioridad}  {frase:45s} {', '.join(donde)}")
    print(f"\nPalabras clave sin presencia en su página: {faltan}")
    return faltan


if __name__ == "__main__":
    raise SystemExit(1 if main() else 0)
