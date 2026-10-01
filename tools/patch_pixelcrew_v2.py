#!/usr/bin/env python3
"""Aplica los parches de la v2 sobre una copia del tutorial PixelCrew.

Cada parche se valida: si el texto original no aparece exactamente una vez,
el script se detiene y avisa. Así evitamos cambios a medio hacer.
"""

from __future__ import annotations

import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DESTINO = RAIZ / "tutorial-bootstrap-5.3.8-pixelcrew-v2.md"

# (buscar, reemplazar, etiqueta, veces esperadas)
PARCHES: list[tuple[str, str, str, int]] = []


def parche(buscar: str, reemplazar: str, etiqueta: str, veces: int = 1) -> None:
    """Registra un parche.

    `veces` indica cuántas apariciones se esperan en el documento. Se usa 2 (o
    más) para bloques que están repetidos a propósito, por ejemplo la plantilla
    del módulo 1 que también aparece en el código completo del final.
    """
    PARCHES.append((buscar, reemplazar, etiqueta, veces))


# --------------------------------------------------------------------------- #
# 1. Portada
# --------------------------------------------------------------------------- #

parche(
    """> **Tutorial guiado de autoestudio · 3 horas y 30 minutos · Nivel principiante**
""",
    """> **Tutorial guiado de autoestudio · 3 horas y 30 minutos · Nivel principiante**
>
> 🧪 **Versión 2 (revisada y verificada).** Corrige cuatro problemas reales que tenía
> la v1 y que se comprobaron abriendo el sitio en un navegador:
>
> | Problema | Qué hace ahora |
> |---|---|
> | El sitio se desplazaba de lado a lado en celular | La portada usa `g-4 g-lg-5` y el CSS parte los textos largos con `overflow-wrap` |
> | El modo oscuro ignoraba la preferencia del sistema | Arranca con el tema del dispositivo (`prefers-color-scheme`) y recuerda el que elijas |
> | La página parpadeaba al cargar | Un script en el `<head>` aplica el tema antes de pintar |
> | Al enviar el formulario el foco no se movía | El foco salta al primer campo con error y al mensaje de éxito |
>
> Además: la galería enseña a usar imágenes reales con `alt`, y se aclara cuándo usar Sass.
""",
    "portada",
)

# --------------------------------------------------------------------------- #
# 2. Suposiciones
# --------------------------------------------------------------------------- #

parche(
    "- **Imágenes:** para que no dependas de descargar archivos, la galería usa emojis sobre bloques de color. En un proyecto real los reemplazarías por fotos con su texto alternativo.",
    "- **Imágenes:** para que no dependas de descargar nada, la galería empieza con emojis sobre bloques de color. En el módulo 2 verás cómo cambiarlos por fotos reales con su `alt` (usaremos fotos de ejemplo de internet; en tu club, pon las tuyas).",
    "suposiciones: imágenes",
)

parche(
    "- **Bootstrap por CDN**, con la versión exacta **5.3.8** y sus hashes de integridad. Sass se presenta como introducción conceptual, no es obligatorio.",
    "- **Modo claro u oscuro:** el sitio **arranca con el tema que ya tiene tu dispositivo** (`prefers-color-scheme`) y recuerda el que elijas después.\n"
    "- **Bootstrap por CDN**, con la versión exacta **5.3.8** y sus hashes de integridad. Sass se presenta como lectura opcional: **no hace falta para nada de este tutorial**.",
    "suposiciones: tema y sass",
)

# --------------------------------------------------------------------------- #
# 3. Módulo 1 · plantilla base
# --------------------------------------------------------------------------- #

parche(
    """```html
<!DOCTYPE html>
<html lang="es" data-bs-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="PixelCrew: el club de videojuegos de tu colegio. Torneos, noches de juego y talleres.">
  <title>PixelCrew | Club de videojuegos</title>

  <!-- Bootstrap 5.3.8 (CSS) -->""",
    """```html
<!DOCTYPE html>
<html lang="es" data-bs-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="PixelCrew: el club de videojuegos de tu colegio. Torneos, noches de juego y talleres.">
  <title>PixelCrew | Club de videojuegos</title>

  <!-- Aplica el tema ANTES de que se vea la página (evita el parpadeo).
       Va primero en el <head> a propósito; en un sitio real se le llama
       "anti-flash" y casi siempre se escribe en una sola línea. -->
  <script>
    (function () {
      try {
        var guardado = localStorage.getItem('pc-tema');
        var oscuroDelSistema = window.matchMedia('(prefers-color-scheme: dark)').matches;
        document.documentElement.setAttribute('data-bs-theme', guardado || (oscuroDelSistema ? 'dark' : 'light'));
      } catch (error) {
        document.documentElement.setAttribute('data-bs-theme', 'light');
      }
    })();
  </script>

  <!-- Bootstrap 5.3.8 (CSS) -->""",
    "módulo 1: script anti-parpadeo",
    2,
)

