# Omakaze Flores

Ornamentos tipográficos («flores de imprenta») del *Monotype: A Journal of
Composing Room Efficiency*, vol. 9, n.º 6 (enero–febrero de 1923),
vectorizados y reunidos en una fuente OpenType, en archivos SVG y en PDF
listos para usar.

Versión de trabajo **0.1**: los ornamentos están limpios y vectorizados,
pero todavía tienen detalles por refinar (ver *Pendientes*).

## Contenido

```
fuente/       OmakazeFlores-Regular.otf — todas las piezas en una fuente
svg/          cada pieza en SVG (vector editable en Inkscape, Illustrator…)
pdf/negro/    cada pieza en PDF, negro
pdf/verde/    cada pieza en PDF, verde (tinta Green de riso aprox.)
pdf/rojo/     capitulares W, O, I en rojo (como en el original)
especimen/    espécimen de la fuente (.tex y .pdf)
herramientas/ script que reconstruye la fuente a partir de los SVG
```

## Mapa de caracteres

| Tecla | Pieza | Página del original |
|---|---|---|
| `a` | remate | 6 |
| `b` | rombo | 5 |
| `c` | cruz | 27 |
| `d` | manita | 27 |
| `e` (también `☙`) | florón izquierdo | 28 |
| `f` (también `❧`) | florón derecho | 28 |
| `g` | cenefa angosta | 6 |
| `h` | cenefa ancha | 7 |
| `i` | marco de título (vacío) | 5 |
| `j` | marco de capitular W (vacío) | 7 |
| `k` | marco de capitular O | 24 |
| `l` | marco de capitular I (vacío) | 28 |
| `m` | marco del retrato (vacío) | 24 |
| `n` | cartela (vacía) | 28 |
| `o` | marco de portada (medallones vacíos) | 1 |
| `p` | marco de contraportada | 32 |
| `q` | retrato de Claude Garamond (va dentro de `m`) | 24 |
| `W` `O` `I` | capitulares (van dentro de `j`, `k`, `l`) | 7, 24, 28 |

Cada pieza mide 1 em de alto: con la fuente a 40 pt, la pieza mide 40 pt de
alto. Las capitulares `W`, `O`, `I` y el retrato `q` están dibujados en las
coordenadas de su marco y tienen el mismo ancho que él, para poder
superponerlos e imprimir marco y letra en tintas distintas.

## Uso en LaTeX (XeLaTeX o LuaLaTeX)

```latex
\usepackage{fontspec,xcolor}
\newfontfamily\flores{OmakazeFlores-Regular.otf}[Path=fuente/]

{\flores\fontsize{30}{30}\selectfont a}                 % un remate
{\flores\fontsize{80}{80}\selectfont
  \leavevmode\rlap{\color{green}j}\color{red}W}         % capitular a dos tintas
```

Para piezas grandes (marcos de portada) también puedes usar los PDF:
`\includegraphics[width=8cm]{pdf/verde/marco-portada.pdf}`.

El archivo `especimen/marco-portada-medallones.json` guarda la posición de
los cuatro medallones del marco de portada, por si quieres poner iniciales.

## Reconstruir la fuente

```
pip install fonttools
python3 herramientas/construir_fuente.py
```

El script lee `svg/` y escribe `fuente/OmakazeFlores-Regular.otf`. Para
cambiar una pieza, edita su SVG y vuelve a correrlo. Los marcos de portada y
contraportada entran a la fuente desde `svg/fuente-simplificada/`: el formato
CFF no admite glifos de más de 64 KB y la versión completa los excede. Los
SVG y PDF completos están en `svg/` y `pdf/`.

## Proceso

1. Escaneos originales (1524 ppi) extraídos del PDF sin recomprimir.
2. Normalización del fondo del papel y separación de tintas (negra y roja).
3. Limpieza: motas, texto vecino y contenidos de los marcos.
4. Vectorización con Potrace.
5. Retoques: medallones vaciados en el marco de portada; esquina inferior
   derecha del marco de la W recreada a partir de la superior izquierda.

## Pendientes (para la versión 1.0)

- Marco de capitular W: queda un fragmento incompleto en la columna derecha.
- Revisar piezas pequeñas que pudieron perderse en los marcos de portada y
  contraportada (se procesaron con un umbral más estricto que el resto).
- Unificar el grosor de los filetes y suavizar bordes irregulares de la
  impresión de 1923.
- Separar las flores repetidas de los marcos como piezas sueltas.
- Kerning y alineación a la línea base para usar las piezas pequeñas en texto.

## Licencia y procedencia

El documento original está en dominio público: su derecho de autor no se
renovó en Estados Unidos (Public Domain Mark 1.0). Reimpresión digital de
CircuitousRoot.com, aportada por David M. MacMillan, disponible en
archive.org: *MonotypeJournalVol09No06JanFeb1923*.

La vectorización, la limpieza y las composiciones de este repositorio se
dedican al dominio público mediante **CC0 1.0 Universal** (ver `LICENSE`).
Puedes usarlas, modificarlas y venderlas sin pedir permiso. Agradecemos el
crédito, pero no es obligatorio.

«Monotype» es una marca registrada de su titular. Este proyecto no tiene
relación con Monotype ni está respaldado por esa empresa; el nombre se usa
solo para identificar la fuente histórica.

Vectorización: Libertad Pantoja · Omakaze Books, 2026.
