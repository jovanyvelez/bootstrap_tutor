#!/usr/bin/env python3
"""
Extrae el proyecto terminado (index.html, css/estilos.css, js/mi-script.js)
desde la sección «Código completo del proyecto terminado» del tutorial en
Markdown y lo escribe en la carpeta `rutouni/`.

Así el Markdown sigue siendo la única fuente de verdad: si corriges el
código dentro del tutorial, este script actualiza el sitio real.

Uso:
    python3 tools/extract_project.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
FUENTE = RAIZ / "BOOTSTRAP-5.3.8-TUTORIAL.md"
DESTINO = RAIZ / "rutouni"

# Otras combinaciones (fuente, destino) que se pueden reconstruir:
#   python3 tools/extract_project.py --variante pixelcrew
VARIANTES = {
    "pixelcrew": ("tutorial-bootstrap-5.3.8-pixelcrew-v2.md", "pixelcrew"),
    "rutuni": ("BOOTSTRAP-5.3.8-TUTORIAL.md", "rutouni"),
}

APPLY = re.compile(r'<meta name="theme-color" content="#1f3a8a">')


def extras_del_proyecto(html: str) -> str:
    """Añade los metadatos y el favicon que usan en el sitio publicado pero que
    no hacen falta dentro de un bloque de código del tutorial."""
    if 'og:title' in html:
        return html

    return html.replace(
        "    <title>",
        '''    <meta name="author" content="Proyecto educativo de ejemplo">
    <meta name="theme-color" content="#1f3a8a">
    <meta property="og:type" content="website">
    <meta property="og:title" content="RutaUni · Acompáñamos tu entrada a la universidad">
    <meta property="og:description" content="Preuniversitario virtual para estudiantes de grado 10 y 11 en Colombia.">
    <title>''',
        1,
    ).replace(
        "</head>",
        '''
    <!-- Favicon SVG en línea (sin archivos extra) -->
    <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>\U0001f9ed</text></svg>">
</head>''',
        1,
    )


def main() -> None:
    global FUENTE, DESTINO
    if len(sys.argv) > 2 and sys.argv[1] == "--variante":
        nombre = sys.argv[2]
        if nombre not in VARIANTES:
            sys.exit(f"Variantes disponibles: {', '.join(VARIANTES)}")
        fuente_rel, destino_rel = VARIANTES[nombre]
        FUENTE = RAIZ / fuente_rel
        DESTINO = RAIZ / destino_rel

    if not FUENTE.is_file():
        sys.exit(f"No encuentro {FUENTE}")

    texto = FUENTE.read_text(encoding="utf-8")

    # Aislamos la sección de código completo (el título puede o no llevar emoji).
    patron = re.compile(
        r"^#{1,3}\s+\S*\s*C[oó]digo completo del proyecto.*?\n"
        r"(.*?)"
        r"^#{1,3}\s+\S*\s*Hoja de referencia r[aá]pida",
        re.S | re.M,
    )
    encontrado = patron.search(texto)
    if not encontrado:
        sys.exit("No encuentro la secci\u00f3n de c\u00f3digo completo en el Markdown")
    seccion = encontrado.group(1)

    bloques = re.findall(r"###\s+`([^`]+)`\s*\n\n```(\w+)\n(.*?)```", seccion, re.S)
    if not bloques:
        bloques = re.findall(r"##\s+`([^`]+)`\s*\n\n```(\w+)\n(.*?)```", seccion, re.S)
    if not bloques:
        sys.exit("No encontré bloques de código en la sección")

    for nombre, lenguaje, codigo in bloques:
        destino = DESTINO / nombre
        destino.parent.mkdir(parents=True, exist_ok=True)
        if destino.suffix == ".html":
            codigo = extras_del_proyecto(codigo)
        destino.write_text(codigo, encoding="utf-8")
        print(f"\u2705 {DESTINO.name}/{nombre} ({len(codigo):,} caracteres)")

    print("\nProyecto sincronizado con el Markdown.")


if __name__ == "__main__":
    main()