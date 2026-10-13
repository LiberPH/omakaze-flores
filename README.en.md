# Omakaze Flores

*[Versión en español](README.md)*

Printer's ornaments (*fleurons*, Spanish *flores de imprenta o florituras*) from
*Monotype: A Journal of Composing Room Efficiency*, vol. 9, no. 6
(January–February 1923), vectorized and collected as an OpenType font and as
ready-to-use SVG and PDF files. They are meant above all for typesetting
books in LaTeX, but they work in any program that takes fonts or vector
images.

Working version **0.2**: the ornaments are clean and vectorized but still
have details to refine (see *To do*).

**See how they were originally used.** The full 1923 issue is digitized on
archive.org, where you can see the frames, borders and initials set on their
pages in two colors:
<https://archive.org/details/MonotypeJournalVol09No06JanFeb1923/page/n3/mode/2up>.
The "Original page" column in the character map tells you on which page of
the *Journal* each piece appears.

File and piece names are in Spanish; the tables below translate them.

## Contents

```
fuente/       OmakazeFlores-Regular.otf — every piece in one font
svg/          each piece as SVG (editable in Inkscape, Illustrator…)
pdf/negro/    each piece as PDF, black
pdf/verde/    each piece as PDF, green (approx. Riso Green ink)
pdf/rojo/     initials W, O, I in red (as in the original)
latex/        omakazeflores.sty package and an example (.tex and .pdf)
especimen/    font specimen (.tex and .pdf)
herramientas/ script that rebuilds the font from the SVGs
```

Open `especimen/especimen.pdf` to see every piece at a glance.

## Character map

| Key | Piece | File name | Original page |
|---|---|---|---|
| `a` | finial / tailpiece | `remate` | 6 |
| `b` | lozenge | `rombo` | 5 |
| `c` | cross | `cruz` | 27 |
| `d` | small leaf ornament | `hoja-pequena` | 27 |
| `e` (also `☙`) | left fleuron | `floron-izq` | 28 |
| `f` (also `❧`) | right fleuron | `floron-der` | 28 |
| `g` | narrow border | `cenefa-angosta` | 6 |
| `h` | wide border | `cenefa-ancha` | 7 |
| `i` | title frame (empty) | `marco-titulo` | 5 |
| `j` | initial frame for W (empty) | `marco-capitular-W` | 7 |
| `k` | initial frame for O | `marco-capitular-O` | 24 |
| `l` | initial frame for I (empty) | `marco-capitular-I` | 28 |
| `m` | portrait frame (empty) | `marco-retrato` | 24 |
| `n` | cartouche (empty) | `cartela` | 28 |
| `o` | title-page frame (empty medallions) | `marco-portada` | 1 |
| `p` | back-cover frame | `marco-contraportada` | 32 |
| `q` | portrait of Claude Garamond (goes inside `m`) | `retrato-garamond` | 24 |
| `W` `O` `I` | initials (go inside `j`, `k`, `l`) | `capitular-W/O/I` | 7, 24, 28 |

Every piece is 1 em tall: with the font at 40 pt, the piece is 40 pt tall.
The initials `W`, `O`, `I` and the portrait `q` are drawn in the coordinates
of their frame and have the same advance width, so you can overprint them
and print frame and letter in different inks.

Font or PDF? Use the **font** for small and medium pieces that live in the
text (tailpieces, fleurons, borders, initials). Use the **PDFs** for the
title-page and back-cover frames: the font carries a simplified version of
those two frames (see *Rebuilding the font*), while the PDFs keep all the
detail.

## Download

