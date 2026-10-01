# RutaUni · proyecto terminado del tutorial

Landing page de una sola página construida con **Bootstrap 5.3.8**, tal como queda al
completar el tutorial [`../BOOTSTRAP-5.3.8-TUTORIAL.md`](../BOOTSTRAP-5.3.8-TUTORIAL.md).

## Cómo abrirlo

Haz doble clic en `index.html`. No necesitas servidor, Node.js ni instalar nada.
Sí necesitas **conexión a internet** para cargar Bootstrap desde el CDN.

> Si el CDN está bloqueado en tu red, revisa el **Paso 5 del Módulo 8**: el tutorial
> explica cómo descargar Bootstrap y usarlo desde archivos locales.

## Archivos

```
rutouni/
├── index.html              ← la página completa (740+ líneas)
├── css/
│   └── estilos.css         ← personalización: variables, degradados, modo oscuro
├── js/
│   └── mi-script.js        ← validación del formulario, modal y tema
├── pruebas-grid.html       ← laboratorio del sistema de grid (Módulo 2)
├── pruebas-tipografia.html ← laboratorio de utilidades (Módulo 3)
└── README.md
```

## Secciones incluidas

| Sección | Componentes de Bootstrap usados |
|---------|---------------------------------|
| Navbar | `navbar`, `navbar-expand-lg`, `navbar-collapse`, `navbar-toggler`, `sticky-top` |
| Hero | `container`, `row`, `col-*` responsive, `display-3`, `btn`, `badge` |
| Cifras | `bg-body-tertiary`, `display-4`, utilidades de color |
| Aviso | `alert`, `btn-close`, `data-bs-dismiss` |
| Programas | `card`, `h-100`, `flex-grow-1`, `mt-auto`, `list-group` |
| Testimonios | `carousel slide`, `carousel-item`, `data-bs-ride` |
| Preguntas | `accordion`, `accordion-collapse`, `data-bs-parent` |
| Contacto | `form-control`, `form-select`, `form-check`, `input-group`, `is-invalid` |
| Modal | `modal fade`, `modal-dialog-centered`, `data-bs-toggle` |
| Footer | Rejilla de 4 columnas, `link-secondary`, `list-inline` |
| Global | `data-bs-theme` (modo oscuro), `localStorage`, variables `--bs-*` |

## Verificaciones hechas

- HTML balanceado: 0 etiquetas sin cerrar.
- 0 `id` duplicados y 0 anclas internas rotas.
- JavaScript validado con `node --check`.
- Navegable solo con teclado, con enlace de salto al contenido.
- Diseño responsive verificado a 375 px, 768 px y 1440 px.

## Ideas para practicarlo más

1. Cambia la paleta editando `--rutuni-azul`, `--rutuni-lima` y `--rutuni-naranja` en `css/estilos.css`.
2. Duplica `pruebas-grid.html` como banco de pruebas para el sistema de grid.
3. Añade un formulario real conectando el `submit` a un `fetch()` hacia tu backend.
