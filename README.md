# Omakaze Flores

*[English version](README.en.md)*

Ornamentos tipográficos («flores de imprenta o florituras») del *Monotype: A Journal of
Composing Room Efficiency*, vol. 9, n.º 6 (enero–febrero de 1923),
vectorizados y reunidos en una fuente OpenType, en archivos SVG y en PDF
listos para usar. Están pensados sobre todo para componer libros en LaTeX,
pero sirven en cualquier programa que acepte fuentes o imágenes vectoriales.

Versión de trabajo **0.2**: los ornamentos están limpios y vectorizados,
pero todavía tienen detalles por refinar (ver *Pendientes*).

**Mira cómo se usaban originalmente.** El número completo de 1923 está
digitalizado en archive.org; ahí se ven los marcos, cenefas y capitulares
compuestos en sus páginas, a dos tintas:
<https://archive.org/details/MonotypeJournalVol09No06JanFeb1923/page/n3/mode/2up>.
La columna «Página del original» del mapa de caracteres indica en qué
página del *Journal* aparece cada pieza.

## Contenido

```
fuente/       OmakazeFlores-Regular.otf — todas las piezas en una fuente
svg/          cada pieza en SVG (vector editable en Inkscape, Illustrator…)
pdf/negro/    cada pieza en PDF, negro
pdf/verde/    cada pieza en PDF, verde (tinta Green de riso aprox.)
pdf/rojo/     capitulares W, O, I en rojo (como en el original)
latex/        paquete omakazeflores.sty y un ejemplo (.tex y .pdf)
especimen/    espécimen de la fuente (.tex y .pdf)
herramientas/ script que reconstruye la fuente a partir de los SVG
```

Abre `especimen/especimen.pdf` para ver todas las piezas de un vistazo.

## Mapa de caracteres

| Tecla | Pieza | Página del original |
|---|---|---|
| `a` | remate | 6 |
| `b` | rombo | 5 |
| `c` | cruz | 27 |
| `d` | pequeño ornamento de hoja | 27 |
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

¿Fuente o PDF? Usa la **fuente** para piezas pequeñas y medianas que van
dentro del texto (remates, florones, cenefas, capitulares). Usa los **PDF**
para los marcos de portada y contraportada: la fuente lleva una versión
simplificada de esos dos marcos (ver *Reconstruir la fuente*), y los PDF
conservan todo el detalle.

## Descarga

