#!/usr/bin/env python3
"""
Genera la versión web del tutorial a partir del archivo Markdown.

Uso:
    python3 tools/build_tutorial.py
    python3 tools/build_tutorial.py --salida tutorial/index.html

Qué hace:
  1. Convierte el Markdown a HTML con la librería `markdown`.
  2. Añade atributos a cada encabezado para poder generar anclas y el índice.
  3. Decora los bloques de código con etiqueta de lenguaje y botón «Copiar».
  4. Envuelve el resultado en una página completa con barra de progreso,
     buscador, índice lateral (scroll-spy) y navegación anterior/siguiente.
  5. Escribe `tutorial/css/tutorial.css` y `tutorial/js/tutorial.js`
     solo si no existen (son archivos editados a mano).
"""

from __future__ import annotations

import argparse
import html
import os
import re
import sys
import unicodedata
from pathlib import Path

try:
    import markdown
except ImportError:  # pragma: no cover
    sys.exit("Falta la librería 'markdown'. Instálala con:  pip install markdown")

RAIZ = Path(__file__).resolve().parent.parent
FUENTE = RAIZ / "BOOTSTRAP-5.3.8-TUTORIAL.md"
SALIDA = RAIZ / "tutorial" / "index.html"

# Se sobrescribe con los argumentos de la línea de comandos.
META = {
    "title": "Bootstrap 5.3.8 desde Cero",
    "subtitle": 'Tutorial guiado de autoestudio · 3 h 30 min · construye "RutaUni"',
    "description": (
        "Tutorial en español de Bootstrap 5.3.8 para principiantes: 10 módulos, "
        "proyecto incremental y código completo."
    ),
}

# Rutas relativas al archivo de salida (hoja de estilos, script y proyecto).
RECURSOS = {
    "css": "../assets/tutorial.css",
    "js": "../assets/tutorial.js",
    "proyecto": "../../rutouni/index.html",
    "etiqueta_proyecto": "Ver el proyecto",
    "md": "../../BOOTSTRAP-5.3.8-TUTORIAL.md",
    "etiqueta_md": "Leer el .md",
}

CONFIG_MD = {
    # Sin la extensión "toc": reservamos los `id` para generar anclas compatibles
    # con GitHub, que es lo que usa la tabla de contenidos escrita a mano en el
    # archivo Markdown (por ejemplo `#módulo-4--navbar-y-navegación-responsive`).
    "extensions": ["extra", "tables", "sane_lists"],
}

# --------------------------------------------------------------------------- #
# Utilidades
# --------------------------------------------------------------------------- #


def slug(texto: str) -> str:
    """Replica el algoritmo de GitHub para generar anclas de encabezado.

    Se conservan letras (incluidas las acentuadas), dígitos, guion, guion bajo
    y espacios; todo lo demás —emojis, símbolos, dos puntos— se elimina, y los
    espacios se convierten en guiones.
    """
    limpio = "".join(
        ch for ch in texto.lower() if ch.isalnum() or ch in "-_ "
    )
    # GitHub no recorta: si el título empezaba por un emoji, el espacio que le
    # sigue se convierte en un guion inicial.
    return limpio.replace(" ", "-")


def limpiar_titulo(texto: str) -> str:
    """Quita los emojis y marcas de un título para mostrarlo limpio."""
    texto = re.sub(r"[`*]", "", texto)
    texto = re.sub(r"[←→]", "", texto)
    return re.sub(r"\s{2,}", " ", texto).strip()


def escapar(txt: str) -> str:
    return html.escape(txt, quote=True)


def terminales(etiqueta: str) -> bool:
    return etiqueta in {
        "area", "base", "br", "col", "embed", "hr", "img", "input",
        "link", "meta", "param", "source", "track", "wbr",
    }


# --------------------------------------------------------------------------- #
# Post-proceso del HTML
# --------------------------------------------------------------------------- #


def atributo_encabezados(ruta_html: str) -> tuple[list[dict], str]:
    """Añade `id` únicos a cada encabezado y devuelve (secciones, html).

    El contenido de los bloques de código va escapado por Markdown, así que un
    `<h1>` real en el HTML siempre proviene de un encabezado del documento.
    Los títulos repetidos («Objetivo», «Pasos»…) reciben un sufijo numérico.
    """
    with open(ruta_html, "r", encoding="utf-8") as fh:
        crudo = fh.read()

    secciones: list[dict] = []
    usadas: dict[str, int] = {}
    patron = re.compile(r"<h([1-4])>(.*?)</h\1>", re.S)

    def reemplaza(m: re.Match) -> str:
        nivel = int(m.group(1))
        texto = re.sub(r"<[^>]+>", "", m.group(2))
        titulo = limpiar_titulo(texto)

        base = slug(texto) or "seccion"
        contador = usadas.get(base, 0) + 1
        usadas[base] = contador
        ancla = base if contador == 1 else f"{base}-{contador}"

        secciones.append({"nivel": nivel, "titulo": titulo, "ancla": ancla})
        return (
            f'<h{nivel} id="{ancla}">'
            f'<a class="ancla-enlace" href="#{ancla}" '
            f'aria-label="Enlace permanente a: {escapar(titulo)}">#</a>'
            f"{titulo}</h{nivel}>"
        )

    return secciones, patron.sub(reemplaza, crudo)


