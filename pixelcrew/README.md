# PixelCrew · proyecto terminado

Sitio del club de videojuegos del colegio, construido con **Bootstrap 5.3.8** siguiendo el
tutorial [`../tutorial-bootstrap-5.3.8-pixelcrew-v2.md`](../tutorial-bootstrap-5.3.8-pixelcrew-v2.md).

## Cómo abrirlo

Doble clic en `index.html`. No necesita servidor, Node.js ni instalar nada; sí conexión a
internet para el CDN (los `<link>` llevan `integrity`, así que los hashes ya están verificados).

## Archivos

```
pixelcrew/
├── index.html          (≈ 500 líneas)
├── css/style.css       personalizaciones: variables, degradados, tarjetas
└── js/main.js          validación con foco, modo claro/oscuro
```

## Secciones

| Sección | Componentes |
|---|---|
| Navbar | `navbar`, `navbar-expand-lg`, `navbar-collapse`, `sticky-top`, botón de tema |
| Hero | `row` + `col-lg-7/5`, `display-3`, degradado con `text-gradient` |
| Estadísticas | `col-6 col-md-3`, `bg-body-tertiary`, `display-6` |
| Qué hacemos | `alert alert-dismissible`, 3 × `card` con `row row-cols-*` |
| Galería | `row-cols-*` + `ratio ratio-1x1`, emojis con `role="img"` |
| Comunidad | `carousel slide` con `figure`/`blockquote` |
| Preguntas | `accordion` + `data-bs-parent` |
| Únete | `form-floating`, `form-select`, `input-group`, `was-validated` |
| Reglas | `modal fade` + `modal-dialog-scrollable` |
| Footer | `d-flex flex-column flex-md-row` |

## Verificado en navegador

- Sin desplazamiento horizontal de 320 a 1440 px.
- El tema arranca con el del dispositivo y recuerda la elección; cambia al cambiar el sistema.
- Al enviar el formulario vacío, el foco salta al primer campo con error; al enviarlo bien,
  salta al mensaje de éxito.
- El modal atrapa el foco, se cierra con `Esc`, con ✕, con «Entendido» y con clic afuera.
- 0 errores en la consola.

## Ideas para practicar más

1. Cambia la paleta editando `--bs-primary`, `--pc-accent` y `--bs-border-radius` en `css/style.css`.
2. Cambia los emojis de la galería por fotos reales con `alt` (el tutorial explica cómo).
3. Conecta el formulario a un backend: reemplaza el `preventDefault()` por un `fetch()`.
