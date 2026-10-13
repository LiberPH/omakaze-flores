#!/usr/bin/env python3
"""
Construye la fuente OmakazeFlores a partir de los SVG de svg/.

Uso:   python3 herramientas/construir_fuente.py
Requiere: fontTools  (pip install fonttools)

Cada pieza se escala para que su alto sea 1000 unidades (1 em) y se
apoya 150 unidades por debajo de la línea base. Las capitulares W, O, I
y el retrato se colocan en las coordenadas de su marco, para poder
superponerlas exactamente (marco en una tinta, letra en otra).
"""
import re, os, json
from fontTools.fontBuilder import FontBuilder
from fontTools.pens.t2CharStringPen import T2CharStringPen
from fontTools.pens.transformPen import TransformPen
from fontTools.svgLib.path import parse_path

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SVG = os.path.join(RAIZ, "svg")
FAMILIA = "Omakaze Flores"
ARCHIVO = "OmakazeFlores-Regular.otf"
VERSION = "0.2"
UPM, ALTO, BAJADA = 1000, 1000, 150

# pieza -> (carácter, otros caracteres que también la muestran)
PIEZAS = {
    "remate":              ("a", []),
    "rombo":               ("b", []),
    "cruz":                ("c", []),
    "hoja-pequena":        ("d", []),
    "floron-izq":          ("e", [0x2619]),   # ☙
    "floron-der":          ("f", [0x2767]),   # ❧
    "cenefa-angosta":      ("g", []),
    "cenefa-ancha":        ("h", []),
    "marco-titulo":        ("i", []),
    "marco-capitular-W":   ("j", []),
    "marco-capitular-O":   ("k", []),
    "marco-capitular-I":   ("l", []),
    "marco-retrato":       ("m", []),
    "cartela":             ("n", []),
    "marco-portada":       ("o", []),
    "marco-contraportada": ("p", []),
}
# piezas que van dentro de un marco: (marco, x, y, ancho) en fracciones del marco
INTERIORES = {
    "capitular-W":      ("W", "marco-capitular-W", 0.1811, 0.1961, 0.6289),
    "capitular-O":      ("O", "marco-capitular-O", 0.1744, 0.1822, 0.6444),
    "capitular-I":      ("I", "marco-capitular-I", 0.2809, 0.2239, 0.4275),
    "retrato-garamond": ("q", "marco-retrato",     0.2067, 0.1876, 0.5866),
}

def leer(nombre):
    # Las piezas muy grandes usan una versión simplificada (svg/fuente-simplificada/):
    # el formato CFF no admite glifos de más de 64 KB.
    simple = os.path.join(SVG, "fuente-simplificada", nombre + ".svg")
    ruta = simple if os.path.exists(simple) else os.path.join(SVG, nombre + ".svg")
    s = open(ruta).read()
    w = float(re.search(r'viewBox="0 0 ([0-9.]+) ([0-9.]+)"', s).group(1))
    h = float(re.search(r'viewBox="0 0 ([0-9.]+) ([0-9.]+)"', s).group(2))
    trazos = [d.replace("\n", " ") for d in re.findall(r'<path d="([^"]+)"', s, re.S)]
    return w, h, trazos

def dibujar(trazos, pen, escala, dx, dy):
    # potrace usa unidades de 0.1 px con el eje y hacia arriba
    tp = TransformPen(pen, (0.1 * escala, 0, 0, 0.1 * escala, dx, dy))
    for d in trazos:
        parse_path(d, tp)

glifos, avances, cmap = {}, {}, {}
for nombre in ["space", ".notdef"]:
    p = T2CharStringPen(300 if nombre == "space" else 500, None)
    glifos[nombre] = p.getCharString(); avances[nombre] = 300 if nombre == "space" else 500
cmap[0x20] = "space"

marcos = {}
for nombre, (car, extra) in PIEZAS.items():
    w, h, trazos = leer(nombre)
    esc = ALTO / h
    avance = round(w * esc)
    pen = T2CharStringPen(avance, None)
    dibujar(trazos, pen, esc, 0, -BAJADA)
    g = nombre.replace("-", "_")
    glifos[g] = pen.getCharString(); avances[g] = avance
    cmap[ord(car)] = g
    for u in extra: cmap[u] = g
    marcos[nombre] = (w, h, esc)

for nombre, (car, marco, fx, fy, fw) in INTERIORES.items():
    w, h, trazos = leer(nombre)
    mw, mh, mesc = marcos[marco]
    esc = fw * mw * mesc / w                 # ancho relativo al marco
    dx = fx * mw * mesc
    dy = fy * mh * mesc - BAJADA
    avance = round(mw * mesc)                # mismo avance que su marco
    pen = T2CharStringPen(avance, None)
    dibujar(trazos, pen, esc, dx, dy)
    g = nombre.replace("-", "_")
    glifos[g] = pen.getCharString(); avances[g] = avance
    cmap[ord(car)] = g

orden = [".notdef", "space"] + [g for g in glifos if g not in (".notdef", "space")]
fb = FontBuilder(UPM, isTTF=False)
fb.setupGlyphOrder(orden)
fb.setupCharacterMap(cmap)
ps = FAMILIA.replace(" ", "") + "-Regular"
fb.setupCFF(ps, {"FullName": FAMILIA + " Regular"}, glifos, {})
fb.setupHorizontalMetrics({g: (avances[g], 0) for g in orden})
fb.setupHorizontalHeader(ascent=ALTO - BAJADA, descent=-BAJADA)
fb.setupNameTable({
    "familyName": FAMILIA, "styleName": "Regular",
    "uniqueFontIdentifier": f"{ps};{VERSION}",
    "fullName": FAMILIA + " Regular", "psName": ps,
    "version": f"Version {VERSION}",
    "copyright": "Ornamentos del Monotype Journal vol. 9 n.º 6 (1923), dominio público. "
                 "Vectorización y composición: Libertad Pantoja, dedicadas al dominio público (CC0 1.0).",
    "licenseDescription": "CC0 1.0 Universal — https://creativecommons.org/publicdomain/zero/1.0/",
    "licenseInfoURL": "https://creativecommons.org/publicdomain/zero/1.0/",
})
fb.setupOS2(sTypoAscender=ALTO - BAJADA, sTypoDescender=-BAJADA, sTypoLineGap=0,
            usWinAscent=ALTO, usWinDescent=BAJADA + 50, achVendID="LPH ",
            fsType=0)  # instalable: sin restricciones de incrustación (CC0)
fb.setupPost()
os.makedirs(os.path.join(RAIZ, "fuente"), exist_ok=True)
salida = os.path.join(RAIZ, "fuente", ARCHIVO)
fb.font.save(salida)
print("Fuente generada:", salida, "—", len(orden) - 2, "piezas")