def decorar_tablas(crudo: str) -> str:
    """Envuelve cada tabla en un contenedor con desplazamiento horizontal."""
    return re.sub(r"<table>", '<div class="tabla-envoltura"><table>', crudo).replace(
        "</table>", "</table></div>"
    )


def decorar_codigo(crudo: str) -> str:
    """Envuelve cada bloque de código en una figura con etiqueta de lenguaje
    y botón «Copiar»."""
    etiquetas = {
        "html": "HTML", "css": "CSS", "js": "JavaScript",
        "javascript": "JavaScript", "bash": "Terminal", "shell": "Terminal",
        "json": "JSON", "text": "Texto", "diagrama": "Diagrama", "arbol": "Estructura",
    }
    # Bloques con lenguaje explícito y bloques "pelados" (``` sin identificador)
    patron = re.compile(
        r'<pre><code(?: class="language-([\w+-]+)")?>(.*?)</code></pre>', re.S
    )

    def reemplaza(m: re.Match) -> str:
        lenguaje = m.group(1) or "diagrama"
        contenido = m.group(2)
        etiqueta = etiquetas.get(lenguaje, lenguaje.upper())
        return (
            '<figure class="bloque-codigo">'
            '<figcaption class="barra-codigo">'
            f'<span class="punto-lenguaje">{etiqueta}</span>'
            '<button type="button" class="btn-copiar" data-copiar '
            'aria-label="Copiar el código"><span aria-hidden="true">⧉</span> Copiar'
            "</button></figcaption>"
            f'<pre class="{lenguaje}" tabindex="0"><code>{contenido}</code></pre>'
            "</figure>"
        )

    return patron.sub(reemplaza, crudo)


def envolver(secciones: list[dict], cuerpo: str) -> str:
    """Arma la página completa. Usa `META` y `RECURSOS` como plantilla."""
    # El nivel de cada encabezado se normaliza: si el documento usa <h2> para
    # los módulos (en vez de <h1>), el índice no debe verse todo sangrado.
    indices = [s["nivel"] for s in secciones] or [1]
    base = min(indices)
    nivel_min = min(base + 1, 3)

    indice = []
    for i, s in enumerate(secciones):
        if s["nivel"] > nivel_min:
            continue
        sangria = {1: "", 2: "ms-2", 3: "ms-4"}[min(s["nivel"] - base + 1, 3)]
        activo = " activo" if i == 0 else ""
        indice.append(
            f'<li class="item-indice nivel-{s["nivel"]}{sangria}">'
            f'<a class="enlace-indice{activo}" href="#{s["ancla"]}">'
            f'{escapar(s["titulo"])}</a></li>'
        )

    navegacion = '<nav class="nav-modulos" aria-label="Navegación entre módulos"></nav>'

    valores = dict(META)
    valores.update({k: escapar(v) for k, v in RECURSOS.items()})

    return f"""<!DOCTYPE html>
<html lang="es" data-bs-theme="light">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{valores['title']} · {valores['subtitle']}</title>
<meta name="description" content="{valores['description']}">
<meta name="theme-color" content="#1f3a8a">
<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>&#128640;</text></svg>">

<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
<link rel="stylesheet" href="{valores['css']}">

<script>
try {{
    var t = localStorage.getItem('tutorial-tema');
    if (!t) t = matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    document.documentElement.setAttribute('data-bs-theme', t);
}} catch (e) {{}}
</script>
</head>
<body>

<a href="#contenido-tutorial" class="saltar-contenido">Saltar al contenido</a>

<div class="barra-progreso" aria-hidden="true"><div class="progreso" id="progreso"></div></div>

<header class="cabecera sticky-top">
    <div class="container-fluid">
        <div class="d-flex align-items-center gap-2">

            <button class="btn btn-light d-lg-none" type="button" id="botonIndice"
                    aria-controls="panelIndice" aria-expanded="false" aria-label="Abrir el índice">
                <i class="bi bi-list"></i>
            </button>

            <a class="marca d-flex align-items-center gap-2 text-decoration-none me-auto" href="#inicio">
                <span class="marca-icono">B5</span>
                <span class="d-none d-sm-inline">
                    <strong class="d-block lh-1">{valores['title']}</strong>
                    <small class="d-block text-secondary lh-1">{valores['subtitle']}</small>
                </span>
            </a>

            <div class="d-none d-md-block" style="min-width: 220px;">
                <label for="buscador" class="visually-hidden">Buscar en el tutorial</label>
                <div class="input-group input-group-sm">
                    <span class="input-group-text"><i class="bi bi-search"></i></span>
                    <input type="search" class="form-control" id="buscador"
                           placeholder="Buscar…" autocomplete="off">
                </div>
            </div>

            <a class="btn btn-sm btn-outline-secondary d-none d-lg-inline-flex" href="{valores['proyecto']}">
                <i class="bi bi-box-arrow-up-right me-1"></i>{valores['etiqueta_proyecto']}
            </a>
            <a class="btn btn-sm btn-outline-secondary d-none d-xl-inline-flex" href="{valores['md']}">
                <i class="bi bi-filetype-md me-1"></i>{valores['etiqueta_md']}
            </a>

            <button class="btn btn-light" type="button" id="botonTema" aria-label="Cambiar el tema">
                <i class="bi bi-moon-stars-fill" id="iconoTema" aria-hidden="true"></i>
            </button>

        </div>
        <p class="resultados-busqueda mb-0" id="resultadosBusqueda" role="status" aria-live="polite"></p>
    </div>
</header>

<div class="container-fluid">
    <div class="fila">

        <aside class="panel-indice" id="panelIndice" aria-label="Índice del tutorial">
            <nav aria-label="Índice">
                <p class="etiqueta-panel">Contenido</p>
                <ul class="lista-indice">
                    {''.join(indice)}
                </ul>
            </nav>
        </aside>

        <main class="contenido" id="contenido-tutorial">
{cuerpo}

{navegacion}
        </main>

    </div>
</div>

<button class="btn-arriba" type="button" id="botonArriba" aria-label="Volver arriba" hidden>
    <i class="bi bi-arrow-up"></i>
</button>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"></script>
<script src="{valores['js']}"></script>
</body>
</html>
"""