parche(
    """- `<html lang="es" data-bs-theme="dark">`: idioma español y **modo oscuro** activado en todo el sitio.""",
    """- `<html lang="es" data-bs-theme="light">`: idioma español y el tema inicial.
- El **script del `<head>`** aplica el tema guardado (o el de tu dispositivo) antes de que se pinte nada. Sin él, el navegador muestra un tema claro y luego salta a oscuro: eso es el parpadeo.""",
    "módulo 1: explicación del head",
)

parche(
    """### Mini-ejercicio

Cambia `data-bs-theme="dark"` por `data-bs-theme="light"` en la etiqueta `<html>` y observa qué cambia. Luego devuélvelo a `dark`. Después, cambia el botón de `btn-primary` a `btn-success`, `btn-danger` y `btn-warning`.""",
    """### Mini-ejercicio

1. Cambia `data-bs-theme="light"` por `data-bs-theme="dark"` en la etiqueta `<html>` **y borra por un momento el script del `<head>`**: verás el sitio oscuro, pero también el parpadeo al recargar. Después vuelve a poner el script.
2. En el sistema operativo, cambia tu tema a oscuro y abre el sitio: ¿qué modo aparece? (Pista: `prefers-color-scheme`).
3. Cambia el botón de `btn-primary` a `btn-success`, `btn-danger` y `btn-warning`.""",
    "módulo 1: mini-ejercicio del tema",
)

parche(
    """| `bootstrap is not defined` en la consola | El script no cargó | Revisa la URL y la pestaña **Network** (`F12`) |""",
    """| `bootstrap is not defined` en la consola | El script no cargó | Revisa la URL y la pestaña **Network** (`F12`) |
| La página parpadea blanco al cargar | Borraste el script del `<head>` o lo moviste después del CSS | Ponlo de nuevo, lo más arriba posible en el `<head>` |
| El modo oscuro no aparece aunque tu sistema esté en oscuro | Quitaste `matchMedia('(prefers-color-scheme: dark)')` | Ese `matchMedia` es lo que hace que el sitio respete tu tema del sistema |""",
    "módulo 1: errores",
)

parche(
    """- [ ] Sé cambiar entre modo claro y oscuro con `data-bs-theme`.""",
    """- [ ] Sé cambiar entre modo claro y oscuro con `data-bs-theme`.
- [ ] Entiendo para qué sirve el script del `<head>` y sé por qué va antes que el CSS.""",
    "módulo 1: punto de control",
)


def main() -> None:
    if not DESTINO.is_file():
        sys.exit(f"No encuentro {DESTINO}. Cópia primero el archivo original.")

    texto = DESTINO.read_text(encoding="utf-8")
    aplicados = 0

    for buscar, reemplazar, etiqueta, veces in PARCHES:
        encontrado = texto.count(buscar)
        if encontrado != veces:
            print(f"✗ [{etiqueta}] aparecía {encontrado} veces (se esperaban {veces}). Se detiene aquí.")
            sys.exit(1)
        texto = texto.replace(buscar, reemplazar)
        aplicados += 1

    DESTINO.write_text(texto, encoding="utf-8")
    print(f"✅ {aplicados} parches aplicados en {DESTINO.name}")



# --- Módulo 6: el foco va al error y al mensaje de éxito --------------------

parche(
    """- `evento.preventDefault()` evita que la página se recargue.
- Si es válido: limpia el formulario y muestra el mensaje de éxito. Si no, activa `was-validated`.""",
    """- `evento.preventDefault()` evita que la página se recargue.
- Si es válido: limpia el formulario, muestra el mensaje de éxito y le **da el foco**.
- Si no: activa `was-validated` y **lleva el foco al primer campo con error**.

#### Por qué importa lo del foco

Marcar los campos en rojo no sirve de nada si la persona sigue mirando el botón.
Al mandar el foco al primer error, quien usa teclado o lector de pantalla escucha
"Correo electrónico, inválido" y puede corregirlo sin buscarlo con el mouse.

Para que `mensajeExito.focus()` funcione, el mensaje necesita poder recibir foco, y eso
se logra con `tabindex="-1"`. Es el valor especial que significa: "puede recibir el foco
por código, pero no aparece en la secuencia del Tab".""",
    "módulo 6: por qué el foco",
)

