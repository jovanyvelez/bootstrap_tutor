# Tutoriales de Bootstrap 5.3.8 · tutorial + proyectos

Paquete con **dos tutoriales en español** para aprender Bootstrap 5.3.8 construyendo un
sitio web real, más los dos proyectos terminados y sus versiones web.

| | Tutorial | Tema | Perfil |
|---|---|---|---|
| 🕹️ | **PixelCrew v2** (`tutorial-bootstrap-5.3.8-pixelcrew-v2.md`) | Club de videojuegos de colegio | 13–17 años, empezando de cero |
| 🎓 | **RutaUni** (`BOOTSTRAP-5.3.8-TUTORIAL.md`) | Preuniversitario y orientación universitaria | Algo de base en HTML/CSS, quiere profundizar |

Los dos duran **210 minutos**, tienen 10 módulos, proyecto incremental y código completo.

## Empezar

| Quiero… | Abre |
|---------|-------|
| Ver las dos webs y comparar | `tutorial/index.html` (o `index.html` y pulsa «Abrir el tutorial») |
| El tutorial para adolescentes | `tutorial/pixelcrew/index.html` |
| El tutorial más profundo | `tutorial/rutauni/index.html` |
| El sitio terminado de PixelCrew | `pixelcrew/index.html` |
| El sitio terminado de RutaUni | `rutouni/index.html` |
| Practicar grid y tipografía | `rutouni/pruebas-grid.html`, `rutouni/pruebas-tipografia.html` |
| Leer en Markdown | los dos archivos `.md` de la raíz |

No hay build ni servidor: doble clic y funciona. Solo necesitas internet para el CDN.

## Estructura

```
.
├── index.html                      ← hub con las dos opciones
├── README.md
├── tutorial-bootstrap-5.3.8-pixelcrew-v2.md   ← fuente (PixelCrew)
├── BOOTSTRAP-5.3.8-TUTORIAL.md                ← fuente (RutaUni)
│
├── tutorial/                       ← las dos webs
│   ├── index.html                  hub de los tutoriales
│   ├── pixelcrew/index.html        (generado)
│   ├── rutauni/index.html          (generado)
│   └── assets/                     tutorial.css + tutorial.js (compartidos)
│
├── pixelcrew/                      ← proyecto PixelCrew v2
│   ├── index.html, css/style.css, js/main.js
│   └── README.md
│
├── rutouni/                        ← proyecto RutaUni
│   ├── index.html, css/estilos.css, js/mi-script.js
│   ├── pruebas-grid.html, pruebas-tipografia.html
│   └── README.md
│
└── tools/
    ├── build_all.sh                reconstruye webs + proyectos
    ├── build_tutorial.py           Markdown → web (--fuente --salida --titulo…)
    ├── extract_project.py          Markdown → proyecto (--variante pixelcrew|rutuni)
    └── patch_pixelcrew_v2.py       aplica los parches v1 → v2 (documenta qué se corrigió)
```

## Reconstruir todo

```bash
bash tools/build_all.sh
```

Los Markdown son la **única fuente de verdad**. El flujo es:

```
tutorial-…-pixelcrew-v2.md ─┬─► tutorial/pixelcrew/index.html
                            └─► pixelcrew/index.html, css/, js/

BOOTSTRAP-5.3.8-TUTORIAL.md ─┬─► tutorial/rutauni/index.html
                              └─► rutouni/index.html, css/, js/
```

Requisitos: Python 3.10+ y `pip install markdown`.

## La web de cada tutorial incluye

- Índice lateral con scroll-spy (marca la sección que estás viendo).
- Buscador en vivo (atajo `/`) que resalta las coincidencias.
- Botón «Copiar» en cada bloque de código, con alternativa sin API de portapapeles.
- Resaltado de sintaxis HTML propio, sin dependencias.
- Barra de progreso y botón «volver arriba».
- Navegación anterior/siguiente que sigue el módulo en pantalla.
- Modo claro/oscuro con `localStorage`.
- Responsive: en móvil el índice se vuelve panel deslizable.
- Accesible: salto al contenido, foco visible, estilos de impresión.

`assets/tutorial.css` y `assets/tutorial.js` se editan a mano y no se sobrescriben.

## La v2 de PixelCrew: qué se corrigió

Los cuatro fallos se comprobaron abriendo el sitio en un navegador antes y después:

| Problema | Causa | Arreglo |
|---|---|---|
| La página se desplazaba de lado a lado en celular | `g-5` dentro de un `.container`: el margen negativo de la fila supera el relleno del contenedor | `g-4 g-lg-5` + `overflow-wrap: anywhere` |
| El modo siempre arrancaba en oscuro | El valor por defecto estaba fijado en `'dark'` | `matchMedia('(prefers-color-scheme: dark)')`, con `try/catch` y escuchador |
| Parpadeo al cargar | El tema se aplicaba con JS al final de la página | Script anti-parpadeo en el `<head>` |
| Al enviar el formulario el foco no se movía | No se buscaba el primer campo inválido | `querySelector(':invalid').focus()` y `tabindex="-1"` en el mensaje de éxito |

Además: la galería enseña imágenes reales con `alt`, `width`/`height`, `loading="lazy"` y
`object-fit-cover`; Sass queda como lectura opcional con su advertencia; y la lista de
accesibilidad del módulo 9 ahora verifica cosas que el tutorial sí usa.

## Verificaciones

| Qué | Resultado |
|---|---|
| Markdown → web | Todos los bloques de código con texto **idéntico** al original |
| Anclas | 0 enlaces internos rotos, 0 `id` duplicados |
| PixelCrew v2 en celular | Sin scroll horizontal a 320, 375, 390, 768, 992 y 1440 px |
| Tema | Sigue el del sistema, recuerda la elección, reacciona a cambios |
| Formulario | El foco va al primer error y luego al mensaje de éxito |
| Consola | 0 errores en los cuatro sitios |
| Accesibilidad | Recorrido completo con teclado en ambos proyectos |