# --------------------------------------------------------------------------- #


def main() -> None:
    ap = argparse.ArgumentParser(description="Genera la web de un tutorial en Markdown.")
    ap.add_argument("--fuente", default=str(FUENTE), help="archivo .md de origen")
    ap.add_argument("--salida", default=str(SALIDA), help="index.html a generar")
    ap.add_argument("--titulo", help="título del tutorial")
    ap.add_argument("--subtitulo", help="subtítulo (tiempo y proyecto)")
    ap.add_argument("--descripcion", help="meta description")
    ap.add_argument("--css", help="ruta de la hoja de estilos (relativa a la salida)")
    ap.add_argument("--js", help="ruta del script (relativa a la salida)")
    ap.add_argument("--proyecto", help="enlace al proyecto terminado")
    ap.add_argument("--etiqueta-proyecto", default="Ver el proyecto")
    ap.add_argument("--md", help="enlace al archivo .md original")
    ap.add_argument("--etiqueta-md", default="Leer el .md")
    args = ap.parse_args()

    if args.titulo:
        META["title"] = args.titulo
    if args.subtitulo:
        META["subtitle"] = args.subtitulo
    if args.descripcion:
        META["description"] = args.descripcion
    for clave, valor in (
        ("css", args.css), ("js", args.js), ("proyecto", args.proyecto),
        ("etiqueta_proyecto", args.etiqueta_proyecto),
        ("md", args.md), ("etiqueta_md", args.etiqueta_md),
    ):
        if valor:
            RECURSOS[clave] = valor

    fuente = Path(args.fuente)
    salida = Path(args.salida)
    if not fuente.is_file():
        sys.exit(f"No encuentro el archivo fuente: {fuente}")

    texto = fuente.read_text(encoding="utf-8")

    # 1) Markdown -> HTML
    cuerpo = markdown.markdown(texto, **CONFIG_MD)

    # 2) Encabezados con id + índice
    temporal = salida.with_suffix(".tmp.html")
    temporal.write_text(cuerpo, encoding="utf-8")
    secciones, cuerpo = atributo_encabezados(str(temporal))
    temporal.unlink()

    # 3) Tablas desplazables y bloques de código decorados
    cuerpo = decorar_tablas(cuerpo)
    cuerpo = decorar_codigo(cuerpo)

    # 4) Página completa
    salida.parent.mkdir(parents=True, exist_ok=True)
    salida.write_text(envolver(secciones, cuerpo), encoding="utf-8")

    ruta = salida.resolve()
    print(f"✅ {ruta.relative_to(RAIZ)} generado")
    modulos = sum(1 for s in secciones if s["nivel"] == 1)
    print(f"   {len(secciones)} encabezados · {modulos} secciones · "
          f"{len(cuerpo):,} caracteres de HTML")


if __name__ == "__main__":
    main()