parche(
    """        <div id="exito" class="alert alert-success d-none" role="status">""",
    """        <div id="exito" class="alert alert-success d-none" role="status" tabindex="-1">""",
    "módulo 6: tabindex en el aviso",
    2,
)

parche(
    """| Usas `form-group` o `form-row` | Son de Bootstrap 4 | En Bootstrap 5: `mb-3` o `row g-3` |""",
    """| Usas `form-group` o `form-row` | Son de Bootstrap 4 | En Bootstrap 5: `mb-3` o `row g-3` |
| Los campos se ponen rojos pero el foco sigue en el botón | Falta la línea que mueve el foco al primer `:invalid` | Agrega el `querySelector(':invalid')` con su `focus()` |
| `mensajeExito.focus()` no hace nada | El mensaje no puede recibir foco | Agrega `tabindex="-1"` al `div` del mensaje |
| `querySelector(':invalid')` devuelve `null` | El formulario es válido | Solo llámalo dentro del `else` |""",
    "módulo 6: errores de foco",
)

parche(
    """- [ ] Entiendo la función de `required`, `novalidate`, `checkValidity()` y `was-validated`.""",
    """- [ ] Entiendo la función de `required`, `novalidate`, `checkValidity()` y `was-validated`.
- [ ] Sé por qué hay que mover el foco al primer error y al mensaje de éxito.""",
    "módulo 6: punto de control",
)

# --- Módulo 7: tabindex y foco en el modal ---------------------------------
parche(
    """- Bootstrap se encarga solo de **atrapar el foco** dentro del modal y de cerrarlo con la tecla `Esc`.""",
    """- Bootstrap se encarga solo de **atrapar el foco** dentro del modal, de cerrarlo con la tecla `Esc`
  y de **devolver el foco al botón** que lo abrió cuando se cierra.
- `tabindex="-1"` en el modal no es un detalle: le permite a Bootstrap poner el foco ahí
  al abrirlo. Si lo quitas, el foco se pierde y la persona que navega con teclado se queda
  sin saber dónde está.""",
    "módulo 7: tabindex y foco",
)


# --- Módulo 8: el tema respeta el sistema y no parpadea ---------------------
parche(
    """#### Modo claro y oscuro

Bootstrap 5.3 trae **dos temas** integrados. Se elige con el atributo `data-bs-theme` (`light` o `dark`) en `<html>` o en cualquier elemento: el tema se aplica a ese elemento y a todo lo que contiene. Por eso para alternar el modo solo hay que **cambiar un atributo** con JavaScript, y recordarlo con `localStorage`.""",
    """#### Modo claro y oscuro

Bootstrap 5.3 trae **dos temas** integrados. Se elige con el atributo `data-bs-theme` (`light` o `dark`) en `<html>` o en cualquier elemento: el tema se aplica a ese elemento y a todo lo que contiene. Por eso para alternar el modo solo hay que **cambiar un atributo** con JavaScript, y recordarlo con `localStorage`.

##### Respetar el tema del sistema

Hay una cosa que un sitio bien hecho sí o sí hace: **adoptar el tema que ya eligió la
persona** en su dispositivo. Se lee con `matchMedia`:

```js
window.matchMedia('(prefers-color-scheme: dark)').matches  // true si el sistema está en oscuro
```

Ese `dark` es el tema del sistema. También existe `(prefers-color-scheme: light)`,
`(prefers-reduced-motion: reduce)` (que ya usaste en el módulo 5) y otras como
`(prefers-contrast: more)`. Todas son la manera correcta de "preguntarle" al dispositivo.

La regla de un sitio bien construido es esta:

> **Primero** respetas el tema del sistema. **Después**, si la persona elige otro con tu
> botón, su elección manda (y se recuerda).

##### El parpadeo: por qué el script va en el `<head>`

Un problema típico: si el tema lo aplica JavaScript **al final** de la página, el navegador
primero pinta el sitio en claro y un instante después lo cambia a oscuro. Se ve un
parpadeo Diez unpleasantísimo.

La solución es la que pusimos en el módulo 1: un `<script>` diminuto en el `<head>`, antes
del CSS, que aplica el tema **antes de que se pinte el primer píxel**. Ese script debe ser
cortísimo y no depender de nada: por eso va dentro de una función immediately ejecutada
(`(function () { ... })()`) y protegido con `try/catch`, para que un navegador en modo
privado (donde `localStorage` puede estar bloqueado) no rompa la página.""",
    "módulo 8: concepto del tema del sistema",
)