Si no usas git, descarga el `.zip` de la última versión en
[*Releases*](https://github.com/LiberPH/omakaze-flores/releases): trae la
fuente, el paquete de LaTeX, los SVG, los PDF y el espécimen.

## Uso en LaTeX

Necesitas **XeLaTeX** o **LuaLaTeX** (pdfLaTeX no carga fuentes OpenType).
En Overleaf: *Menu → Compiler → XeLaTeX*.

### Con el paquete `omakazeflores` (recomendado)

1. Copia junto a tu `.tex` estos dos archivos:
   `latex/omakazeflores.sty` y `fuente/OmakazeFlores-Regular.otf`.
   (En Overleaf, súbelos con *Upload*.)
2. En el preámbulo:
   ```latex
   \usepackage{omakazeflores}
   ```
3. Compila con `xelatex` o `lualatex`.

Si prefieres dejar la fuente en otra carpeta, indícala con `ruta`
(con `/` al final): `\usepackage[ruta=fuente/]{omakazeflores}`. Si
instalaste la fuente en tu árbol de TeX (`~/Library/texmf/fonts/opentype/`
en macOS, `~/texmf/fonts/opentype/` en Linux), no hace falta.

Órdenes del paquete:

| Orden | Qué hace |
|---|---|
| `\flor[tamaño]{teclas}` | piezas de la fuente; el tamaño fija su alto (24pt por omisión). Ej.: `\flor[30pt]{a}` |
| `\separador[tamaño]` | un remate centrado entre párrafos (30pt) |
| `\florones[tamaño]{texto}` | texto entre los florones ☙ ❧ (14pt) |
| `\cenefa[ancha]` o `\cenefa[angosta]` | cenefa al ancho de la línea |
| `\capitular[tamaño]{W}` | capitular W, O o I dentro de su marco, a dos tintas (80pt) |
| `\retrato[tamaño]` | retrato de Garamond en su marco (110pt) |
| `\flores` | cambia a la fuente de ornamentos: `{\flores ☙}` |

Opciones de `\usepackage[…]{omakazeflores}`:

| Opción | Valores | Por omisión |
|---|---|---|
| `ruta` | carpeta de la fuente, con `/` final | junto al `.tex` |
| `marco` | color del marco (cualquier color de `xcolor`) | verde (`omfverde`) |
| `letra` | color de la letra capitular | rojo (`omfrojo`) |
| `plancha` | `ambas`, `marco` o `letra` | `ambas` |

Por ejemplo, `\usepackage[marco=black, letra=omfrojo]{omakazeflores}`.
Los colores se llaman `tintamarco` y `tintaletra` y también puedes
cambiarlos dentro del documento con `\colorlet{tintamarco}{blue}`.

`latex/ejemplo.tex` es un documento completo que usa todas las órdenes
(`cd latex && xelatex ejemplo.tex`); el resultado está en
`latex/ejemplo.pdf`.

#### Imprimir a dos tintas (riso, offset)

Compila el documento dos veces, cambiando la opción `plancha`:

```latex
\usepackage[plancha=marco]{omakazeflores}  % plancha 1: solo los marcos, en negro
\usepackage[plancha=letra]{omakazeflores}  % plancha 2: solo las letras, en negro
```

Cada PDF es una plancha y las dos coinciden al milímetro: la pieza que no
toca se deja como espacio en blanco. La opción solo afecta a `\capitular` y
`\retrato`. Por ahora el texto y los demás ornamentos salen en las dos planchas;
para separarlos del todo, haz una versión del documento para cada plancha.

### Sin el paquete

Si prefieres no usar el `.sty`, basta con `fontspec`:

```latex
\usepackage{fontspec,xcolor}
\newfontfamily\flores{OmakazeFlores-Regular.otf}[Path=fuente/]

{\flores\fontsize{30}{30}\selectfont a}                        % un remate
{\flores\fontsize{80}{80}\selectfont
  \leavevmode\rlap{\color{green}j}\color{red}W}                % capitular a dos tintas
```

`especimen/especimen.tex` está hecho así (`cd especimen && xelatex
especimen.tex`; usa EB Garamond como fuente de texto, que viene con
TeX Live).

### Más recetas

Una portada con el marco completo en PDF, centrado en la página (necesita
`\usepackage{tikz}`):

```latex
\thispagestyle{empty}
\begin{tikzpicture}[remember picture,overlay]
  \node at (current page.center)
    {\includegraphics[height=.85\paperheight]{pdf/verde/marco-portada.pdf}};
  \node[font=\Huge\itshape] at (current page.center) {Título del libro};
\end{tikzpicture}
\null\newpage
```

Iniciales en los medallones del marco de portada. El archivo
`especimen/marco-portada-medallones.json` da el centro de cada medallón
(`cx`, `cy`) y su alto (`h`) como fracciones del ancho y alto del marco,
medidas desde la esquina inferior izquierda. Con TikZ basta colocar la
imagen en el origen y usar esas fracciones como coordenadas:

```latex
\begin{tikzpicture}
  \node[anchor=south west,inner sep=0] (marco)
    {\includegraphics[width=12cm]{pdf/negro/marco-portada.pdf}};
  \begin{scope}[x={(marco.south east)},y={(marco.north west)}]
    \node[font=\Large] at (0.5130,0.8315) {O};   % arriba
    \node[font=\Large] at (0.1768,0.4909) {M};   % izquierda
    \node[font=\Large] at (0.8479,0.4913) {K};   % derecha
    \node[font=\Large] at (0.5108,0.1527) {B};   % abajo
  \end{scope}
\end{tikzpicture}
```

Una capitular de verdad, con el texto alrededor: mide la capitular y
pon el párrafo a su lado (así está hecho `latex/ejemplo.tex`):

```latex
\sbox0{\capitular[56pt]{O}}%
\noindent\usebox0\hspace{4pt}%
\parbox[b]{\dimexpr\linewidth-\wd0-4pt}{nce upon a time…}
```

Los PDF de `pdf/negro/`, `pdf/verde/` y `pdf/rojo/` tienen el mismo
encuadre en las tres carpetas, así que también sirven como planchas.

## Uso en otros programas

- **Instalar la fuente:** abre `fuente/OmakazeFlores-Regular.otf` y pulsa
  *Instalar* (macOS: Catálogo Tipográfico; Windows: clic derecho →
  *Instalar*; Linux: cópiala a `~/.local/share/fonts/`).
- **Word, LibreOffice, Pages, InDesign, Affinity:** elige la fuente
  *Omakaze Flores* y escribe la tecla de la pieza. Para dos tintas, pon
  marco y letra en cuadros de texto superpuestos en la misma posición.
- **Inkscape, Illustrator:** abre o importa el SVG o el PDF; los trazos se
  pueden recolorear y editar.
- **Typst:**
  `#text(font: "Omakaze Flores", size: 30pt)[a]` (con la fuente instalada o
  la carpeta indicada con `--font-path fuente/`).
- **Web (CSS):**
  ```css
  @font-face { font-family: "Omakaze Flores";
               src: url("OmakazeFlores-Regular.otf") format("opentype"); }
  .flor { font-family: "Omakaze Flores"; font-size: 3rem; }
  ```

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

### Empaquetar una versión

```
sh herramientas/empaquetar.sh 0.2
```

Crea `dist/omakaze-flores-0.2.zip` con lo que está en el último commit,
listo para subirlo a *Releases* en GitHub.

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
Puedes usarlas, modificarlas y venderlas sin pedir permiso, también en
libros comerciales y sin restricciones de incrustación de la fuente en PDF.
Agradecemos el crédito, pero no es obligatorio.

«Monotype» es una marca registrada de su titular. Este proyecto no tiene
relación con Monotype ni está respaldado por esa empresa; el nombre se usa
solo para identificar la fuente histórica.

Vectorización: Libertad Pantoja · Omakaze Books, 2026.
