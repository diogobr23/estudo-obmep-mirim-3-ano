# -*- coding: utf-8 -*-
"""Recorta questões das provas oficiais em PNG para o roteiro.

Uso: python pesquisa/recorta.py 2023-1fase:1 2024-1fase:7 ...
Gera roteiro/img/<prova>-q<N>.png. Acha o topo de cada questão pelo número ("7.") no texto
do PDF e corta até o topo da próxima questão (ou o fim da página).
"""
import re
import sys
from pathlib import Path

import fitz  # PyMuPDF

RAIZ = Path(__file__).resolve().parent.parent
PROVAS, SAIDA = RAIZ / "provas", RAIZ / "roteiro" / "img"
DPI, FOLGA, RODAPE = 150, 8, 815


def topos(pagina):
    """{numero: y} das questões que começam nesta página."""
    achados = {}
    for x0, y0, x1, y1, texto, *_ in pagina.get_text("blocks"):
        m = re.match(r"^(\d{1,2})\s*[.)]", texto.strip())
        if m and 1 <= int(m.group(1)) <= 15 and x0 < 80:
            achados.setdefault(int(m.group(1)), y0)
    return achados


def recorta(prova, numero):
    doc = fitz.open(PROVAS / f"{prova}-prova.pdf")
    for pagina in list(doc)[1:]:  # a página 1 é a capa (tem instruções numeradas "1.", "2.")
        t = topos(pagina)
        if numero not in t:
            continue
        abaixo = sorted(y for y in t.values() if y > t[numero])
        fim = abaixo[0] - FOLGA if abaixo else RODAPE
        clip = fitz.Rect(0, t[numero] - FOLGA, pagina.rect.width, fim)
        destino = SAIDA / f"{prova}-q{numero}.png"
        pagina.get_pixmap(dpi=DPI, clip=clip).save(destino)
        return f"{destino.name}  pág. {pagina.number + 1}  altura {round(fim - t[numero])}pt"
    return f"{prova} q{numero}: NÃO ACHEI"


if __name__ == "__main__":
    SAIDA.mkdir(parents=True, exist_ok=True)
    for arg in sys.argv[1:]:
        prova, n = arg.split(":")
        print(recorta(prova, int(n)))
