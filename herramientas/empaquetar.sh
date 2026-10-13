#!/bin/sh
# Empaqueta la versión publicada (lo que está en el último commit) en un zip
# para la página de Releases de GitHub.
#
# Uso:   sh herramientas/empaquetar.sh 0.2
# Sale:  dist/omakaze-flores-0.2.zip
set -e
VERSION="${1:?Uso: sh herramientas/empaquetar.sh VERSION}"
cd "$(dirname "$0")/.."
mkdir -p dist
git archive --format=zip --prefix="omakaze-flores-$VERSION/" \
  -o "dist/omakaze-flores-$VERSION.zip" HEAD
echo "Listo: dist/omakaze-flores-$VERSION.zip"