If you don't use git, download the `.zip` of the latest version from
[*Releases*](https://github.com/LiberPH/omakaze-flores/releases): it has the
font, the LaTeX package, the SVGs, the PDFs and the specimen.

## Using it in LaTeX

You need **XeLaTeX** or **LuaLaTeX** (pdfLaTeX cannot load OpenType fonts).
On Overleaf: *Menu → Compiler → XeLaTeX*.

### With the `omakazeflores` package (recommended)

1. Copy these two files next to your `.tex`:
   `latex/omakazeflores.sty` and `fuente/OmakazeFlores-Regular.otf`.
   (On Overleaf, add them with *Upload*.)
2. In the preamble:
   ```latex
   \usepackage{omakazeflores}
   ```
3. Compile with `xelatex` or `lualatex`.

To keep the font in another folder, give it with `ruta` ("path", with a
trailing `/`): `\usepackage[ruta=fuente/]{omakazeflores}`. If the font is
in your TeX tree (`~/Library/texmf/fonts/opentype/` on macOS,
`~/texmf/fonts/opentype/` on Linux), you don't need it.

Package commands (names are Spanish):

| Command | What it does |
|---|---|
| `\flor[size]{keys}` | font pieces; the size sets their height (24pt by default). E.g. `\flor[30pt]{a}` |
| `\separador[size]` | a centered tailpiece between paragraphs (30pt) |
| `\florones[size]{text}` | text between the ☙ ❧ fleurons (14pt) |
| `\cenefa[ancha]` or `\cenefa[angosta]` | wide or narrow border across the line |
| `\capitular[size]{W}` | initial W, O or I inside its frame, in two colors (80pt) |
| `\retrato[size]` | Garamond's portrait in its frame (110pt) |
| `\flores` | switches to the ornament font: `{\flores ☙}` |

Options for `\usepackage[…]{omakazeflores}`:

| Option | Values | Default |
|---|---|---|
| `ruta` | font folder, with trailing `/` | next to the `.tex` |
| `marco` | frame color (any `xcolor` color) | green (`omfverde`) |
| `letra` | initial letter color | red (`omfrojo`) |
| `plancha` | `ambas` (both), `marco` (frame) or `letra` (letter) | `ambas` |

For example, `\usepackage[marco=black, letra=omfrojo]{omakazeflores}`.
The colors are named `tintamarco` and `tintaletra`, and you can also change
them inside the document with `\colorlet{tintamarco}{blue}`.

`latex/ejemplo.tex` is a complete document using every command
(`cd latex && xelatex ejemplo.tex`); the output is `latex/ejemplo.pdf`.

#### Two-color printing (Riso, offset)

Compile the document twice, changing the `plancha` ("plate") option:

```latex
\usepackage[plancha=marco]{omakazeflores}  % plate 1: frames only, in black
\usepackage[plancha=letra]{omakazeflores}  % plate 2: letters only, in black
```

Each PDF is one plate and they register exactly: the piece that doesn't
belong on a plate is left as blank space. The option only affects
`\capitular` and `\retrato`. For now, body text and other ornaments appear on
both plates; to separate them completely, make one version of the document
per plate.

### Without the package

If you'd rather not use the `.sty`, `fontspec` is enough:

```latex
\usepackage{fontspec,xcolor}
\newfontfamily\flores{OmakazeFlores-Regular.otf}[Path=fuente/]

{\flores\fontsize{30}{30}\selectfont a}                        % a tailpiece
{\flores\fontsize{80}{80}\selectfont
  \leavevmode\rlap{\color{green}j}\color{red}W}                % two-color initial
```

`especimen/especimen.tex` is built this way (`cd especimen && xelatex
especimen.tex`; it uses EB Garamond for the text, which ships with TeX
Live).

### More recipes

A title page with the full PDF frame centered on the page (needs
`\usepackage{tikz}`):

```latex
\thispagestyle{empty}
\begin{tikzpicture}[remember picture,overlay]
  \node at (current page.center)
    {\includegraphics[height=.85\paperheight]{pdf/verde/marco-portada.pdf}};
  \node[font=\Huge\itshape] at (current page.center) {Book Title};
\end{tikzpicture}
\null\newpage
```

Initials in the title-page frame's medallions. The file
`especimen/marco-portada-medallones.json` gives each medallion's center
(`cx`, `cy`) and height (`h`) as fractions of the frame's width and height,
measured from the bottom-left corner (`arriba` = top, `izquierda` = left,
`derecha` = right, `abajo` = bottom). In TikZ, place the image at the origin
and use those fractions as coordinates:

```latex
\begin{tikzpicture}
  \node[anchor=south west,inner sep=0] (marco)
    {\includegraphics[width=12cm]{pdf/negro/marco-portada.pdf}};
  \begin{scope}[x={(marco.south east)},y={(marco.north west)}]
    \node[font=\Large] at (0.5130,0.8315) {O};   % top
    \node[font=\Large] at (0.1768,0.4909) {M};   % left
    \node[font=\Large] at (0.8479,0.4913) {K};   % right
    \node[font=\Large] at (0.5108,0.1527) {B};   % bottom
  \end{scope}
\end{tikzpicture}
```

A real drop cap with the text beside it: measure the initial and set the
paragraph next to it (this is how `latex/ejemplo.tex` does it):

```latex
\sbox0{\capitular[56pt]{O}}%
\noindent\usebox0\hspace{4pt}%
\parbox[b]{\dimexpr\linewidth-\wd0-4pt}{nce upon a time…}
```

The PDFs in `pdf/negro/`, `pdf/verde/` and `pdf/rojo/` have the same
bounding box across the three folders, so they also work as plates.

## Using it in other programs

- **Installing the font:** open `fuente/OmakazeFlores-Regular.otf` and click
  *Install* (macOS: Font Book; Windows: right-click → *Install*; Linux: copy
  it to `~/.local/share/fonts/`).
- **Word, LibreOffice, Pages, InDesign, Affinity:** choose the *Omakaze
  Flores* font and type the piece's key. For two colors, put frame and letter
  in two text boxes stacked at the same position.
- **Inkscape, Illustrator:** open or import the SVG or PDF; the paths can be
  recolored and edited.
- **Typst:**
  `#text(font: "Omakaze Flores", size: 30pt)[a]` (with the font installed,
  or pass `--font-path fuente/`).
- **Web (CSS):**
  ```css
  @font-face { font-family: "Omakaze Flores";
               src: url("OmakazeFlores-Regular.otf") format("opentype"); }
  .flor { font-family: "Omakaze Flores"; font-size: 3rem; }
  ```

## Rebuilding the font

```
pip install fonttools
python3 herramientas/construir_fuente.py
```

The script reads `svg/` and writes `fuente/OmakazeFlores-Regular.otf`. To
change a piece, edit its SVG and run the script again. The title-page and
back-cover frames go into the font from `svg/fuente-simplificada/`: the CFF
format does not allow glyphs larger than 64 KB, and the full versions exceed
that. The full SVGs and PDFs are in `svg/` and `pdf/`.

### Packaging a release

```
sh herramientas/empaquetar.sh 0.2
```

Creates `dist/omakaze-flores-0.2.zip` from the latest commit, ready to
upload to GitHub *Releases*.

## Process

1. Original scans (1524 ppi) extracted from the PDF without recompression.
2. Paper background normalized; inks separated (black and red).
3. Cleanup: specks, neighboring text and frame contents removed.
4. Vectorized with Potrace.
5. Touch-ups: medallions emptied in the title-page frame; bottom-right
   corner of the W frame recreated from the top-left one.

## To do (for version 1.0)

- W initial frame: an incomplete fragment remains in the right column.
- Check for small pieces that may have been lost in the title-page and
  back-cover frames (they were processed with a stricter threshold).
- Even out rule weights and smooth the irregular edges of the 1923
  printing.
- Separate the frames' repeated flowers into individual pieces.
- Kerning and baseline alignment so the small pieces can be used in running
  text.

## License and provenance

The original document is in the public domain: its US copyright was not
renewed (Public Domain Mark 1.0). Digital reprint by CircuitousRoot.com,
contributed by David M. MacMillan, available on archive.org:
*MonotypeJournalVol09No06JanFeb1923*.

The vectorization, cleanup and compositions in this repository are dedicated
to the public domain under **CC0 1.0 Universal** (see `LICENSE`). You may
use, modify and sell them without asking permission, including in commercial
books, and the font can be embedded in PDFs without restriction. Credit is
appreciated but not required.

"Monotype" is a registered trademark of its owner. This project is not
affiliated with or endorsed by Monotype; the name is used only to identify
the historical source.

Vectorization: Libertad Pantoja · Omakaze Books, 2026.