parche(
    """Luego enlazas `css/custom.css` en lugar del CSS del CDN. Es normal que Sass muestre avisos de *deprecation* sobre `@import`: Bootstrap 5.3 todavía usa esa sintaxis y los avisos no impiden que funcione.""",
    """Luego enlazas `css/custom.css` en lugar del CSS del CDN.

⚠️ **Esto es solo lectura, no lo hagas todavía.** Si lo intentas hoy vas a ver una montaña
de avisos rojos: Bootstrap 5.3 todavía usa `@import` (la sintaxis vieja) y el compilador de
Sass moderno la marca como *deprecada*. **Los avisos no rompen nada**, pero desconciertan
mucho. Además compilar Sass necesita Node.js instalado, y en un portátil del colegio eso
puede ser un problema.

La ruta moderna es `@use`, pero Bootstrap todavía no la usa por dentro. Por ahora quédate
con las **variables CSS del paso 3**, que不需要 compilar nada y hacen el 90 % de lo que
querrías hacer con Sass. Cuando tengas un proyecto propio y Node.js funcionando, vuelve
aquí.""",
    "módulo 8: aviso de Sass",
)

parche(
    """| En modo oscuro algunos colores no cambian | Pusiste tu bloque oscuro antes que `:root` | `[data-bs-theme="dark"]` debe ir **después** de `:root` |""",
    """| En modo oscuro algunos colores no cambian | Pusiste tu bloque oscuro antes que `:root` | `[data-bs-theme="dark"]` debe ir **después** de `:root` |
| El sitio arranca siempre en oscuro, aunque tu sistema esté en claro | Usaste `|| 'dark'` como valor por defecto | Deja que el default sea el del sistema: `matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'` |
| El sitio parpadea al cargar | El tema se aplica con JavaScript al final de la página | Pon el script del `<head>` (módulo 1), antes del CSS |
| `SecurityError` o `localStorage is not defined` | Modo privado con almacenamiento bloqueado | Ya está protegido con `try/catch`; si ves esto, revisa que lo pegaste bien |
| Cambias el tema del sistema y el sitio no se mueve | La persona ya había elegido con el botón | Es lo correcto: su elección manda. Borra `pc-tema` en la consola para volver al del sistema |""",
    "módulo 8: errores del tema",
)

parche(
    """- [ ] Mi sitio alterna entre modo claro y oscuro con el botón.
- [ ] El modo elegido se mantiene al recargar.""",
    """- [ ] Mi sitio alterna entre modo claro y oscuro con el botón.
- [ ] El modo elegido se mantiene al recargar.
- [ ] Si borro la preferencia guardada, el sitio arranca con el tema de mi dispositivo.
- [ ] Sé por qué el script del tema va en el `<head>` y no al final.""",
    "módulo 8: punto de control",
)

# --- Módulo 9: la lista de accesibilidad, ahora sí verificable -------------
parche(
    """| **Textos alternativos:** imágenes con `alt` o `role="img"` + `aria-label` | Revisa las de la galería |""",
    """| **Textos alternativos:** cada foto con `alt="descripción real"`, y los emojis decorativos con `role="img"` + `aria-label` | Las fotos que agregaste en el módulo 2 y los seis emojis de la galería |
| **Foco al enviar un formulario:** el foco va al primer error o al mensaje de éxito | Envía el formulario vacío y presiona `Tab`: el foco debe estar en el campo marcado |
| **Anclas:** ningún enlace apunta a un `id` inexistente | Haz clic en cada enlace del menú y en "Volver arriba" |
| **Sin desbordes:** nada obliga a desplazar la página de lado a lado | A 375 px no debe aparecer barra horizontal |""",
    "módulo 9: checklist de accesibilidad",
)

