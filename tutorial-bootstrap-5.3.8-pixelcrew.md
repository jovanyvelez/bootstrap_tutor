# Bootstrap 5.3.8 paso a paso: construye el sitio de tu club de videojuegos

> **Tutorial guiado de autoestudio · 3 horas y 30 minutos · Nivel principiante**

¡Bienvenido/a! En las próximas 3 horas y media vas a construir **PixelCrew**, la página web de un club de videojuegos de colegio. Vas a empezar con un archivo casi vacío y terminar con un sitio completo, responsive, con modo oscuro y modo claro, formulario con validación, carrusel, acordeón y ventana emergente.

Y lo más importante: al final no solo tendrás un sitio terminado. Tendrás las herramientas para **crear tus propios proyectos con Bootstrap sin necesitar este tutorial**.

---

## Tabla de contenidos

1. [Antes de empezar](#antes-de-empezar)
2. [Módulo 1: Preparación del entorno](#módulo-1-preparación-del-entorno) (15 min)
3. [Módulo 2: Contenedores, grid y breakpoints](#módulo-2-contenedores-grid-y-breakpoints) (30 min)
4. [Módulo 3: Tipografía, color y utilidades](#módulo-3-tipografía-color-y-utilidades) (20 min)
5. [Módulo 4: Navbar y navegación responsive](#módulo-4-navbar-y-navegación-responsive) (25 min)
6. [Módulo 5: Tarjetas, botones, badges y alertas](#módulo-5-tarjetas-botones-badges-y-alertas) (25 min)
7. [Módulo 6: Formularios y validación](#módulo-6-formularios-y-validación) (25 min)
8. [Módulo 7: Componentes interactivos con JavaScript](#módulo-7-componentes-interactivos-con-javascript) (25 min)
9. [Módulo 8: Personalización, modo oscuro y Sass](#módulo-8-personalización-modo-oscuro-y-sass) (20 min)
10. [Módulo 9: Integración final y buenas prácticas](#módulo-9-integración-final-y-buenas-prácticas) (15 min)
11. [Módulo 10: Tu reto final y siguientes pasos](#módulo-10-tu-reto-final-y-siguientes-pasos) (10 min)
12. [Código completo del proyecto](#código-completo-del-proyecto)
13. [Hoja de referencia rápida](#hoja-de-referencia-rápida)
14. [Retos adicionales y recursos oficiales](#retos-adicionales-y-recursos-oficiales)

---

## Antes de empezar

### Qué vas a construir

Una página con estas secciones, todas hechas con Bootstrap 5.3.8:

| Sección | Lo que practicas |
|---|---|
| Barra de navegación | Navbar responsive con menú hamburguesa |
| Hero (portada) | Tipografía, utilidades, color |
| Estadísticas y galería | Sistema de grid y breakpoints |
| "Qué hacemos" | Tarjetas, botones, badges, alertas |
| Comunidad | Carrusel |
| Preguntas frecuentes | Acordeón |
| Inscripción | Formularios con validación |
| Reglas del club | Modal (ventana emergente) |
| Todo el sitio | Modo claro/oscuro y personalización |

### Prerrequisitos

- Saber lo básico de **HTML** (etiquetas, atributos, enlaces) y de **CSS** (selectores, colores, márgenes).
- Un **editor de código**. Recomendado: [Visual Studio Code](https://code.visualstudio.com/) con la extensión *Live Server* (te recarga la página sola cada vez que guardas).
- Un navegador moderno (Chrome, Edge o Firefox).
- **Conexión a internet** mientras practicas (Bootstrap se carga desde un CDN).
- No necesitas instalar nada más, ni saber JavaScript, ni conocer Bootstrap.

### Cómo usar este tutorial

1. **Hazlo en orden.** Cada módulo agrega una pieza al mismo sitio, así que los módulos dependen unos de otros.
2. **Escribe o pega el código tú mismo/a y míralo funcionar.** No basta con leer.
3. **Cada módulo tiene el mismo formato:** objetivo, concepto, pasos, resultado esperado, errores comunes, mini-ejercicio y punto de control.
4. **Intenta el mini-ejercicio antes de abrir la pista** y la solución. Equivocarse ahí es parte del aprendizaje.
5. **Usa el punto de control** al final de cada módulo. Si no puedes marcar todo, repasa antes de seguir.
6. Si algo no se ve como debería, revisa la sección de **errores comunes** y las **Herramientas del navegador** (tecla `F12`).

Íconos que verás: 💡 tip · ⚠️ ojo con esto · ✅ punto de control.

### Plan de tiempo

| Módulo | Tema | Tiempo |
|---|---|---|
| 1 | Preparación del entorno | 15 min |
| 2 | Contenedores, grid y breakpoints | 30 min |
| 3 | Tipografía, color y utilidades | 20 min |
| 4 | Navbar y navegación responsive | 25 min |
| 5 | Tarjetas, botones, badges y alertas | 25 min |
| 6 | Formularios y validación | 25 min |
| 7 | Componentes interactivos (JS) | 25 min |
| 8 | Personalización, modo oscuro y Sass | 20 min |
| 9 | Integración final y buenas prácticas | 15 min |
| 10 | Reto final: planificación y primer paso | 10 min |
| | **Total** | **210 min (3 h 30 min)** |

💡 Los tiempos son estimaciones para una persona que escribe a ritmo normal. Si vas más rápido, aprovecha para hacer los retos adicionales; si vas más lento, está bien: lo importante es entender, no terminar primero.

### Suposiciones que hice

Para no dejar decisiones abiertas, asumí lo siguiente:

- **Tema del proyecto:** un club de videojuegos de colegio (PixelCrew). Los nombres, cifras y testimonios son ficticios.
- **Imágenes:** para que no dependas de descargar archivos, la galería usa emojis sobre bloques de color. En un proyecto real los reemplazarías por fotos con su texto alternativo.
- **Bootstrap por CDN**, con la versión exacta **5.3.8** y sus hashes de integridad. Sass se presenta como introducción conceptual, no es obligatorio.
- **El formulario no envía datos** a ningún servidor: es solo práctica de interfaz y validación.
- Todo el contenido está en **español** y usa solo clases de **Bootstrap 5** (nada de jQuery ni de clases de Bootstrap 4).

---

## Módulo 1: Preparación del entorno

⏱ **15 minutos**

🎯 **Objetivo:** crear la estructura de archivos, cargar Bootstrap 5.3.8 y comprobar que funciona.

### Concepto

**Bootstrap** es un framework de front-end: una colección de CSS y JavaScript ya escrita que te da tres cosas:

- Un **sistema de rejilla (grid)** para organizar la página en filas y columnas.
- **Componentes** listos para usar: barras de navegación, tarjetas, botones, formularios, modales...
- **Utilidades**: clases pequeñas que hacen una sola cosa (`mt-3` = margen arriba, `text-center` = texto centrado).

Es **mobile-first**: el diseño base piensa en celulares y luego se adapta a pantallas más grandes.

Hay dos formas de usarlo. Usaremos la primera:

| Forma | Cómo | Cuándo |
|---|---|---|
| **CDN** | Enlazas el CSS y el JS desde internet | Aprender, prototipos, sitios sencillos |
| **npm + Sass** | Lo instalas y lo compilas | Proyectos grandes con personalización profunda |

Bootstrap tiene dos archivos: el **CSS** (los estilos) y el **bundle JS**, que incluye todo el JavaScript de los componentes y a *Popper* (necesario para menús desplegables). Por eso usamos `bootstrap.bundle.min.js` y no el JS suelto.

### Pasos

**1. Crea esta estructura de carpetas y archivos** (puedes hacerlo desde VS Code):

```text
pixelcrew/
├── index.html
├── css/
│   └── style.css
└── js/
    └── main.js
```

Deja `style.css` y `main.js` vacíos por ahora.

**2. Pega esta plantilla en `index.html`.** Es el esqueleto de todo el proyecto. Fíjate en los comentarios `<!-- HERO -->`, `<!-- NAVBAR -->`, etc.: son **marcadores** donde pegarás código en los módulos siguientes.

```html
<!DOCTYPE html>
<html lang="es" data-bs-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="PixelCrew: el club de videojuegos de tu colegio. Torneos, noches de juego y talleres.">
  <title>PixelCrew | Club de videojuegos</title>

  <!-- Bootstrap 5.3.8 (CSS) -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">

  <!-- Tu CSS (siempre DESPUÉS de Bootstrap) -->
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <!-- NAVBAR -->

  <main id="contenido">
    <!-- PRUEBA -->
    <!-- HERO -->
    <!-- ESTADÍSTICAS -->
    <!-- QUÉ HACEMOS -->
    <!-- GALERÍA -->
    <!-- COMUNIDAD -->
    <!-- PREGUNTAS -->
    <!-- ÚNETE -->
  </main>

  <!-- FOOTER -->

  <!-- MODAL -->

  <!-- Bootstrap 5.3.8 (JS con Popper incluido) -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js" integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI" crossorigin="anonymous"></script>

  <!-- Tu JavaScript (después de Bootstrap) -->
  <script src="js/main.js"></script>
</body>
</html>
```

Observa lo importante:

- `<html lang="es" data-bs-theme="dark">`: idioma español y **modo oscuro** activado en todo el sitio.
- `<meta name="viewport" ...>`: sin esta línea, Bootstrap **no** se adapta a celulares.
- El CSS de Bootstrap va **antes** que tu `style.css`, para que tus estilos puedan sobrescribirlo.
- Los scripts van al **final** del `<body>`.
- Los atributos `integrity` y `crossorigin` verifican que el archivo del CDN no fue alterado. No los modifiques.

**3. Agrega un bloque de prueba.** Pega esto justo debajo del comentario `<!-- PRUEBA -->`:

```html
<div class="container py-5">
  <h1 class="display-4">¡Hola, Bootstrap 5.3.8!</h1>
  <p class="lead">Si ves esto con estilo, todo está funcionando.</p>
  <button type="button" class="btn btn-primary">Mi primer botón</button>
</div>
```

**4. Ábrelo en el navegador.** Con Live Server: clic derecho en `index.html` → *Open with Live Server*. Sin Live Server: doble clic en el archivo.

**5. Comprueba la versión.** Abre las herramientas del navegador (`F12`), ve a la pestaña **Console** y escribe:

```js
bootstrap.Tooltip.VERSION
```

Debe responder `"5.3.8"`.

### Resultado esperado

Una página oscura con un título grande, un párrafo destacado y un botón azul con esquinas redondeadas. Si ves letras blancas simples sobre fondo blanco y un botón gris, Bootstrap no cargó.

### Errores comunes

| Síntoma | Causa probable | Solución |
|---|---|---|
| La página se ve sin estilos | Sin internet, o error al copiar la URL del CDN | Revisa la conexión y compara los enlaces con los de la plantilla |
| La consola dice que bloqueó el recurso por `integrity` | Se alteró el hash al copiar | Vuelve a copiar la línea completa, sin espacios extra |
| El botón se ve bien pero los componentes no responden | Falta el `<script>` del bundle | Revisa que esté antes de `</body>` |
| En el celular todo se ve diminuto | Falta la etiqueta `viewport` | Agrégala dentro de `<head>` |
| `bootstrap is not defined` en la consola | El script no cargó | Revisa la URL y la pestaña **Network** (`F12`) |

### Mini-ejercicio

Cambia `data-bs-theme="dark"` por `data-bs-theme="light"` en la etiqueta `<html>` y observa qué cambia. Luego devuélvelo a `dark`. Después, cambia el botón de `btn-primary` a `btn-success`, `btn-danger` y `btn-warning`.

<details>
<summary>💡 Pista</summary>

Solo cambian palabras dentro del atributo `class`. Bootstrap tiene una clase para cada color: `btn-primary`, `btn-secondary`, `btn-success`, `btn-danger`, `btn-warning`, `btn-info`, `btn-light`, `btn-dark`.

</details>

### ✅ Punto de control

- [ ] Tengo la estructura `pixelcrew/` con sus tres archivos.
- [ ] Mi página muestra el título y el botón con estilo de Bootstrap.
- [ ] `bootstrap.Tooltip.VERSION` responde `"5.3.8"` en la consola.
- [ ] Sé cambiar entre modo claro y oscuro con `data-bs-theme`.

---

## Módulo 2: Contenedores, grid y breakpoints

⏱ **30 minutos**

🎯 **Objetivo:** organizar contenido en filas y columnas que se reacomodan según el tamaño de pantalla.

### Concepto

El grid de Bootstrap tiene tres piezas que siempre van **anidadas en este orden**:

```text
.container   →   .row   →   .col-*
(centra y        (fila,      (columna: cada fila se divide
 limita el        agrupa      en 12 partes)
 ancho)           columnas)
```

Cada fila tiene **12 unidades**. Una `col-6` ocupa la mitad, una `col-4` un tercio, una `col-3` un cuarto. Si las columnas suman más de 12, las sobrantes **saltan a la línea de abajo**.

#### Breakpoints: el corazón de lo responsive

Un *breakpoint* es el ancho de pantalla a partir del cual cambia el diseño. Bootstrap tiene seis:

| Prefijo | Se activa desde | Dispositivo típico |
|---|---|---|
| *(ninguno)* | 0 px | Celular vertical |
| `sm` | 576 px | Celular horizontal |
| `md` | 768 px | Tablet |
| `lg` | 992 px | Laptop |
| `xl` | 1200 px | Escritorio |
| `xxl` | 1400 px | Pantalla grande |

La regla clave es **mobile-first**: una clase sin prefijo aplica a **todas** las pantallas, y una clase con prefijo aplica **desde ese tamaño hacia arriba**. Ejemplo:

```html
<div class="col-12 col-md-6 col-lg-4">
```

Se lee así: *"ocupa las 12 columnas (todo el ancho) en celular; 6 (la mitad) desde tablet; 4 (un tercio) desde laptop"*.

Otras herramientas del grid que usaremos:

- `g-3`: **gutter** (espacio entre columnas) de tamaño 3.
- `row-cols-2`: en vez de dar un ancho a cada columna, dices cuántas columnas caben por fila.
- `container` (ancho fijo por breakpoint) vs `container-fluid` (siempre 100 % del ancho).

### Pasos

**1. Laboratorio de grid (temporal).** Reemplaza el bloque de prueba del módulo anterior por este (bórralo todo y pega):

```html
<div class="container py-4">
  <div class="row g-3">
    <div class="col-12 col-md-6 col-lg-4">
      <div class="p-3 bg-primary-subtle border rounded text-center">A</div>
    </div>
    <div class="col-12 col-md-6 col-lg-4">
      <div class="p-3 bg-success-subtle border rounded text-center">B</div>
    </div>
    <div class="col-12 col-md-6 col-lg-4">
      <div class="p-3 bg-danger-subtle border rounded text-center">C</div>
    </div>
  </div>
</div>
```

**2. Experimenta.** Abre las herramientas del navegador (`F12`) y activa el **modo responsive** (el ícono de celular y tablet). Cambia el ancho y observa:

- Menos de 768 px → las tres cajas **apiladas**, una por fila.
- Entre 768 y 991 px → **dos** por fila (la C baja).
- 992 px o más → **tres** en una fila.

💡 Entre 768 y 991 px, A y B (`col-md-6` cada una) suman las 12 unidades de la fila, por eso C no cabe y salta a la línea de abajo.

**3. Borra el laboratorio.** Ya aprendiste lo esencial. Elimina todo el bloque que pegaste en el paso 1.

**4. Construye la franja de estadísticas.** Pega justo debajo de `<!-- ESTADÍSTICAS -->`:

```html
<section class="py-4 border-top border-bottom bg-body-tertiary" aria-label="El club en números">
  <div class="container">
    <div class="row g-3 text-center">
      <div class="col-6 col-md-3">
        <p class="display-6 fw-bold text-primary-emphasis mb-0">120+</p>
        <p class="text-body-secondary mb-0">miembros</p>
      </div>
      <div class="col-6 col-md-3">
        <p class="display-6 fw-bold text-primary-emphasis mb-0">12</p>
        <p class="text-body-secondary mb-0">torneos al año</p>
      </div>
      <div class="col-6 col-md-3">
        <p class="display-6 fw-bold text-primary-emphasis mb-0">3</p>
        <p class="text-body-secondary mb-0">talleres semanales</p>
      </div>
      <div class="col-6 col-md-3">
        <p class="display-6 fw-bold text-primary-emphasis mb-0">1</p>
        <p class="text-body-secondary mb-0">sala gamer</p>
      </div>
    </div>
  </div>
</section>
```

Aquí hay varias ideas nuevas:

- `col-6 col-md-3`: dos por fila en celular, cuatro por fila desde tablet.
- `bg-body-tertiary`: un fondo que se adapta solo al modo claro u oscuro.
- `border-top border-bottom`: bordes arriba y abajo.
- `display-6`: un texto grande y llamativo (más sobre esto en el módulo 3).

**5. Construye la galería.** Pega justo debajo de `<!-- GALERÍA -->`:

```html
<section id="galeria" class="py-5">
  <div class="container">
    <h2 class="text-center mb-2">Momentos del club</h2>
    <p class="text-center text-body-secondary mb-4">Un vistazo a lo que pasa en las reuniones. (Aquí irían tus fotos reales.)</p>

    <div class="row row-cols-2 row-cols-md-3 row-cols-lg-6 g-3">
      <div class="col">
        <div class="ratio ratio-1x1">
          <div class="rounded-4 bg-primary d-flex align-items-center justify-content-center fs-1" role="img" aria-label="Ilustración de un trofeo">🏆</div>
        </div>
      </div>
      <div class="col">
        <div class="ratio ratio-1x1">
          <div class="rounded-4 bg-success d-flex align-items-center justify-content-center fs-1" role="img" aria-label="Ilustración de un joystick">🕹️</div>
        </div>
      </div>
      <div class="col">
        <div class="ratio ratio-1x1">
          <div class="rounded-4 bg-danger d-flex align-items-center justify-content-center fs-1" role="img" aria-label="Ilustración de unos audífonos">🎧</div>
        </div>
      </div>
      <div class="col">
        <div class="ratio ratio-1x1">
          <div class="rounded-4 bg-warning d-flex align-items-center justify-content-center fs-1" role="img" aria-label="Ilustración de un computador">💻</div>
        </div>
      </div>
      <div class="col">
        <div class="ratio ratio-1x1">
          <div class="rounded-4 bg-info d-flex align-items-center justify-content-center fs-1" role="img" aria-label="Ilustración de un dado">🎲</div>
        </div>
      </div>
      <div class="col">
        <div class="ratio ratio-1x1">
          <div class="rounded-4 bg-secondary d-flex align-items-center justify-content-center fs-1" role="img" aria-label="Ilustración de un apretón de manos">🤝</div>
        </div>
      </div>
    </div>
  </div>
</section>
```

Mira la clase `row row-cols-2 row-cols-md-3 row-cols-lg-6`: ya no le damos ancho a cada columna, sino que decimos **cuántas caben**: 2 en celular, 3 en tablet, 6 en laptop. Además:

- `ratio ratio-1x1` crea un cuadrado perfecto sin importar el ancho.
- `role="img"` y `aria-label` describen el emoji para lectores de pantalla (accesibilidad).

### Resultado esperado

Una franja con 4 cifras y una galería de 6 cuadrados de colores. Al achicar la ventana, la franja pasa de 4 columnas a 2 + 2, y la galería de 6 a 3 + 3 y luego a 2 + 2 + 2.

### Errores comunes

| Síntoma | Causa | Solución |
|---|---|---|
| Las columnas se pegan a los bordes de la pantalla | Falta el `.container` | Envuelve la fila en un `.container` |
| Las columnas no se alinean bien | Pusiste `.col` sin `.row` | Las columnas **siempre** van dentro de una `.row` |
| Una columna salta de línea sin razón | Las columnas suman más de 12 | Revisa la suma de los números `col-*` |
| `col-xs-6` o `col-sm-offset-2` no funcionan | Son de Bootstrap 3 | En Bootstrap 5 es `col-6` y `offset-sm-2` |
| No ves cambios al achicar la ventana | Te falta la etiqueta `viewport` o estás mirando otro breakpoint | Usa el modo responsive de `F12` y revisa los anchos de la tabla |

### Mini-ejercicio

Modifica la galería para que en pantallas `lg` se vean **4 cuadrados por fila** (en vez de 6) y agrega **2 cuadrados más** (con otro emoji y otro color) para completar 2 filas parejas de 4.

<details>
<summary>💡 Pista</summary>

Solo necesitas cambiar un número en `row-cols-lg-6` y duplicar dos bloques `<div class="col">`. Para los colores usa `bg-dark`, `bg-light` o los que ya usaste con otro emoji.

</details>

<details>
<summary>✅ Solución</summary>

Cambia `row-cols-lg-6` por `row-cols-lg-4` y agrega, por ejemplo:

```html
<div class="col">
  <div class="ratio ratio-1x1">
    <div class="rounded-4 bg-dark d-flex align-items-center justify-content-center fs-1" role="img" aria-label="Ilustración de una estrella">⭐</div>
  </div>
</div>
```

Repite con otro emoji para tener 8 cuadrados en total.

</details>

💡 Puedes dejar la galería como la dejaste: el resto del tutorial no depende de cuántos cuadrados tenga.

### ✅ Punto de control

- [ ] Puedo explicar la jerarquía `container → row → col`.
- [ ] Entiendo que `col-12 col-md-6 col-lg-4` significa "mobile-first".
- [ ] Mi franja de estadísticas pasa de 4 a 2 columnas en celular.
- [ ] Mi galería cambia el número de cuadrados por fila según el ancho.
- [ ] Sé usar el modo responsive de las herramientas del navegador.

---

## Módulo 3: Tipografía, color y utilidades

⏱ **20 minutos**

🎯 **Objetivo:** dar estilo a tu contenido usando clases utilitarias de Bootstrap, y construir la portada (hero) del sitio.

### Concepto

Las **utilidades** son clases que hacen *una sola cosa*. Combinándolas puedes diseñar casi todo **sin escribir CSS**. Las más importantes:

| Familia | Ejemplos | Qué hacen |
|---|---|---|
| Tipografía | `display-1`…`display-6`, `lead`, `fs-1`…`fs-6`, `fw-bold`, `fw-semibold`, `text-uppercase`, `small` | Tamaño, peso y estilo del texto |
| Alineación | `text-center`, `text-start`, `text-end` | Alineación horizontal |
| Color de texto | `text-primary`, `text-body-secondary`, `text-white` | Color del texto |
| Color de fondo | `bg-primary`, `bg-success-subtle`, `bg-body-tertiary` | Color de fondo |
| Espaciado | `m-3`, `p-4`, `mt-2`, `px-5`, `py-3`, `ms-auto`, `gap-3` | Márgenes, relleno y separación |
| Display y flex | `d-flex`, `d-none`, `d-lg-block`, `flex-column`, `justify-content-between`, `align-items-center` | Mostrar, ocultar y alinear |
| Bordes y sombras | `border`, `rounded-4`, `rounded-pill`, `shadow`, `shadow-lg` | Aspecto de las cajas |

#### La escala de espaciado

Los números del 0 al 5 siguen esta escala:

| Número | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| Tamaño | 0 | 0,25 rem | 0,5 rem | 1 rem | 1,5 rem | 3 rem |

Y las letras indican **dónde** aplica:

- `m` = margen (afuera), `p` = padding (adentro).
- `t` arriba, `b` abajo, `s` inicio (izquierda), `e` final (derecha), `x` izquierda y derecha, `y` arriba y abajo.
- Sin letra = los cuatro lados.

Así, `mt-4` es "margen arriba tamaño 4" y `px-5` es "relleno horizontal tamaño 5". Y todas aceptan breakpoints: `py-3 py-lg-5`.

#### Colores adaptables

Fíjate en que usamos `text-body-secondary` y `bg-body-tertiary` en vez de colores fijos como `text-muted` o `bg-light`. Los primeros **cambian solos** entre modo claro y oscuro, y son los recomendados desde Bootstrap 5.3.

💡 **Regla práctica:** usa utilidades para el 90 % del estilo y escribe CSS propio solo para lo que Bootstrap no trae (como un degradado).

### Pasos

**1. Agrega el HTML del hero.** Pega justo debajo de `<!-- HERO -->`:

```html
<section id="inicio" class="hero py-5">
  <div class="container py-lg-5">
    <div class="row align-items-center g-5">

      <div class="col-lg-7">
        <p class="text-uppercase fw-semibold text-primary-emphasis small mb-2">Club de videojuegos del colegio</p>
        <h1 class="display-3 fw-bold mb-3">Juega, crea y compite con <span class="text-gradient">PixelCrew</span></h1>
        <p class="lead text-body-secondary mb-4">
          Somos el club donde los videojuegos se juegan, se estudian y hasta se programan.
          Si tienes entre 14 y 18 años, hay un lugar para ti en el equipo.
        </p>
        <div class="d-flex flex-column flex-sm-row gap-3">
          <a href="#unete" class="btn btn-primary btn-lg px-4">Únete al club</a>
          <a href="#juegos" class="btn btn-outline-secondary btn-lg px-4">Descubre qué hacemos</a>
        </div>
      </div>

      <div class="col-lg-5 d-none d-lg-block">
        <div class="hero-card rounded-4 shadow-lg p-5 text-center text-white" aria-hidden="true">
          <div class="display-1">🎮</div>
          <p class="fs-4 fw-semibold mb-0">Nivel 1: ¡empieza hoy!</p>
        </div>
      </div>

    </div>
  </div>
</section>
```

Detalles para fijarte:

- `py-5` y `py-lg-5` en el contenedor: relleno vertical, más grande en pantallas grandes.
- `display-3 fw-bold`: el título enorme y en negrita. `lead` hace un párrafo destacado.
- `d-flex flex-column flex-sm-row gap-3`: los botones se apilan en celular y se ponen uno al lado del otro desde `sm`.
- `d-none d-lg-block`: la tarjeta decorativa **solo aparece desde pantallas grandes**.
- `aria-hidden="true"`: es decoración, así que los lectores de pantalla la saltan.
- `<h1>`: solo hay **uno** por página.

**2. Agrega CSS propio.** Bootstrap no trae degradados, así que esta es una buena excusa para escribir un poco de CSS. Pega esto en `css/style.css`:

```css
/* ===== 3. Hero ===== */
.hero {
  background:
    radial-gradient(circle at 15% 20%, rgba(124, 77, 255, 0.25), transparent 45%),
    radial-gradient(circle at 85% 80%, rgba(13, 139, 217, 0.18), transparent 45%);
}

.text-gradient {
  background: linear-gradient(90deg, #7c4dff, #0d8bd9);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

.hero-card {
  background: linear-gradient(135deg, #7c4dff, #0d8bd9);
}
```

La clase `text-gradient` pinta el texto con un degradado recortando el fondo con la forma de las letras.

### Resultado esperado

Una portada con título gigante (la palabra "PixelCrew" con degradado de morado a azul), un texto descriptivo en gris, dos botones y, en pantallas anchas, una tarjeta decorativa a la derecha. En celular la tarjeta desaparece y los botones ocupan todo el ancho.

### Errores comunes

⚠️ Clases que **ya no existen o están obsoletas** (las verás en tutoriales viejos):

| Si ves… | Usa… |
|---|---|
| `ml-3`, `mr-3` | `ms-3`, `me-3` |
| `pl-2`, `pr-2` | `ps-2`, `pe-2` |
| `text-left`, `text-right` | `text-start`, `text-end` |
| `float-left`, `float-right` | `float-start`, `float-end` |
| `font-weight-bold` | `fw-bold` |
| `text-muted` | `text-body-secondary` |
| `badge-primary` | `text-bg-primary` |
| `data-toggle`, `data-target` | `data-bs-toggle`, `data-bs-target` |

Otros problemas:

- **El título no tiene degradado:** revisa que `style.css` esté enlazado y que escribiste `-webkit-background-clip` y `background-clip`.
- **Tu CSS no pisa a Bootstrap:** confirma que `style.css` se carga **después** del CSS de Bootstrap.

### Mini-ejercicio

En celular, centra el título y el párrafo del hero. Desde pantallas `lg`, deben volver a alinearse a la izquierda.

<details>
<summary>💡 Pista</summary>

Es una clase de alineación con y sin prefijo de breakpoint. Va en la columna que contiene el texto (`col-lg-7`).

</details>

<details>
<summary>✅ Solución</summary>

Agrega `text-center text-lg-start` a la columna: `<div class="col-lg-7 text-center text-lg-start">`.

</details>

### ✅ Punto de control

- [ ] Mi hero muestra el título con degradado y dos botones.
- [ ] Entiendo qué significa `mt-4`, `px-5` y `py-lg-5`.
- [ ] Sé usar `d-none d-lg-block` para ocultar elementos según el tamaño de pantalla.
- [ ] Sé cuáles clases de Bootstrap 4 ya no debo usar.

---

## Módulo 4: Navbar y navegación responsive

⏱ **25 minutos**

🎯 **Objetivo:** crear una barra de navegación que se colapsa en un menú hamburguesa en pantallas pequeñas y que permanece fija arriba.

### Concepto

La **navbar** es un componente completo de Bootstrap. Se compone de:

- `.navbar`: el contenedor principal.
- `.navbar-expand-lg`: define **desde qué breakpoint** el menú se muestra expandido. Por debajo de `lg`, se colapsa.
- `.navbar-brand`: el logo o nombre del sitio.
- `.navbar-toggler`: el botón hamburguesa.
- `.navbar-collapse`: la parte que se oculta y se muestra.
- `.navbar-nav`, `.nav-item`, `.nav-link`: la lista de enlaces.

El botón hamburguesa **funciona sin que escribas JavaScript**: Bootstrap lee atributos `data-bs-*` en el HTML. Aquí, `data-bs-toggle="collapse"` y `data-bs-target="#menuPrincipal"` significan "al hacer clic, muestra u oculta el elemento con id `menuPrincipal`".

#### Accesibilidad en la navbar

- `aria-label` en el `<nav>` y en el botón dice a los lectores de pantalla qué son.
- `aria-expanded` indica si el menú está abierto (Bootstrap lo actualiza solo).
- Un **enlace "Saltar al contenido"** permite a quien navega con teclado evitar repetir todo el menú.

### Pasos

**1. Pega la navbar** justo debajo de `<!-- NAVBAR -->`:

```html
<a class="visually-hidden-focusable" href="#contenido">Saltar al contenido</a>

<header class="sticky-top">
  <nav class="navbar navbar-expand-lg bg-body-tertiary border-bottom" aria-label="Navegación principal">
    <div class="container">
      <a class="navbar-brand fw-bold" href="#inicio">🎮 PixelCrew</a>

      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#menuPrincipal" aria-controls="menuPrincipal" aria-expanded="false" aria-label="Abrir o cerrar el menú">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="menuPrincipal">
        <ul class="navbar-nav ms-auto mb-2 mb-lg-0 align-items-lg-center">
          <li class="nav-item"><a class="nav-link" href="#juegos">Qué hacemos</a></li>
          <li class="nav-item"><a class="nav-link" href="#galeria">Galería</a></li>
          <li class="nav-item"><a class="nav-link" href="#testimonios">Comunidad</a></li>
          <li class="nav-item"><a class="nav-link" href="#faq">Preguntas</a></li>
          <li class="nav-item ms-lg-3 my-2 my-lg-0"><a class="btn btn-primary btn-sm" href="#unete">Únete</a></li>
        </ul>
      </div>
    </div>
  </nav>
</header>
```

**2. Revisa los detalles:**

- `sticky-top`: la barra se queda fija arriba al hacer scroll.
- `bg-body-tertiary border-bottom`: un fondo suave que se adapta al modo claro/oscuro.
- `ms-auto`: empuja los enlaces hacia la derecha (el margen izquierdo es "automático").
- `align-items-lg-center`: alinea verticalmente solo desde `lg`.
- `visually-hidden-focusable`: el enlace de saltar está oculto hasta que lo enfocas con la tecla `Tab`.

**3. Pruébalo:**

- Estira y encoge la ventana: pasado `lg` (992 px), el menú se oculta tras el botón hamburguesa.
- Haz clic en la hamburguesa: el menú se despliega.
- Los enlaces del menú todavía no te llevan a ningún lado: las secciones a las que apuntan las vas a crear en los próximos módulos.
- Presiona `Tab` apenas cargue la página: debe aparecer "Saltar al contenido".

### Resultado esperado

Una barra superior con el nombre del club a la izquierda y los enlaces a la derecha. En celular, solo se ve el nombre y el botón de tres rayitas.

### Errores comunes

| Síntoma | Causa | Solución |
|---|---|---|
| El botón hamburguesa no hace nada | Falta el bundle JS, o el `id` no coincide con `data-bs-target` | Revisa que `data-bs-target="#menuPrincipal"` y `id="menuPrincipal"` sean idénticos |
| Los enlaces quedan a la izquierda | Falta `ms-auto` | Agrégalo al `<ul class="navbar-nav">` |
| El menú nunca se colapsa | Falta `navbar-expand-lg` o `collapse` | Revisa ambos nombres de clase |
| La navbar tapa el contenido al navegar a una sección | Es normal con `sticky-top` | Lo corregiremos con una línea de CSS en el módulo 8 |
| El ícono hamburguesa no aparece | Falta `<span class="navbar-toggler-icon">` | Agrégalo dentro del botón |

### Mini-ejercicio

Haz que el menú se expanda desde pantallas **medianas** (`md`) en lugar de `lg`.

<details>
<summary>💡 Pista</summary>

Cambia el breakpoint en una clase de la navbar. Hay otras clases con `lg` dentro de la navbar que también deberías ajustar para que todo sea coherente.

</details>

<details>
<summary>✅ Solución</summary>

Cambia `navbar-expand-lg` por `navbar-expand-md`, y en el `<ul>` usa `mb-md-0` y `align-items-md-center`. También ajusta `ms-lg-3` y `my-lg-0` del botón "Únete" a `ms-md-3` y `my-md-0`.

</details>

### ✅ Punto de control

- [ ] La navbar se ve completa en pantalla ancha y se colapsa en pantalla angosta.
- [ ] El botón hamburguesa abre y cierra el menú.
- [ ] La barra se queda fija arriba al hacer scroll.
- [ ] Entiendo cómo `data-bs-toggle` y `data-bs-target` conectan un botón con un elemento.
- [ ] Probé el enlace "Saltar al contenido" con la tecla `Tab`.

---

## Módulo 5: Tarjetas, botones, badges y alertas

⏱ **25 minutos**

🎯 **Objetivo:** usar los componentes más comunes de Bootstrap para presentar información de forma atractiva.

### Concepto

Un **componente** es un bloque de interfaz listo para usar. Se arma con una clase base y variantes:

- **Botones:** base `.btn` + variante de color (`.btn-primary`) o contorno (`.btn-outline-primary`) + tamaño (`.btn-lg`, `.btn-sm`).
- **Badges:** etiquetas pequeñas, con `.badge text-bg-warning` (el fondo y el texto con buen contraste ya vienen resueltos).
- **Alertas:** mensajes contextuales: `.alert alert-success`, `alert-danger`, `alert-warning`, `alert-info`. Pueden cerrarse con un botón.
- **Tarjetas:** `.card` > `.card-body` > `.card-title`, `.card-text`. También `.card-header` y `.card-footer`.

Los **colores contextuales** significan algo, y es bueno respetarlo:

| Color | Significado |
|---|---|
| `primary` | Acción principal |
| `secondary` | Acción secundaria |
| `success` | Todo salió bien |
| `danger` | Error o peligro |
| `warning` | Atención |
| `info` | Información neutral |

Una tarjeta que ocupa toda la fila no es útil por sí sola; lo común es ponerlas **dentro de un grid**, como aprendiste en el módulo 2: `row row-cols-1 row-cols-md-3 g-4`. Y para que todas midan lo mismo de alto, cada tarjeta lleva `h-100`.

### Pasos

**1. Agrega la sección "Qué hacemos".** Pega justo debajo de `<!-- QUÉ HACEMOS -->`:

```html
<section id="juegos" class="py-5">
  <div class="container">

    <div class="alert alert-info alert-dismissible fade show" role="alert">
      <strong>¡Inscripciones abiertas!</strong> Hay cupos disponibles hasta el 31 de octubre.
      <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Cerrar aviso"></button>
    </div>

    <div class="row justify-content-center my-5">
      <div class="col-lg-7 text-center">
        <h2 class="mb-2">Más que jugar</h2>
        <p class="text-body-secondary mb-0">Tres formas de formar parte del club. Elige la tuya (o prueba las tres).</p>
      </div>
    </div>

    <div class="row row-cols-1 row-cols-md-3 g-4">

      <div class="col">
        <div class="card h-100 card-hover shadow-sm">
          <div class="card-body">
            <span class="badge text-bg-warning mb-3">Cada viernes</span>
            <h3 class="card-title h5">🏆 Torneos</h3>
            <p class="card-text text-body-secondary">Compite en equipo o en solitario en juegos para todos los niveles. Hay premios, diplomas y mucha rivalidad sana.</p>
          </div>
          <div class="card-footer bg-transparent border-0 pb-3">
            <a href="#unete" class="btn btn-outline-primary w-100">Quiero competir</a>
          </div>
        </div>
      </div>

      <div class="col">
        <div class="card h-100 card-hover shadow-sm">
          <div class="card-body">
            <span class="badge text-bg-success mb-3">Cada miércoles</span>
            <h3 class="card-title h5">🕹️ Noches de juego</h3>
            <p class="card-text text-body-secondary">Juegos cooperativos y de mesa, música y snacks. Ideal para conocer gente nueva sin presión.</p>
          </div>
          <div class="card-footer bg-transparent border-0 pb-3">
            <a href="#unete" class="btn btn-outline-primary w-100">Me apunto</a>
          </div>
        </div>
      </div>

      <div class="col">
        <div class="card h-100 card-hover shadow-sm">
          <div class="card-body">
            <span class="badge text-bg-info mb-3">Cada martes</span>
            <h3 class="card-title h5">💻 Taller de creación</h3>
            <p class="card-text text-body-secondary">Aprende a diseñar niveles y personajes, y a programar tu primer videojuego desde cero.</p>
          </div>
          <div class="card-footer bg-transparent border-0 pb-3">
            <a href="#unete" class="btn btn-outline-primary w-100">Quiero crear</a>
          </div>
        </div>
      </div>

    </div>
  </div>
</section>
```

Qué mirar:

- La **alerta** al inicio tiene `alert-dismissible fade show` y un botón `btn-close` con `data-bs-dismiss="alert"`: se cierra con un clic, sin que escribas JS.
- Las tres **tarjetas** usan `h-100` para igualar alturas y `card-footer bg-transparent border-0` para un pie limpio.
- Cada **badge** usa un color distinto según el día.
- Los títulos son `<h3 class="h5">`: semánticamente son un `h3` (porque están debajo de un `h2`), pero se ven con tamaño `h5`. Es un truco muy útil.
- Los botones `w-100` ocupan todo el ancho de su tarjeta.

**2. Agrega el efecto "levitar" al pasar el mouse.** Pega al final de `css/style.css`:

```css
/* ===== 4. Tarjetas ===== */
.card-hover {
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.card-hover:hover {
  transform: translateY(-6px);
  box-shadow: 0 0.75rem 1.5rem rgba(0, 0, 0, 0.25) !important;
}

@media (prefers-reduced-motion: reduce) {
  .card-hover { transition: none; }
  .card-hover:hover { transform: none; }
}
```

El bloque `prefers-reduced-motion` desactiva la animación para quienes tienen activada la opción de "reducir movimiento" en su dispositivo. Es una buena práctica de accesibilidad.

### Resultado esperado

Una alerta azul cerrable, un título centrado y tres tarjetas del mismo alto, con una etiqueta de color, un título con emoji, una descripción y un botón. Al pasar el mouse, cada tarjeta sube un poco. En celular, las tarjetas se apilan.

### Errores comunes

| Síntoma | Causa | Solución |
|---|---|---|
| Las tarjetas tienen alturas distintas | Falta `h-100` en `.card` | Agrégalo a cada `.card` |
| La alerta no se puede cerrar | Falta el bundle JS o `data-bs-dismiss="alert"` | Revisa ambos |
| El texto del badge no se lee | Usaste `bg-warning` sin color de texto | Usa `text-bg-warning` que ya incluye ambos |
| Las tarjetas ocupan todo el ancho | Olvidaste el `row row-cols-*` | Envuélvelas en un grid |
| `btn btn-default` no se ve | No existe en Bootstrap 5 | Usa `btn-secondary` o `btn-outline-secondary` |

### Mini-ejercicio

Agrega una **cuarta tarjeta** llamada "📚 Zona de estudio" con un badge `text-bg-danger` que diga "Antes de exámenes". Haz que en pantallas `lg` se vean las **4 en una fila**, y en `md`, **2 por fila**.

<details>
<summary>💡 Pista</summary>

Duplica una `<div class="col">...</div>` completa, cambia los textos y ajusta `row-cols-md-3` para que además tenga una regla para `lg`.

</details>

<details>
<summary>✅ Solución</summary>

Cambia la fila a `row row-cols-1 row-cols-md-2 row-cols-lg-4 g-4` y agrega la cuarta tarjeta copiando la estructura de una existente (badge `text-bg-danger`, título "📚 Zona de estudio" y su texto).

</details>

### ✅ Punto de control

- [ ] Veo tres tarjetas del mismo alto dentro de un grid.
- [ ] La alerta se cierra con su botón.
- [ ] Entiendo para qué sirven `h-100`, `text-bg-*` y `btn-close`.
- [ ] Sé elegir el color contextual correcto según el mensaje.
- [ ] Las tarjetas se apilan en celular.

---

## Módulo 6: Formularios y validación

⏱ **25 minutos**

🎯 **Objetivo:** construir un formulario de inscripción accesible y validarlo con las herramientas del navegador y Bootstrap.

### Concepto

Bootstrap da estilo a los formularios con pocas clases:

| Clase | Para qué sirve |
|---|---|
| `.form-control` | Campos de texto, correo, número, textarea |
| `.form-select` | Listas desplegables |
| `.form-check` + `.form-check-input` + `.form-check-label` | Casillas y botones de opción |
| `.form-label` | Etiqueta sobre un campo |
| `.form-floating` | Etiqueta que "flota" dentro del campo |
| `.input-group` + `.input-group-text` | Un campo con un texto o ícono pegado (como el `@`) |

#### Cómo funciona la validación

La validación tiene **tres piezas**:

1. **Atributos HTML5** que definen las reglas: `required`, `minlength`, `min`, `max`, `type="email"`, `pattern`. El navegador ya sabe evaluarlos.
2. **JavaScript** que pregunta al navegador si el formulario es válido con `formulario.checkValidity()`.
3. **La clase `.was-validated`** en el `<form>`. Al agregarla, Bootstrap pinta de **verde** los campos válidos y de **rojo** los inválidos, y muestra los mensajes `.invalid-feedback`.

También agregamos `novalidate` al `<form>` para **apagar los globitos feos del navegador** y mostrar los mensajes de Bootstrap en su lugar.

#### Accesibilidad en formularios

Todo campo necesita una `<label>` conectada con el `id` del campo (`for="nombre"` ↔ `id="nombre"`). Sin eso, los lectores de pantalla no saben qué se pide, y hacer clic en la etiqueta no enfoca el campo. En el campo `@` que no tiene etiqueta visible usamos `aria-label`.

### Pasos

**1. Agrega el formulario.** Pega justo debajo de `<!-- ÚNETE -->`:

```html
<section id="unete" class="py-5">
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-lg-7">

        <h2 class="text-center mb-2">Únete a PixelCrew</h2>
        <p class="text-center text-body-secondary mb-4">Completa el formulario y te contamos cuándo es la primera reunión.</p>

        <div id="exito" class="alert alert-success d-none" role="status">
          🎉 ¡Listo! Recibimos tu inscripción. Nos vemos en el siguiente nivel.
        </div>

        <form id="formUnete" class="row g-3" novalidate>

          <div class="col-md-6">
            <div class="form-floating">
              <input type="text" class="form-control" id="nombre" placeholder="Tu nombre" required minlength="2" autocomplete="given-name">
              <label for="nombre">Nombre</label>
              <div class="invalid-feedback">Escribe tu nombre (mínimo 2 letras).</div>
            </div>
          </div>

          <div class="col-md-6">
            <div class="form-floating">
              <input type="email" class="form-control" id="correo" placeholder="tucorreo@ejemplo.com" required autocomplete="email">
              <label for="correo">Correo electrónico</label>
              <div class="invalid-feedback">Escribe un correo válido, por ejemplo nombre@correo.com.</div>
            </div>
          </div>

          <div class="col-md-4">
            <div class="form-floating">
              <input type="number" class="form-control" id="edad" placeholder="16" required min="13" max="18">
              <label for="edad">Edad</label>
              <div class="invalid-feedback">El club es para edades entre 13 y 18 años.</div>
            </div>
          </div>

          <div class="col-md-8">
            <div class="form-floating">
              <select class="form-select" id="interes" required>
                <option value="" selected disabled>Elige una opción…</option>
                <option>Torneos</option>
                <option>Noches de juego</option>
                <option>Taller de creación</option>
                <option>Todo lo anterior</option>
              </select>
              <label for="interes">¿Qué te interesa más?</label>
              <div class="invalid-feedback">Elige una opción de la lista.</div>
            </div>
          </div>

          <div class="col-12">
            <div class="input-group">
              <span class="input-group-text" id="arroba">@</span>
              <input type="text" class="form-control" id="usuario" placeholder="Tu usuario gamer (opcional)" aria-label="Tu usuario gamer (opcional)" aria-describedby="arroba">
            </div>
          </div>

          <div class="col-12">
            <label for="mensaje" class="form-label">Cuéntanos tu juego favorito (opcional)</label>
            <textarea class="form-control" id="mensaje" rows="3"></textarea>
          </div>

          <div class="col-12">
            <div class="form-check">
              <input class="form-check-input" type="checkbox" id="reglas" required>
              <label class="form-check-label" for="reglas">Acepto las reglas del club</label>
              <div class="invalid-feedback">Debes aceptar las reglas para inscribirte.</div>
            </div>
          </div>

          <div class="col-12 d-grid">
            <button class="btn btn-primary btn-lg" type="submit">Enviar inscripción</button>
          </div>

        </form>
      </div>
    </div>
  </div>
</section>
```

Qué observar:

- `row g-3` + `col-md-6`: ¡el grid también sirve para formularios! Dos campos por fila en pantallas medianas, uno por fila en celular.
- El `<select>` tiene una primera opción con `value=""` y `disabled selected`: es el "texto guía". Como está vacía y `required`, obliga a elegir una opción real.
- `edad` usa `min="13" max="18"`: el navegador rechaza valores fuera de rango.
- `d-none` en la alerta de éxito: está oculta hasta que se necesite.
- `d-grid` en el botón: lo estira a todo el ancho.

**2. Agrega el JavaScript.** Pega en `js/main.js`:

```js
// ===== Validación del formulario de inscripción =====
const formulario = document.getElementById('formUnete');
const mensajeExito = document.getElementById('exito');

formulario.addEventListener('submit', (evento) => {
  evento.preventDefault(); // este sitio de práctica no envía datos a ningún servidor

  if (formulario.checkValidity()) {
    formulario.reset();
    formulario.classList.remove('was-validated');
    mensajeExito.classList.remove('d-none');
  } else {
    mensajeExito.classList.add('d-none');
    formulario.classList.add('was-validated');
  }
});
```

Léelo con calma. Es poco código:

- `getElementById` busca los elementos por su `id`.
- `addEventListener('submit', ...)` ejecuta una función cuando se intenta enviar el formulario.
- `evento.preventDefault()` evita que la página se recargue.
- Si es válido: limpia el formulario y muestra el mensaje de éxito. Si no, activa `was-validated`.

**3. Pruébalo así:**

1. Presiona **Enviar inscripción** con todo vacío → campos en rojo con sus mensajes.
2. Escribe un correo mal escrito (`ana@`) → sigue en rojo.
3. Escribe edad `25` → rojo; con `16` → verde.
4. Completa todo correctamente y marca las reglas → aparece el mensaje de éxito.

⚠️ **Sobre datos personales:** este formulario **no guarda ni envía nada**. En un sitio real que recoja datos de menores de edad se necesita permiso de madres, padres o tutores y un manejo cuidadoso de la información. Nunca publiques datos personales de otras personas.

### Resultado esperado

Un formulario centrado con campos de etiqueta flotante. Al enviarlo vacío, todo lo obligatorio se marca en rojo con su mensaje explicativo. Al completarlo bien, el formulario se limpia y aparece una alerta verde.

### Errores comunes

| Síntoma | Causa | Solución |
|---|---|---|
| Aparecen globitos del navegador en vez de los mensajes de Bootstrap | Falta `novalidate` en el `<form>` | Agrégalo |
| Nada se pone rojo ni verde | No se agregó `was-validated` o `main.js` no está enlazado | Revisa la consola (`F12`) por errores y confirma que el script esté al final del `<body>` |
| El mensaje de error nunca aparece | El `.invalid-feedback` no está después del campo, como hermano | Colócalo justo después del `<input>` o del `<label>` |
| Los campos flotantes se ven mal | Falta `placeholder` en el input | Los `form-floating` **requieren** un `placeholder` (aunque sea con una palabra) |
| `Cannot read properties of null` en la consola | El `id` en JS no coincide con el HTML | Compara `formUnete` y `exito` en ambos |
| Usas `form-group` o `form-row` | Son de Bootstrap 4 | En Bootstrap 5: `mb-3` o `row g-3` |

### Mini-ejercicio

Haz que el campo **usuario gamer** (opcional) solo acepte **letras, números y guion bajo, de 3 a 16 caracteres**. Si escriben algo distinto, debe mostrar un mensaje de error. Si lo dejan vacío, debe seguir siendo válido.

<details>
<summary>💡 Pista</summary>

Existe un atributo HTML5 llamado `pattern` que recibe una expresión regular. Para que el mensaje de error se vea bien dentro de un `.input-group`, agrega la clase `has-validation` al grupo y pon el `.invalid-feedback` **dentro** del grupo.

</details>

<details>
<summary>✅ Solución</summary>

```html
<div class="input-group has-validation">
  <span class="input-group-text" id="arroba">@</span>
  <input type="text" class="form-control" id="usuario"
         placeholder="Tu usuario gamer (opcional)"
         aria-label="Tu usuario gamer (opcional)" aria-describedby="arroba"
         pattern="[A-Za-z0-9_]{3,16}">
  <div class="invalid-feedback">Usa de 3 a 16 letras, números o guion bajo.</div>
</div>
```

Un campo vacío sin `required` es válido aunque tenga `pattern`.

</details>

### ✅ Punto de control

- [ ] Mi formulario tiene todos sus campos con etiqueta asociada.
- [ ] Al enviarlo vacío se ven los errores en rojo con mensajes.
- [ ] Al llenarlo bien aparece el mensaje de éxito y se limpia.
- [ ] Entiendo la función de `required`, `novalidate`, `checkValidity()` y `was-validated`.
- [ ] Sé que no debo pedir ni publicar datos personales sin cuidado.

---

## Módulo 7: Componentes interactivos con JavaScript

⏱ **25 minutos**

🎯 **Objetivo:** usar el JavaScript de Bootstrap para crear un acordeón, un carrusel y una ventana modal.

### Concepto

Bootstrap trae su propio JavaScript para los componentes interactivos. Puedes usarlo de **dos maneras**:

| Forma | Cómo | Cuándo |
|---|---|---|
| **Atributos `data-bs-*`** | Solo HTML, sin escribir JS | La mayoría de los casos (lo que usaremos) |
| **API de JavaScript** | `bootstrap.Modal.getOrCreateInstance(...)` | Cuando necesitas abrir o cerrar con tu propia lógica |

Los atributos más importantes:

| Atributo | Significado |
|---|---|
| `data-bs-toggle="modal"` / `"collapse"` | Qué tipo de componente activa este botón |
| `data-bs-target="#id"` | A qué elemento afecta |
| `data-bs-dismiss="modal"` / `"alert"` | Cierra el componente |
| `data-bs-slide="prev"` / `"next"` | Mueve el carrusel |
| `data-bs-parent="#id"` | En un acordeón, hace que solo se abra uno a la vez |

La regla de oro: **los `id` deben coincidir exactamente** entre el botón y el elemento al que apunta, y no pueden repetirse en la página.

### Pasos

**1. Acordeón de preguntas frecuentes.** Pega debajo de `<!-- PREGUNTAS -->`:

```html
<section id="faq" class="py-5">
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-lg-8">
        <h2 class="text-center mb-4">Preguntas frecuentes</h2>

        <div class="accordion" id="acordeonFaq">
          <div class="accordion-item">
            <h3 class="accordion-header">
              <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#faq1" aria-expanded="true" aria-controls="faq1">
                ¿Necesito experiencia para entrar?
              </button>
            </h3>
            <div id="faq1" class="accordion-collapse collapse show" data-bs-parent="#acordeonFaq">
              <div class="accordion-body">Para nada. Hay miembros que juegan desde hace años y otros que nunca han tenido una consola. Te ayudamos a empezar.</div>
            </div>
          </div>
          <div class="accordion-item">
            <h3 class="accordion-header">
              <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#faq2" aria-expanded="false" aria-controls="faq2">
                ¿Cuánto cuesta?
              </button>
            </h3>
            <div id="faq2" class="accordion-collapse collapse" data-bs-parent="#acordeonFaq">
              <div class="accordion-body">Unirte es gratis. Solo pedimos que cuides el material y participes en las actividades.</div>
            </div>
          </div>
          <div class="accordion-item">
            <h3 class="accordion-header">
              <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#faq3" aria-expanded="false" aria-controls="faq3">
                ¿Cuándo nos reunimos?
              </button>
            </h3>
            <div id="faq3" class="accordion-collapse collapse" data-bs-parent="#acordeonFaq">
              <div class="accordion-body">Los martes, miércoles y viernes después de clases. Te enviamos el calendario completo cuando te inscribas.</div>
            </div>
          </div>
          <div class="accordion-item">
            <h3 class="accordion-header">
              <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#faq4" aria-expanded="false" aria-controls="faq4">
                ¿Necesito mi propio equipo?
              </button>
            </h3>
            <div id="faq4" class="accordion-collapse collapse" data-bs-parent="#acordeonFaq">
              <div class="accordion-body">No. El club tiene consolas, computadores y mandos para todos. Si quieres traer el tuyo, ¡bienvenido!</div>
            </div>
          </div>
        </div>

      </div>
    </div>
  </div>
</section>
```

Fíjate en el patrón: cada botón apunta (`data-bs-target="#faq1"`) a su panel (`id="faq1"`). El primer ítem tiene `show` (abierto) y los demás `collapsed` en el botón.

**2. Carrusel de testimonios.** Pega debajo de `<!-- COMUNIDAD -->`:

```html
<section id="testimonios" class="py-5 bg-body-tertiary">
  <div class="container">
    <h2 class="text-center mb-4">Lo que dice la comunidad</h2>

    <div class="row justify-content-center">
      <div class="col-lg-8">

        <div id="carruselComunidad" class="carousel slide" aria-label="Testimonios de miembros del club">

          <div class="carousel-indicators">
            <button type="button" data-bs-target="#carruselComunidad" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Testimonio 1"></button>
            <button type="button" data-bs-target="#carruselComunidad" data-bs-slide-to="1" aria-label="Testimonio 2"></button>
            <button type="button" data-bs-target="#carruselComunidad" data-bs-slide-to="2" aria-label="Testimonio 3"></button>
          </div>

          <div class="carousel-inner rounded-4 shadow">
            <div class="carousel-item active">
              <figure class="testimonio text-white text-center px-5 py-5 mb-0 d-flex flex-column justify-content-center">
                <blockquote class="fs-4 mb-3">“Entré por los torneos y salí sabiendo hacer mi primer videojuego.”</blockquote>
                <figcaption class="fw-semibold">Valentina, 16 años</figcaption>
              </figure>
            </div>
            <div class="carousel-item">
              <figure class="testimonio text-white text-center px-5 py-5 mb-0 d-flex flex-column justify-content-center">
                <blockquote class="fs-4 mb-3">“Aquí conocí a mis mejores amigos. Jugar en equipo es otro nivel.”</blockquote>
                <figcaption class="fw-semibold">Santiago, 17 años</figcaption>
              </figure>
            </div>
            <div class="carousel-item">
              <figure class="testimonio text-white text-center px-5 py-5 mb-0 d-flex flex-column justify-content-center">
                <blockquote class="fs-4 mb-3">“Pensé que era solo jugar, pero también aprendí a organizar eventos.”</blockquote>
                <figcaption class="fw-semibold">Camila, 15 años</figcaption>
              </figure>
            </div>
          </div>

          <button class="carousel-control-prev" type="button" data-bs-target="#carruselComunidad" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Anterior</span>
          </button>
          <button class="carousel-control-next" type="button" data-bs-target="#carruselComunidad" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Siguiente</span>
          </button>

        </div>

        <p class="text-center text-body-secondary small mt-3 mb-0">Los nombres de este ejemplo son ficticios.</p>
      </div>
    </div>
  </div>
</section>
```

El carrusel tiene tres partes: los **indicadores** (puntitos de abajo), las **diapositivas** (`carousel-item`; **una** debe llevar `active`) y los **controles** (flechas). Usamos botones con texto oculto (`visually-hidden`) para que las flechas sean comprensibles con lectores de pantalla. No lo configuramos con avance automático a propósito: el movimiento solo se activa por decisión de quien usa la página.

Agrega estilo a las diapositivas. Pega al final de `css/style.css`:

```css
/* ===== 5. Carrusel de la comunidad ===== */
.testimonio {
  min-height: 280px;
  background: linear-gradient(135deg, #4b2bb5, #0b6fa8);
}

/* En modo oscuro Bootstrap pone controles negros en los carruseles.
   Como nuestras diapositivas son oscuras en ambos modos, los forzamos a blanco. */
.carousel {
  --bs-carousel-indicator-active-bg: #fff;
  --bs-carousel-caption-color: #fff;
  --bs-carousel-control-icon-filter: none;
}
```

**3. Modal de reglas.** Primero pega el modal justo debajo de `<!-- MODAL -->`:

```html
<div class="modal fade" id="modalReglas" tabindex="-1" aria-labelledby="tituloReglas" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
    <div class="modal-content">

      <div class="modal-header">
        <h2 class="modal-title fs-5" id="tituloReglas">📜 Reglas de PixelCrew</h2>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Cerrar"></button>
      </div>

      <div class="modal-body">
        <ol class="mb-0">
          <li class="mb-2"><strong>Respeto ante todo.</strong> Nada de insultos ni burlas, ni dentro ni fuera del juego.</li>
          <li class="mb-2"><strong>Juego limpio.</strong> Sin trampas, hacks ni cuentas prestadas en los torneos.</li>
          <li class="mb-2"><strong>Equilibrio.</strong> Las tareas del colegio van primero; el club puede esperar.</li>
          <li class="mb-2"><strong>Cuidamos el material.</strong> Consolas, mandos y equipos son de todos.</li>
          <li class="mb-2"><strong>Contenido apto.</strong> Los juegos deben ser adecuados para la edad de todos.</li>
          <li><strong>Si algo te incomoda</strong>, avísale a una persona responsable del club. Siempre te vamos a escuchar.</li>
        </ol>
      </div>

      <div class="modal-footer">
        <button type="button" class="btn btn-primary" data-bs-dismiss="modal">Entendido</button>
      </div>

    </div>
  </div>
</div>
```

Luego conecta un botón con él. En el formulario del módulo anterior, **reemplaza** esta línea:

```html
<label class="form-check-label" for="reglas">Acepto las reglas del club</label>
```

por esta, que convierte "reglas del club" en un botón que abre el modal:

```html
<label class="form-check-label" for="reglas">
                Acepto las
                <button type="button" class="btn btn-link p-0 align-baseline" data-bs-toggle="modal" data-bs-target="#modalReglas">reglas del club</button>
              </label>
```

Puntos importantes del modal:

- `fade` da una animación suave al aparecer.
- `modal-dialog-centered` lo centra verticalmente y `modal-dialog-scrollable` permite desplazar el contenido si es largo.
- `aria-labelledby="tituloReglas"` conecta el modal con su título para lectores de pantalla.
- Bootstrap se encarga solo de **atrapar el foco** dentro del modal y de cerrarlo con la tecla `Esc`.
- El modal se coloca al final del `<body>`, **fuera** de cualquier sección, para evitar problemas de posición.

**4. Prueba la API de JavaScript.** Abre la consola (`F12`) y escribe:

```js
const modal = bootstrap.Modal.getOrCreateInstance(document.getElementById('modalReglas'));
modal.show();
```

Se abre el modal desde código. Ciérralo con `modal.hide()`. Cuando una acción (por ejemplo, un temporizador) debe abrir un componente, usarás esta forma.

### Resultado esperado

- **Acordeón:** al abrir una pregunta, la anterior se cierra.
- **Carrusel:** puedes pasar de testimonio con las flechas o los puntitos.
- **Modal:** al hacer clic en "reglas del club" aparece una ventana centrada con el fondo oscurecido; se cierra con ✕, con "Entendido", con `Esc` o haciendo clic afuera.

### Errores comunes

| Síntoma | Causa | Solución |
|---|---|---|
| El carrusel no muestra nada | Ninguna diapositiva tiene `active` | Pon `active` en la primera `carousel-item` |
| Los puntitos no cambian de diapositiva | `data-bs-slide-to` no coincide con el número de diapositivas | Cuéntalas: empiezan en `0` |
| El modal no abre | El `data-bs-target` no coincide con el `id` | Compara `#modalReglas` con `id="modalReglas"` |
| El fondo del modal queda gris y bloqueado | Un error de JS dejó el modal a medias | Recarga y revisa la consola |
| Se abren varias preguntas a la vez | Falta `data-bs-parent` | Agrégalo a cada `accordion-collapse` |
| Dos acordeones se afectan entre sí | Repetiste `id` | Cada `id` debe ser único |

### Mini-ejercicio

1. Haz que el acordeón permita tener **varias preguntas abiertas** a la vez.
2. Haz que el carrusel cambie de diapositiva con un efecto de **desvanecimiento** en vez de deslizamiento.

<details>
<summary>💡 Pista</summary>

Para el 1, piensa qué atributo es el que "cierra a las demás". Para el 2, busca en la documentación oficial de Carousel el modificador `carousel-fade`.

</details>

<details>
<summary>✅ Solución</summary>

1. Quita el atributo `data-bs-parent="#acordeonFaq"` de cada `accordion-collapse`.
2. Cambia `class="carousel slide"` por `class="carousel slide carousel-fade"`.

</details>

### ✅ Punto de control

- [ ] El acordeón abre una pregunta a la vez.
- [ ] El carrusel cambia con las flechas y con los puntitos.
- [ ] El modal abre desde el enlace de las reglas y se cierra de varias maneras.
- [ ] Entiendo qué relación hay entre `data-bs-target` e `id`.
- [ ] Abrí el modal desde la consola con `bootstrap.Modal`.

---

## Módulo 8: Personalización, modo oscuro y Sass

⏱ **20 minutos**

🎯 **Objetivo:** cambiar la apariencia de Bootstrap con tus colores, activar un botón de modo claro/oscuro y entender cuándo conviene usar Sass.

### Concepto

Hasta ahora tu sitio se ve "como Bootstrap". Para que se vea **tuyo** hay tres niveles de personalización, de menor a mayor esfuerzo:

| Nivel | Cómo | Cuándo |
|---|---|---|
| 1. Utilidades | Clases como `bg-primary`, `rounded-4` | Siempre |
| 2. **Variables CSS** | Sobrescribes `--bs-*` en tu `style.css` | Cambios de color, bordes y fuentes |
| 3. **Sass** | Compilas Bootstrap con tus valores | Proyectos grandes con tema propio |

#### Variables CSS

Desde la versión 5.3, Bootstrap guarda sus colores, bordes y fuentes en **variables CSS** (`--bs-primary`, `--bs-body-bg`, `--bs-border-radius`...). Al cambiar una variable, todo lo que la usa cambia. Puedes verlas en las herramientas del navegador: selecciona la etiqueta `<html>` en la pestaña **Elements** y mira el panel **Styles**.

Hay dos tipos:

- **Globales** (en `:root`): afectan a todo el sitio. Ejemplo: `--bs-border-radius`.
- **Locales de un componente**: viven dentro de cada componente. Ejemplo: un botón usa `--bs-btn-bg`. Para cambiar solo los botones primarios, sobrescribes esa variable en `.btn-primary`.

#### Modo claro y oscuro

Bootstrap 5.3 trae **dos temas** integrados. Se elige con el atributo `data-bs-theme` (`light` o `dark`) en `<html>` o en cualquier elemento: el tema se aplica a ese elemento y a todo lo que contiene. Por eso para alternar el modo solo hay que **cambiar un atributo** con JavaScript, y recordarlo con `localStorage`.

### Pasos

**1. Agrega el botón de modo.** En la navbar, pega **después del `<li>` del botón "Únete"** (dentro del mismo `<ul>`):

```html
<li class="nav-item ms-lg-2 mb-2 mb-lg-0">
  <button id="themeToggle" class="btn btn-outline-secondary btn-sm" type="button" aria-label="Cambiar entre modo claro y modo oscuro">
    <span id="themeIcon" aria-hidden="true">☀️</span>
  </button>
</li>
```

**2. Agrega el JavaScript** al final de `js/main.js`:

```js
// ===== Modo claro / oscuro =====
const raiz = document.documentElement;
const botonTema = document.getElementById('themeToggle');
const iconoTema = document.getElementById('themeIcon');

function aplicarTema(tema) {
  raiz.setAttribute('data-bs-theme', tema);
  iconoTema.textContent = tema === 'dark' ? '☀️' : '🌙'; // el icono muestra a qué modo cambiarás
  localStorage.setItem('pc-tema', tema);                 // recuerda la elección
}

// Al cargar: usa el tema guardado o, si no hay, el oscuro
aplicarTema(localStorage.getItem('pc-tema') || 'dark');

botonTema.addEventListener('click', () => {
  const actual = raiz.getAttribute('data-bs-theme');
  aplicarTema(actual === 'dark' ? 'light' : 'dark');
});
```

Qué hace: aplica el tema, cambia el emoji del botón y guarda la preferencia. Al recargar la página, el sitio "recuerda" el modo que elegiste.

**3. Personaliza con variables CSS.** Pega **al inicio** de `css/style.css` (antes de lo que ya escribiste):

```css
/* ===== 1. Variables: personalizamos Bootstrap sin tocar sus archivos ===== */
:root {
  --pc-accent: #7c4dff;

  /* Variables de Bootstrap que sobrescribimos */
  --bs-primary: #7c4dff;
  --bs-primary-rgb: 124, 77, 255;
  --bs-primary-text-emphasis: #4a22b8;
  --bs-primary-bg-subtle: #e9e0ff;
  --bs-primary-border-subtle: #cbb8ff;
  --bs-border-radius: 0.75rem;
}

/* Este bloque va DESPUÉS de :root para ganar en modo oscuro */
[data-bs-theme="dark"] {
  --bs-body-bg: #0e0f1f;
  --bs-body-bg-rgb: 14, 15, 31;
  --bs-tertiary-bg: #161833;
  --bs-tertiary-bg-rgb: 22, 24, 51;
  --bs-primary-text-emphasis: #b8a0ff;
  --bs-primary-bg-subtle: #241a4d;
  --bs-primary-border-subtle: #4a2fa8;
}

/* Los componentes de Bootstrap guardan sus colores en variables LOCALES.
   Las cambiamos para que los botones también usen nuestro morado. */
.btn-primary {
  --bs-btn-bg: var(--pc-accent);
  --bs-btn-border-color: var(--pc-accent);
  --bs-btn-hover-bg: #6a3de8;
  --bs-btn-hover-border-color: #6a3de8;
  --bs-btn-active-bg: #5a30d0;
  --bs-btn-active-border-color: #5a30d0;
  --bs-btn-disabled-bg: var(--pc-accent);
  --bs-btn-disabled-border-color: var(--pc-accent);
  --bs-btn-focus-shadow-rgb: 124, 77, 255;
}

.btn-outline-primary {
  --bs-btn-color: var(--bs-primary-text-emphasis);
  --bs-btn-border-color: var(--pc-accent);
  --bs-btn-hover-color: #fff;
  --bs-btn-hover-bg: var(--pc-accent);
  --bs-btn-hover-border-color: var(--pc-accent);
  --bs-btn-active-color: #fff;
  --bs-btn-active-bg: #5a30d0;
  --bs-btn-active-border-color: #5a30d0;
  --bs-btn-focus-shadow-rgb: 124, 77, 255;
}

.card {
  --bs-card-bg: var(--bs-tertiary-bg);
}
```

```css
/* ===== 2. Ajustes generales ===== */
@media (prefers-reduced-motion: no-preference) {
  html { scroll-behavior: smooth; }
}

/* Evita que la navbar fija tape los títulos al navegar por el menú */
section[id] { scroll-margin-top: 4.5rem; }
```

Observa los dos patrones:

- Variables globales (`--bs-primary`, `--bs-body-bg`...) que definen la paleta, una para el modo claro (`:root`) y otra para el oscuro (`[data-bs-theme="dark"]`).
- Variables locales de componentes (`.btn-primary`, `.btn-outline-primary`) para que los botones también adopten el morado.

⚠️ Cambiar `--bs-primary` **no** cambia el color de `.btn-primary`, porque los botones tienen su propia copia del color. Por eso fue necesario sobrescribir también `--bs-btn-bg` y sus variantes. Si tuvieras que hacer esto con muchos componentes, ahí es donde conviene Sass.

También verás que `section[id] { scroll-margin-top }` resuelve el problema del módulo 4: la navbar fija ya no tapa los títulos al navegar.

**4. Introducción a Sass (lectura, opcional para practicar).**

**Sass** es un lenguaje que se *compila* a CSS. Con Bootstrap te permite cambiar sus **variables internas antes de generar el CSS**, y entonces **toda la paleta** (botones, alertas, fondos suaves, bordes...) se recalcula automáticamente.

El flujo es:

```bash
# 1. Crear un proyecto e instalar Bootstrap y Sass (necesitas Node.js)
npm init -y
npm install bootstrap@5.3.8 sass
```

```scss
// scss/custom.scss
// 2. Tus variables ANTES de importar Bootstrap
$primary: #7c4dff;
$border-radius: 0.75rem;

// 3. Importa Bootstrap
@import "bootstrap/scss/bootstrap";
```

```bash
# 4. Compila a CSS
npx sass --load-path=node_modules scss/custom.scss css/custom.css
```

Luego enlazas `css/custom.css` en lugar del CSS del CDN. Es normal que Sass muestre avisos de *deprecation* sobre `@import`: Bootstrap 5.3 todavía usa esa sintaxis y los avisos no impiden que funcione.

💡 **¿Cuándo usar cada una?** Variables CSS para ajustes rápidos y para cambiar de tema en tiempo real. Sass cuando quieres una identidad visual completa y estás en un proyecto con herramientas de desarrollo.

### Resultado esperado

El sitio tiene una paleta morada. En la barra hay un botón con ☀️ (en modo oscuro) o 🌙 (en modo claro) que cambia todo el sitio. Al recargar, se mantiene el modo elegido. Los botones principales son morados y las esquinas son un poco más redondeadas.

### Errores comunes

| Síntoma | Causa | Solución |
|---|---|---|
| Mis variables no se aplican | `style.css` se carga antes que Bootstrap | Debe ir **después** en el `<head>` |
| El botón de modo no hace nada | `main.js` falló antes | Revisa la consola: un error en el formulario detiene todo el archivo |
| `Cannot read properties of null (reading 'addEventListener')` | El botón no existe en el HTML | Confirma que pegaste el `<li>` con `id="themeToggle"` |
| El modo oscuro no recuerda mi elección | `localStorage` bloqueado por el navegador | Prueba con otro navegador o con Live Server |
| Cambié `--bs-primary` pero los botones siguen azules | Los botones usan variables locales | Sobrescribe también `--bs-btn-bg` en `.btn-primary` |
| En modo oscuro algunos colores no cambian | Pusiste tu bloque oscuro antes que `:root` | `[data-bs-theme="dark"]` debe ir **después** de `:root` |

### Mini-ejercicio

1. Cambia el **radio de las esquinas** de todo el sitio (botones, tarjetas, campos) con **una sola línea**.
2. Cambia la **fuente** del sitio por una de sistema como `Georgia, serif`.

<details>
<summary>💡 Pista</summary>

Mira la lista de variables `--bs-*` en el panel Styles. Hay una variable de radio de borde y otra de familia de fuente del cuerpo (`--bs-body-font-family`).

</details>

<details>
<summary>✅ Solución</summary>

En `:root` de tu `style.css`:

```css
:root {
  --bs-border-radius: 1.25rem;
  --bs-body-font-family: Georgia, serif;
}
```

Si ya tenías `--bs-border-radius` definido en ese bloque, solo cambia su valor.

</details>

### ✅ Punto de control

- [ ] Mi sitio alterna entre modo claro y oscuro con el botón.
- [ ] El modo elegido se mantiene al recargar.
- [ ] Los botones y los colores principales usan mi paleta.
- [ ] Entiendo la diferencia entre variables globales y variables locales de componente.
- [ ] Sé para qué sirve Sass y cuándo conviene usarlo.

---

## Módulo 9: Integración final y buenas prácticas

⏱ **15 minutos**

🎯 **Objetivo:** terminar el sitio con el pie de página y revisarlo como lo haría un profesional: accesibilidad, orden del código y pruebas en distintos tamaños.

### Concepto

Un sitio "terminado" no es el que se ve bien en tu computador, sino el que **funciona para todas las personas y en todos los dispositivos**. Hay tres frentes de revisión: **estructura y accesibilidad**, **responsive** y **calidad del código**.

### Pasos

**1. Agrega el pie de página.** Pega debajo de `<!-- FOOTER -->`:

```html
<footer class="border-top py-4 mt-5">
  <div class="container d-flex flex-column flex-md-row justify-content-between align-items-center gap-3">
    <p class="mb-0 text-body-secondary small">© 2026 PixelCrew · Hecho con Bootstrap 5.3.8</p>

    <ul class="nav">
      <li class="nav-item"><a class="nav-link px-2" href="#juegos">Qué hacemos</a></li>
      <li class="nav-item"><a class="nav-link px-2" href="#faq">Preguntas</a></li>
      <li class="nav-item"><a class="nav-link px-2" href="#unete">Únete</a></li>
    </ul>

    <a href="#inicio" class="btn btn-outline-secondary btn-sm">Volver arriba ↑</a>
  </div>
</footer>
```

Detalles: `flex-column flex-md-row` apila los elementos en celular y los pone en línea desde tablet, y `justify-content-between` los reparte a los extremos. `mt-5` separa el pie del contenido.

**2. Haz la revisión de accesibilidad.** Recorre esta lista con tu sitio abierto:

| Qué revisar | Cómo comprobarlo |
|---|---|
| **Un solo `<h1>`** y títulos en orden (`h1` → `h2` → `h3`) | Busca `<h1` con `Ctrl + F` en el código |
| **Landmarks:** `<header>`, `<nav>`, `<main>`, `<footer>` | Revisa que estén presentes y que no falten |
| **Teclado:** todo se puede usar solo con `Tab`, `Enter` y `Esc` | Deja el mouse quieto y recorre el sitio |
| **Foco visible:** al tabular se ve dónde estás | Bootstrap lo trae; no lo quites con `outline: none` |
| **Textos alternativos:** imágenes con `alt` o `role="img"` + `aria-label` | Revisa las de la galería |
| **Etiquetas en formularios:** todo campo tiene su `<label>` | Haz clic en una etiqueta: debe enfocar su campo |
| **Contraste de colores:** texto legible sobre su fondo | Usa [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/) |
| **Movimiento:** nada se mueve solo; se respeta `prefers-reduced-motion` | Ya lo hicimos en el CSS |
| **Enlace "Saltar al contenido"** | Presiona `Tab` al cargar |

**3. Prueba el diseño responsive.** En las herramientas del navegador, comprueba estos anchos: **375 px** (celular), **768 px** (tablet), **1280 px** (laptop). En cada uno confirma que: no hay scroll horizontal, nada se corta, los botones se pueden tocar con facilidad y los textos se leen sin hacer zoom.

**4. Haz una auditoría automática.** En Chrome o Edge: `F12` → pestaña **Lighthouse** → marca *Accessibility* y *Best Practices* → **Analyze page load**. Lee las sugerencias. No necesitas 100 puntos, pero entender cada aviso te enseña mucho.

**5. Valida tu HTML** pegándolo en el [validador del W3C](https://validator.w3.org/#validate_by_input). Corrige lo que marque como error.

### Buenas prácticas para tus propios proyectos

- **Usa utilidades primero**, y CSS propio solo cuando no exista una utilidad.
- **No modifiques los archivos de Bootstrap.** Siempre sobrescribe en tu propio CSS.
- **Evita `!important`.** Si lo necesitas mucho, tu CSS está mal ordenado o es muy débil.
- **Mantén el orden:** primero el CSS de Bootstrap, luego el tuyo; primero el JS de Bootstrap, luego el tuyo.
- **Usa HTML semántico** (`<section>`, `<nav>`, `<footer>`) y no solo `<div>`.
- **Piensa primero en el celular** y luego agrega `md`, `lg`, etc.
- **Nombra tus clases propias con sentido** (`.hero-card`, `.text-gradient`).
- **Un `id` solo una vez** por página.
- **Consulta la documentación** de cada componente: cada una trae el HTML mínimo y las variantes.

### Resultado esperado

El sitio completo: navbar, hero, estadísticas, tarjetas, galería, carrusel, acordeón, formulario, modal y pie de página, con modo claro y oscuro. Sin errores en la consola.

### Errores comunes

| Síntoma | Causa | Solución |
|---|---|---|
| Hay scroll horizontal en celular | Un elemento más ancho que la pantalla | Con `F12`, selecciona elementos hasta encontrar al culpable; revisa `container` y `row` |
| El pie queda a mitad de pantalla en páginas cortas | Poco contenido | Es normal en este sitio; para pegarlo abajo puedes usar `d-flex flex-column min-vh-100` en el `<body>` |
| Lighthouse reporta bajo contraste | Texto gris sobre fondo oscuro | Usa `text-body-secondary` o aclara el color |
| Los `id` están duplicados | Copiaste bloques sin cambiarlos | Cámbialos y actualiza sus referencias |

### Mini-ejercicio

Ejecuta Lighthouse en modo **claro** y en modo **oscuro**. Escribe el número de accesibilidad de cada uno y elige **un** aviso para corregir.

<details>
<summary>💡 Pista</summary>

Cambia de modo con el botón de la navbar y vuelve a analizar. Para entender un aviso, haz clic sobre él: Lighthouse te muestra el elemento y un enlace con la explicación.

</details>

### ✅ Punto de control

- [ ] El pie de página está agregado y se ve bien en celular y escritorio.
- [ ] Recorrí todo el sitio usando solo el teclado.
- [ ] Probé el sitio en 375, 768 y 1280 px sin scroll horizontal.
- [ ] Ejecuté Lighthouse y leí sus sugerencias.
- [ ] La consola del navegador no muestra errores.

---

## Módulo 10: Tu reto final y siguientes pasos

⏱ **10 minutos** de planificación y primer paso. *El reto completo te tomará entre 30 y 60 minutos adicionales a tu ritmo.*

🎯 **Objetivo:** pasar de "seguir instrucciones" a "tomar decisiones". Aquí no hay código para copiar.

### Reto 1: amplía PixelCrew

Agrega una nueva sección **"Calendario de torneos"** a tu sitio, **sin copiar código del tutorial**. Debe cumplir:

- [ ] Estar entre las secciones "Galería" y "Comunidad", con su enlace en la navbar.
- [ ] Usar **al menos 3 componentes** que no hayas usado en el sitio. Opciones: **tabla** (`table`, `table-striped`) dentro de `table-responsive`, **pestañas** (`nav-tabs` con `tab-content`), **lista de grupo** (`list-group`), **barra de progreso** (`progress`), **tooltip** o **toast**.
- [ ] Verse bien en 375, 768 y 1280 px.
- [ ] Funcionar en modo claro y oscuro.
- [ ] Respetar las reglas de accesibilidad del módulo 9.

💡 Busca cada componente en la documentación oficial: copia su HTML mínimo y adáptalo. Leer la documentación y adaptar ejemplos es **exactamente** cómo trabajan los profesionales.

### Reto 2: tu propio proyecto

Elige algo que te importe y que quieras construir. Ideas:

| Idea | Secciones sugeridas |
|---|---|
| Portafolio personal | Presentación, proyectos (tarjetas), contacto |
| Sitio de tu banda o equipo | Integrantes, próximos eventos, galería |
| Página de un evento del colegio | Programa, ubicación, inscripción |
| Mini tienda de un emprendimiento | Productos (tarjetas), preguntas, contacto |
| Fan site de un hobby (anime, deportes, música) | Noticias, galería, comunidad |

**Plan de 10 minutos (haz esto ahora):**

1. **Dibuja en papel** cómo se vería en celular: bloques de arriba hacia abajo.
2. **Lista las secciones** y al lado escribe qué componente de Bootstrap usarías para cada una (usa la tabla de abajo).
3. **Crea el esqueleto**: copia la plantilla del módulo 1, cambia el título y deja los marcadores.
4. **Construye la primera sección** y pruébala en el celular (modo responsive) antes de seguir.

**¿Qué componente uso para...?**

| Necesito... | Uso... |
|---|---|
| Menú de navegación | `navbar` |
| Un bloque de portada | `container` + utilidades (como el hero) |
| Mostrar productos, personas o proyectos | `card` dentro de un grid |
| Mostrar varias fotos en fila | `row-cols-*` + `ratio` o `card` |
| Preguntas y respuestas | `accordion` |
| Información que aparece sobre la página | `modal` u `offcanvas` |
| Mensajes de aviso | `alert` o `toast` |
| Datos ordenados | `table` dentro de `table-responsive` |
| Cambiar entre contenidos en el mismo espacio | `nav-tabs` o `nav-pills` |
| Recoger datos del usuario | `form` + validación |

### Siguientes pasos

Cuando te sientas cómodo/a con Bootstrap, estas son las rutas naturales para crecer:

1. **Íconos:** [Bootstrap Icons](https://icons.getbootstrap.com/) (más de 2000 íconos gratis).
2. **JavaScript:** aprende lo básico del lenguaje para dar más vida a tus sitios (el módulo 6 y el 8 te dieron una probada).
3. **Git y GitHub:** guarda tu código y publica tu sitio gratis con *GitHub Pages*.
4. **Herramientas modernas:** npm, Sass y un empaquetador como Vite.
5. **Otras ideas de diseño:** estudia las [plantillas de ejemplo de Bootstrap](https://getbootstrap.com/docs/5.3/examples/) para ver cómo se combinan los componentes.

---

## Código completo del proyecto

Compara tu trabajo con la versión final. Si algo falla, busca la diferencia con tu archivo.

### `index.html`

```html
<!DOCTYPE html>
<html lang="es" data-bs-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="PixelCrew: el club de videojuegos de tu colegio. Torneos, noches de juego y talleres.">
  <title>PixelCrew | Club de videojuegos</title>

  <!-- Bootstrap 5.3.8 (CSS) -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">

  <!-- Tu CSS (siempre DESPUÉS de Bootstrap) -->
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <!-- NAVBAR -->
  <a class="visually-hidden-focusable" href="#contenido">Saltar al contenido</a>

  <header>
    <nav class="navbar navbar-expand-lg bg-body-tertiary border-bottom sticky-top" aria-label="Navegación principal">
      <div class="container">
        <a class="navbar-brand fw-bold" href="#inicio">🎮 PixelCrew</a>

        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#menuPrincipal" aria-controls="menuPrincipal" aria-expanded="false" aria-label="Abrir o cerrar el menú">
          <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="menuPrincipal">
          <ul class="navbar-nav ms-auto mb-2 mb-lg-0 align-items-lg-center">
            <li class="nav-item"><a class="nav-link" href="#juegos">Qué hacemos</a></li>
            <li class="nav-item"><a class="nav-link" href="#galeria">Galería</a></li>
            <li class="nav-item"><a class="nav-link" href="#testimonios">Comunidad</a></li>
            <li class="nav-item"><a class="nav-link" href="#faq">Preguntas</a></li>
            <li class="nav-item ms-lg-3 my-2 my-lg-0"><a class="btn btn-primary btn-sm" href="#unete">Únete</a></li>
            <li class="nav-item ms-lg-2 mb-2 mb-lg-0">
              <button id="themeToggle" class="btn btn-outline-secondary btn-sm" type="button" aria-label="Cambiar entre modo claro y modo oscuro">
                <span id="themeIcon" aria-hidden="true">☀️</span>
              </button>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>

  <main id="contenido">
    <!-- HERO -->
    <section id="inicio" class="hero py-5">
      <div class="container py-lg-5">
        <div class="row align-items-center g-5">

          <div class="col-lg-7">
            <p class="text-uppercase fw-semibold text-primary-emphasis small mb-2">Club de videojuegos del colegio</p>
            <h1 class="display-3 fw-bold mb-3">Juega, crea y compite con <span class="text-gradient">PixelCrew</span></h1>
            <p class="lead text-body-secondary mb-4">
              Somos el club donde los videojuegos se juegan, se estudian y hasta se programan.
              Si tienes entre 14 y 18 años, hay un lugar para ti en el equipo.
            </p>
            <div class="d-flex flex-column flex-sm-row gap-3">
              <a href="#unete" class="btn btn-primary btn-lg px-4">Únete al club</a>
              <a href="#juegos" class="btn btn-outline-secondary btn-lg px-4">Descubre qué hacemos</a>
            </div>
          </div>

          <div class="col-lg-5 d-none d-lg-block">
            <div class="hero-card rounded-4 shadow-lg p-5 text-center text-white" aria-hidden="true">
              <div class="display-1">🎮</div>
              <p class="fs-4 fw-semibold mb-0">Nivel 1: ¡empieza hoy!</p>
            </div>
          </div>

        </div>
      </div>
    </section>
    <!-- ESTADÍSTICAS -->
    <section class="py-4 border-top border-bottom bg-body-tertiary" aria-label="El club en números">
      <div class="container">
        <div class="row g-3 text-center">
          <div class="col-6 col-md-3">
            <p class="display-6 fw-bold text-primary-emphasis mb-0">120+</p>
            <p class="text-body-secondary mb-0">miembros</p>
          </div>
          <div class="col-6 col-md-3">
            <p class="display-6 fw-bold text-primary-emphasis mb-0">12</p>
            <p class="text-body-secondary mb-0">torneos al año</p>
          </div>
          <div class="col-6 col-md-3">
            <p class="display-6 fw-bold text-primary-emphasis mb-0">3</p>
            <p class="text-body-secondary mb-0">talleres semanales</p>
          </div>
          <div class="col-6 col-md-3">
            <p class="display-6 fw-bold text-primary-emphasis mb-0">1</p>
            <p class="text-body-secondary mb-0">sala gamer</p>
          </div>
        </div>
      </div>
    </section>
    <!-- QUÉ HACEMOS -->
    <section id="juegos" class="py-5">
      <div class="container">

        <div class="alert alert-info alert-dismissible fade show" role="alert">
          <strong>¡Inscripciones abiertas!</strong> Hay cupos disponibles hasta el 31 de octubre.
          <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Cerrar aviso"></button>
        </div>

        <div class="row justify-content-center my-5">
          <div class="col-lg-7 text-center">
            <h2 class="mb-2">Más que jugar</h2>
            <p class="text-body-secondary mb-0">Tres formas de formar parte del club. Elige la tuya (o prueba las tres).</p>
          </div>
        </div>

        <div class="row row-cols-1 row-cols-md-3 g-4">

          <div class="col">
            <div class="card h-100 card-hover shadow-sm">
              <div class="card-body">
                <span class="badge text-bg-warning mb-3">Cada viernes</span>
                <h3 class="card-title h5">🏆 Torneos</h3>
                <p class="card-text text-body-secondary">Compite en equipo o en solitario en juegos para todos los niveles. Hay premios, diplomas y mucha rivalidad sana.</p>
              </div>
              <div class="card-footer bg-transparent border-0 pb-3">
                <a href="#unete" class="btn btn-outline-primary w-100">Quiero competir</a>
              </div>
            </div>
          </div>

          <div class="col">
            <div class="card h-100 card-hover shadow-sm">
              <div class="card-body">
                <span class="badge text-bg-success mb-3">Cada miércoles</span>
                <h3 class="card-title h5">🕹️ Noches de juego</h3>
                <p class="card-text text-body-secondary">Juegos cooperativos y de mesa, música y snacks. Ideal para conocer gente nueva sin presión.</p>
              </div>
              <div class="card-footer bg-transparent border-0 pb-3">
                <a href="#unete" class="btn btn-outline-primary w-100">Me apunto</a>
              </div>
            </div>
          </div>

          <div class="col">
            <div class="card h-100 card-hover shadow-sm">
              <div class="card-body">
                <span class="badge text-bg-info mb-3">Cada martes</span>
                <h3 class="card-title h5">💻 Taller de creación</h3>
                <p class="card-text text-body-secondary">Aprende a diseñar niveles y personajes, y a programar tu primer videojuego desde cero.</p>
              </div>
              <div class="card-footer bg-transparent border-0 pb-3">
                <a href="#unete" class="btn btn-outline-primary w-100">Quiero crear</a>
              </div>
            </div>
          </div>

        </div>
      </div>
    </section>
    <!-- GALERÍA -->
    <section id="galeria" class="py-5">
      <div class="container">
        <h2 class="text-center mb-2">Momentos del club</h2>
        <p class="text-center text-body-secondary mb-4">Un vistazo a lo que pasa en las reuniones. (Aquí irían tus fotos reales.)</p>

        <div class="row row-cols-2 row-cols-md-3 row-cols-lg-6 g-3">
          <div class="col">
            <div class="ratio ratio-1x1">
              <div class="rounded-4 bg-primary d-flex align-items-center justify-content-center fs-1" role="img" aria-label="Ilustración de un trofeo">🏆</div>
            </div>
          </div>
          <div class="col">
            <div class="ratio ratio-1x1">
              <div class="rounded-4 bg-success d-flex align-items-center justify-content-center fs-1" role="img" aria-label="Ilustración de un joystick">🕹️</div>
            </div>
          </div>
          <div class="col">
            <div class="ratio ratio-1x1">
              <div class="rounded-4 bg-danger d-flex align-items-center justify-content-center fs-1" role="img" aria-label="Ilustración de unos audífonos">🎧</div>
            </div>
          </div>
          <div class="col">
            <div class="ratio ratio-1x1">
              <div class="rounded-4 bg-warning d-flex align-items-center justify-content-center fs-1" role="img" aria-label="Ilustración de un computador">💻</div>
            </div>
          </div>
          <div class="col">
            <div class="ratio ratio-1x1">
              <div class="rounded-4 bg-info d-flex align-items-center justify-content-center fs-1" role="img" aria-label="Ilustración de un dado">🎲</div>
            </div>
          </div>
          <div class="col">
            <div class="ratio ratio-1x1">
              <div class="rounded-4 bg-secondary d-flex align-items-center justify-content-center fs-1" role="img" aria-label="Ilustración de un apretón de manos">🤝</div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <!-- COMUNIDAD -->
    <section id="testimonios" class="py-5 bg-body-tertiary">
      <div class="container">
        <h2 class="text-center mb-4">Lo que dice la comunidad</h2>

        <div class="row justify-content-center">
          <div class="col-lg-8">

            <div id="carruselComunidad" class="carousel slide" aria-label="Testimonios de miembros del club">

              <div class="carousel-indicators">
                <button type="button" data-bs-target="#carruselComunidad" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Testimonio 1"></button>
                <button type="button" data-bs-target="#carruselComunidad" data-bs-slide-to="1" aria-label="Testimonio 2"></button>
                <button type="button" data-bs-target="#carruselComunidad" data-bs-slide-to="2" aria-label="Testimonio 3"></button>
              </div>

              <div class="carousel-inner rounded-4 shadow">
                <div class="carousel-item active">
                  <figure class="testimonio text-white text-center px-5 py-5 mb-0 d-flex flex-column justify-content-center">
                    <blockquote class="fs-4 mb-3">“Entré por los torneos y salí sabiendo hacer mi primer videojuego.”</blockquote>
                    <figcaption class="fw-semibold">Valentina, 16 años</figcaption>
                  </figure>
                </div>
                <div class="carousel-item">
                  <figure class="testimonio text-white text-center px-5 py-5 mb-0 d-flex flex-column justify-content-center">
                    <blockquote class="fs-4 mb-3">“Aquí conocí a mis mejores amigos. Jugar en equipo es otro nivel.”</blockquote>
                    <figcaption class="fw-semibold">Santiago, 17 años</figcaption>
                  </figure>
                </div>
                <div class="carousel-item">
                  <figure class="testimonio text-white text-center px-5 py-5 mb-0 d-flex flex-column justify-content-center">
                    <blockquote class="fs-4 mb-3">“Pensé que era solo jugar, pero también aprendí a organizar eventos.”</blockquote>
                    <figcaption class="fw-semibold">Camila, 15 años</figcaption>
                  </figure>
                </div>
              </div>

              <button class="carousel-control-prev" type="button" data-bs-target="#carruselComunidad" data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Anterior</span>
              </button>
              <button class="carousel-control-next" type="button" data-bs-target="#carruselComunidad" data-bs-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Siguiente</span>
              </button>

            </div>

            <p class="text-center text-body-secondary small mt-3 mb-0">Los nombres de este ejemplo son ficticios.</p>
          </div>
        </div>
      </div>
    </section>
    <!-- PREGUNTAS -->
    <section id="faq" class="py-5">
      <div class="container">
        <div class="row justify-content-center">
          <div class="col-lg-8">
            <h2 class="text-center mb-4">Preguntas frecuentes</h2>

            <div class="accordion" id="acordeonFaq">
              <div class="accordion-item">
                <h3 class="accordion-header">
                  <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#faq1" aria-expanded="true" aria-controls="faq1">
                    ¿Necesito experiencia para entrar?
                  </button>
                </h3>
                <div id="faq1" class="accordion-collapse collapse show" data-bs-parent="#acordeonFaq">
                  <div class="accordion-body">Para nada. Hay miembros que juegan desde hace años y otros que nunca han tenido una consola. Te ayudamos a empezar.</div>
                </div>
              </div>
              <div class="accordion-item">
                <h3 class="accordion-header">
                  <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#faq2" aria-expanded="false" aria-controls="faq2">
                    ¿Cuánto cuesta?
                  </button>
                </h3>
                <div id="faq2" class="accordion-collapse collapse" data-bs-parent="#acordeonFaq">
                  <div class="accordion-body">Unirte es gratis. Solo pedimos que cuides el material y participes en las actividades.</div>
                </div>
              </div>
              <div class="accordion-item">
                <h3 class="accordion-header">
                  <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#faq3" aria-expanded="false" aria-controls="faq3">
                    ¿Cuándo nos reunimos?
                  </button>
                </h3>
                <div id="faq3" class="accordion-collapse collapse" data-bs-parent="#acordeonFaq">
                  <div class="accordion-body">Los martes, miércoles y viernes después de clases. Te enviamos el calendario completo cuando te inscribas.</div>
                </div>
              </div>
              <div class="accordion-item">
                <h3 class="accordion-header">
                  <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#faq4" aria-expanded="false" aria-controls="faq4">
                    ¿Necesito mi propio equipo?
                  </button>
                </h3>
                <div id="faq4" class="accordion-collapse collapse" data-bs-parent="#acordeonFaq">
                  <div class="accordion-body">No. El club tiene consolas, computadores y mandos para todos. Si quieres traer el tuyo, ¡bienvenido!</div>
                </div>
              </div>
            </div>

          </div>
        </div>
      </div>
    </section>
    <!-- ÚNETE -->
    <section id="unete" class="py-5">
      <div class="container">
        <div class="row justify-content-center">
          <div class="col-lg-7">

            <h2 class="text-center mb-2">Únete a PixelCrew</h2>
            <p class="text-center text-body-secondary mb-4">Completa el formulario y te contamos cuándo es la primera reunión.</p>

            <div id="exito" class="alert alert-success d-none" role="status">
              🎉 ¡Listo! Recibimos tu inscripción. Nos vemos en el siguiente nivel.
            </div>

            <form id="formUnete" class="row g-3" novalidate>

              <div class="col-md-6">
                <div class="form-floating">
                  <input type="text" class="form-control" id="nombre" placeholder="Tu nombre" required minlength="2" autocomplete="given-name">
                  <label for="nombre">Nombre</label>
                  <div class="invalid-feedback">Escribe tu nombre (mínimo 2 letras).</div>
                </div>
              </div>

              <div class="col-md-6">
                <div class="form-floating">
                  <input type="email" class="form-control" id="correo" placeholder="tucorreo@ejemplo.com" required autocomplete="email">
                  <label for="correo">Correo electrónico</label>
                  <div class="invalid-feedback">Escribe un correo válido, por ejemplo nombre@correo.com.</div>
                </div>
              </div>

              <div class="col-md-4">
                <div class="form-floating">
                  <input type="number" class="form-control" id="edad" placeholder="16" required min="13" max="18">
                  <label for="edad">Edad</label>
                  <div class="invalid-feedback">El club es para edades entre 13 y 18 años.</div>
                </div>
              </div>

              <div class="col-md-8">
                <div class="form-floating">
                  <select class="form-select" id="interes" required>
                    <option value="" selected disabled>Elige una opción…</option>
                    <option>Torneos</option>
                    <option>Noches de juego</option>
                    <option>Taller de creación</option>
                    <option>Todo lo anterior</option>
                  </select>
                  <label for="interes">¿Qué te interesa más?</label>
                  <div class="invalid-feedback">Elige una opción de la lista.</div>
                </div>
              </div>

              <div class="col-12">
                <div class="input-group">
                  <span class="input-group-text" id="arroba">@</span>
                  <input type="text" class="form-control" id="usuario" placeholder="Tu usuario gamer (opcional)" aria-label="Tu usuario gamer (opcional)" aria-describedby="arroba">
                </div>
              </div>

              <div class="col-12">
                <label for="mensaje" class="form-label">Cuéntanos tu juego favorito (opcional)</label>
                <textarea class="form-control" id="mensaje" rows="3"></textarea>
              </div>

              <div class="col-12">
                <div class="form-check">
                  <input class="form-check-input" type="checkbox" id="reglas" required>
                  <label class="form-check-label" for="reglas">
                    Acepto las
                    <button type="button" class="btn btn-link p-0 align-baseline" data-bs-toggle="modal" data-bs-target="#modalReglas">reglas del club</button>
                  </label>
                  <div class="invalid-feedback">Debes aceptar las reglas para inscribirte.</div>
                </div>
              </div>

              <div class="col-12 d-grid">
                <button class="btn btn-primary btn-lg" type="submit">Enviar inscripción</button>
              </div>

            </form>
          </div>
        </div>
      </div>
    </section>
  </main>

  <!-- FOOTER -->
  <footer class="border-top py-4 mt-5">
    <div class="container d-flex flex-column flex-md-row justify-content-between align-items-center gap-3">
      <p class="mb-0 text-body-secondary small">© 2026 PixelCrew · Hecho con Bootstrap 5.3.8</p>

      <ul class="nav">
        <li class="nav-item"><a class="nav-link px-2" href="#juegos">Qué hacemos</a></li>
        <li class="nav-item"><a class="nav-link px-2" href="#faq">Preguntas</a></li>
        <li class="nav-item"><a class="nav-link px-2" href="#unete">Únete</a></li>
      </ul>

      <a href="#inicio" class="btn btn-outline-secondary btn-sm">Volver arriba ↑</a>
    </div>
  </footer>

  <!-- MODAL -->
  <div class="modal fade" id="modalReglas" tabindex="-1" aria-labelledby="tituloReglas" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
      <div class="modal-content">

        <div class="modal-header">
          <h2 class="modal-title fs-5" id="tituloReglas">📜 Reglas de PixelCrew</h2>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Cerrar"></button>
        </div>

        <div class="modal-body">
          <ol class="mb-0">
            <li class="mb-2"><strong>Respeto ante todo.</strong> Nada de insultos ni burlas, ni dentro ni fuera del juego.</li>
            <li class="mb-2"><strong>Juego limpio.</strong> Sin trampas, hacks ni cuentas prestadas en los torneos.</li>
            <li class="mb-2"><strong>Equilibrio.</strong> Las tareas del colegio van primero; el club puede esperar.</li>
            <li class="mb-2"><strong>Cuidamos el material.</strong> Consolas, mandos y equipos son de todos.</li>
            <li class="mb-2"><strong>Contenido apto.</strong> Los juegos deben ser adecuados para la edad de todos.</li>
            <li><strong>Si algo te incomoda</strong>, avísale a una persona responsable del club. Siempre te vamos a escuchar.</li>
          </ol>
        </div>

        <div class="modal-footer">
          <button type="button" class="btn btn-primary" data-bs-dismiss="modal">Entendido</button>
        </div>

      </div>
    </div>
  </div>

  <!-- Bootstrap 5.3.8 (JS con Popper incluido) -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js" integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI" crossorigin="anonymous"></script>

  <!-- Tu JavaScript (después de Bootstrap) -->
  <script src="js/main.js"></script>
</body>
</html>
```

### `css/style.css`

```css
/* ===== 1. Variables: personalizamos Bootstrap sin tocar sus archivos ===== */
:root {
  --pc-accent: #7c4dff;

  /* Variables de Bootstrap que sobrescribimos */
  --bs-primary: #7c4dff;
  --bs-primary-rgb: 124, 77, 255;
  --bs-primary-text-emphasis: #4a22b8;
  --bs-primary-bg-subtle: #e9e0ff;
  --bs-primary-border-subtle: #cbb8ff;
  --bs-border-radius: 0.75rem;
}

/* Este bloque va DESPUÉS de :root para ganar en modo oscuro */
[data-bs-theme="dark"] {
  --bs-body-bg: #0e0f1f;
  --bs-body-bg-rgb: 14, 15, 31;
  --bs-tertiary-bg: #161833;
  --bs-tertiary-bg-rgb: 22, 24, 51;
  --bs-primary-text-emphasis: #b8a0ff;
  --bs-primary-bg-subtle: #241a4d;
  --bs-primary-border-subtle: #4a2fa8;
}

/* Los componentes de Bootstrap guardan sus colores en variables LOCALES.
   Las cambiamos para que los botones también usen nuestro morado. */
.btn-primary {
  --bs-btn-bg: var(--pc-accent);
  --bs-btn-border-color: var(--pc-accent);
  --bs-btn-hover-bg: #6a3de8;
  --bs-btn-hover-border-color: #6a3de8;
  --bs-btn-active-bg: #5a30d0;
  --bs-btn-active-border-color: #5a30d0;
  --bs-btn-disabled-bg: var(--pc-accent);
  --bs-btn-disabled-border-color: var(--pc-accent);
  --bs-btn-focus-shadow-rgb: 124, 77, 255;
}

.btn-outline-primary {
  --bs-btn-color: var(--bs-primary-text-emphasis);
  --bs-btn-border-color: var(--pc-accent);
  --bs-btn-hover-color: #fff;
  --bs-btn-hover-bg: var(--pc-accent);
  --bs-btn-hover-border-color: var(--pc-accent);
  --bs-btn-active-color: #fff;
  --bs-btn-active-bg: #5a30d0;
  --bs-btn-active-border-color: #5a30d0;
  --bs-btn-focus-shadow-rgb: 124, 77, 255;
}

.card {
  --bs-card-bg: var(--bs-tertiary-bg);
}

/* ===== 2. Ajustes generales ===== */
@media (prefers-reduced-motion: no-preference) {
  html { scroll-behavior: smooth; }
}

/* Evita que la navbar fija tape los títulos al navegar por el menú */
section[id] { scroll-margin-top: 4.5rem; }

/* ===== 3. Hero ===== */
.hero {
  background:
    radial-gradient(circle at 15% 20%, rgba(124, 77, 255, 0.25), transparent 45%),
    radial-gradient(circle at 85% 80%, rgba(13, 139, 217, 0.18), transparent 45%);
}

.text-gradient {
  background: linear-gradient(90deg, #7c4dff, #0d8bd9);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

.hero-card {
  background: linear-gradient(135deg, #7c4dff, #0d8bd9);
}

/* ===== 4. Tarjetas ===== */
.card-hover {
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.card-hover:hover {
  transform: translateY(-6px);
  box-shadow: 0 0.75rem 1.5rem rgba(0, 0, 0, 0.25) !important;
}

@media (prefers-reduced-motion: reduce) {
  .card-hover { transition: none; }
  .card-hover:hover { transform: none; }
}

/* ===== 5. Carrusel de la comunidad ===== */
.testimonio {
  min-height: 280px;
  background: linear-gradient(135deg, #4b2bb5, #0b6fa8);
}

/* En modo oscuro Bootstrap pone controles negros en los carruseles.
   Como nuestras diapositivas son oscuras en ambos modos, los forzamos a blanco. */
.carousel {
  --bs-carousel-indicator-active-bg: #fff;
  --bs-carousel-caption-color: #fff;
  --bs-carousel-control-icon-filter: none;
}
```

### `js/main.js`

```js
// ===== Validación del formulario de inscripción =====
const formulario = document.getElementById('formUnete');
const mensajeExito = document.getElementById('exito');

formulario.addEventListener('submit', (evento) => {
  evento.preventDefault(); // este sitio de práctica no envía datos a ningún servidor

  if (formulario.checkValidity()) {
    formulario.reset();
    formulario.classList.remove('was-validated');
    mensajeExito.classList.remove('d-none');
  } else {
    mensajeExito.classList.add('d-none');
    formulario.classList.add('was-validated');
  }
});

// ===== Modo claro / oscuro =====
const raiz = document.documentElement;
const botonTema = document.getElementById('themeToggle');
const iconoTema = document.getElementById('themeIcon');

function aplicarTema(tema) {
  raiz.setAttribute('data-bs-theme', tema);
  iconoTema.textContent = tema === 'dark' ? '☀️' : '🌙'; // el icono muestra a qué modo cambiarás
  localStorage.setItem('pc-tema', tema);                 // recuerda la elección
}

// Al cargar: usa el tema guardado o, si no hay, el oscuro
aplicarTema(localStorage.getItem('pc-tema') || 'dark');

botonTema.addEventListener('click', () => {
  const actual = raiz.getAttribute('data-bs-theme');
  aplicarTema(actual === 'dark' ? 'light' : 'dark');
});
```

---

## Hoja de referencia rápida

### Grid y contenedores

| Clase | Efecto |
|---|---|
| `container`, `container-fluid`, `container-lg` | Contenedor centrado / a todo el ancho / fluido hasta `lg` |
| `row` | Fila |
| `col`, `col-6`, `col-md-4`, `col-lg-auto` | Columna: igual reparto / 6 de 12 / 4 desde `md` / según contenido |
| `row-cols-1`, `row-cols-md-3` | Cuántas columnas por fila |
| `g-3`, `gx-2`, `gy-4` | Separación entre columnas |
| `offset-md-2` | Deja espacio vacío a la izquierda |

### Espaciado

| Clase | Efecto |
|---|---|
| `m-*`, `p-*` | Margen / relleno (0–5, `auto`) |
| `mt-*`, `mb-*`, `ms-*`, `me-*` | Arriba, abajo, inicio, final |
| `mx-*`, `my-*`, `px-*`, `py-*` | Horizontal / vertical |
| `gap-*` | Separación entre elementos en flex o grid |

### Texto y color

| Clase | Efecto |
|---|---|
| `display-1`…`display-6`, `h1`…`h6`, `lead`, `small` | Tamaños de texto |
| `fs-1`…`fs-6` | Tamaño de fuente |
| `fw-bold`, `fw-semibold`, `fw-normal`, `fst-italic` | Peso y estilo |
| `text-start`, `text-center`, `text-end` | Alineación |
| `text-uppercase`, `text-truncate` | Transformación del texto |
| `text-primary`, `text-body-secondary`, `text-white` | Color de texto |
| `bg-primary`, `bg-body-tertiary`, `bg-success-subtle` | Color de fondo |
| `text-bg-primary` | Fondo y texto con buen contraste a la vez |

### Display y flexbox

| Clase | Efecto |
|---|---|
| `d-none`, `d-block`, `d-flex`, `d-lg-none` | Mostrar y ocultar (con breakpoints) |
| `flex-row`, `flex-column`, `flex-wrap` | Dirección y salto de línea |
| `justify-content-center`, `-between`, `-end` | Alineación en el eje principal |
| `align-items-center`, `-start`, `-end` | Alineación en el eje cruzado |
| `ms-auto`, `me-auto` | Empuja hacia un lado |

### Bordes, sombras y tamaños

| Clase | Efecto |
|---|---|
| `border`, `border-top`, `border-0` | Bordes |
| `rounded`, `rounded-3`, `rounded-pill`, `rounded-circle` | Esquinas |
| `shadow-sm`, `shadow`, `shadow-lg` | Sombras |
| `w-100`, `h-100`, `mw-100`, `min-vh-100` | Anchos y altos |
| `ratio ratio-16x9` | Proporción fija |
| `position-relative`, `sticky-top`, `fixed-bottom` | Posición |
| `visually-hidden`, `visually-hidden-focusable` | Oculto visualmente pero accesible |

### Componentes

| Componente | Estructura mínima |
|---|---|
| Botón | `btn btn-primary`, `btn-outline-*`, `btn-lg`, `btn-sm` |
| Badge | `badge text-bg-primary` |
| Alerta | `alert alert-success` (+ `alert-dismissible`) |
| Tarjeta | `card` > `card-body` > `card-title`, `card-text` |
| Navbar | `navbar navbar-expand-lg` > `navbar-brand`, `navbar-toggler`, `navbar-collapse` |
| Formulario | `form-control`, `form-select`, `form-check`, `form-floating`, `invalid-feedback` |
| Lista de grupo | `list-group` > `list-group-item` |
| Tabla | `table table-striped` dentro de `table-responsive` |
| Barra de progreso | `progress` > `progress-bar` |
| Modal | `modal` > `modal-dialog` > `modal-content` > `modal-header/body/footer` |
| Acordeón | `accordion` > `accordion-item` > `accordion-header`, `accordion-collapse` |
| Carrusel | `carousel` > `carousel-inner` > `carousel-item` |
| Pestañas | `nav nav-tabs` + `tab-content` > `tab-pane` |

### Atributos de JavaScript

| Atributo | Uso |
|---|---|
| `data-bs-toggle` | `collapse`, `modal`, `tab`, `dropdown`, `tooltip`, `offcanvas` |
| `data-bs-target` | Selector (`#id`) del elemento afectado |
| `data-bs-dismiss` | `modal`, `alert`, `toast`, `offcanvas` |
| `data-bs-slide`, `data-bs-slide-to` | Carrusel |
| `data-bs-parent` | Acordeón de uno a la vez |
| `data-bs-theme` | `light` o `dark` en cualquier elemento |

### De Bootstrap 4 a Bootstrap 5

| Bootstrap 4 | Bootstrap 5 |
|---|---|
| `ml-*`, `mr-*`, `pl-*`, `pr-*` | `ms-*`, `me-*`, `ps-*`, `pe-*` |
| `text-left`, `text-right` | `text-start`, `text-end` |
| `float-left`, `float-right` | `float-start`, `float-end` |
| `font-weight-bold` | `fw-bold` |
| `data-toggle`, `data-target`, `data-dismiss` | `data-bs-toggle`, `data-bs-target`, `data-bs-dismiss` |
| `form-group`, `form-row` | `mb-3`, `row g-3` |
| `badge badge-primary` | `badge text-bg-primary` |
| `btn-block` | `d-grid` en el contenedor, o `w-100` |
| `sr-only` | `visually-hidden` |
| `text-muted` | `text-body-secondary` |
| `jQuery` | No es necesario: Bootstrap 5 funciona con JavaScript puro |

---

## Retos adicionales y recursos oficiales

### Retos adicionales

Cuando termines, prueba cualquiera de estos (están de menor a mayor dificultad):

1. **Tooltips:** agrega un tooltip a los emojis de la galería. *(Necesitas inicializarlos con JavaScript: busca "Tooltips" en la documentación.)*
2. **Dropdown:** convierte "Qué hacemos" en la navbar en un menú desplegable con los tres tipos de actividad.
3. **Toast:** al enviar el formulario con éxito, muestra un *toast* en una esquina en vez de la alerta verde.
4. **Offcanvas:** crea un panel lateral con las reglas del club en vez del modal.
5. **Scrollspy:** resalta en la navbar la sección que estás viendo. *(Busca "Scrollspy".)*
6. **Un tercer tema:** en lugar de solo claro y oscuro, crea una clase `.tema-retro` con tus propias variables y alterna entre tres modos.
7. **Sass real:** monta el proyecto con npm y Sass, con una paleta propia de 3 colores.
8. **Publica tu sitio:** súbelo a GitHub Pages y compártelo con tus amistades.

### Recursos oficiales

| Recurso | Para qué |
|---|---|
| [Documentación de Bootstrap 5.3](https://getbootstrap.com/docs/5.3/getting-started/introduction/) | La referencia definitiva, con ejemplos de cada componente |
| [Ejemplos oficiales](https://getbootstrap.com/docs/5.3/examples/) | Plantillas completas para inspirarte |
| [Bootstrap Icons](https://icons.getbootstrap.com/) | Íconos gratuitos para tus proyectos |
| [MDN Web Docs (español)](https://developer.mozilla.org/es/) | HTML, CSS y JavaScript explicados con detalle |
| [WCAG: guía rápida de accesibilidad](https://www.w3.org/WAI/WCAG22/quickref/) | Criterios de accesibilidad web |
| [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/) | Comprueba el contraste de colores |
| [Validador HTML del W3C](https://validator.w3.org/) | Encuentra errores en tu HTML |

---

### Lo que lograste

Empezaste con una página vacía y hoy sabes: organizar contenido con el **grid**, dar estilo con **utilidades**, armar **componentes**, validar **formularios**, usar el **JavaScript de Bootstrap**, **personalizar** colores y temas, y revisar la **accesibilidad** de un sitio. Eso es una base real de desarrollo front-end.

La mejor forma de consolidarlo es **construir algo que te importe**. Empieza hoy con el Reto 2. 🚀
