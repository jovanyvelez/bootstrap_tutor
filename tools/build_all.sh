#!/usr/bin/env bash
# Reconstruye las dos versiones web del tutorial y el hub.
set -euo pipefail
cd "$(dirname "$0")/.."

echo "== PixelCrew v2 =="
python3 tools/build_tutorial.py \
  --fuente tutorial-bootstrap-5.3.8-pixelcrew-v2.md \
  --salida tutorial/pixelcrew/index.html \
  --titulo "Bootstrap 5.3.8 · PixelCrew" \
  --subtitulo "Tutorial de autoestudio · 3 h 30 min · tema club de videojuegos" \
  --descripcion "Tutorial en español de Bootstrap 5.3.8 para adolescentes: construye el sitio de un club de videojuegos con 10 módulos." \
  --css ../assets/tutorial.css --js ../assets/tutorial.js \
  --proyecto ../../pixelcrew/index.html --etiqueta-proyecto "Ver PixelCrew" \
  --md ../../tutorial-bootstrap-5.3.8-pixelcrew-v2.md --etiqueta-md "Leer el .md"

echo "== RutaUni =="
python3 tools/build_tutorial.py \
  --fuente BOOTSTRAP-5.3.8-TUTORIAL.md \
  --salida tutorial/rutauni/index.html \
  --titulo "Bootstrap 5.3.8 · RutaUni" \
  --subtitulo "Tutorial de autoestudio · 3 h 30 min · tema preuniversitario" \
  --descripcion "Tutorial en español de Bootstrap 5.3.8: construye una landing page de preuniversitario con 10 módulos." \
  --css ../assets/tutorial.css --js ../assets/tutorial.js \
  --proyecto ../../rutouni/index.html --etiqueta-proyecto "Ver RutaUni" \
  --md ../../BOOTSTRAP-5.3.8-TUTORIAL.md --etiqueta-md "Leer el .md"

echo "== Proyectos =="
python3 tools/extract_project.py --variante pixelcrew
python3 tools/extract_project.py --variante rutouni

echo "Listo."