parche(
    """| Hay scroll horizontal en celular | Un elemento más ancho que la pantalla | Con `F12`, selecciona elementos hasta encontrar al culpable; revisa `container` y `row` |""",
    """| Hay scroll horizontal en celular |Casi siempre hay dos causas: un `g-5` dentro de un `.container`, o un texto largo sin partir | Con `F12` selecciona el elemento culpable: si es una `.row`, cambia a `g-4 g-lg-5`; si es un texto (correo, URL), agrega `overflow-wrap: anywhere` al `body` |
| La barra horizontal aparece solo en celular | Estás viendo el gutter grande en pantallas chicas | `g-4` en móvil y sube a `g-5` con `g-lg-5` |
| El sitio parpadea al abrir | El tema se aplica al final del JS | Mueve el script del tema al `<head>` (módulo 1) |""",
    "módulo 9: errores de responsive",
)

parche(
    """- [ ] Ejecuté Lighthouse y leí sus sugerencias.
- [ ] La consola del navegador no muestra errores.""",
    """- [ ] Ejecuté Lighthouse y leí sus sugerencias.
- [ ] La consola del navegador no muestra errores.
- [ ] En el formulario, el foco salta al primer error y luego al mensaje de éxito.
- [ ] Borré la preferencia de tema guardada y el sitio arrancó con el tema de mi sistema.""",
    "módulo 9: punto de control",
)


# =========================================================================== #
#  PARCHES 2 · Módulos 2, 3, 6, 7, 8 y 9 (se añaden al final del archivo)
# =========================================================================== #

# --- Módulo 2: la galería con fotos reales y su `alt` ------------------------
parche(
    """Mira la clase `row row-cols-2 row-cols-md-3 row-cols-lg-6`: ya no le damos ancho a cada columna, sino que decimos **cuántas caben**: 2 en celular, 3 en tablet, 6 en laptop. Además:

- `ratio ratio-1x1` crea un cuadrado perfecto sin importar el ancho.
- `role="img"` y `aria-label` describen el emoji para lectores de pantalla (accesibilidad).""",
    """Mira la clase `row row-cols-2 row-cols-md-3 row-cols-lg-6`: ya no le damos ancho a cada columna, sino que decimos **cuántas caben**: 2 en celular, 3 en tablet, 6 en laptop. Además:

- `ratio ratio-1x1` crea un cuadrado perfecto sin importar el ancho.
- `role="img"` y `aria-label` describen el emoji para lectores de pantalla (accesibilidad).

**6. (Opcional) Cambia dos cuadrados por fotos reales.** Los emojis son cómodo para
practicar, pero un sitio de verdad lleva fotos. Reemplaza **dos** de los `<div class="col">`
por estos (usamos fotos de ejemplo de internet; tú pon las tuyas):

```html
<div class="col">
  <div class="ratio ratio-1x1">
    <img src="https://picsum.photos/seed/pixelcrew-torneo/400/400"
         class="rounded-4 object-fit-cover w-100 h-100"
         alt="Jugadores alrededor de una mesa con consolas en un torneo del club"
         width="400" height="400" loading="lazy" decoding="async">
  </div>
</div>
```

Qué aprendiste ahí, y son cosas que se usan todo el tiempo:

| Atributo o clase | Para qué |
|---|---|
| `alt` | **Describe la imagen** para quien no la ve. Si es solo decorativa, se deja vacío: `alt=""` |
| `width` y `height` | El navegador reserva el espacio antes de descargar la foto: la página no "salta" al cargar |
| `loading="lazy"` | No descarga la foto hasta que está cerca de la pantalla. Acelera páginas largas |
| `object-fit-cover` | Rellena el cuadrado sin deformar la foto |
| `decoding="async"` | El navegador la decodifica sin bloquear el dibujado |

⚠️ **`alt` no es un adorno.** Escribir `alt="foto 1"` no sirve de nada: quien usa un
lector de pantalla solo oirá ese texto inútil. Describe lo que la imagen muestra.""",
    "módulo 2: fotos reales con alt",
)

parche(
    """### Resultado esperado

Una franja con 4 cifras y una galería de 6 cuadrados de colores.""",
    """### Resultado esperado

Una franja con 4 cifras y una galería de 6 cuadrados de colores.""",
    "módulo 2: resultado (sin cambio)",
)

parche(
    """| No ves cambios al achicar la ventana | Te falta la etiqueta `viewport` o estás mirando otro breakpoint | Usa el modo responsive de `F12` y revisa los anchos de la tabla |""",
    """| No ves cambios al achicar la ventana | Te falta la etiqueta `viewport` o estás mirando otro breakpoint | Usa el modo responsive de `F12` y revisa los anchos de la tabla |
| **La página se desplaza a los lados en celular** | Usaste un `g-5` (gutter grande) dentro de un `.container` | Una fila con gutter se come la mitad del gutter en margen negativo a cada lado. Si eso supera el relleno del contenedor, la fila se sale de la pantalla. Solución: `g-4 g-lg-5` |""",
    "módulo 2: error de gutter",
)

parche(
    """- [ ] Mi galería cambia el número de cuadrados por fila según el ancho.
- [ ] Sé usar el modo responsive de las herramientas del navegador.""",
    """- [ ] Mi galería cambia el número de cuadrados por fila según el ancho.
- [ ] Sé usar el modo responsive de las herramientas del navegador.
- [ ] Sé por qué un `g-5` dentro de un `.container` puede hacer scroll horizontal, y sé usar `g-4 g-lg-5`.""",
    "módulo 2: punto de control",
)

# --- Módulo 3: el gutter del hero y los textos largos -----------------------
parche(
    """    <div class="row align-items-center g-5">

      <div class="col-lg-7">""",
    """    <div class="row align-items-center g-4 g-lg-5">

      <div class="col-lg-7">""",
    "módulo 3: gutter del hero (módulo)",
)

parche(
    """        <div class="row align-items-center g-5">

          <div class="col-lg-7">""",
    """        <div class="row align-items-center g-4 g-lg-5">

          <div class="col-lg-7">""",
    "módulo 3: gutter del hero (código final)",
)

parche(
    """- `aria-hidden="true"`: es decoración, así que los lectores de pantalla la saltan.
- `<h1>`: solo hay **uno** por página.""",
    """- `aria-hidden="true"`: es decoración, así que los lectores de pantalla la saltan.
- `<h1>`: solo hay **uno** por página.
- `g-4 g-lg-5` en la fila: en celular usamos un gutter mediano y lo subimos en pantallas
  grandes. ¿Por qué? Porque una fila con `g-5` tiene un margen negativo de 24 px a cada
  lado, más ancho que el relleno del contenedor, y eso hace que la página **se desplace
  horizontalmente** en el celular. Es un error muy común; pruébalo: cambia a `g-5` a secas,
  achica la ventana y verás cómo aparece la barra de desplazamiento horizontal.""",
    "módulo 3: por qué g-4 g-lg-5",
)

parche(
    """```css
/* ===== 3. Hero ===== */""",
    """```css
/* Un texto muy largo (un correo, una URL) puede empujar la página y crear
   scroll horizontal en celular. `overflow-wrap: anywhere` lo parte.
   Ojo: `anywhere`, no `break-word`, porque es el único que además reduce el
   ancho mínimo de las celdas de un grid. */
body {
  overflow-wrap: anywhere;
}

/* ===== 3. Hero ===== */""",
    "módulo 3: overflow-wrap (módulo)",
)

parche(
    """/* Evita que la navbar fija tape los títulos al navegar por el menú */
section[id] { scroll-margin-top: 4.5rem; }

/* ===== 3. Hero ===== */""",
    """/* Evita que la navbar fija tape los títulos al navegar por el menú */
section[id] { scroll-margin-top: 4.5rem; }

/* Un texto muy largo (un correo, una URL) puede empujar la página y crear
   scroll horizontal en celular. `overflow-wrap: anywhere` lo parte.
   Ojo: `anywhere`, no `break-word`, porque es el único que además reduce el
   ancho mínimo de las celdas de un grid. */
body {
  overflow-wrap: anywhere;
}

/* ===== 3. Hero ===== */""",
    "módulo 3: overflow-wrap (código final)",
)

parche(
    """- **Tu CSS no pisa a Bootstrap:** confirma que `style.css` se carga **después** del CSS de Bootstrap.""",
    """- **Tu CSS no pisa a Bootstrap:** confirma que `style.css` se carga **después** del CSS de Bootstrap.
- **La página se desplaza en celular:** casi siempre es un `g-5` dentro de un `.container` o un
  texto largo sin partir. Usa `g-4 g-lg-5` y agrega `overflow-wrap: anywhere` al `body`.""",
    "módulo 3: error de scroll",
)


if __name__ == "__main__":
    main()
