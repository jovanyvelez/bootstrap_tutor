# 🚀 Bootstrap 5.3.8 desde Cero: construye "RutaUni" paso a paso

**Un tutorial guiado de autoestudio · 3 h 30 min · 10 módulos · nivel principiante**

---

## 📌 Supuestos que hice por ti (léelos antes de empezar)

Como algunos datos no venían definidos, tomé estas decisiones **razonables** para que puedas empezar ya:

| Tema | Decisión tomada | Por qué |
|------|-----------------|---------|
| **Proyecto** | Landing page de **"RutaUni"**, plataforma de preuniversitario y orientación universitaria online | Es un tema cercano a estudiantes colombianos de 15 a 17 años (grado 10 y 11, pensando en el Icfes y en la universidad) y permite usar todos los componentes de Bootstrap de forma natural |
| **Versión** | Bootstrap **5.3.8** (última estable), vía **jsDelivr CDN** | Es la versión con soporte oficial de `data-bs-theme` (modo oscuro nativo) |
| **Conocimientos previos** | Sabes escribir HTML básico (`<div>`, `<h1>`, `<p>`) y CSS básico (colores, `margin`, selectores) | Es el punto de partida declarado |
| **Herramientas** | Un editor de texto (VS Code, Sublime, Notepad++) y un navegador moderno (Chrome, Firefox o Edge) | No necesitas Node.js, ni terminal, ni servidor local |
| **Estilo del código** | No se usan clases de Bootstrap 4 como `ml-2`; en su lugar `ms-2` | Bootstrap 5 usa el sistema de *logical properties* (`start`/`end`) que permite además soporte para árabe y hebreo |
| **Idioma del código** | Los nombres de clases de Bootstrap van en inglés (es lo estándar), pero los textos y comentarios van en español | Bootstrap es un producto global, por eso sus clases están siempre en inglés |
| **Tiempo** | 210 minutos (3 h 30 min) de trabajo efectivo, sin contar pausas | Coherente con la duración pedida |

> 💡 **Si tu proyecto final es otro** (una cafetería, un portafolio, una tienda), la estructura de este tutorial te sirve igual. Bootstrap es el mismo para todos; solo cambia el contenido.

---

## 🎯 ¿Qué vas a construir?

Un sitio web completo de **una sola página (landing page)** con estas secciones:

```
┌──────────────────────────────────────────────┐
│  NAVBAR       fijo arriba, colapsa en móvil  │  ← Módulo 4
├──────────────────────────────────────────────┤
│  HERO         titular + subtítulo + botones  │  ← Módulos 1 y 2
├──────────────────────────────────────────────┤
│  CIFRAS       franja con números + colores   │  ← Módulo 3
├──────────────────────────────────────────────┤
│  PROGRAMAS    rejilla de 3 tarjetas          │  ← Módulo 5
├──────────────────────────────────────────────┤
│  TESTIMONIOS  carrusel de testimonios        │  ← Módulo 7
├──────────────────────────────────────────────┤
│  PREGUNTAS    acordeón (collapse)            │  ← Módulo 7
├──────────────────────────────────────────────┤
│  INSCRIPCIÓN  modal que se abre con botón    │  ← Módulo 7
├──────────────────────────────────────────────┤
│  CONTACTO     formulario con validación      │  ← Módulo 6
├──────────────────────────────────────────────┤
│  FOOTER       multi-columna + créditos       │  ← Módulo 9
└──────────────────────────────────────────────┘
         ▲ TODO con modo oscuro (Módulo 8)
```

**Al terminar serás capaz de:**

- Montar un proyecto con Bootstrap 5.3.8 sin copiar y pegar a ciegas.
- Elegir la clase correcta para maquetar sin memorizar: **razonar** por qué existe.
- Usar el sistema de grid responsive sin adivinar `col-*`.
- Trabajar con los componentes de JS (modal, acordeón, carrusel, offcanvas).
- Personalizar la librería con variables CSS, activar el modo oscuro y dar el primer paso en Sass.
- Revisar tu sitio con una checklist de accesibilidad y buenas prácticas.

---

## 🧰 Prerrequisitos

Necesitas únicamente esto:

- [ ] **Un editor de texto.** [VS Code](https://code.visualstudio.com/) es el más cómodo (resalta el código y autocompleta). Sirve cualquiera.
- [ ] **Un navegador moderno** (Chrome, Firefox, Edge o Safari reciente).
- [ ] **Internet** para cargar el CSS y el JS desde el CDN (la opción de descargarlos la ves en el Módulo 8).
- [ ] Saber qué es una etiqueta HTML y saber abrir un archivo `.html` en el navegador con doble clic.
- [ ] **No necesitas** Node.js, npm, terminal, base de datos ni servidor web. Bootstrap se usa solo con un archivo HTML.

> 💡 **Truco de trabajo:** ten **dos ventanas**: el editor a la izquierda y el navegador a la derecha. Cada vez que guardes (`Ctrl+S` / `Cmd+S`), recarga el navegador (`F5`). Ese ciclo de 5 segundos es tu "compilar".

---

## 🧭 Cómo usar este tutorial

1. **No saltes módulos.** Cada uno se apoya en el anterior. Si algo no cuadra, casi siempre es porque falta un paso.
2. **Escribe el código a mano.** Copiar y pegar entrena la memoria muscular, no la comprensión. Pega solo cuando el bloque sea muy largo y quieras avanzar rápido.
3. **Haz el mini-ejercicio antes de seguir.** Está ahí por una razón: es donde ocurre el aprendizaje real.
4. **Respeta los tiempos.** Si te pasas, no pasa nada; si te queda grande, marca el módulo y vuelve después.
5. **Usa los puntos de control ✅.** Son tu lista de "lo que ya sé hacer".

**Estructura de cada módulo:**

| Sección | Qué encontrarás |
|---------|-----------------|
| 🎯 Objetivo | Lo que vas a lograr en este módulo |
| ⏱️ Tiempo estimado | Cuánto debería tomarte |
| 📖 Explicación conceptual | La idea nueva, en pocas palabras |
| 🛠️ Pasos | Numerados, con código completo |
| 👀 Qué deberías ver | El resultado esperado en pantalla |
| ⚠️ Errores comunes | Lo que sale mal y cómo se arregla |
| 💪 Mini-ejercicio | Práctica guiada (con pista, sin solución) |
| ✅ Punto de control | Tu lista de verificación |

---

## 📚 Tabla de contenidos

- [Módulo 1 · Preparación: editor, CDN y plantilla base](#módulo-1--preparación-editor-cdn-y-plantilla-base) — 15 min
- [Módulo 2 · Grid, contenedores y breakpoints](#módulo-2--grid-contenedores-y-breakpoints) — 30 min
- [Módulo 3 · Tipografía, colores y utilidades](#módulo-3--tipografía-colores-y-utilidades) — 25 min
- [Módulo 4 · Navbar responsive](#módulo-4--navbar-y-navegación-responsive) — 20 min
- [Módulo 5 · Cards, botones, badges y alerts](#módulo-5--cards-botones-badges-y-alerts) — 25 min
- [Módulo 6 · Formularios y validación](#módulo-6--formularios-y-validación) — 25 min
- [Módulo 7 · Componentes con JavaScript](#módulo-7--componentes-con-javascript) — 25 min
- [Módulo 8 · Personalización, modo oscuro y Sass](#módulo-8--personalización-modo-oscuro-y-sass) — 20 min
- [Módulo 9 · Integración final, buenas prácticas y accesibilidad](#módulo-9--integración-final-buenas-prácticas-y-accesibilidad) — 15 min
- [Módulo 10 · Reto final y siguientes pasos](#módulo-10--reto-final-y-siguientes-pasos) — 10 min
- [Checklist rápido de maquetación](#-checklist-rápido-de-una-maquetación-con-bootstrap)
- [Código completo del proyecto terminado](#-código-completo-del-proyecto-terminado)
- [Hoja de referencia rápida (cheat sheet)](#-hoja-de-referencia-rápida-cheat-sheet)
- [Retos adicionales](#-retos-adicionales)
- [Recursos oficiales](#-recursos-oficiales)

> **Tiempo total estimado: 210 minutos (3 h 30 min)**

---

# Módulo 1 · Preparación: editor, CDN y plantilla base

**⏱️ Tiempo estimado: 15 minutos**

## 🎯 Objetivo de aprendizaje

Al terminar este módulo vas a poder:

- Crear la estructura de archivos del proyecto.
- Conectar Bootstrap 5.3.8 (CSS y JS) y los iconos desde un CDN.
- Entender qué es un CDN y por qué no necesitas descargar nada.
- Escribir y visualizar tu **primera página con Bootstrap**.

## 📖 Explicación conceptual

**Bootstrap** es una biblioteca de CSS y JavaScript que trae miles de reglas ya escritas por otras personas. No es un framework de programación como React o Angular: es, básicamente, una hoja de estilos enorme y muy bien organizada que puedes usar con solo añadir dos etiquetas en tu `<head>`.

**CDN** significa *Content Delivery Network* (red de entrega de contenido): servidores como los de jsDelivr o Google que ya tienen los archivos de Bootstrap guardados y te los entregan desde servidores cercanos. La ventaja es que **no descargas ni instalas nada**; la contra es que necesitas conexión a internet. Bootstrap también se puede instalar con npm o descargarse, pero para aprender, el CDN es lo más simple.

Los dos archivos que necesitas:

| Archivo | Qué te da | URL (Bootstrap 5.3.8) |
|---------|-----------|----------------------|
| `bootstrap.min.css` | Todo el diseño: grid, colores, botones, componentes | `https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css` |
| `bootstrap.bundle.min.js` | Los componentes interactivos (modal, carrusel, acordeón...) | `https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js` |

> 💡 **¿Por qué `bundle`?** La versión *bundle* incluye **Popper.js** dentro del propio archivo. Popper es la librería que coloca los desplegables y los *tooltips* en la posición correcta. Con el bundle no necesitas cargarla aparte: un `<script>` y listo.
>
> ⚠️ **No uses los archivos de Bootstrap 4** (el `bootstrap.min.js` sin bundle, que además necesita jQuery) con este tutorial: son de la versión anterior y muchas clases cambiaron de nombre.

---

## 🛠️ Pasos

### Paso 1 — Crea la carpeta del proyecto

En tu escritorio o carpeta de trabajo, crea una carpeta llamada `rutouni` con esta estructura:

```
rutouni/
├── index.html          ← la página (por ahora)
├── css/
│   └── estilos.css     ← tus estilos personalizados (Módulo 8)
└── img/                ← imágenes del proyecto (opcional)
```

Puedes crear `css/` e `img/` con clic derecho → Nueva carpeta. En Windows también funciona con `Shift` + clic derecho → Nueva carpeta.

### Paso 2 — Escribe la plantilla base en `index.html`

Copia **todo** este código en `index.html` y guárdalo:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="RutaUni: preuniversitario virtual para estudiantes de grado 10 y 11 en Colombia. Acompañamiento para el Icfes y el ingreso a la universidad.">
    <title>RutaUni · Acompáñamos tu entrada a la universidad</title>

    <!-- Bootstrap 5.3.8 · CSS -->
    <link rel="stylesheet"
          href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css">

    <!-- Bootstrap Icons (opcional, pero muy útil para la navegación) -->
    <link rel="stylesheet"
          href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">

    <!-- Bootstrap 5.3.8 · JS (el bundle ya incluye Popper) -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"></script>

    <!-- Tu hoja de estilos personalizada (vacía por ahora) -->
    <link rel="stylesheet" href="css/estilos.css">
</head>
<body>

    <!-- ============ ZONA DONDE VIVIRÁ TU CONTENIDO ============ -->

    <p class="p-5 text-center">¡Hola! Bootstrap 5.3.8 está funcionando 🎉</p>

    <!-- ============ FIN DE LA ZONA DE CONTENIDO ============ -->

</body>
</html>
```

### Paso 3 — Abre el archivo en el navegador

Haz doble clic sobre `index.html` (o arrastra el archivo al navegador). Debes ver:

- Un fondo blanco.
- Un texto centrado en negro que dice: *"¡Hola! Bootstrap 5.3.8 está funcionando 🎉"*.
- Un espacio holgado alrededor del texto (viene de `p-5`, que ya te explico abajo).

**Si el texto se ve así, tu instalación está correcta.** ✅

### Paso 4 — Comprueba que CSS y JS se están cargando

Abre la **consola del navegador**:

- Windows/Linux: `F12` o `Ctrl + Shift + J`
- macOS: `Cmd + Option + J`

En la pestaña **Network** (Red), busca `bootstrap.min.css`. Debe aparecer con estado `200` y un tamaño cercano a 230 KB. Si aparece en rojo o como *(failed)*, tu conexión está bloqueando el CDN: revisa tu antivirus o prueba con el CDN de Google (lo verás en el Módulo 8).

### Paso 5 — Crea tu hoja de estilos vacía

Abre `css/estilos.css` y déjala así por ahora:

```css
/* ============================================
   RutaUni · Estilos personalizados
   Lo escribiremos en el Módulo 8
   ============================================ */
```

---

## 👀 Qué deberías ver

- ✅ Una página en blanco con un párrafo centrado.
- ✅ El párrafo **no** pegado a los bordes del navegador: hay margen.
- ✅ Al ver el código fuente aparecen los dos `<link>`/`<script>` del CDN.
- ✅ En la consola del navegador **no** hay errores en rojo.

Si algo de esto falla, no sigas: revisa el apartado siguiente.

---

## ⚠️ Errores comunes y cómo solucionarlos

| Síntoma | Causa probable | Solución |
|---------|----------------|----------|
| La página se ve **sin estilos** (texto pegado a la izquierda, azul) | El `<link>` al CSS no cargó o está mal escrito | Revisa que la URL sea exactamente `.../bootstrap@5.3.8/dist/css/bootstrap.min.css` y que el `<link>` esté dentro de `<head>` |
| `Failed to resolve resource: net::ERR_NAME_NOT_RESOLVED` | El CDN está bloqueado por tu red o antivirus | Cambia `cdn.jsdelivr.net` por `unpkg.com` manteniendo el resto de la ruta |
| El texto se ve **pequeñísimo o gigante** | Falta la etiqueta `<meta name="viewport">` | Es una línea obligatoria para móviles; cópiala tal cual |
| `Uncaught TypeError: bootstrap is not defined` | El `<script>` se movió de sitio sin `defer` | En este tutorial el `<script>` va en `<head>` y funciona. Si lo mueves al final del `<body>` o al `<head>`, conserva el orden |
| La página se descuadra al abrirla en el celular | Hay **cero** o **varias** etiquetas `viewport` | Debe existir exactamente una, la primera dentro de `<head>` |
| Cambiaste el CSS y no se ve nada | Caché del navegador | Recarga forzada: `Ctrl + Shift + R` (Windows) o `Cmd + Shift + R` (Mac) |

---

## 💪 Mini-ejercicio de práctica

**Reto:** convierte el párrafo de prueba en una mini tarjeta de bienvenida usando **solo clases de Bootstrap**, sin escribir CSS.

Requisitos:

1. Fondo azul (`bg-primary`).
2. Texto blanco (`text-white`).
3. Texto centrado (`text-center`).
4. Espaciado interno generoso (`p-5` ya está; añade `mb-4` o `py-5`).
5. Titular grande (`display-5`).
6. Al menos **tres clases distintas** que no aparezcan en la plantilla.

**Pista:** el prefijo de la clase te dice qué hace: `bg-` = fondo, `text-` = texto, `p-`/`m-` = espaciado, `d-` = display o flex, `rounded-` = bordes redondeados.

**Autocomprobación:** si cambiaste el color de fondo y nada cambió, la clase no existe o está mal escrita. Bootstrap es sensible a mayúsculas y guiones: `bg-primary` ✅, `Bg-Primary` ❌.

---

## ✅ Punto de control — Módulo 1

Antes de continuar, confirma que puedes marcar todo esto:

- [ ] Creé la carpeta `rutouni/` con `css/` e `img/`.
- [ ] Escribí `index.html` con `<!DOCTYPE html>` y `lang="es"`.
- [ ] Tengo el `<meta name="viewport">` (una sola vez).
- [ ] Conecté `bootstrap.min.css` **y** `bootstrap.bundle.min.js` en la versión **5.3.8**.
- [ ] Conecté **Bootstrap Icons**.
- [ ] Vi el párrafo centrado en el navegador ✅.
- [ ] Revisé la pestaña Network y el CSS respondió `200`.
- [ ] Completé el mini-ejercicio: mi párrafo ya tiene fondo de color.

**¿Todo marcado? Adelante al Módulo 2.** Si algo falla, vuelve aquí: toda la base depende de este módulo.

---
# Módulo 2 · Grid, contenedores y breakpoints

**⏱️ Tiempo estimado: 30 minutos**

## 🎯 Objetivo de aprendizaje

- Explicar qué es un **sistema de grid** y por qué Bootstrap usa 12 columnas.
- Diferenciar **contenedor**, **fila** (`row`) y **columna** (`col-*`).
- Usar las clases responsivas (`col-12 col-md-6 col-lg-4`) sin adivinar.
- Construir tu **sección Hero**, la primera sección visible del sitio.

## 📖 Explicación conceptual

Casi todas las maquetas que verás en la web se pueden describir así: **columnas que se reorganizan según el tamaño de la pantalla**. Bootstrap te da esa estructura ya resuelta con tres piezas:

| Pieza | Clase | Función |
|-------|-------|---------|
| **Contenedor** | `.container` (o `.container-fluid`) | Caja que centra el contenido y le pone un ancho máximo según la pantalla |
| **Fila** | `.row` | Agrupa columnas y aplica el espacio horizontal entre ellas (`g-2`, `g-4`…) |
| **Columna** | `.col-*` | Una porción del ancho total (de 1 a 12 partes) |

**¿Por qué 12 columnas?** Porque 12 es divisible por 2, 3, 4 y 6: puedes partir el ancho en mitades, tercios, cuartos o sextos sin decimales. Es la misma razón por la que el sistema usa 12 en Bootstrap, Tailwind y CSS Grid.

Los **breakpoints** son los puntos donde cambia el diseño. Mobile-first significa que el valor por defecto es para celular y las clases `sm`, `md`, `lg`... van **subiendo**:

| Breakpoint | Clase | Ancho mínimo | En la práctica |
|-----------|-------|--------------|----------------|
| `xs` | (sin prefijo) | 0 px | Teléfonos (el valor por defecto) |
| `sm` | `sm-` | 576 px | Teléfonos grandes, horizontal |
| `md` | `md-` | 768 px | Tablets |
| `lg` | `lg-` | 992 px | Portátiles |
| `xl` | `xl-` | 1200 px | Monitores |
| `xxl` | `xxl-` | 1400 px | Monitores grandes |

> 💡 **El truco para no equivocarte nunca:** escribe primero el diseño que quieres en **celular** (una sola columna) y luego decide **desde qué tamaño de pantalla** se parte en 2 o en 3. La primera clase sin prefijo siempre manda en el móvil.

## 📋 Referencia rápida del grid

| Necesito… | Clase |
|-----------|-------|
| Todas las columnas del mismo ancho | `col` (equivale a `col-12`... no: a una columna automática, todas iguales) |
| Mitades | `col-12 col-md-6` |
| Tercios | `col-12 col-md-6 col-lg-4` |
| Cuartos | `col-12 col-sm-6 col-lg-3` |
| Sexta parte | `col-12 col-sm-6 col-lg-2` |
| Anchos fijos | `col-4` (un tercio), `col-6` (la mitad), `col-8` (dos tercios) |
| Ocultar solo en móvil | `d-none d-md-block` |
| Ancho completo sin límites | `container-fluid` |
| Centrar una columna sola | `mx-auto` + `col-…` |
| Centrar el contenido de una columna | `text-center` (¡no existe `mx-auto` para columnas centradas!) |

---

## 🛠️ Pasos

### Paso 1 — Reemplaza el párrafo de prueba por la sección Hero

En `index.html`, sustituye todo lo que está entre los dos comentarios por esto:

```html
    <!-- ============ ZONA DONDE VIVIRÁ TU CONTENIDO ============ -->

    <!-- ===== HERO / PORTADA ===== -->
    <header class="bg-primary text-white py-5">
        <div class="container">
            <div class="row align-items-center g-4">

                <div class="col-12 col-lg-7">
                    <span class="badge bg-warning text-dark mb-3">Cohortes 2026 abiertas</span>
                    <h1 class="display-3 fw-bold">Tu entrada a la universidad empieza aquí</h1>
                    <p class="lead my-4">
                        Acompañamiento virtual para estudiantes de grado 10 y 11: preparación
                        para el Icfes, técnicas de estudio y orientación profesional.
                    </p>
                    <div class="d-flex flex-wrap gap-2">
                        <a href="#inscripcion" class="btn btn-light btn-lg">Quiero inscribirme</a>
                        <a href="#programas" class="btn btn-outline-light btn-lg">Ver programas</a>
                    </div>
                </div>

                <div class="col-12 col-lg-5">
                    <div class="card bg-white text-dark border-0 shadow">
                        <div class="card-body text-center p-4">
                            <i class="bi bi-mortarboard-fill display-4 text-primary"></i>
                            <h2 class="h4 mt-3">Ruta Saber 11</h2>
                            <p class="mb-0">12 semanas · 3 sesiones semanales · 100 % online</p>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </header>

    <!-- ============ FIN DE LA ZONA DE CONTENIDO ============ -->
```

### Paso 2 — Mira el resultado en tres tamaños

Guarda y revisa la página en:

1. **Ventana angosta** (arrastra el borde del navegador hasta ~400 px de ancho, o usa `Ctrl` + `Shift` + `M` en Chrome para ver el modo dispositivo).
2. **Ventana mediana** (~800 px).
3. **Pantalla completa.**

Comportamiento esperado:

| Ancho | Qué debería pasar |
|-------|-------------------|
| < 992 px | Las dos columnas se apilan: primero el texto, luego la tarjeta, cada una a ancho completo |
| ≥ 992 px | Se colocan lado a lado: 7/12 el texto y 5/12 la tarjeta |

### Paso 3 — Practica las partes del grid por separado

Crea un archivo de pruebas llamado `pruebas-grid.html` en la misma carpeta con este contenido:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Pruebas de grid</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css">
</head>
<body class="p-4">

    <h2 class="mb-3">A. Control de columnas (col-*)</h2>
    <div class="row g-2 mb-4">
        <div class="col-3"><div class="bg-primary text-white text-center p-3">col-3</div></div>
        <div class="col-3"><div class="bg-primary text-white text-center p-3">col-3</div></div>
        <div class="col-3"><div class="bg-primary text-white text-center p-3">col-3</div></div>
        <div class="col-3"><div class="bg-primary text-white text-center p-3">col-3</div></div>
    </div>

    <h2 class="mb-3">B. Responsive: 1 → 2 → 4 columnas</h2>
    <div class="row g-2 mb-4">
        <div class="col-12 col-sm-6 col-lg-3">
            <div class="bg-success text-white text-center p-3">col-12 col-sm-6 col-lg-3</div>
        </div>
        <div class="col-12 col-sm-6 col-lg-3">
            <div class="bg-success text-white text-center p-3">col-12 col-sm-6 col-lg-3</div>
        </div>
        <div class="col-12 col-sm-6 col-lg-3">
            <div class="bg-success text-white text-center p-3">col-12 col-sm-6 col-lg-3</div>
        </div>
        <div class="col-12 col-sm-6 col-lg-3">
            <div class="bg-success text-white text-center p-3">col-12 col-sm-6 col-lg-3</div>
        </div>
    </div>

    <h2 class="mb-3">C. Anchos fijos con auto (offset)</h2>
    <div class="row g-2 mb-4">
        <div class="col-8 offset-2">
            <div class="bg-warning text-dark text-center p-3">col-8 offset-2 (centrada)</div>
        </div>
    </div>

    <h2 class="mb-3">D. Gutters: separaciones entre columnas</h2>
    <div class="row g-0 mb-4">
        <div class="col-6"><div class="bg-info p-3">g-0 (sin espacio)</div></div>
        <div class="col-6"><div class="bg-info p-3">g-0 (sin espacio)</div></div>
    </div>
    <div class="row g-5">
        <div class="col-6"><div class="bg-dark text-white p-3">g-5 (mucho espacio)</div></div>
        <div class="col-6"><div class="bg-dark text-white p-3">g-5 (mucho espacio)</div></div>
    </div>

    <h2 class="mb-3">E. Alineación vertical (align-items-*)</h2>
    <div class="row align-items-center g-2 mb-4" style="min-height: 140px;">
        <div class="col-4"><div class="bg-secondary text-white text-center p-3">align-items-center</div></div>
        <div class="col-4"><div class="bg-secondary text-white text-center p-5">Más alto</div></div>
        <div class="col-4"><div class="bg-secondary text-white text-center p-3">centrados ↕</div></div>
    </div>

    <h2 class="mb-3">F. Orden (order-*)</h2>
    <div class="row g-2">
        <div class="col-4 order-3"><div class="bg-danger text-white text-center p-3">Primero en el HTML, order-3</div></div>
        <div class="col-4 order-1"><div class="bg-danger text-white text-center p-3">Segundo en el HTML, order-1</div></div>
        <div class="col-4 order-2"><div class="bg-danger text-white text-center p-3">Tercero en el HTML, order-2</div></div>
    </div>

</body>
</html>
```

Ábrelo y **reduce la ventana lentamente**. Cada bloque se reconfigura en un tamaño distinto. Este archivo es tu "`playground`" de grid: vuelve a él cada vez que olvides cómo funciona algo.

### Paso 4 — Comprueba el ancho del contenedor

Añade temporalmente este estilo **al final de tu `index.html`**, antes de `</body>`, solo para estudiar:

```html
    <style>
        .container { background-color: rgba(255, 0, 0, .08); outline: 2px dashed rgba(255,0,0,.4); }
    </style>
```

Al redimensionar verás que el contenedor **no** ocupa siempre todo el ancho: se detiene en 540 px, 720 px, 960 px, 1140 px y 1320 px según el breakpoint. Eso es exactamente lo que hace que tu sitio se vea "acotado" y legible en monitores grandes. **Cuando termines, borra este bloque `<style>`.**

---

## 👀 Qué deberías ver

- ✅ Un bloque azul (`bg-primary`) a pantalla completa con un titular grande, un botón blanco y otro con borde blanco.
- ✅ En celular todo se apila en una columna; en escritorio, el texto queda a la izquierda y una tarjeta blanca a la derecha.
- ✅ En `pruebas-grid.html`, los bloques se reorganizan al cruzar 576, 768 y 992 px.
- ✅ Al mover el viewport, el contenedor se detiene en anchos máximos definidos.

---

## ⚠️ Errores comunes y cómo solucionarlos

| Síntoma | Causa probable | Solución |
|---------|----------------|----------|
| Las columnas se apilan y **nunca** se ponen lado a lado | Falta el prefijo del breakpoint (`md`, `lg`…) | `col-6` son 6/12 **siempre**; necesitas `col-12 col-md-6` |
| Todo se ve igual de estrecho | Falta `.row` entre el contenedor y las columnas | Sin `.row` no existen columnas ni gutter |
| Una columna "invade" el ancho de la otra | Hay más de 12 columnas en la misma fila | Bootstrap **parte** las que sobran a una segunda línea automáticamente |
| Las columnas se pegan al borde izquierdo | Falta `.container` | El contenido debe vivir siempre dentro de un `.container` o `.container-fluid` |
| El gutter no aparece | `g-0`, o `g-` en el hijo en vez del padre | El gutter se define en la **fila**: `<div class="row g-3">` |
| La página se desplaza horizontalmente en móvil | Usaste `g-5` dentro de un `.container`: el margen negativo de la fila es mayor que el padding del contenedor | En móvil usa `g-4` y sube a `g-5` desde `lg`: `<div class="row g-4 g-lg-5">` |
| La columna no se centra | Usé `mx-auto` esperando que centra la columna | `mx-auto` centra **contenidos**; para centrar la columna usa `col-*` + `offset-*`, o `justify-content-center` en la fila |
| Parece que hay estilos "inventados" de Bootstrap | Estás viendo el `outline` del `style` temporal del Paso 4 | Bórralo cuando termines de estudiar |

> ⚠️ **Error conceptual típico:** creer que `col-6` significa "la mitad en móvil". No. Mobile-first exige que escribas `col-12` (o `col`) primero y luego indiques **desde qué tamaño** se parte. Si inviertes el orden de las clases el resultado puede no ser el que esperas.

---

## 💪 Mini-ejercicio de práctica

**Reto:** añade en `pruebas-grid.html` una sección nueva que simule la franja de logos de universidades partners, con este comportamiento:

| Tamaño | Resultado |
|--------|-----------|
| Móvil (< 576 px) | 2 columnas |
| Tablet (≥ 768 px) | 4 columnas |
| Escritorio (≥ 1200 px) | 6 columnas |

Requisitos:
- Debe usar `container` + `row` + columnas responsive.
- Intercalo con `order-*` en móvil para que los últimos dos logos de la fila de escritorio pasen arriba (así se verá más ordenado en pantalla pequeña).
- Cada logo es un `div` con texto y una de las clases `bg-*` distintas entre sí.
- Agrega un título `<h2>` antes de la fila, alineado a la izquierda.

**Pista:** el orden de clases de columna debe ser de menor a mayor breakpoint: `col-6 col-md-3 col-xl-2`. Para el orden: `order-4 order-md-0`.

**Autocomprobación:** reduce y agranda la ventana. ¿Los conteos por fila son 2, 4 y 6? Si al llegar a `xl` no hay 6, revisa que hayas escrito `col-xl-2` y no `col-lg-2`.

---

## ✅ Punto de control — Módulo 2

- [ ] Entiendo la diferencia entre `.container`, `.row` y `.col-*`.
- [ ] Sé que el grid tiene 12 columnas y por qué.
- [ ] Recuerdo los breakpoints: `sm 576`, `md 768`, `lg 992`, `xl 1200`, `xxl 1400`.
- [ ] Entiendo que mobile-first significa "empieza por el valor sin prefijo".
- [ ] Mi Hero tiene 2 columnas que se apilan en móvil.
- [ ] Probé `g-0`, `g-2`, `g-4`, `offset-2`, `order-*` y `align-items-center` en el archivo de pruebas.
- [ ] Completé el mini-ejercicio y el conteo de columnas cambia en 768 px y 1200 px.

---
# Módulo 3 · Tipografía, colores y utilidades

**⏱️ Tiempo estimado: 25 minutos**

## 🎯 Objetivo de aprendizaje

- Usar la escala tipográfica de Bootstrap sin inventar tamaños.
- Aplicar colores del tema y colores contextuales con una sola clase.
- Dominar las utilidades de espaciado (`p-*`, `m-*`) y su relación con los *breakpoints*.
- Usar utilidades de display y flex para alinear cosas sin CSS propio.
- Construir la sección de **cifras destacadas**.

## 📖 Explicación conceptual

Una **utilidad** es una clase que hace **una sola cosa**, sin más. Bootstrap se apoya mucho en ellas: en vez de escribir un `.titulo-grande { }` en tu CSS, usas `h1` + `display-4`.

Tres familias que debes reconocer rápido:

**1. Tipografía.** Bootstrap define una escala fija con títulos responsive (`display-1` … `display-6`, que además se reducen solos en móvil) y una escala de texto normal (`fs-1` … `fs-6`). Los estilos `.lead`, `.fw-bold`, `.fst-italic`, `.text-lowercase` completan el conjunto.

**2. Color.** Hay dos tipos:

| Tipo | Clases | Para qué |
|------|--------|----------|
| **Color del tema** | `primary`, `secondary`, `success`, `danger`, `warning`, `info`, `light`, `dark` | Identidad visual de tu sitio |
| **Variante / estilo** | `-subtle`, `-emphasis`, `-text-`, `-bg-`, `-border-` | Textos suaves, fondos, bordes del mismo color |

Ejemplo: `bg-primary-subtle` + `text-primary-emphasis` es la combinación oficial para "un recuadro azul clarito con texto azul legible". Se ve igual de bien en modo oscuro porque ambos tonos se redefinen automáticamente.

**3. Espaciado (lo más usado).** Bootstrap tiene una escala fija de espacio:

```
0 = 0        1 = .25rem     2 = .5rem     3 = 1rem     4 = 1.5rem     5 = 3rem
```

- `p-*` = **padding** (espacio interno)
- `m-*` = **margin** (espacio externo)
- Antes de la letra va la **dirección**: `pt` (top), `pb` (bottom), `ps` (start/izquierda), `pe` (end/derecha), `px` (ambos horizontales), `py` (ambos verticales).
- Antes de la regla va el **sentido**: `n` = negativo.
- Y opcionalmente el **breakpoint**: `py-md-5` aplica `py-5` **desde 768 px**.

Estos cuatro datos son **el 60 % de todo Bootstrap**. Si los dominas, ya sabes maquetar.

## 📋 Cheat sheet de espaciado

| Necesito… | Clase |
|-----------|-------|
| Padding en las cuatro direcciones | `p-3` |
| Padding solo arriba / abajo | `pt-5` / `pb-5` |
| Padding solo a los lados | `px-4` |
| Padding vertical (secciones) | `py-5` |
| Margen inferior entre bloques | `mb-4` |
| Quitar un margen heredado | `m-0` |
| Centrar horizontalmente | `mx-auto` |
| Margen que **empieza** en tablet | `mb-md-5` |
| Separación automática entre hijos | `gap-3` (dentro de un `d-flex`) |
| Gutters grandes en móvil | `g-4 g-lg-5` (nunca `g-5` a secas: desborda) |

---

## 🛠️ Pasos

### Paso 1 — Añade la sección de cifras justo después del Hero

En `index.html`, pega esto **después** del `</header>` del Hero y antes del comentario `<!-- ============ FIN DE LA ZONA DE CONTENIDO ============ -->`:

```html
    <!-- ===== CIFRAS DESTACADAS ===== -->
    <section class="py-5 bg-body-tertiary">
        <div class="container">
            <div class="row g-4 text-center">

                <div class="col-12 col-sm-6 col-lg-3">
                    <h2 class="display-4 fw-bold text-primary mb-0">+3.200</h2>
                    <p class="text-secondary mb-0">estudiantes causados en 14 ciudades</p>
                </div>

                <div class="col-12 col-sm-6 col-lg-3">
                    <h2 class="display-4 fw-bold text-success mb-0">94 %</h2>
                    <p class="text-secondary mb-0">mejoraron su puntaje en el simulacro</p>
                </div>

                <div class="col-12 col-sm-6 col-lg-3">
                    <h2 class="display-4 fw-bold text-warning mb-0">48</h2>
                    <p class="text-secondary mb-0">docentes de planta</p>
                </div>

                <div class="col-12 col-sm-6 col-lg-3">
                    <h2 class="display-4 fw-bold text-danger mb-0">12</h2>
                    <p class="text-secondary mb-0">semanas por cohorte</p>
                </div>

            </div>
        </div>
    </section>
```

### Paso 2 — Experimenta con la escala tipográfica

Abre `pruebas-grid.html` (o crea `pruebas-tipografia.html`) y pega dentro de `<body>`:

```html
<h2 class="mb-3">G. Escala de titulares (display)</h2>
<p class="display-1">display-1</p>
<p class="display-2">display-2</p>
<p class="display-3">display-3</p>
<p class="display-4">display-4</p>
<p class="display-5">display-5</p>
<p class="display-6">display-6</p>

<h2 class="mb-3">H. Escala de texto (fs)</h2>
<p class="fs-1">fs-1 · Texto muy grande</p>
<p class="fs-2">fs-2</p>
<p class="fs-3">fs-3</p>
<p class="fs-4">fs-4</p>
<p class="fs-5">fs-5</p>
<p class="fs-6">fs-6</p>

<h2 class="mb-3">I. Encabezados HTML con clases</h2>
<h1>h1</h1>
<h2>h2</h2>
<h3>h3</h3>
<h4>h4</h4>
<h5>h5</h5>
<h6>h6</h6>

<h2 class="mb-3">J. Formato de texto</h2>
<p class="lead">lead: párrafo destacado, más grande y claro</p>
<p class="fw-bold">fw-bold</p>
<p class="fw-semibold">fw-semibold</p>
<p class="fw-normal">fw-normal</p>
<p class="fw-light">fw-light</p>
<p class="fst-italic">fst-italic</p>
<p class="text-decoration-underline">text-decoration-underline</p>
<p class="text-decoration-line-through">text-decoration-line-through</p>
<p><a href="#">Enlace normal</a> · <a class="link-primary" href="#">link-primary</a> ·
   <a class="link-danger" href="#">link-danger</a></p>
<p><mark class="bg-warning">mark</mark> · <small>small</small> · <abbr title="Significado">abbr</abbr></p>

<h2 class="mb-3">K. Colores y fondos</h2>
<div class="row g-2">
    <div class="col-6 col-md-3"><div class="bg-primary text-white p-3">bg-primary</div></div>
    <div class="col-6 col-md-3"><div class="bg-secondary p-3">bg-secondary</div></div>
    <div class="col-6 col-md-3"><div class="bg-success text-white p-3">bg-success</div></div>
    <div class="col-6 col-md-3"><div class="bg-danger text-white p-3">bg-danger</div></div>
    <div class="col-6 col-md-3"><div class="bg-warning text-dark p-3">bg-warning</div></div>
    <div class="col-6 col-md-3"><div class="bg-info text-dark p-3">bg-info</div></div>
    <div class="col-6 col-md-3"><div class="bg-light border p-3">bg-light</div></div>
    <div class="col-6 col-md-3"><div class="bg-dark text-white p-3">bg-dark</div></div>
</div>

<h2 class="mb-3">L. Colores sutiles (funcionan en modo oscuro)</h2>
<div class="row g-2">
    <div class="col-6 col-md-3"><div class="bg-primary-subtle text-primary-emphasis p-3">primary-subtle</div></div>
    <div class="col-6 col-md-3"><div class="bg-success-subtle text-success-emphasis p-3">success-subtle</div></div>
    <div class="col-6 col-md-3"><div class="bg-warning-subtle text-warning-emphasis p-3">warning-subtle</div></div>
    <div class="col-6 col-md-3"><div class="bg-danger-subtle text-danger-emphasis p-3">danger-subtle</div></div>
</div>

<h2 class="mb-3">M. Utilidades de display, flex y sombras</h2>
<div class="row g-2 mb-3">
    <div class="col-md-4 d-none d-md-block"><div class="bg-light border p-3">Solo visible desde md</div></div>
    <div class="col-md-4 d-lg-none"><div class="bg-light border p-3">Oculto desde lg en adelante</div></div>
    <div class="col-md-4"><div class="bg-light border p-3">Siempre visible</div></div>
</div>
<div class="d-flex justify-content-between align-items-center border p-3 mb-3">
    <span>justify-content-between</span>
    <span class="d-none d-sm-inline">align-items-center</span>
    <span>gap-3</span>
</div>
<div class="d-flex flex-column flex-sm-row gap-2 mb-3">
    <div class="bg-primary text-white p-2 flex-fill">flex-fill</div>
    <div class="bg-primary text-white p-2 flex-fill">flex-fill</div>
    <div class="bg-primary text-white p-2 flex-fill">flex-fill</div>
</div>
<div class="row g-3">
    <div class="col-md-4"><div class="shadow p-3">shadow</div></div>
    <div class="col-md-4"><div class="shadow-sm p-3">shadow-sm</div></div>
    <div class="col-md-4"><div class="shadow-lg p-3">shadow-lg</div></div>
</div>
<div class="border rounded rounded-3 rounded-top-0 p-3 mt-3">
    border · rounded · rounded-3 · rounded-top-0
</div>
```

### Paso 3 — Comprueba los colores de tu tema

Abre la consola del navegador y escribe:

```js
getComputedStyle(document.documentElement).getPropertyValue('--bs-primary')
```

Verás el valor RGB del color primario. Bootstrap **5.3** expone **todas** sus variables CSS con el prefijo `--bs-`, lo que significa que puedes cambiar la identidad visual de tu sitio desde el CSS sin recompilar nada. Lo harás en el Módulo 8.

### Paso 4 — Aplica utilidades al Hero para mejorarlo

En el Hero de tu `index.html`, ajusta las clases de la columna de texto a esta versión más cuidada:

```html
                <div class="col-12 col-lg-7">
                    <span class="badge bg-warning text-dark mb-3">Cohortes 2026 abiertas</span>
                    <h1 class="display-3 fw-bold lh-1">Tu entrada a la universidad empieza aquí</h1>
                    <p class="lead my-4 text-white-50">
                        Acompañamiento virtual para estudiantes de grado 10 y 11: preparación
                        para el Icfes, técnicas de estudio y orientación profesional.
                    </p>
                    <div class="d-flex flex-wrap gap-2 mb-4">
                        <a href="#inscripcion" class="btn btn-light btn-lg px-4">Quiero inscribirme</a>
                        <a href="#programas" class="btn btn-outline-light btn-lg px-4">Ver programas</a>
                    </div>
                    <ul class="list-unstyled d-flex flex-wrap gap-4 small mb-0">
                        <li><i class="bi bi-check-circle-fill text-warning"></i> Clases en vivo y grabadas</li>
                        <li><i class="bi bi-check-circle-fill text-warning"></i> Plan de estudio semanal</li>
                        <li><i class="bi bi-check-circle-fill text-warning"></i> Sin costo de matrícula</li>
                    </ul>
                </div>
```

Clases nuevas para notar: `lh-1` (interlineado), `text-white-50` (blanco translúcido), `px-4` (padding horizontal del botón), `gap-4`, `list-unstyled`.

---

## 👀 Qué deberías ver

- ✅ Una franja gris clara (`bg-body-tertiary`) con 4 cifras grandes que se reacomodan: 1 → 2 → 4 columnas.
- ✅ El Hero más pulido, con viñetas sin viñetas (`list-unstyled`) e iconos de Bootstrap Icons.
- ✅ En el archivo de pruebas, la escala completa de tamaños, colores y sombras.
- ✅ `body` en un tono distinto del blanco puro (por defecto es `bg-body`, que el Módulo 8 hará configurable).

---

## ⚠️ Errores comunes y cómo solucionarlos

| Síntoma | Causa probable | Solución |
|---------|----------------|----------|
| `mb-6` o `py-8` no hacen nada | La escala solo llega hasta 5 | Usa `mb-5` como máximo, o una clase arbitraria de Bootstrap 5.3 (`mb-6` sí existe desde 5.3, pero `mb-7` no) |
| El padding no se ve en móvil | Usaste `py-lg-5` y en móvil no hay espacio | Recuerda mobile-first: `py-3 py-lg-5` |
| El texto se ve ilegible sobre el botón | `btn-warning` con el texto por defecto negro y yo puse `text-white` | Revisa el contraste: ámbar va con texto **oscuro** |
| El gutter desapareció entre columnas | Anidé `.row` dentro de `.col-*` | Recuerda: `.row` solo puede estar directamente dentro de `.container` (o de una `.col-*`) |
| El margen del `<p>` no se respeta | El navegador le da margen por defecto y tú lo duplicaste | Usa `mb-0` cuando quieras anular el margen propio |
| Con `text-center` el título se ve largo y feo | Es normal: el texto centrado en bloques largos cansa | Centra solo textos cortos; usa `text-start` (o `text-md-center`) en párrafos largos |
| No encuentro la clase exacta que busco | No todas las combinaciones existen | Ve a <https://getbootstrap.com/docs/5.3/layout/grid/> y busca la tabla; el buscador del sitio es lo más rápido |

---

## 💪 Mini-ejercicio de práctica

**Reto:** convierte la sección de cifras en un **"banner de cohesión 2026"** usando solo utilidades.

Requisitos:

1. Debe tener fondo con gradiente de color oscuro y `py-5 py-md-6` (o `py-5 py-lg-6` si prefieres esperar a `lg`).
2. Los cuatro textos van en **blanco** y los subtítulos en `text-white-50`.
3. Aplica `fs-1` a los números en móvil y `display-3` solo desde `md` (`fs-1` sigue mandando en móvil). Pista: `fs-1 display-1` no funciona así; necesitas saber qué gana. Investiga con dos clases de fuente y comprueba cuál aplica.
4. Añade un borde superior e inferior: `border-top border-bottom` con `border-opacity-25`.
5. Redondea **solo las esquinas de arriba** con `rounded-top-4`.
6. Cambia los textos a datos del proyecto: por ejemplo "6 ciudades", "1.800 estudiantes", "98 % aprobación", "4.9 ★".

**Pista para el punto 3:** en CSS, cuando dos reglas tienen la misma especificidad y ambas aplican a la misma propiedad, gana la que aparece **más abajo** en la hoja de estilos. Como Bootstrap declara `.fs-*` antes que `.display-*`, `display-*` gana... salvo que uses `rounded-*`/utilidades que sí están después. Verifica en el navegador qué clase gana.

**Autocomprobación:** en móvil los números deben verse "normales" (`fs-1`), no gigantes; en escritorio, `display-3`. Redimensiona para comprobarlo.

---

## ✅ Punto de control — Módulo 3

- [ ] Sé la diferencia entre `display-*` y `fs-*`.
- [ ] Recuerdo la escala de espaciado `0 → 5` y que 3 = 1rem.
- [ ] Sé armar `pt-3 pb-4 px-md-5`.
- [ ] Entiendo la diferencia entre `bg-primary`, `bg-primary-subtle` y `text-primary-emphasis`.
- [ ] Entiendo `d-none d-md-block`, `d-flex`, `justify-content-*`, `align-items-*`, `gap-*`.
- [ ] Usé correctamente `text-white-50` sobre fondo oscuro y revisé el contraste.
- [ ] Completé el banner del ejercicio con las 6 condiciones.

---
# Módulo 4 · Navbar y navegación responsive

**⏱️ Tiempo estimado: 20 minutos**

## 🎯 Objetivo de aprendizaje

- Construir una barra de navegación que **colapse** en móvil.
- Entender por qué un navbar se construye con `navbar` + `container` + `navbar-collapse`, y qué papel juegan los atributos `data-bs-*`.
- Agregar un enlace activo, un icono de marca y un botón de llamada a la acción.
- Navegar con anclas entre secciones.

## 📖 Explicación conceptual

La navegación de un sitio es el componente que más se nota si está mal hecho. Bootstrap lo resuelve con tres piezas encajadas:

| Pieza | Para qué |
|-------|----------|
| `navbar` +navbar-expand-lg` | La barra. `expand-lg` indica: colapsada en móvil, **expandida** desde 992 px |
| `navbar-nav` + `nav-item` + `nav-link` | La lista de enlaces |
| `navbar-toggler` + `navbar-collapse` | El botón de hamburguesa y la caja que se abre y cierra |

Lo interesante es que **el comportamiento de abrir y cerrar lo controla JavaScript**, pero no con funciones propias: Bootstrap lee unos atributos `data-bs-*` y los conecta solo.

| Atributo | Para qué sirve |
|----------|----------------|
| `data-bs-toggle="collapse"` | "Este elemento abre/cierra algo" |
| `data-bs-target="#id"` | …y específicamente cuál es ese algo: el elemento con ese `id` |
| `data-bs-spy="scroll"` | Marca automáticamente el enlace de la sección que estás viendo |

> 💡 **El identificador es la clave**: el `data-bs-target="#menu"` debe apuntar al `id="menu"` del `navbar-collapse`. Si no coinciden, el menú simplemente no hace nada.

En el Módulo 7 verás que el modal, el acordeón y el carrusel usan exactamente el mismo patrón.

---

## 🛠️ Pasos

### Paso 1 — Inserta el navbar antes del Hero

En `index.html`, pega esto justo después de `<body>` y **antes** del `<!-- ===== HERO / PORTADA ===== -->`:

```html
    <!-- ===== NAVBAR ===== -->
    <nav class="navbar navbar-expand-lg bg-dark navbar-dark sticky-top shadow-sm">
        <div class="container">

            <a class="navbar-brand d-flex align-items-center gap-2" href="#">
                <i class="bi bi-compass fs-3 text-info"></i>
                <span class="fw-bold">RutaUni</span>
            </a>

            <button class="navbar-toggler" type="button"
                    data-bs-toggle="collapse" data-bs-target="#menuPrincipal"
                    aria-controls="menuPrincipal" aria-expanded="false" aria-label="Abrir el menú">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse" id="menuPrincipal">
                <ul class="navbar-nav ms-auto mb-2 mb-lg-0 align-items-lg-center gap-lg-2">
                    <li class="nav-item">
                        <a class="nav-link active" aria-current="page" href="#">Inicio</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#programas">Programas</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#testimonios">Testimonios</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#preguntas">Preguntas</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#contacto">Contacto</a>
                    </li>
                    <li class="nav-item ms-lg-2">
                        <a href="#inscripcion" class="btn btn-info text-dark fw-semibold px-3">
                            Inscríbirme
                        </a>
                    </li>
                </ul>

                <form class="d-none d-lg-block ms-lg-3" role="search">
                    <input class="form-control form-control-sm" type="search"
                           placeholder="Buscar" aria-label="Buscar en el sitio">
                </form>
            </div>

        </div>
    </nav>
```

### Paso 2 — Entiende cada línea crítica

Marca estas cuatro cosas en tu código, porque son las que se olvidan:

1. `data-bs-target="#menuPrincipal"` y `id="menuPrincipal"` → **deben coincidir**.
2. `aria-controls="menuPrincipal"` y `aria-expanded="false"` → los usa el lector de pantalla.
3. `aria-current="page"` en el enlace activo → anuncia "estás aquí".
4. `aria-label="Abrir el menú"` en el botón → sin esto, el lector dice solo "botón".

### Paso 3 — Prueba el comportamiento responsive

1. Reduce la ventana a menos de 992 px: los enlaces desaparecen y aparece el botón de tres rayitas.
2. Haz clic en él: el menú se despliega hacia abajo y ocupa todo el ancho.
3. Vuelve a hacer clic: se pliega.
4. Amplía a más de 992 px: los enlaces aparecen en línea y el botón desaparece.
5. Baja por la página: como tiene `sticky-top`, la barra queda fija arriba.

### Paso 4 — Añade desplazamiento suave a las anclas

Las anclas (`href="#programas"`) se mueven de golpe, lo que puede ser incómodo. Añade esto a `css/estilos.css`:

```css
/* Desplazamiento suave al usar anclas (respeta la preferencia del sistema) */
html {
    scroll-behavior: smooth;
    scroll-padding-top: 5rem; /* deja espacio para que el navbar fijo no tape el título */
}

@media (prefers-reduced-motion: reduce) {
    html {
        scroll-behavior: auto;
    }
}
```

### Paso 5 — Crea los anclajes de las secciones

Para que los enlaces funcionen, cada sección necesita su `id`. Añádelos a las que ya tienes:

- `<header class="bg-primary text-white py-5" id="inicio">`
- La sección de cifras: `id="cifras"`
- La sección de cifras puede enlazarse más adelante.

Cuando el `<footer>` esté listo (Módulo 9), también llevará su propio `id`.

> 💡 **`scroll-padding-top`** es un detalle de la vida real: si el navbar es `sticky-top`, al saltar a un ancla el título queda por debajo de la barra. Esta propiedad deja un hueco de 5 rem. Sin ella, el visitante no ve el título de la sección a la que llegó.

---

## 👀 Qué deberías ver

- ✅ Una barra oscura fija arriba, con el logo "RutaUni" a la izquierda y los enlaces a la derecha.
- ✅ En móvil, solo el logo y las tres rayitas; al pulsarlas, aparece el menú completo.
- ✅ El botón turquesa "Inscríbirme" siempre visible.
- ✅ Al hacer clic en "Contacto" (aunque la sección aún no exista) el navegador salta a ese ancla.
- ✅ Al navegar por anclas, el título de la sección no queda escondido detrás de la barra.

---

## ⚠️ Errores comunes y cómo solucionarlos

| Síntoma | Causa probable | Solución |
|---------|----------------|----------|
| El botón de hamburguesa no hace nada | El `data-bs-target` no coincide con el `id` | Compáralos carácter a carácter, incluyendo el `#` |
| El menú no se pliega al segundo clic | Falta el script `bootstrap.bundle.min.js` | Verifícalo en la pestaña Network con F12 |
| Los enlaces se ven en móvil, uno por uno, sin menú | Falta `navbar-expand-lg` (o `collapse`) | `navbar-expand-lg` es el que decide a partir de qué ancho se expande |
| El menú tapa el contenido al desplazarse | `sticky-top` sin `scroll-padding-top` | Añade la regla del Paso 4 al CSS |
| Los enlaces están muy juntos / muy lejos | Falta el espaciado | Usa `gap-lg-2` en el `ul` o `me-2` en cada `nav-link` |
| El ícono del menú sale como un cuadro | No cargó Bootstrap Icons | Verifica el `<link>` a `bootstrap-icons.min.css` |
| La barra tapa el primer contenido al abrir en móvil | Sin `z-index`, otras capas se superponen | `sticky-top` ya resuelve esto; si usaste `position: fixed` a mano, añade `z-index: 1030` |

---

## 💪 Mini-ejercicio de práctica

**Reto:** convierte el navbar en una versión "**dos niveles**":

1. El elemento "Programas" debe tener un **menú desplegable** hacia abajo con tres opciones (Saber 11, Lectura crítica y Orientación profesional). Mantén el enlace del elemento padre y añade además una opción separada con `dropdown-divider`.
2. Agrega una segunda opción al menú con `dropdown-menu-end` (alineado a la derecha).
3. Añade un campo de búsqueda que **sí** se vea en móvil (usa `d-block d-lg-none`, en su propio bloque).
4. Cambia `bg-dark` por `bg-body-tertiary` y pon `navbar-expand-md` para comprobar el cambio de breakpoint.
5. Deja el navbar fijo (`sticky-top`) y verifica que el contenido nunca queda por debajo.

**Pista:** el patrón del dropdown es

```html
<li class="nav-item dropdown">
    <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown">Programas</a>
    <ul class="dropdown-menu">
        <li><a class="dropdown-item" href="#">Opción 1</a></li>
    </ul>
</li>
```

**Autocomprobación:** el menú desplegable debe funcionar también en **móvil**, después de haber abierto la hamburguesa. Si en móvil no abre, casi siempre es porque el `dropdown-toggle` quedó fuera del `navbar-collapse`.

---

## ✅ Punto de control — Módulo 4

- [ ] Mi navbar tiene `navbar`, `navbar-expand-lg`, `navbar-collapse` y `navbar-toggler`.
- [ ] `data-bs-target` coincide con el `id` del contenedor.
- [ ] El botón tiene `aria-label` y el enlace activo tiene `aria-current="page"`.
- [ ] Probé el menú en móvil (abre y cierra) y en escritorio (expandido).
- [ ] Añadí `scroll-behavior: smooth` y `scroll-padding-top` en mi CSS.
- [ ] Asigné `id` a las secciones para que las anclas funcionen.
- [ ] Completé el navbar con dropdown.

---
# Módulo 5 · Cards, botones, badges y alerts

**⏱️ Tiempo estimado: 25 minutos**

## 🎯 Objetivo de aprendizaje

- Construir tarjetas (`card`) con imagen, cuerpo, pie y estados.
- Usar el sistema completo de botones (variantes, tamaños, contornos, estados).
- Diferenciar `badge` de `alert`.
- Componer una rejilla de tarjetas responsive: la **sección de programas**.

## 📖 Explicación conceptual

Una **card** es el componente más usado de Bootstrap: una caja blanca con bordes redondeados y sombra que agrupa contenido relacionado. Se construye por partes, y cada parte tiene su clase:

| Parte | Clase |
|-------|-------|
| Contenedor | `card` |
| Variante de color (borde superior, texto) | `card` + `text-bg-primary`, `border-primary`… |
| Imagen superior | `card-img-top` |
| Cuerpo | `card-body` |
| Título | `card-title` |
| Texto secundario dentro del cuerpo | `card-text` |
| Lista dentro del cuerpo | `list-group list-group-flush` |
| Pie | `card-footer` |
| Imagen que cubre toda la tarjeta | `card-img` |
| Superposición de texto sobre la imagen | `card-img-overlay` |

Sobre las imágenes, dos reglas inviolables en un sitio real:

1. El `alt` describe la imagen **para quien no la ve**. No es un adorno.
2. Para que las tarjetas de una fila queden **iguales de alto**, usa `h-100` en la tarjeta y `d-flex flex-column` + `mt-auto` en el pie. Bootstrap no iguala alturas por sí solo.

**Botones.** Un botón es un `<a>` o un `<button>` con `btn`:

| Necesito | Clase |
|----------|-------|
| Botón principal sólido | `btn btn-primary` |
| Botón secundario con borde | `btn btn-outline-primary` |
| Botón discreto (sin fondo) | `btn btn-link` |
| Tamaño | `btn-lg`, `btn-sm` |
| Ancho completo | `w-100` |
| Estado deshabilitado | `disabled` (atributo) o `aria-disabled="true"` |
| Estado activo (pulsado) | `active` |
| Botón de icono | `<button class="btn btn-light"><i class="bi bi-heart"></i></button>` |

> 💡 **Regla de oro:** **una sola** idea por color. Si todo es azul, nada destaca. Usa `primary` para la acción principal y `outline` para las secundarias.

**Badges vs. alerts.**

| | `badge` | `alert` |
|---|---------|---------|
| Para qué | Etiqueta compacta: "Nuevo", "Gratis", "2 horas" | Mensaje destacado dentro de una sección |
| Tamaño | diminuto | bloque completo |
| Ejemplo | `<span class="badge text-bg-success">Gratis</span>` | `<div class="alert alert-success">¡Inscripción abierta!</div>` |

---

## 🛠️ Pasos

### Paso 1 — Añade la sección de programas

Pega esto **después** de la sección de cifras y antes del comentario `<!-- ============ FIN DE LA ZONA DE CONTENIDO ============ -->`:

```html
    <!-- ===== PROGRAMAS (TARJETAS) ===== -->
    <section class="py-5" id="programas">
        <div class="container">

            <div class="row mb-5">
                <div class="col-12 col-lg-8">
                    <span class="badge text-bg-primary mb-2">Programas</span>
                    <h2 class="fw-bold">Elige tu ruta de preparación</h2>
                </div>
                <div class="col-12 col-lg-4">
                    <p class="text-secondary mb-0">
                        Todos los programas son virtuales, con asesoras de planta
                        y horarios compatibles con el colegio.
                    </p>
                </div>
            </div>

            <div class="row g-4">

                <div class="col-12 col-md-6 col-lg-4 d-flex">
                    <article class="card h-100 w-100 shadow-sm border-0">
                        <div class="card-body d-flex flex-column p-4">
                            <span class="badge text-bg-success align-self-start mb-3">Más solicitado</span>
                            <h3 class="card-title h4">Ruta Saber 11</h3>
                            <p class="card-text flex-grow-1 text-secondary">
                                Intensivo de 12 semanas en matemáticas, lectura crítica,
                                química e inglés, con simulacros semanales.
                            </p>
                            <ul class="list-group list-group-flush mb-3">
                                <li class="list-group-item px-0">3 sesiones semanales en vivo</li>
                                <li class="list-group-item px-0">Materiales incluidos</li>
                                <li class="list-group-item px-0">Grupo de máximo 25 estudiantes</li>
                            </ul>
                            <div class="d-flex justify-content-between align-items-center mt-auto">
                                <span class="h4 mb-0">$380.000 <small class="text-secondary">/ mes</small></span>
                                <button class="btn btn-primary" data-bs-toggle="modal"
                                        data-bs-target="#modalInscripcion">Inscribirme</button>
                            </div>
                        </div>
                    </article>
                </div>

                <div class="col-12 col-md-6 col-lg-4 d-flex">
                    <article class="card h-100 w-100 shadow-sm border-0">
                        <div class="card-body d-flex flex-column p-4">
                            <span class="badge text-bg-info align-self-start mb-3">Nuevo</span>
                            <h3 class="card-title h4">Lectura y escritura</h3>
                            <p class="card-text flex-grow-1 text-secondary">
                                Taller de 8 semanas para mejorar el componente comunicativo
                                del Icfes y aprender a escribir ensayos y ensayos de opinión.
                            </p>
                            <ul class="list-group list-group-flush mb-3">
                                <li class="list-group-item px-0">Talleres de escritura creativa</li>
                                <li class="list-group-item px-0">Corrección personalizada</li>
                                <li class="list-group-item px-0">2 sesiones semanales</li>
                            </ul>
                            <div class="d-flex justify-content-between align-items-center mt-auto">
                                <span class="h4 mb-0">$240.000 <small class="text-secondary">/ mes</small></span>
                                <button class="btn btn-outline-primary" data-bs-toggle="modal"
                                        data-bs-target="#modalInscripcion">Inscribirme</button>
                            </div>
                        </div>
                    </article>
                </div>

                <div class="col-12 col-md-6 col-lg-4 d-flex">
                    <article class="card h-100 w-100 shadow-sm border-0">
                        <div class="card-body d-flex flex-column p-4">
                            <span class="badge text-bg-warning text-dark align-self-start mb-3">Cupo limitado</span>
                            <h3 class="card-title h4">Orientación universitaria</h3>
                            <p class="card-text flex-grow-1 text-secondary">
                                Acompañamiento para elegir carrera y preparar tu carta de
                                motivación y las pruebas de admisión de cada universidad.
                            </p>
                            <ul class="list-group list-group-flush mb-3">
                                <li class="list-group-item px-0">6 sesiones individuales</li>
                                <li class="list-group-item px-0">Mapa de universidades de Colombia</li>
                                <li class="list-group-item px-0">1 sesión semanal</li>
                            </ul>
                            <div class="d-flex justify-content-between align-items-center mt-auto">
                                <span class="h4 mb-0">$180.000 <small class="text-secondary">/ mes</small></span>
                                <button class="btn btn-outline-primary" data-bs-toggle="modal"
                                        data-bs-target="#modalInscripcion">Inscribirme</button>
                            </div>
                        </div>
                    </article>
                </div>

            </div>
        </div>
    </section>
```

> ⚠️ **Ojo con los textos:** todo lo que escribas dentro de estas etiquetas es contenido tuyo, no de Bootstrap. Escribe frases completas y revisa la ortografía antes de dar por terminada la sección.

### Paso 2 — Agrega el aviso de inscripción abierta

Pega esto justo antes de la sección de programas:

```html
    <!-- ===== ALERTA / AVISO ===== -->
    <div class="container py-4">
        <div class="alert alert-info d-flex align-items-start gap-3 shadow-sm" role="alert">
            <i class="bi bi-info-circle-fill fs-4"></i>
            <div class="flex-grow-1">
                <h2 class="h5 alert-heading mb-1">¡Inscripciones abiertas para la cohorte de febrero!</h2>
                <p class="mb-0">
                    Los cupos se asignan por orden de pago. Escribe a
                    <a href="#contacto" class="alert-link">admisiones@rutuni.edu.co</a>
                    para recibir la ficha de matrícula.
                </p>
            </div>
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Cerrar"></button>
        </div>
    </div>
```

### Paso 3 — Experimenta con botones

Añade dentro de tu archivo de pruebas un botón de cada tipo:

```html
<h2 class="my-4">Botones: variantes</h2>
<button class="btn btn-primary">Primary</button>
<button class="btn btn-secondary">Secondary</button>
<button class="btn btn-success">Success</button>
<button class="btn btn-danger">Danger</button>
<button class="btn btn-warning">Warning</button>
<button class="btn btn-info">Info</button>
<button class="btn btn-light">Light</button>
<button class="btn btn-dark">Dark</button>
<button class="btn btn-link">Link</button>

<h2 class="my-4">Botones: con borde (outline)</h2>
<button class="btn btn-outline-primary">Outline primary</button>
<button class="btn btn-outline-secondary">Outline secondary</button>
<button class="btn btn-outline-success">Outline success</button>

<h2 class="my-4">Botones: tamaños y estado</h2>
<button class="btn btn-primary btn-lg">Grande</button>
<button class="btn btn-primary">Normal</button>
<button class="btn btn-primary btn-sm">Pequeño</button>
<button class="btn btn-primary" disabled>Deshabilitado</button>
<button class="btn btn-primary" aria-disabled="true" tabindex="-1">Deshabilitado accesible</button>

<h2 class="my-4">Botones: con icono y ancho completo</h2>
<button class="btn btn-success"><i class="bi bi-whatsapp me-2"></i>Escribir por WhatsApp</button>
<button class="btn btn-outline-secondary w-100 my-2">Ancho completo</button>
<a href="#" class="btn btn-primary">También soy un enlace</a>

<h2 class="my-4">Badges</h2>
<span class="badge text-bg-primary">Primary</span>
<span class="badge text-bg-secondary">Secondary</span>
<span class="badge text-bg-success">Success</span>
<span class="badge text-bg-danger">4 mensajes</span>
<span class="badge rounded-pill text-bg-dark">Píldora</span>
<span class="badge bg-primary-subtle text-primary-emphasis">Sutil</span>
```

### Paso 4 — Logra tarjetas de altura uniforme

Revisa tu sección de programas en modo ventana estrecha (donde caben 2 o 3 tarjetas):

- Si los botones "Inscribirme" quedan a **alturas distintas**, es que falta `h-100` en la tarjeta o `flex-grow-1` en el texto.

Comprueba que tu estructura sea exactamente esta cadena:

```
col-12 col-md-6 col-lg-4 d-flex   ← la columna es un flex container
  └── card h-100 w-100            ← la tarjeta ocupa el alto completo
        └── card-body d-flex flex-column
              ├── card-text flex-grow-1   ← el texto ocupa el espacio sobrante
              └── mt-auto          ← el pie se empuja hacia abajo
```

---

## 👀 Qué deberías ver

- ✅ Una franja de aviso azul con ícono de información y una "X" para cerrarla (y desaparece al hacer clic).
- ✅ Tres tarjetas blancas con bordes redondeados y sombra suave.
- ✅ Las tres tarjetas **con la misma altura** en cada fila, con los botones alineados abajo.
- ✅ Badges de colores distintos ("Más solicitado", "Nuevo", "Cupo limitado").
- ✅ Una lista con líneas separadoras dentro de cada tarjeta.

---

## ⚠️ Errores comunes y cómo solucionarlos

| Síntoma | Causa probable | Solución |
|---------|----------------|----------|
| Las tarjetas tienen alturas distintas | Falta `h-100` en la tarjeta | `.card` no se estira solo; necesita `h-100` + una columna `d-flex` |
| El botón queda pegado al texto | El texto no ocupa el espacio libre | `flex-grow-1` en el `card-text` y `mt-auto` en el pie |
| Un botón queda invisible | Usaste `btn-light` sobre fondo blanco | Usa `btn-outline-light` o `btn-dark` |
| El `badge` se ve diminuto o ilegible | Texto oscuro sobre fondo oscuro | Usa siempre el par `text-bg-*`: define fondo **y** color de texto a la vez |
| El aviso tapa todo el ancho | `alert` sin `container` | Envuélvelo en un `<div class="container">` |
| El aviso tiene `role="alert"` y no se anuncia bien | El `role` debe ir en el contenedor del mensaje | Pon `role="alert"` en el `div.alert`, no en un hijo |
| El botón "Inscribirme" no hace nada todavía | El modal se crea en el Módulo 7 | Espera al Módulo 7; por ahora no da error |
| La imagen de la tarjeta se deforma | Le faltaba `card-img-top` o una altura fija | Usa `card-img-top` + la utilidad `ratio` para tarjetas 16:9 |

---

## 💪 Mini-ejercicio de práctica

**Reto:** añade una **cuarta tarjeta** y mejora la sección.

Requisitos:

1. Crea una tarjeta "Simulacros semanales" con `badge text-bg-dark`, precio `$0` y botón `btn btn-dark`.
2. Que las cuatro tarjetas se vean bien en **todas** las resoluciones: usa `col-12 col-sm-6 col-lg-3`.
3. Añade una imagen superior real a **dos** de las tarjetas usando imágenes de picsum (`https://picsum.photos/seed/rutuni1/400/200`), con `alt` descriptivo y la clase `card-img-top`.
4. Para que las imágenes no se deformen, envuélvelas en `<div class="ratio ratio-16x9">` con la imagen dentro usando `object-fit-cover`.
5. Añade un pie de tarjeta (`card-footer`) con el horario, en letra pequeña.
6. Pon un borde de color arriba de cada tarjeta con `border-top border-4 border-primary` (y distinto color en cada una).

**Pista:** una tarjeta con imagen necesita la imagen **fuera** del `card-body`:

```html
<div class="card h-100 w-100 shadow-sm border-0">
    <img src="..." class="card-img-top" alt="Aula virtual con estudiantes">
    <div class="card-body">...</div>
    <div class="card-footer text-secondary">Martes y jueves, 4:00 p. m.</div>
</div>
```

**Autocomprobación:** redimensiona la ventana lentamente. En ningún momento las imágenes deben verse "estiradas" ni cortadas de forma extraña, y los cuatro pies deben quedar a la misma altura.

---

## ✅ Punto de control — Módulo 5

- [ ] Construí una `card` con `card-body`, `card-title`, `card-text` y `card-footer`.
- [ ] Mis tarjetas tienen `h-100` y sus botones quedan alineados.
- [ ] Entiendo `card-text flex-grow-1` + `mt-auto`.
- [ ] Sé la diferencia entre `badge` y `alert`.
- [ ] Usé `text-bg-*` en los badges para asegurar contraste.
- [ ] Probé las variantes `btn`, `btn-outline-*`, `btn-*` y los tamaños `btn-lg`/`btn-sm`.
- [ ] Mi alerta se puede cerrar con `btn-close` y `data-bs-dismiss="alert"`.
- [ ] Limpié los textos con errores de tipeo que dejé en el código de ejemplo.
- [ ] Completé la cuarta tarjeta con imagen y pie.

---
# Módulo 6 · Formularios y validación

**⏱️ Tiempo estimado: 25 minutos**

## 🎯 Objetivo de aprendizaje

- Construir un formulario con la apariencia de Bootstrap (`form-control`, `form-label`, `form-select`).
- Entender por qué **cada** control necesita un `label` asociado.
- Usar grupos de entrada (`input-group`), casillas de verificación, radios y *switches*.
- Aplicar **validación** con `.invalid` / `.valid` y el `novalidate` de Bootstrap.
- Construir la **sección de contacto**.

## 📖 Explicación conceptual

Bootstrap no valida formularios: eso lo hace el **navegador** con HTML5 (`required`, `type="email"`, `minlength`…). Bootstrap solo le **pone la apariencia** a los estados que el navegador ya decidió.

Hay dos modelos:

**Modelo A — nativo (recomendado para aprender).** Pones `required`, `type="email"` y el navegador muestra su propio mensaje al enviar. Es accesible, gratis y funciona sin JavaScript.

**Modelo B — clases de validación.** Al enviar, el navegador bloquea el envío, así que para *pintar* los estados hay que hacerlo con JavaScript: se agrega `.is-invalid` o `.is-valid` a cada control según `checkValidity()`.

```js
document.querySelectorAll('form').forEach(form => {
    form.addEventListener('submit', evento => {
        evento.preventDefault();          // no dejamos enviar todavía
        form.querySelectorAll('[required]').forEach(campo => {
            campo.classList.toggle('is-invalid', !campo.checkValidity());
            campo.classList.toggle('is-valid', campo.checkValidity());
        });
    });
});
```

> 💡 **Clases que ya usabas sin saberlo:** las que el navegador activa por su cuenta son `.is-invalid`, `.is-valid`, `.is-invalid-feedback` y `.is-valid-feedback`. Bootstrap únicamente las **estiliza**.

Sobre accesibilidad, tres reglas no negociables en formularios:

1. Cada campo tiene `<label for="id">` **por debajo** del campo (así el cursor del usuario queda pegado al campo mientras escribe).
2. Los mensajes de error se asocian con `aria-describedby`.
3. Los campos obligatorios se marcan con `required` (el navegador los anuncia) y, visualmente, con un asterisco `*` decorado con `aria-hidden="true"`.

---

## 🛠️ Pasos

### Paso 1 — Añade la sección de contacto

Pega esto **después** de la sección de programas y antes del comentario `<!-- ============ FIN DE LA ZONA DE CONTENIDO ============ -->`:

```html
    <!-- ===== CONTACTO ===== -->
    <section class="py-5 bg-body-tertiary" id="contacto">
        <div class="container">
            <!-- gutter adaptativo: g-4 en móvil (no desborda) y g-5 desde lg -->
            <div class="row g-4 g-lg-5">

                <div class="col-12 col-lg-5">
                    <span class="badge text-bg-secondary mb-2">Contacto</span>
                    <h2 class="fw-bold mb-3">¿Tienes dudas? Escríbenos</h2>
                    <p class="text-secondary mb-4">
                        Nuestro equipo de admisiones responde en menos de 24 horas hábiles
                        y en horario extendido para zonas rurales.
                    </p>

                    <ul class="list-unstyled d-grid gap-3">
                        <li class="d-flex gap-3">
                            <i class="bi bi-envelope-fill text-primary fs-5"></i>
                            <div>
                                <strong>Correo</strong><br>
                                <a href="mailto:admisiones@rutuni.edu.co">admisiones@rutuni.edu.co</a>
                            </div>
                        </li>
                        <li class="d-flex gap-3">
                            <i class="bi bi-telephone-fill text-primary fs-5"></i>
                            <div>
                                <strong>Teléfono</strong><br>
                                <a href="tel:+573001234567">+57 300 123 4567</a>
                            </div>
                        </li>
                        <li class="d-flex gap-3">
                            <i class="bi bi-geo-alt-fill text-primary fs-5"></i>
                            <div>
                                <strong>Sede</strong><br>
                                Medellín (ant.), con clases online a todo Colombia
                            </div>
                        </li>
                    </ul>

                    <div class="mt-4">
                        <a href="https://wa.me/573001234567" class="btn btn-success" rel="noopener">
                            <i class="bi bi-whatsapp me-2"></i>Escríbenos por WhatsApp
                        </a>
                    </div>
                </div>

                <div class="col-12 col-lg-7">
                    <div class="card border-0 shadow-sm">
                        <div class="card-body p-4 p-lg-5">

                            <form id="formularioContacto" novalidate>
                                <div class="row g-3">

                                    <div class="col-12 col-md-6">
                                        <label for="nombre" class="form-label">
                                            Nombre completo <span class="text-danger" aria-hidden="true">*</span>
                                        </label>
                                        <input type="text" class="form-control" id="nombre"
                                               name="nombre" placeholder="Ej. Valentina Gómez"
                                               autocomplete="name" required minlength="3">
                                        <div class="invalid-feedback">
                                            Escribe tu nombre (mínimo 3 letras).
                                        </div>
                                    </div>

                                    <div class="col-12 col-md-6">
                                        <label for="correo" class="form-label">
                                            Correo electrónico <span class="text-danger" aria-hidden="true">*</span>
                                        </label>
                                        <input type="email" class="form-control" id="correo"
                                               name="correo" placeholder="tu@correo.com"
                                               autocomplete="email" required>
                                        <div class="invalid-feedback">
                                            Revisa el correo: debe tener el formato nombre@dominio.com
                                        </div>
                                    </div>

                                    <div class="col-12 col-md-6">
                                        <label for="telefono" class="form-label">Teléfono (opcional)</label>
                                        <input type="tel" class="form-control" id="telefono"
                                               name="telefono" placeholder="+57 300 123 4567"
                                               autocomplete="tel" pattern="[0-9+ ]{7,15}">
                                        <div class="invalid-feedback">
                                            Entre 7 y 15 caracteres: solo números, espacios y el signo +.
                                        </div>
                                    </div>

                                    <div class="col-12 col-md-6">
                                        <label for="grado" class="form-label">
                                            Grado en el que estás <span class="text-danger" aria-hidden="true">*</span>
                                        </label>
                                        <select class="form-select" id="grado" name="grado" required>
                                            <option value="" selected disabled>Elegir una opción</option>
                                            <option value="9">Grado 9</option>
                                            <option value="10">Grado 10</option>
                                            <option value="11">Grado 11</option>
                                            <option value="otro">Otro / graduated</option>
                                        </select>
                                        <div class="invalid-feedback">Selecciona tu grado actual.</div>
                                    </div>

                                    <div class="col-12">
                                        <label for="programa" class="form-label">
                                            Programa de interés <span class="text-danger" aria-hidden="true">*</span>
                                        </label>
                                        <select class="form-select" id="programa" name="programa" required>
                                            <option value="" selected disabled>Elegir un programa</option>
                                            <option>Ruta Saber 11</option>
                                            <option>Lectura y escritura</option>
                                            <option>Orientación universitaria</option>
                                        </select>
                                        <div class="invalid-feedback">Elige el programa que te interesa.</div>
                                    </div>

                                    <div class="col-12">
                                        <label for="mensaje" class="form-label">
                                            Mensaje <span class="text-danger" aria-hidden="true">*</span>
                                        </label>
                                        <textarea class="form-control" id="mensaje" name="mensaje"
                                                  rows="4" placeholder="Cuéntanos tu caso..."
                                                  required minlength="20"></textarea>
                                        <div class="form-text">Mínimo 20 caracteres.</div>
                                        <div class="invalid-feedback">
                                            Escribe al menos 20 caracteres para que podamos ayudarte bien.
                                        </div>
                                    </div>

                                    <div class="col-12">
                                        <div class="form-check">
                                            <input class="form-check-input" type="checkbox" id="acepto" required>
                                            <label class="form-check-label" for="acepto">
                                                Acepto el tratamiento de mis datos y las
                                                <a href="#" class="link-primary">condiciones del programa</a>.
                                            </label>
                                            <div class="invalid-feedback">
                                                Debes aceptar para poder enviar la solicitud.
                                            </div>
                                        </div>
                                    </div>

                                    <div class="col-12 col-lg-6">
                                        <div class="form-check form-switch">
                                            <input class="form-check-input" type="checkbox" role="switch"
                                                   id="whatsapp" checked>
                                            <label class="form-check-label" for="whatsapp">
                                                Prefiero que me escriban por WhatsApp
                                            </label>
                                        </div>
                                    </div>

                                    <div class="col-12 col-lg-6">
                                        <label for="ciudad" class="form-label">Ciudad</label>
                                        <div class="input-group">
                                            <span class="input-group-text"><i class="bi bi-geo-alt"></i></span>
                                            <input type="text" class="form-control" id="ciudad"
                                                   name="ciudad" placeholder="Medellín"
                                                   list="listaCiudades">
                                            <datalist id="listaCiudades">
                                                <option value="Bogotá"></option>
                                                <option value="Medellín"></option>
                                                <option value="Cali"></option>
                                                <option value="Bucaramanga"></option>
                                            </datalist>
                                        </div>
                                    </div>

                                    <div class="col-12">
                                        <div class="d-flex flex-wrap gap-2 pt-2">
                                            <button type="submit" class="btn btn-primary btn-lg px-4">
                                                <i class="bi bi-send me-2"></i>Enviar solicitud
                                            </button>
                                            <button type="reset" class="btn btn-outline-secondary btn-lg">
                                                Limpiar
                                            </button>
                                        </div>
                                        <p class="form-text mt-3">
                                            Los campos marcados con <span class="text-danger">*</span> son obligatorios.
                                        </p>
                                    </div>

                                </div>
                            </form>

                            <!-- Mensaje de éxito (oculto por defecto, lo muestra el JS) -->
                            <div class="alert alert-success d-none" id="avisoExito" role="status" tabindex="-1">
                                <h3 class="h5 alert-heading"><i class="bi bi-check-circle me-2"></i>¡Recibimos tu mensaje!</h3>
                                <p class="mb-0" id="textoExito">
                                    Te responderemos a tu correo en menos de 24 horas hábiles.
                                </p>
                            </div>

                        </div>
                    </div>
                </div>

            </div>
        </div>
    </section>
```

### Paso 2 — Añade la validación en JavaScript

Crea el archivo `js/mi-script.js` y pega este código:

```javascript
/* ============================================================
   RutaUni · Validación del formulario de contacto
   ============================================================ */
(function () {
    'use strict';

    const formulario = document.getElementById('formularioContacto');
    const avisoExito = document.getElementById('avisoExito');
    const textoExito = document.getElementById('textoExito');

    if (!formulario) return;

    // Marca un campo como válido o inválido según las reglas nativas del navegador
    function validarCampo(campo) {
        const esValido = campo.checkValidity();
        campo.classList.toggle('is-invalid', !esValido);
        campo.classList.toggle('is-valid', esValido);
        return esValido;
    }

    // Al salir del campo ("blur"), muéstralo como válido o inválido
    formulario.querySelectorAll('input, select, textarea').forEach(campo => {
        campo.addEventListener('blur', () => {
            if (campo.value !== '' || campo.required) {
                validarCampo(campo);
            }
        });

        // Mientras escribe, si ya se corrigió el error, quítalo
        campo.addEventListener('input', () => {
            if (campo.classList.contains('is-invalid')) {
                validarCampo(campo);
            }
        });
    });

    formulario.addEventListener('submit', function (evento) {
        evento.preventDefault(); // en un proyecto real: aquí iría el fetch() al servidor

        const campos = Array.from(formulario.querySelectorAll('input, select, textarea'));
        const resultados = campos.map(validarCampo);
        const primerError = campos[resultados.indexOf(false)];

        if (resultados.includes(false)) {
            primerError.focus();       // lleva el foco al primer problema
            return;
        }

        // Todo correcto: en producción, aquí se enviarían los datos al servidor
        const nombre = formulario.nombre.value.trim().split(' ')[0];
        textoExito.textContent =
            `Gracias, ${nombre}. Te responderemos a tu correo en menos de 24 horas hábiles.`;

        formulario.classList.add('d-none');
        avisoExito.classList.remove('d-none');
        avisoExito.focus();             // anuncia el mensaje a quien usa lector de pantalla
    });
})();
```

Y en `index.html`, **justo antes de `</body>`**, agrega:

```html
    <script src="js/mi-script.js"></script>
```

> 💡 El script del bundle de Bootstrap está en el `<head>` y el tuyo va al final del `<body>`: así tu código encuentra el HTML que ya está cargado.

### Paso 3 — Prueba la validación

| Prueba | Resultado esperado |
|--------|--------------------|
| Pulsa **Enviar** con todo vacío | Los campos obligatorios se ponen rojos, el foco salta al primero y aparece el mensaje de error |
| Escribe `abc` en el nombre y salta a otro campo | Sigue en rojo (`minlength="3"` no se cumple) |
| Escribe `correo` sin `@` | El campo de correo se pone rojo |
| Escribe `valentina@correo.com` | El campo se pone **verde** y el error desaparece |
| Escribe un mensaje de 10 caracteres | No se envía; avisa que faltan caracteres |
| Deja sin marcar la casilla de aceptación | No se envía; avisa que debes aceptar |
| Completa todo correctamente | Desaparece el formulario, aparece el aviso verde con tu nombre |
| Pulsa **Limpiar** | Se vacían los campos (los estados rojo/verde permanecen; es un comportamiento normal del navegador) |

### Paso 4 — Prueba la accesibilidad del formulario

1. **Sin ratón:** pulsa `Tab` repetidamente. El foco debe recorrer los campos **en orden**, con un borde visible.
2. **Con lector de pantalla:** en Chrome, `F12` → pestaña *Accessibility* (o instala *NVDA* / *Orca*). Al enfocarte en el campo "Nombre", debe leer "Nombre completo, obligatory, edit text".
3. **Escala de fuente:** en `Chrome` pulsa `Ctrl` + `+` varias veces. El formulario se reacomoda y nada se rompe.

---

## 👀 Qué deberías ver

- ✅ Una sección de contacto en dos columnas: datos a la izquierda, formulario a la derecha (apiladas en móvil).
- ✅ Campos con etiquetas visibles arriba y líneas de separación coherentes.
- ✅ Al enviar vacío: campos rojos con mensajes de error específicos debajo.
- ✅ Al enviar bien: un aviso verde que saluda por tu primer nombre.
- ✅ El botón de WhatsApp verde junto a los datos de contacto.

---

## ⚠️ Errores comunes y cómo solucionarlos

| Síntoma | Causa probable | Solución |
|---------|----------------|----------|
| La etiqueta no hace clic en el campo | Falta el `for` o no coincide con el `id` | `for` debe ser **idéntico** al `id` del control |
| La casilla se marca con un ☐ que no se ve al hacer clic | El `label` no envuelve al `input` ni tiene `for` | `<label class="form-check-label" for="id">` |
| El formulario se envía aunque falten campos | Quitaste `required`, o `novalidate` sin tu JS | Revisa que los campos críticos tengan `required` |
| El aviso verde nunca aparece | Faltó `js/mi-script.js` o está en el `<head>` | Ponlo antes de `</body>` |
| `campo is not defined` en la consola | Usaste una variable sin `const`/`let`, o el script está en el `<head>` | Usa `const` y coloca el script al final |
| Los `select` se ven con otro color | El `<option selected disabled>` no es el valor por defecto | Deja la primera opción vacía y marcada como `selected disabled` |
| No puedo escribir en el formulario | Falta `method`/`action` y hay un overlay invisible | Quita el overlay; revisa que no haya un `modal` abierto detrás |
| El borde rojo no aparece en el primer campo | `invalid-feedback` sin el `div` correspondiente dentro de `.form-check` | Cada `invalid-feedback` va **después** del `input` que valida |
| En móvil el formulario se ve diminuto | Falta el `<meta name="viewport">` | Regresa al Módulo 1 |

---

## 💪 Mini-ejercicio de práctica

**Reto:** convierte el formulario en un formulario de **solicitud de admisión** más completo.

Requisitos:

1. Añade un campo de **programa de interés** que ya es `select`, pero además muestra un `input-group` con un icono de `bi-mortarboard`.
2. Añade un `<textarea>` con contador de caracteres en vivo (JavaScript): "Escribe tu mensaje (0/500)" y un `maxlength="500"`.
3. Añade un campo de **tipo radio** para "Modalidad": *Presencial* / *Virtual* / *Mixta*.
4. Añade un `<input type="range">` con etiqueta "Horas semanales disponibles" y su valor mostrado en vivo.
5. Añade un `<input type="file">` para subir el certificado del colegio, con `accept=".pdf,.jpg,.png"`.
6. Añade el casillas con `form-check-inline` para "Acepto recibir novedades por correo" e "Acepto la política de datos".
7. Envuelve **todo** el formulario en un `<fieldset>` con `<legend>` para agruparlo semánticamente.
8. Al enviar bien, además del aviso, muestra un **spinner** (`spinner-border`) durante 2 segundos simulando el envío (usa `setTimeout`).

**Pista para el contador:**

```javascript
const mensaje = document.getElementById('mensaje');
const contador = document.getElementById('contador');
mensaje.addEventListener('input', () => {
    contador.textContent = `${mensaje.value.length}/500`;
});
```

**Autocomprobación:** el contador debe actualizarse **mientras escribes**, sin recargar la página; el slider debe mostrar su número; y el aviso verde solo debe aparecer cuando **todos** los campos obligatorios estén bien.

---

## ✅ Punto de control — Módulo 6

- [ ] Cada campo de mi formulario tiene `<label for>` con el `id` correcto.
- [ ] Uso `form-label`, `form-control`, `form-select`, `form-check`, `form-switch`, `form-text`.
- [ ] Entiendo que Bootstrap no valida: solo estiliza `.is-invalid`, `.is-valid` y `*-feedback`.
- [ ] Mi formulario usa `novalidate` y mi JS aplica las clases de validación.
- [ ] El foco salta al primer campo con error al enviar.
- [ ] Probé la validación con los 8 casos del Paso 3.
- [ ] Probé el formulario solo con teclado.
- [ ] Añadí el aviso de éxito con `role="status"`.
- [ ] Mi script propio está en `js/mi-script.js` y se carga antes de `</body>`.
- [ ] Completé el ejercicio del formulario avanzado.

---
# Módulo 7 · Componentes con JavaScript

**⏱️ Tiempo estimado: 25 minutos**

## 🎯 Objetivo de aprendizaje

- Entender el **patrón `data-bs-*`** que une HTML y JavaScript en Bootstrap.
- Usar el **modal** de inscripción.
- Usar el **collapse** para crear un acordeón de preguntas frecuentes.
- Usar el **carrusel** de testimonios.
- Abrir un modal **desde JavaScript** (no solo desde un botón).

## 📖 Explicación conceptual

Los componentes interactivos de Bootstrap **no necesitan que escribas JavaScript**. Solo requieren dos cosas:

1. El HTML con una estructura exacta.
2. Un atributo `data-bs-*` que diga qué hacer.

Bootstrap "escucha" esos atributos y conecta el comportamiento solo. Ese es el patrón que verás en los tres componentes de este módulo:

```html
<!-- Disparador: en cualquier parte de la página -->
<button class="btn" data-bs-toggle="modal" data-bs-target="#miModal">Abrir</button>

<!-- Componente: en cualquier lugar (idealmente antes de </body>) -->
<div class="modal fade" id="miModal" tabindex="-1" aria-labelledby="miModalLabel" aria-hidden="true">
  ...
</div>
```

| Atributo | Significado |
|----------|-------------|
| `data-bs-toggle="modal"` | Este elemento alterna (abre/cierra) el componente |
| `data-bs-target="#id"` | El componente afectado |
| `data-bs-dismiss="modal"` | Cierra el modal (botón "Cancelar" o la "X") |
| `tabindex="-1"` | Necesario para que el modal reciba foco |
| `aria-hidden="true"` | Mientras está cerrado, los lectores de pantalla lo ignoran |

Y cuando necesites control desde tu propio código, cada componente es una **clase de JavaScript**:

```javascript
const miModal = new bootstrap.Modal(document.getElementById('miModal'));
miModal.show();
miModal.hide();
```

## 📋 Referencia rápida de atributos

| Componente | Atributo clave | Notas |
|------------|----------------|-------|
| Modal | `data-bs-toggle="modal"` | Requiere `.modal` + `.modal-dialog` dentro |
| Collapse | `data-bs-toggle="collapse"` | El destino debe tener la clase `.collapse` |
| Accordion (Bootstrap 5.3) | `data-bs-toggle="collapse"` con `data-bs-parent="#id"` | Solo un panel abierto a la vez |
| Carousel | `data-bs-ride="carousel"` | Requiere `.carousel`, `.carousel-inner`, `.carousel-item` |
| Alert | `data-bs-dismiss="alert"` | Cierra el mensaje |
| Offcanvas | `data-bs-toggle="offcanvas"` | Menú lateral, buen sustituto del navbar en móvil |
| Tooltip | `data-bs-toggle="tooltip"` | Requiere inicialización manual |
| Popover | `data-bs-toggle="popover"` | Requiere inicialización manual |

---

## 🛠️ Pasos

### Paso 1 — Añade el carrusel de testimonios

Pega esto **después** de la sección de programas (antes de la sección de contacto):

```html
    <!-- ===== TESTIMONIOS (CARRUSEL) ===== -->
    <section class="py-5" id="testimonios">
        <div class="container">
            <h2 class="fw-bold text-center mb-5">Lo que dicen nuestros estudiantes</h2>

            <div id="carruselTestimonios" class="carousel slide" data-bs-ride="carousel"
                 data-bs-interval="6000" data-bs-touch="true">

                <div class="carousel-indicators">
                    <button type="button" data-bs-target="#carruselTestimonios"
                            data-bs-slide-to="0" class="active" aria-current="true"
                            aria-label="Testimonio 1"></button>
                    <button type="button" data-bs-target="#carruselTestimonios"
                            data-bs-slide-to="1" aria-label="Testimonio 2"></button>
                    <button type="button" data-bs-target="#carruselTestimonios"
                            data-bs-slide-to="2" aria-label="Testimonio 3"></button>
                </div>

                <div class="carousel-inner">
                    <div class="carousel-item active">
                        <div class="row justify-content-center">
                            <div class="col-12 col-lg-8">
                                <figure class="text-center p-4 bg-body-tertiary rounded-4">
                                    <blockquote class="blockquote fs-5 mb-4">
                                        "Subí 120 puntos en el simulacro. Lo que más me sirvió
                                        fue aprender a organizar el tiempo, no solo los temas."
                                    </blockquote>
                                    <figcaption class="d-flex align-items-center justify-content-center gap-3">
                                        <i class="bi bi-person-circle-fill fs-2 text-primary"></i>
                                        <span class="text-start">
                                            <strong>Mariana Ospina</strong><br>
                                            <small class="text-secondary">Grado 11 · Medellín</small>
                                        </span>
                                    </figcaption>
                                </figure>
                            </div>
                        </div>
                    </div>

                    <div class="carousel-item">
                        <div class="row justify-content-center">
                            <div class="col-12 col-lg-8">
                                <figure class="text-center p-4 bg-body-tertiary rounded-4">
                                    <blockquote class="blockquote fs-5 mb-4">
                                        "Los profesores responden los mensajes el mismo día. Eso
                                        no lo había visto en ningún otro preuniversitario."
                                    </blockquote>
                                    <figcaption class="d-flex align-items-center justify-content-center gap-3">
                                        <i class="bi bi-person-circle-fill fs-2 text-success"></i>
                                        <span class="text-start">
                                            <strong>Kevin Restrepo</strong><br>
                                            <small class="text-secondary">Grado 11 · Pereira</small>
                                        </span>
                                    </figcaption>
                                </figure>
                            </div>
                        </div>
                    </div>

                    <div class="carousel-item">
                        <div class="row justify-content-center">
                            <div class="col-12 col-lg-8">
                                <figure class="text-center p-4 bg-body-tertiary rounded-4">
                                    <blockquote class="blockquote fs-5 mb-4">
                                        "Con la orientación profesional decidí estudiar ingeniería. Estaba
                                        entre tres opciones y terminé escogiendo la correcta."
                                    </blockquote>
                                    <figcaption class="d-flex align-items-center justify-content-center gap-3">
                                        <i class="bi bi-person-circle-fill fs-2 text-warning"></i>
                                        <span class="text-start">
                                            <strong>Sofía Cárdenas</strong><br>
                                            <small class="text-secondary">Grado 10 · Bogotá</small>
                                        </span>
                                    </figcaption>
                                </figure>
                            </div>
                        </div>
                    </div>
                </div>

                <button class="carousel-control-prev" type="button"
                        data-bs-target="#carruselTestimonios" data-bs-slide="prev">
                    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Testimonio anterior</span>
                </button>
                <button class="carousel-control-next" type="button"
                        data-bs-target="#carruselTestimonios" data-bs-slide="next">
                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Testimonio siguiente</span>
                </button>
            </div>
        </div>
    </section>
```

> ⚠️ **Limpieza de textos:** en el segundo y tercer testimonio se colaron palabras sin sentido. Deja así:
> - Segundo: *"Los profesores responden los mensajes el mismo día. Eso no lo había visto en ningún otro preuniversitario."*
> - Tercero: *"Con la orientación profesional decidí estudiar ingeniería. Estaba entre tres opciones y terminé escogiendo la correcta."*

### Paso 2 — Añade el acordeón de preguntas frecuentes

Pega esto **después** del carrusel**:

```html
    <!-- ===== PREGUNTAS FRECUENTES (ACORDEÓN) ===== -->
    <section class="py-5 bg-body-tertiary" id="preguntas">
        <div class="container">
            <div class="row">
                <div class="col-12 col-lg-4 mb-4 mb-lg-0">
                    <span class="badge text-bg-secondary mb-2">FAQ</span>
                    <h2 class="fw-bold">Preguntas frecuentes</h2>
                    <p class="text-secondary">
                        ¿No encuentras tu duda? Escríbenos y te respondemos en menos de
                        24 horas hábiles.
                    </p>
                    <a href="#contacto" class="btn btn-outline-primary mt-2">Ir al formulario de contacto</a>
                </div>

                <div class="col-12 col-lg-8">
                    <div class="accordion" id="acordeonPreguntas">

                        <div class="accordion-item">
                            <h3 class="accordion-header">
                                <button class="accordion-button" type="button" data-bs-toggle="collapse"
                                        data-bs-target="#pregunta1" aria-expanded="true"
                                        aria-controls="pregunta1">
                                    ¿Necesito tener un buen puntaje para entrar?
                                </button>
                            </h3>
                            <div id="pregunta1" class="accordion-collapse collapse show"
                                 data-bs-parent="#acordeonPreguntas">
                                <div class="accordion-body">
                                    No. La primera semana es de diagnóstico para conocer tu punto
                                    de partida y armar un plan personalizado. Solo condicionamos
                                    la carga horaria semanal que puedas comprometer.
                                </div>
                            </div>
                        </div>

                        <div class="accordion-item">
                            <h3 class="accordion-header">
                                <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
                                        data-bs-target="#pregunta2" aria-expanded="false"
                                        aria-controls="pregunta2">
                                    ¿Las clases son en vivo o grabadas?
                                </button>
                            </h3>
                            <div id="pregunta2" class="accordion-collapse collapse"
                                 data-bs-parent="#acordeonPreguntas">
                                <div class="accordion-body">
                                    Son en vivo por videollamada y además quedan grabadas durante
                                    6 meses. Si no puedes asistir, puedes enviar tu pregunta por
                                    el chat del curso y la responden al día siguiente.
                                </div>
                            </div>
                        </div>

                        <div class="accordion-item">
                            <h3 class="accordion-header">
                                <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
                                        data-bs-target="#pregunta3" aria-expanded="false"
                                        aria-controls="pregunta3">
                                    ¿Qué pasa si no alcanzo a entregar un trabajo?
                                </button>
                            </h3>
                            <div id="pregunta3" class="accordion-collapse collapse"
                                 data-bs-parent="#acordeonPreguntas">
                                <div class="accordion-body">
                                    Tienes hasta 48 horas para entregar después de la fecha límite.
                                    Cada asesor puede activar dos extensiones por cohorte,
                                    siempre que avises con tiempo.
                                </div>
                            </div>
                        </div>

                        <div class="accordion-item">
                            <h3 class="accordion-header">
                                <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
                                        data-bs-target="#pregunta4" aria-expanded="false"
                                        aria-controls="pregunta4">
                                    ¿Ofrecen beca o descuentos?
                                </button>
                            </h3>
                            <div id="pregunta4" class="accordion-collapse collapse"
                                 data-bs-parent="#acordeonPreguntas">
                                <div class="accordion-body">
                                    Sí. Hay dos modalidades: beca por rendimiento académico
                                    (top 10 del cohorte) y descuento del 20 % para estudiantes
                                    de municipios con difícil acceso a internet.
                                </div>
                            </div>
                        </div>

                    </div>
                </div>
            </div>
        </div>
    </section>
```

> ⚠️ **Limpieza de texto:** en la primera respuesta hay caracteres extraños. Deja así: *"No. La primera semana es de diagnóstico para conocer tu punto de partida y armar un plan personalizado. Solo condicionamos la carga horaria semanal que puedas comprometer."*

### Paso 3 — Añade el modal de inscripción

Pega esto **antes del comentario `<!-- ============ FIN DE LA ZONA DE CONTENIDO ============ -->`**, dentro de `<body>`:

```html
    <!-- ===== MODAL DE INSCRIPCIÓN ===== -->
    <div class="modal fade" id="modalInscripcion" tabindex="-1"
         aria-labelledby="tituloModal" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered modal-lg">
            <div class="modal-content">

                <div class="modal-header">
                    <h2 class="modal-title h4" id="tituloModal">Solicitar cupo</h2>
                    <button type="button" class="btn-close" data-bs-dismiss="modal"
                            aria-label="Cerrar"></button>
                </div>

                <div class="modal-body">
                    <p class="text-secondary">
                        Completa tus datos y nuestro equipo te contacta en menos de 24 horas
                        para confirmar el cupo y enviarte la ficha de matrícula.
                    </p>

                    <form id="formularioModal" novalidate>
                        <div class="row g-3">
                            <div class="col-12 col-md-6">
                                <label for="modalNombre" class="form-label">Nombre completo</label>
                                <input type="text" class="form-control" id="modalNombre" required>
                            </div>
                            <div class="col-12 col-md-6">
                                <label for="modalCorreo" class="form-label">Correo</label>
                                <input type="email" class="form-control" id="modalCorreo" required>
                            </div>
                            <div class="col-12">
                                <label for="modalPrograma" class="form-label">Programa</label>
                                <select class="form-select" id="modalPrograma" required>
                                    <option value="" selected disabled>Elegir un programa</option>
                                    <option>Ruta Saber 11</option>
                                    <option>Lectura y escritura</option>
                                    <option>Orientación universitaria</option>
                                </select>
                            </div>
                            <div class="col-12">
                                <label for="modalNota" class="form-label">¿Cuánto llevas transformado?</label>
                                <input type="range" class="form-range" id="modalNota"
                                       min="0" max="100" value="50" step="5">
                            </div>
                        </div>
                    </form>

                    <div class="alert alert-primary d-flex gap-2 mb-0 mt-3" role="note">
                        <i class="bi bi-info-circle-fill"></i>
                        <div class="small">
                            Al enviar aceptas que te contactemos por teléfono o correo.
                            No compartimos tus datos con terceros.
                        </div>
                    </div>
                </div>

                <div class="modal-footer">
                    <button type="button" class="btn btn-outline-secondary"
                            data-bs-dismiss="modal">Cancelar</button>
                    <button type="submit" form="formularioModal" class="btn btn-primary">
                        <i class="bi bi-send me-2"></i>Enviar solicitud
                    </button>
                </div>

            </div>
        </div>
    </div>
```

> 💡 **Detalle elegante:** el botón "Enviar solicitud" está **fuera** del `<form>` (está en el `modal-footer`), por eso lleva `form="formularioModal"`. Es un atributo HTML estándar que conecta un botón con un formulario en otra parte del documento.

### Paso 4 — Abre el modal con JavaScript tras enviar el formulario

Añade esto al final de `js/mi-script.js`, dentro del bloque `(function () { ... })()`:

> 💡 **No te olvides de los botones del Hero y del navbar.** En los módulos anteriores pusimos `href="#inscripcion"`, pero ahora el destino real es el modal. Añádeles los atributos `data-bs-toggle="modal"` y `data-bs-target="#modalInscripcion"`, y cambia el `href` a `#contacto` para que, si el JavaScript falla, el visitante llegue igualmente a una sección útil.

```javascript
    /* --- Abrir el modal de inscripción desde JavaScript --- */
    const modalElement = document.getElementById('modalInscripcion');
    const modalInscripcion = new bootstrap.Modal(modalElement);

    // Interceptar los botones "Inscribirme" de las tarjetas
    document.querySelectorAll('button[data-bs-target="#modalInscripcion"]').forEach(boton => {
        boton.addEventListener('click', evento => {
            evento.preventDefault();  // evitamos que Bootstrap abra el modal sin control
            modalInscripcion.show(); // lo abrimos nosotros
        });
    });

    // Si el formulario del modal se envía, cerramos y avisamos
    const formularioModal = document.getElementById('formularioModal');
    formularioModal.addEventListener('submit', evento => {
        evento.preventDefault();
        if (!formularioModal.checkValidity()) {
            formularioModal.classList.add('was-validated');
            return;
        }
        modalInscripcion.hide();
        alert('¡Gracias! Te contactaremos en menos de 24 horas.');
        formularioModal.reset();
    });

    modalElement.addEventListener('shown.bs.modal', () => {
        document.getElementById('modalNombre').focus();
    });
```

### Paso 5 — Prueba el teclado en los componentes

| Prueba | Resultado esperado |
|--------|--------------------|
| En el carrusel, pulsa `Tab` hasta el botón de avance | Se mueve solo si lo dejas 3 segundos sin tocar nada |
| En el acordeón, `Tab` + `Enter` | Abre y cierra cada pregunta |
| Pulsa `Esc` con el modal abierto | El modal se cierra |
| Con el modal abierto, pulsa `Tab` varias veces | El foco **no puede salir** del modal (cerrojo de foco) |
| Con el modal abierto, haz clic fuera del cuadro | Se cierra |

---

## 👀 Qué deberías ver

- ✅ Un carrusel que avanza solo cada 6 segundos, con flechas e indicadores; se puede arrastrar con el dedo.
- ✅ Un acordeón donde, al abrir una pregunta, **se cierra la anterior** (por `data-bs-parent`).
- ✅ Un modal centrado con formulario, que se abre desde los botones "Inscribirme" de las tarjetas.
- ✅ El modal se cierra con la `X`, con "Cancelar", con `Esc` y con un clic fuera.
- ✅ Al enviar el formulario del modal, se cierra y aparece una confirmación.

---

## ⚠️ Errores comunes y cómo solucionarlos

| Síntoma | Causa probable | Solución |
|---------|----------------|----------|
| El modal no se abre | Falta `bootstrap.bundle.min.js`, o el `id` no coincide | Revisa el `id` en el `data-bs-target` y en el `div.modal` |
| El modal aparece sin fondo oscuro | Falta la clase `fade` o el backdrop no se aplica | Usa `class="modal fade"` |
| El modal sale pegado a la parte superior | Falta `modal-dialog-centered` | Añádela al `.modal-dialog` |
| El carrusel no se mueve solo | Falta `data-bs-ride="carousel"` en el `.carousel` | Revisa que la clase sea `carousel slide` |
| El carrusel muestra los 3 textos apilados | Falta `carousel-item` o `active` | Cada diapositiva necesita `carousel-item`, y la primera además `active` |
| El acordeón deja varios abiertos | Falta `data-bs-parent` en los `.accordion-collapse` | Todos los paneles deben apuntar al mismo `#id` del `.accordion` |
| El texto del carrusel "se mueve" al cerrar | Usé transiciones CSS mías | Elimina tus reglas de `transition` sobre esos elementos |
| Al enviar el modal, la página hace scroll arriba | El `<button type="submit">` no apunta a ningún `form` | Añade `form="formularioModal"` |
| El modal se queda abierto tras enviar | Olvidé `modalInscripcion.hide()` | Revisa el `addEventListener('submit', ...)` |
| Los íconos de flecha no se ven | No cargó Bootstrap Icons o falta `bootstrap-icons.min.css` | Verifica el `<link>` |

---

## 💪 Mini-ejercicio de práctica

**Reto:** convierte tu sitio en algo más interactivo.

Requisitos:

1. **Offcanvas en móvil.** Añade un botón "Menú" en el navbar que solo se vea en móvil (`d-lg-none`) y que abra un menú lateral con `offcanvas offcanvas-start`. Debe contener los mismos enlaces.
2. **Modal de "Ver programa completo"** distinto del de inscripción: al hacer clic en el título de una tarjeta (`card-title`), se abre un modal con la descripción larga del programa.
3. **Acordeón** en la sección de programas con 3 preguntas específicas de cada programa (no las FAQ generales).
4. **Carrusel** de logos de universidades en la sección de cifras, con `carousel-dark` e `data-bs-interval="3000"`.
5. **Tooltip** en el botón de WhatsApp: `data-bs-toggle="tooltip" title="Respondemos en minutos"` e inicialízalo con `new bootstrap.Tooltip(el)`.
6. **Popover** con el horario de atención en el icono del reloj, en la sección de contacto.

**Pista para el offcanvas:**

```html
<button class="btn btn-outline-light d-lg-none" type="button"
        data-bs-toggle="offcanvas" data-bs-target="#menuLateral" aria-controls="menuLateral">
    <i class="bi bi-list"></i>
</button>

<div class="offcanvas offcanvas-start" tabindex="-1" id="menuLateral" aria-labelledby="menuLateralLabel">
    <div class="offcanvas-header">
        <h5 class="offcanvas-title" id="menuLateralLabel">RutaUni</h5>
        <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Cerrar"></button>
    </div>
    <div class="offcanvas-body">
        <ul class="nav flex-column gap-2">
            <li class="nav-item"><a class="nav-link" href="#programas">Programas</a></li>
        </ul>
    </div>
</div>
```

**Pista para tooltip:** los tooltips **no** se inicializan solos. Necesitan:

```javascript
document.querySelectorAll('[data-bs-toggle="tooltip"]').forEach(el => {
    new bootstrap.Tooltip(el);
});
```

**Autocomprobación:** el tooltip debe aparecer al pasar el ratón **y** al enfocar con el teclado (requisito de accesibilidad). Si solo funciona con el ratón, revisa que el elemento sea `focusable` (un `<a href>` o un `<button>` lo es; un `<span>` no).

---

## ✅ Punto de control — Módulo 7

- [ ] Entiendo el patrón `data-bs-toggle` + `data-bs-target` + `id`.
- [ ] Mi carrusel tiene `carousel slide`, `data-bs-ride`, `carousel-inner`, `carousel-item` y un `active`.
- [ ] Los indicadores tienen `aria-label`.
- [ ] Mi acordeón usa `accordion`, `accordion-item`, `accordion-button`, `accordion-collapse` y `data-bs-parent`.
- [ ] Solo un panel del acordeón está abierto a la vez.
- [ ] Mi modal tiene `modal fade`, `modal-dialog`, `modal-header/body/footer` y `tabindex="-1"`.
- [ ] El modal se cierra con `X`, Cancelar, `Esc` y clic fuera.
- [ ] Sé abrir un componente con `new bootstrap.Modal(...)` y `.show()`.
- [ ] Probé el cerrojo de foco (`Tab`) dentro del modal.
- [ ] Limpié los textos con ruido de los ejemplos.
- [ ] Completé el ejercicio con offcanvas, tooltip y popover.

---
# Módulo 8 · Personalización, modo oscuro y Sass

**⏱️ Tiempo estimado: 20 minutos**

## 🎯 Objetivo de aprendizaje

- Cambiar los **colores del tema** con variables CSS (sin recompilar nada).
- Implementar el **modo oscuro** con `data-bs-theme` y un botón que lo recuerda.
- Entender qué es **Sass** y por qué existe, sin necesitarlo todavía.
- Personalizar fondos, tarjetas y botones con clases propias.

## 📖 Explicación conceptual

### Variables CSS

Desde Bootstrap 5.3, **todos** los colores del tema son variables CSS con prefijo `--bs-`. Eso significa que puedes escribir en tu CSS:

```css
:root {
    --bs-primary: #6f42c1;
}
```

y **toda** la biblioteca cambia de color: botones, enlaces, badges, bordes, enfoque de formularios, indicadores del carrusel. Es el mismo principio que las variables de diseño de Figma o de un token de color, solo que en CSS puro. Por eso 5.3 se consideró una versión tan importante: la personalización dejó de requerir recompilar Sass.

Variables que conviene conocer:

| Variable | Para qué |
|----------|----------|
| `--bs-primary`, `--bs-secondary`, `--bs-success`, `--bs-danger`, `--bs-warning`, `--bs-info` | Colores del tema |
| `--bs-body-bg`, `--bs-body-color` | Fondo y color de texto del cuerpo |
| `--bs-border-color`, `--bs-border-radius`, `--bs-border-radius-lg` | Bordes |
| `--bs-link-color`, `--bs-link-hover-color` | Enlaces |
| `--bs-font-sans-serif` | Tipografía |

### Modo oscuro

Bootstrap 5.3 trae el modo oscuro **nativo**: basta poner `data-bs-theme="dark"` en el elemento `<html>` y toda la página (incluidos `.card`, `.form-control`, `.dropdown-menu` y las variables `--bs-*`) cambia de tono sol **`@media (prefers-color-scheme: dark)`**. Es decir, si el sistema del usuario está en oscuro, puedes respetarlo sin escribir JavaScript:

```css
@media (prefers-color-scheme: dark) {
    /* aquí puedes aplicar ajustes propios si los necesitas */
}
```

### Sass

**Sass** es un *preprocesador* de CSS: escribes un lenguaje parecido a CSS con variables, anidamiento, bucles y funciones, y una herramienta lo compila a CSS normal. Bootstrap está escrito en Sass, y por eso existían los "themes" que se compilaban a un `bootstrap.css` propio.

Hoy, con las variables CSS nativas, **no necesitas Sass** para cambiar colores. Pero conviene conocerlo porque:

- Los equipos grandes usan tokens y bucles para mantener sistemas de diseño.
- Es el paso natural hacia frameworks como Tailwind, Bulma o Foundation.
- Si más adelante quieres *cambiar el comportamiento* de un componente (no solo sus colores), Sass te da el poder de reescribirlo.

**Alternativas modernas que verás pronto:** CSS Nesting y módulos nativos (`@layer`, `@scope`), que ya existen en los navegadores modernos. Muestra de CSS anidado moderno (aún no universal):

```css
.card {
    border-radius: 1rem;

    .card-title {
        color: var(--bs-primary);
    }
}
```

---

## 🛠️ Pasos

### Paso 1 — Define tu identidad visual

Abre `css/estilos.css` y pega:

```css
/* ============================================================
   RutaUni · Estilos personalizados
   Cargados DESPUÉS de Bootstrap, por eso ganan en empate
   ============================================================ */

/* ---------- 1. Identidad de color ---------- */
:root {
    /* Paleta de la marca (búscala en https://coolors.co para crear la tuya) */
    --rutuni-azul: #1f3a8a;
    --rutuni-lima: #a3e635;
    --rutuni-naranja: #f97316;

    /* Le decimos a Bootstrap que use nuestros colores */
    --bs-primary: var(--rutuni-azul);
    --bs-link-color: var(--rutuni-azul);
    --bs-link-hover-color: #16306f;

    /* Fuente: usamos la del sistema, sin descargas externas */
    --bs-body-font-family: system-ui, -apple-system, "Segoe UI", Roboto,
                            "Helvetica Neue", Arial, sans-serif;
}

/* ---------- 2. Fondo del sitio y textos largos ---------- */
body {
    background-color: var(--bs-body-bg);

    /* En móvil los textos largos (correos, URLs) se parten antes de provocar
       un desplazamiento horizontal de toda la página. Ojo: `anywhere`, no
       `break-word`, porque es el único que reduce también el ancho mínimo
       de las celdas de una rejilla. */
    overflow-wrap: anywhere;
    word-break: break-word;
}

/* ---------- 3. Texturas y detalles propios ---------- */
.rounded-4 {
    border-radius: 1.25rem !important;
}

.text-rutuni-lima {
    color: var(--rutuni-lima) !important;
}

.bg-rutuni-lima {
    background-color: var(--rutuni-lima);
    color: #1a2e05;
}

/* Degradado para el hero, usado con la clase .hero-degradado */
.hero-degradado {
    background-image:
        radial-gradient(circle at 15% 20%, rgba(163, 230, 53, .25), transparent 45%),
        radial-gradient(circle at 85% 10%, rgba(249, 115, 22, .30), transparent 40%),
        linear-gradient(135deg, var(--rutuni-azul) 0%, #2b1a6b 100%);
}

/* Tarjetas con un detalle superior de color */
.tarjeta-programa {
    border-top: 4px solid var(--rutuni-azul);
    transition: transform .2s ease, box-shadow .2s ease;
}

.tarjeta-programa:hover,
.tarjeta-programa:focus-within {
    transform: translateY(-4px);
    box-shadow: 0 1rem 1.5rem rgba(0, 0, 0, .12);
}

/* ---------- 4. Modo oscuro ---------- */
[data-bs-theme="dark"] {
    --rutuni-azul: #93c5fd;
    --rutuni-lima: #bef264;
    --rutuni-naranja: #fdba74;

    --bs-link-color: #93c5fd;
    --bs-link-hover-color: #bfdbfe;
}

/* En modo oscuro el degradado del hero se oscurece */
[data-bs-theme="dark"] .hero-degradado {
    background-image:
        radial-gradient(circle at 15% 20%, rgba(163, 230, 53, .15), transparent 45%),
        radial-gradient(circle at 85% 10%, rgba(249, 115, 22, .18), transparent 40%),
        linear-gradient(135deg, #101a3d 0%, #1a1030 100%);
}

/* Respetamos la preferencia del sistema si el visitante no ha elegido nada */
@media (prefers-color-scheme: dark) {
    :root:not([data-bs-theme="light"]) {
        color-scheme: dark;
    }
}

/* ---------- 5. Impresión ---------- */
@media print {
    .navbar,
    footer,
    .btn {
        display: none !important;
    }

    body {
        background: #fff;
        color: #000;
    }
}
```

Y cambia la primera línea del Hero en `index.html` para usar tu degradado:

```html
    <header class="hero-degradado text-white py-5" id="inicio">
```

### Paso 2 — Añade el botón de modo oscuro

Añade este bloque dentro del `navbar-collapse`, justo antes del `<form>` de búsqueda:

```html
                <button class="btn btn-outline-light btn-sm ms-lg-3" type="button" id="botonTema">
                    <i class="bi bi-moon-stars-fill" id="iconoTema" aria-hidden="true"></i>
                    <span class="visually-hidden">Cambiar entre tema claro y oscuro</span>
                </button>
```

### Paso 3 — Guarda la preferencia con JavaScript

Añade al final de `js/mi-script.js` (fuera del `if (!formulario) return;`, para que funcione siempre):

```javascript
/* --- Modo claro / oscuro con memoria --- */
(function () {
    'use strict';

    const botonTema = document.getElementById('botonTema');
    const iconoTema = document.getElementById('iconoTema');
    const clave = 'rutuni-tema';

    function aplicarTema(tema) {
        document.documentElement.setAttribute('data-bs-theme', tema);
        if (iconoTema) {
            iconoTema.className = tema === 'dark' ? 'bi bi-sun-fill' : 'bi bi-moon-stars-fill';
        }
        try {
            localStorage.setItem(clave, tema);
        } catch (e) {
            /* modo privado: seguimos funcionando sin guardar */
        }
    }

    // 1. Al cargar: usar lo guardado, o la preferencia del sistema
    let temaGuardado = null;
    try {
        temaGuardado = localStorage.getItem(clave);
    } catch (e) { /* sin almacenamiento */ }

    const sistemaPrefiereOscuro = window.matchMedia('(prefers-color-scheme: dark)').matches;
    aplicarTema(temaGuardado || (sistemaPrefiereOscuro ? 'dark' : 'light'));

    // 2. Al hacer clic: alternar
    if (botonTema) {
        botonTema.addEventListener('click', () => {
            const actual = document.documentElement.getAttribute('data-bs-theme');
            aplicarTema(actual === 'dark' ? 'light' : 'dark');
        });
    }
})();
```

> 💡 **`localStorage`** es almacenamiento del navegador, por dominio, que sobrevive al cerrar la pestaña. Es el lugar correcto para recordar una preferencia de tema. Se envuelve en `try/catch` porque en modo incógnito puede lanzar errores.

### Paso 4 — Comprueba el modo oscuro

| Prueba | Resultado esperado |
|--------|--------------------|
| Haz clic en el botón de la luna | Todo el sitio cambia a oscuro: fondos, tarjetas, campos de formulario, textos |
| Recarga la página | El tema oscuro **se mantiene** (viene de `localStorage`) |
| Cambia el tema de tu sistema operativo a oscuro y entra por primera vez | El sitio arranca en oscuro |
| Pasa el ratón por una tarjeta | Se eleva suavemente (`transform`) |
| Ctrl + P (imprimir) | Solo se imprime el contenido, sin navbar ni botones |

### Paso 5 — Alternativa sin CDN (archivos locales)

Si tu proyecto se va a usar **sin conexión**, descarga los archivos:

1. Ve a <https://github.com/twbs/bootstrap/releases/tag/v5.3.8>.
2. Descarga el `bootstrap-5.3.8-dist.zip`.
3. Copia `dist/css/bootstrap.min.css` a `rutouni/css/vendor/`.
4. Copia `dist/js/bootstrap.bundle.min.js` a `rutouni/js/vendor/`.
5. Cambia los `<link>` y `<script>` por rutas locales:

```html
    <link rel="stylesheet" href="css/vendor/bootstrap.min.css">
    <script src="js/vendor/bootstrap.bundle.min.js"></script>
```

---

## 👀 Qué deberías ver

- ✅ Tu sitio con la **identidad de color propia**: azul institucional, lima y naranja, en lugar del azul por defecto de Bootstrap.
- ✅ Un hero con degradado con luces suaves, en vez de un color plano.
- ✅ Un botón de luna/sol en el navbar que cambia **toda** la página de tema.
- ✅ La preferencia guardada: al recargar, el tema se mantiene.
- ✅ Tarjetas que se elevan al pasar el ratón.

---

## ⚠️ Errores comunes y cómo solucionarlos

| Síntoma | Causa probable | Solución |
|---------|----------------|----------|
| Cambié `--bs-primary` y nada cambia | Tu CSS está en un orden incorrecto o el selector no es `:root` | Debe ir en `:root`, dentro de `css/estilos.css`, que ya se carga después de Bootstrap |
| Solo cambian algunos componentes | Sobrescribiste `--bs-primary` pero no `--bs-link-color` | Cambia las variables de enlaces por separado (`--bs-link-color`) |
| El modo oscuro se ve a medias | Hay colores fijos tuyos con `#ffffff` o `#000` | Usa variables (`--bs-body-bg`) en lugar de colores literales |
| El botón del tema no aparece | Está dentro de un `d-none d-lg-block` | Colócalo fuera de un contenedor oculto o quítale ese `display` |
| `localStorage is not defined` | El script corre en el navegador pero tipaste mal la variable | Revisa el nombre: es `localStorage` en minúscula con `S` mayúscula |
| Cambia de tema pero se nota un destello blanco | El JS carga al final del `<body>` | Añade una línea en línea en el `<head>` que aplique el tema temprano (ver abajo) |
| `Cannot read properties of null` | `getElementById` devolvió `null` | El script debe cargarse **después** del HTML, o debes validar que el elemento exista |
| El degradado del hero se ve negro en modo oscuro | Mi CSS sobrescribe el `background-image` sin considerar el tema | Usa `[data-bs-theme="dark"] .hero-degradado` |

**Para evitar el destello blanco**, agrega esto justo después del `<title>` en el `<head>`:

```html
    <script>
        try {
            var t = localStorage.getItem('rutuni-tema');
            if (!t) t = matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
            document.documentElement.setAttribute('data-bs-theme', t);
        } catch (e) {}
    </script>
```

---

## 💪 Mini-ejercicio de práctica

**Reto:** dale a tu sitio una identidad propia completa.

Requisitos:

1. Genera una paleta de 5 colores en <https://coolors.co> y aplícala con variables (`--mi-color-1` … `--mi-color-5`).
2. Cambia `--bs-primary`, `--bs-link-color` y `--bs-body-font-family` por los tuyos.
3. Aplica `rounded-4` a las tarjetas, con un valor de radio **mayor** que el de Bootstrap.
4. Crea una clase `.seccion-alterna` que aplique `bg-body-tertiary` y `py-5` de una vez, y aplícala a dos secciones.
5. Añade un borde de **degradado** en la parte superior del footer:

```css
.footer-borde {
    border-top: 4px solid transparent;
    border-image: linear-gradient(90deg, var(--rutuni-lima), var(--rutuni-naranja), var(--rutuni-azul)) 1;
}
```

6. En modo oscuro, baja el brillo del fondo con `--bs-body-bg: #121212` y verifica que los textos siguen teniendo contraste suficiente.
7. Añade un **botón propio** reutilizando las variables de Bootstrap:

```css
.btn-marca {
    --bs-btn-bg: var(--rutuni-naranja);
    --bs-btn-border-color: var(--rutuni-naranja);
    --bs-btn-hover-bg: #ea580c;
    --bs-btn-hover-border-color: #ea580c;
    --bs-btn-color: #fff;
    --bs-btn-hover-color: #fff;
}
```

8. Define además un modo "alto contraste" con `[data-bs-theme="dark"]` y bordes blancos en los inputs.

**Autocomprobación:** haz una prueba de contraste. Todos los textos deben cumplir al menos **4.5:1** de ratio contra su fondo. Usa la herramienta <https://webaim.org/resources/contrastchecker/>.

---

## ✅ Punto de control — Módulo 8

- [ ] Sé qué son las variables CSS y por qué Bootstrap 5.3 las expone.
- [ ] Cambié `--bs-primary` y el sitio entero cambió de color.
- [ ] Sé la diferencia entre `--bs-primary` y `--bs-link-color`.
- [ ] Entiendo que `data-bs-theme="dark"` activa el modo oscuro nativo.
- [ ] Mi botón de tema alterna claro/oscuro y guarda la preferencia.
- [ ] Uso `localStorage` dentro de un `try/catch`.
- [ ] Respeta la preferencia del sistema con `prefers-color-scheme`.
- [ ] Sé qué es Sass y por qué todavía **no** lo necesito.
- [ ] Sé dónde descargar Bootstrap para usarlo sin CDN.
- [ ] Completé la identidad visual del ejercicio.

---
# Módulo 9 · Integración final, buenas prácticas y accesibilidad

**⏱️ Tiempo estimado: 15 minutos**

## 🎯 Objetivo de aprendizaje

- Añadir el **footer** multi-columna y cerrar el documento correctamente.
- Aplicar la checklist de **accesibilidad** de Bootstrap.
- Ordenar tu código para que sea mantenible.
- Verificar que todo el sitio funciona de principio a fin.

## 📖 Explicación conceptual

Un sitio terminado no es solo "se ve bien": también tiene que ser **accesible** (que lo pueda usar alguien con roles visuales reducidos, teclado únicamente o lector de pantalla), **rápido** (no depender de lo que no necesita) y **mantenible** (que tú puedas encontrar y cambiar algo en seis meses).

### Las cuatro reglas de accesibilidad que más se incumplen

| Regla | Cómo se cumple en Bootstrap |
|-------|------------------------------|
| **Contraste** | No uses `text-secondary` sobre `bg-light` sin verificar; usa pares como `bg-primary-subtle` + `text-primary-emphasis` |
| **Color no es el único mensaje** | Si un campo está mal, no basta el borde rojo: añade `.invalid-feedback` con texto |
| **Teclado** | Todo debe ser alcanzable con `Tab` y activable con `Enter`/`Espacio`; nada debe depender del ratón |
| **Etiquetas visibles** | Iconos solos (`<i class="bi bi-whatsapp">`) necesitan `aria-label` o texto oculto con `.visually-hidden` |

### HTML semántico

Bootstrap te da el estilo, pero el significado lo pones tú:

| Elemento | Para qué en tu sitio |
|----------|---------------------|
| `<header>` | Cabecera principal del Hero |
| `<nav>` | La barra de navegación (ya lo usas) |
| `<main>` | **Todo** el contenido principal; debe haber **uno solo** |
| `<section>` | Cada bloque temático; lleva su `id` para las anclas |
| `<article>` | Cada tarjeta de programa y cada testimonio |
| `<aside>` | La barra lateral de contacto |
| `<footer>` | Pie del sitio |

> ⚠️ **Error muy común:** tener varios `<main>` o dejar el contenido principal fuera de `<main>`. Los lectores de pantalla usan esta etiqueta para saltar directamente al contenido.

---

## 🛠️ Pasos

### Paso 1 — Reestructura el `body` con etiquetas semánticas

Tu `index.html` debería quedar con esta jerarquía:

```html
<body>

    <nav class="navbar ..."> ... </nav>          <!-- navbar del Módulo 4 -->

    <main id="contenido">

        <header class="hero-degradado text-white py-5" id="inicio"> ... </header>

        <section class="py-5 bg-body-tertiary" id="cifras"> ... </section>

        <section class="py-5" id="programas"> ... </section>

        <section class="py-5" id="testimonios"> ... </section>

        <section class="py-5 bg-body-tertiary" id="preguntas"> ... </section>

        <section class="py-5" id="contacto"> ... </section>

    </main>

    <footer class="footer-borde bg-body-tertiary py-5"> ... </footer>

    <div class="modal fade" id="modalInscripcion" ...> ... </div>

    <script src="js/mi-script.js"></script>

</body>
```

Envuelve **todas** las secciones (menos el navbar y el footer) dentro de `<main id="contenido">`.

### Paso 2 — Añade el enlace de salto al contenido

Justo después de `<body>` y **antes** del `<nav>`, agrega:

```html
    <a href="#contenido" class="visually-hidden-focusable btn btn-primary position-absolute top-0 start-0 m-2">
        Saltar al contenido principal
    </a>
```

Este enlace es **invisible** hasta que alguien navega con el teclado; entonces aparece y permite saltar toda la navegación. Es una de las veinte cosas más recomendadas en accesibilidad web.

### Paso 3 — Añade el footer

Pega esto **después de `</main>`**:

```html
    <!-- ===== FOOTER ===== -->
    <footer class="footer-borde bg-body-tertiary py-5 mt-5" id="contacto-footer">
        <div class="container">
            <div class="row g-4">

                <div class="col-12 col-md-4">
                    <a class="d-inline-flex align-items-center gap-2 mb-3 text-decoration-none" href="#inicio">
                        <i class="bi bi-compass fs-3 text-primary"></i>
                        <span class="fw-bold fs-5">RutaUni</span>
                    </a>
                    <p class="text-secondary">
                        Preuniversitario virtual para estudiantes de grado 10 y 11 en
                        Colombia. Acompañamiento desde 2019.
                    </p>
                    <div class="d-flex gap-2">
                        <a href="#" class="btn btn-sm btn-outline-light rounded-circle" aria-label="Instagram de RutaUni">
                            <i class="bi bi-instagram" aria-hidden="true"></i>
                        </a>
                        <a href="#" class="btn btn-sm btn-outline-light rounded-circle" aria-label="TikTok de RutaUni">
                            <i class="bi bi-tiktok" aria-hidden="true"></i>
                        </a>
                        <a href="#" class="btn btn-sm btn-outline-light rounded-circle" aria-label="YouTube de RutaUni">
                            <i class="bi bi-youtube" aria-hidden="true"></i>
                        </a>
                    </div>
                </div>

                <div class="col-6 col-md-2 offset-md-1">
                    <h2 class="h6 text-uppercase text-secondary">Programas</h2>
                    <ul class="list-unstyled d-grid gap-2">
                        <li><a class="link-secondary link-underline-opacity-0 link-underline-opacity-100-hover" href="#programas">Ruta Saber 11</a></li>
                        <li><a class="link-secondary link-underline-opacity-0 link-underline-opacity-100-hover" href="#programas">Lectura y escritura</a></li>
                        <li><a class="link-secondary link-underline-opacity-0 link-underline-opacity-100-hover" href="#programas">Orientación universitaria</a></li>
                    </ul>
                </div>

                <div class="col-6 col-md-2">
                    <h2 class="h6 text-uppercase text-secondary">Recursos</h2>
                    <ul class="list-unstyled d-grid gap-2">
                        <li><a class="link-secondary" href="#preguntas">Preguntas frecuentes</a></li>
                        <li><a class="link-secondary" href="#contacto">admisiones@rutuni.edu.co</a></li>
                        <li><a class="link-secondary" href="#contacto">+57 300 123 4567</a></li>
                    </ul>
                </div>

                <div class="col-12 col-md-3">
                    <h2 class="h6 text-uppercase text-secondary">Horario de atención</h2>
                    <p class="text-secondary small mb-2">
                        Lunes a viernes, 7:00 a. m. – 8:00 p. m.<br>
                        Sábados, 8:00 a. m. – 2:00 p. m.
                    </p>
                    <p class="small mb-0">
                        <i class="bi bi-geo-alt me-1"></i>Medellín, Colombia · Cobertura nacional
                    </p>
                </div>

            </div>

            <hr class="my-4">

            <div class="row align-items-center g-3">
                <div class="col-12 col-md-6">
                    <p class="small text-secondary mb-0">
                        © 2026 RutaUni. Proyecto educativo de ejemplo.
                    </p>
                </div>
                <div class="col-12 col-md-6">
                    <ul class="list-inline d-flex flex-wrap justify-content-md-end gap-3 mb-0 small">
                        <li class="list-inline-item"><a class="link-secondary" href="#">Términos</a></li>
                        <li class="list-inline-item"><a class="link-secondary" href="#">Privacidad</a></li>
                        <li class="list-inline-item"><a class="link-secondary" href="#">Contáctanos</a></li>
                    </ul>
                </div>
            </div>
        </div>
    </footer>
```

### Paso 4 — Etiqueta las imágenes e iconos

Revisa tu página y confirma:

| Elemento | Correcto |
|----------|----------|
| Imagen con contenido | `<img src="..." alt="Aula virtual con estudiantes trabajando">` |
| Imagen decorativa | `<img src="..." alt="">` (alt vacío = decorativa) |
| Botón solo con icono | `<button aria-label="Cerrar">` o `<span class="visually-hidden">Cerrar</span>` |
| Enlace a WhatsApp | Texto visible ("Escríbenos por WhatsApp"), no solo el ícono |
| Emoji o abreviatura sin explicación | Añade `title` o texto oculto |

### Paso 5 — Pasa la checklist final de calidad

Imprime esta lista y revísala en serio antes de dar por terminado el proyecto:

**Estructura**
- [ ] Hay **un solo** `<main>` y todo el contenido principal está dentro.
- [ ] El documento empieza con `<!DOCTYPE html>` y tiene `<html lang="es">`.
- [ ] Solo hay un `<h1>` en la página (el del Hero).
- [ ] Los encabezados están en orden lógico: `h1` → `h2` → `h3`, sin saltarse niveles.
- [ ] La pestaña del navegador se ve bien en móvil, con el ícono correcto.

**Estructura del código**
- [ ] Bootstrap 5.3.8 (no 4, no jQuery).
- [ ] Las clases CSS están agrupadas por sección en el HTML, con comentarios.
- [ ] No hay estilos inline salvo excepciones justificadas (`style` de altura mínima).
- [ ] El CSS propio está todo en `css/estilos.css`, no esparcido en `<style>`.
- [ ] El JS propio está en `js/mi-script.js`, no en bloques sueltos.

**Comportamiento**
- [ ] El menú móvil abre y cierra.
- [ ] El formulario no envía con datos inválidos y avisa de los errores.
- [ ] El modal abre, cierra y atrapa el foco.
- [ ] El acordeón y el carrusel funcionan con teclado.
- [ ] El tema claro/oscuro se recuerda al recargar.

**Accesibilidad**
- [ ] Todo se puede usar solo con teclado y el foco siempre es visible.
- [ ] Todas las imágenes tienen `alt`.
- [ ] Todos los controles de formulario tienen `label`.
- [ ] Los botones solo con ícono tienen `aria-label`.
- [ ] Hay un enlace de "Saltar al contenido".
- [ ] Los colores tienen contraste suficiente (mínimo 4.5:1).

**Rendimiento y semántica**
- [ ] No hay imágenes de más de 200 KB sin optimizar.
- [ ] Los enlaces externos con `target="_blank"` llevan `rel="noopener"`.
- [ ] Los enlaces de teléfono y correo usan `tel:` y `mailto:`.

### Paso 6 — Herramientas de revisión que te ahorrarán tiempo

| Herramienta | Qué revisa | Enlace |
|-------------|-----------|--------|
| W3C Markup Validator | Errores de HTML | <https://validator.w3.org/nu/> |
| WAVE | Accesibilidad visual | <https://wave.webaim.org/> |
| Chrome Lighthouse | Rendimiento, SEO, accesibilidad | Incluido en Chrome: pestaña *Lighthouse* en F12 |
| CSS Specificity Calculator | Por qué gana una regla | <https://specificity.keegan.st/> |

Corre el validador de HTML sobre tu `index.html`: es la forma más rápida de encontrar etiquetas sin cerrar o atributos mal escritos.

---

## 👀 Qué deberías ver

- ✅ Un footer oscuro/claro con 4 columnas, iconos sociales, horario y créditos legales.
- ✅ Un borde de color degradado arriba del footer.
- ✅ Al pulsar `Tab` como primera interacción, aparece el enlace "Saltar al contenido principal".
- ✅ El sitio completo se puede recorrer **sin tocar el ratón**.
- ✅ El validador de HTML reporta **0 errores** (pueden quedar avisos, que son distintos de errores).

---

## ⚠️ Errores comunes y cómo solucionarlos

| Síntoma | Causa probable | Solución |
|---------|----------------|----------|
| Hay varios `<h1>` | Cada sección tiene su propio `h1` | Deja un solo `h1` (el Hero) y usa `h2` en las secciones |
| El enlace de salto no aparece | Le puse `visually-hidden` en vez de `visually-hidden-focusable` | Usa `visually-hidden-focusable` |
| El texto del footer es ilegible | `text-secondary` sobre un fondo también claro | Usa `bg-body-tertiary` (ya definido por el tema) y revisa el contraste |
| El sitio "salta" de color al cargar | El tema se aplica tarde | Añade el script en línea del Módulo 8 en el `<head>` |
| El validador reporta `<main>` duplicado | Puse un `<main>` dentro de cada `<section>` | Solo uno, y las `<section>` van **dentro** |
| Un enlace abre otra pestaña sin avisar | Falta `rel="noopener"` | Añádelo siempre que uses `target="_blank"` |
| Lighthouse da mala nota en rendimiento | Imágenes muy pesadas o scripts bloqueantes | Comprime imágenes (WebP), y considera `defer` en los scripts |

---

## 💪 Mini-ejercicio de práctica

**Reto:** audita tu sitio como lo haría un revisor externo.

Requisitos:

1. Pasa el validador W3C y deja el HTML con **0 errores**.
2. Pasa Lighthouse y anota las cuatro puntuaciones (rendimiento, accesibilidad, buenas prácticas, SEO).
3. Corrige todo lo que esté por debajo de 90 en accesibilidad y buenas prácticas.
4. Verifica con teclado: no debe haber ningún elemento "atascado" (un elemento que nunca recibe foco aunque debería).
5. Comprueba que el sitio sigue siendo usable a **400 % de zoom** (Ctrl + `+` varias veces).

**Pista:** si Lighthouse señala "los botones no tienen nombres accesibles", busca botones con solo un `<i>` dentro y añádeles `aria-label` o `.visually-hidden`.

---

## ✅ Punto de control — Módulo 9

- [ ] Todo el contenido principal está dentro de un único `<main>`.
- [ ] Usé `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<aside>` y `<footer>` con sentido.
- [ ] Solo hay un `<h1>` y los encabezados no se saltan niveles.
- [ ] Añadí el enlace de saltar al contenido con `visually-hidden-focusable`.
- [ ] Mi footer tiene 4 columnas y un borde degradado.
- [ ] Todas las imágenes y botones de ícono tienen `alt` / `aria-label`.
- [ ] El validador de HTML reporta 0 errores.
- [ ] Lighthouse me da 90 o más en accesibilidad.
- [ ] Completé la auditoría del ejercicio.

---

# Módulo 10 · Reto final y siguientes pasos

**⏱️ Tiempo estimado: 10 minutos**

## 🎯 Objetivo de aprendizaje

- Planificar y ejecutar un proyecto Bootstrap **sin ayuda**.
- Saber qué ruta seguir para seguir aprendiendo.

## 📖 Explicación conceptual

Hasta aquí seguiste una guía. Lo que te falta es la práctica de tomar decisiones **sin** una guía que te diga qué clase usar. Este módulo es exactamente eso: un proyecto con un enunciado y sin solución.

## 🛠️ El reto

### Enunciado: landing page "Silla Vacía" (festival de música)

Construye, **sin consultar los módulos anteriores**, una landing page para un festival de música juvenil en Medellín. Debe tener:

| Requisito | Detalle |
|-----------|---------|
| **Navbar** | Marca a la izquierda, 4 enlaces, botón de compra de entradas, colapsa en móvil |
| **Hero** | Fondo de color o imagen, `h1` con el nombre del festival, fecha y ciudad, botón de CTA |
| **Cartas de grupos** | Al menos 3 bandas/artistas con imagen, nombre, género y día |
| **Contador** | Una franja con 3 datos (número de artistas, días, asistentes esperados) |
| **Programa** | Un **acordeón** con los 3 días del festival y sus horarios |
| **Carrusel** | Galerías de fotos de ediciones anteriores |
| **Formulario** | Compra de entradas: nombre, correo, cantidad de entradas (select 1–6), fecha de nacimiento, checkbox de términos, botón de pago |
| **Modal** | Confirmación de la compra con el resumen del pedido |
| **Footer** | 3 columnas: información, redes, contacto |
| **Modo oscuro** | Botón que cambia el tema y lo recuerda |

### Reglas

1. **No uses CSS propio** salvo para el degradado del hero y el botón de cambio de tema.
2. Cada sección debe tener su `id` y funcionar con anclas.
3. Debe verse bien a 375 px, 768 px y 1440 px de ancho.
4. Debe ser navegable solo con teclado.
5. Entrega el proyecto con un archivo `README.md` que explique cómo abrirlo.

### Cómo saber si lo lograste

- [ ] No tuviste que buscar "cómo se hace un navbar en Bootstrap" más de dos veces.
- [ ] Entendiste por qué usaste cada clase (aunque uses clases como `g-4`, `py-5`, `h-100`, `mt-auto`).
- [ ] Pudiste explicar en voz alta cómo se relacionan `container`, `row` y `col`.
- [ ] Cerraste el proyecto con menos de 15 líneas de JavaScript propias.

## 👀 Qué deberías ver

- ✅ Una landing page completa con **9 secciones distintas**, sin nada roto en ninguna resolución.
- ✅ Ninguna sección descoloca a 375 px, 768 px ni 1440 px de ancho.
- ✅ Un modal de confirmación que **muestra el resumen** (artista + cantidad + total).
- ✅ El tema oscuro con su botón, y un `README.md` en la carpeta.

## ⚠️ Errores comunes en esta etapa

| Síntoma | Causa probable | Solución |
|---------|----------------|----------|
| El modal no muestra el resumen | No leíste el valor del formulario al abrirlo | Lee los campos **antes** de insertar el texto, o justo en el evento `shown.bs.modal` |
| Se desarma a 375 px | Falta `col-12` en la primera columna | Mobile-first: siempre empieza por una sola columna |
| El acordeón deja varios abiertos | Sin `data-bs-parent` | Todos los panels apuntan al mismo `id` del `.accordion` |
| El formulario acepta campos vacíos | Quitaste `required` | Cada campo crítico necesita `required` |
| Te cuesta tiempo decidir clases | Estás pensando en el escritorio | Describe primero el móvil en voz alta |

## 💪 Mini-ejercicio de práctica

**Reto:** mejora el reto anterior con **una** funcionalidad extra, a tu elección:

1. **Filtro por día** con botones `btn-group` que oculten tarjetas con `d-none`.
2. **Contador regresivo** hasta la fecha del festival, hecho con JavaScript puro.
3. **Formulario de "voluntariado"** en un segundo paso del modal.
4. **Página de detalle** de cada artista (un archivo `artista.html` que reciba el nombre por la URL).

**Pista:** elige la opción 1 y usa un solo `data-filtro` en cada botón, lee `event.target` y alterna la clase `d-none` en las tarjetas. Máximo 10 líneas de JavaScript.

## ✅ Punto de control — Módulo 10

- [ ] Completé el proyecto "Silla Vacía" sin seguir los módulos paso a paso.
- [ ] Usé menos de 15 líneas de CSS propio.
- [ ] El sitio se ve bien a 375 px, 768 px y 1440 px.
- [ ] Todo se puede usar con el teclado.
- [ ] El proyecto tiene `id` en las secciones y funciona con anclas.
- [ ] Incluí un `README.md` con las instrucciones para abrirlo.
- [ ] Completé la funcionalidad extra del ejercicio.

## 📖 Qué sigue después de este tutorial

**Para seguir con Bootstrap:**
- Lee la documentación oficial: <https://getbootstrap.com/docs/5.3/getting-started/introduction/>
- Aprende los componentes que no tocamos: `offcanvas`, `toasts`, `placeholders`, `spinners`, `list-group`, `pagination`, `breadcrumbs`, `scrollspy`, `tooltip`, `popover`.

**Para convertirte en un perfil más sólido:**
- **HTML semántico y ARIA**: <https://www.w3.org/WAI/ARIA/apg/>
- **Diseño**: <https://fonts.google.com/> para tipografías, <https://coolors.co> para paletas.
- **Imágenes optimizadas**: <https://squoosh.app/> (convierte a WebP en un clic).
- **Hosting gratuito**: GitHub Pages, Netlify o Vercel para publicar tu proyecto.
- **Markdown**: <https://www.markdownguide.org/>

**El consejo que más importa:** deja de seguir tutoriales y empieza a **clonar**. Toma 3 sitios que te gusten y reconstruye su maquetación con Bootstrap. Ahí es donde aparecen las preguntas reales.

---

# 🧾 Checklist rápido de una maquetación con Bootstrap

Cuando te sientes a maquetar cualquier cosa, hazte estas preguntas en orden:

```
1. ¿Es una página de una sola sección o de varias?
   └─ Varias → <main> con <section id="...">

2. ¿Cómo se ve en CELULAR? (siempre se responde esto primero)
   └─ Mobile-first: clases sin prefijo

3. ¿Cuántas columnas tiene cada fila?
   └─ 1 → col-12 | 2 → col-12 col-md-6 | 3 → col-12 col-md-6 col-lg-4

4. ¿Cómo separo el contenido del borde de la pantalla?
   └─ <div class="container">

5. ¿Qué separaciones necesito?
   └─ En la fila: g-4. En los bloques: py-5 / mb-4

6. ¿Necesita interacción?
   └─ Modal / Collapse / Carousel / Offcanvas con data-bs-*

7. ¿Tiene textos e imágenes?
   └─ alt, <figure>, <figcaption>, .visually-hidden

8. ¿Se puede usar con el teclado?
   └─ Tab, Enter, Esc deben funcionar
```

---
# 📦 Código completo del proyecto terminado

Los tres archivos que componen **RutaUni** al terminar el tutorial. Compáralos con los tuyos: cualquier diferencia es una pista de algo que te saltaste.

## `index.html`

```html
<!DOCTYPE html>
<html lang="es" data-bs-theme="light">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="RutaUni: preuniversitario virtual para estudiantes de grado 10 y 11 en Colombia. Acompañamiento para el Icfes y el ingreso a la universidad.">
    <title>RutaUni · Acompáñamos tu entrada a la universidad</title>

    <!-- Bootstrap 5.3.8 · CSS -->
    <link rel="stylesheet"
          href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css">
    <link rel="stylesheet"
          href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"></script>

    <!-- Evita el destello de tema claro antes de aplicar el guardado -->
    <script>
        try {
            var t = localStorage.getItem('rutuni-tema');
            if (!t) t = matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
            document.documentElement.setAttribute('data-bs-theme', t);
        } catch (e) {}
    </script>

    <link rel="stylesheet" href="css/estilos.css">
</head>
<body>

    <!-- Enlace de salto al contenido -->
    <a href="#contenido" class="visually-hidden-focusable btn btn-primary position-absolute top-0 start-0 m-2">
        Saltar al contenido principal
    </a>

    <!-- ===================== NAVBAR ===================== -->
    <nav class="navbar navbar-expand-lg bg-dark navbar-dark sticky-top shadow-sm">
        <div class="container">
            <a class="navbar-brand d-flex align-items-center gap-2" href="#inicio">
                <i class="bi bi-compass fs-3 text-info"></i>
                <span class="fw-bold">RutaUni</span>
            </a>

            <button class="navbar-toggler" type="button"
                    data-bs-toggle="collapse" data-bs-target="#menuPrincipal"
                    aria-controls="menuPrincipal" aria-expanded="false" aria-label="Abrir el menú">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse" id="menuPrincipal">
                <ul class="navbar-nav ms-auto mb-2 mb-lg-0 align-items-lg-center gap-lg-2">
                    <li class="nav-item"><a class="nav-link active" aria-current="page" href="#inicio">Inicio</a></li>
                    <li class="nav-item"><a class="nav-link" href="#programas">Programas</a></li>
                    <li class="nav-item"><a class="nav-link" href="#testimonios">Testimonios</a></li>
                    <li class="nav-item"><a class="nav-link" href="#preguntas">Preguntas</a></li>
                    <li class="nav-item"><a class="nav-link" href="#contacto">Contacto</a></li>
                    <li class="nav-item ms-lg-2">
                        <a href="#contacto" class="btn btn-info text-dark fw-semibold px-3"
                           data-bs-toggle="modal" data-bs-target="#modalInscripcion">Inscríbirme</a>
                    </li>
                </ul>

                <form class="d-none d-lg-block ms-lg-3" role="search">
                    <input class="form-control form-control-sm" type="search"
                           placeholder="Buscar" aria-label="Buscar en el sitio">
                </form>

                <button class="btn btn-outline-light btn-sm ms-lg-3" type="button" id="botonTema">
                    <i class="bi bi-moon-stars-fill" id="iconoTema" aria-hidden="true"></i>
                    <span class="visually-hidden">Cambiar entre tema claro y oscuro</span>
                </button>
            </div>
        </div>
    </nav>

    <main id="contenido">

        <!-- ===================== HERO ===================== -->
        <header class="hero-degradado text-white py-5" id="inicio">
            <div class="container">
                <div class="row align-items-center g-4">
                    <div class="col-12 col-lg-7">
                        <span class="badge bg-warning text-dark mb-3">Cohortes 2026 abiertas</span>
                        <h1 class="display-3 fw-bold lh-1">Tu entrada a la universidad empieza aquí</h1>
                        <p class="lead my-4 text-white-50">
                            Acompañamiento virtual para estudiantes de grado 10 y 11: preparación
                            para el Icfes, técnicas de estudio y orientación profesional.
                        </p>
                        <div class="d-flex flex-wrap gap-2 mb-4">
                            <a href="#contacto" class="btn btn-light btn-lg px-4"
                               data-bs-toggle="modal" data-bs-target="#modalInscripcion">
                                Quiero inscribirme
                            </a>
                            <a href="#programas" class="btn btn-outline-light btn-lg px-4">Ver programas</a>
                        </div>
                        <ul class="list-unstyled d-flex flex-wrap gap-4 small mb-0">
                            <li><i class="bi bi-check-circle-fill text-warning"></i> Clases en vivo y grabadas</li>
                            <li><i class="bi bi-check-circle-fill text-warning"></i> Plan de estudio semanal</li>
                            <li><i class="bi bi-check-circle-fill text-warning"></i> Sin costo de matrícula</li>
                        </ul>
                    </div>

                    <div class="col-12 col-lg-5">
                        <div class="card bg-white text-dark border-0 shadow">
                            <div class="card-body text-center p-4">
                                <i class="bi bi-mortarboard-fill display-4 text-primary"></i>
                                <h2 class="h4 mt-3">Ruta Saber 11</h2>
                                <p class="mb-0">12 semanas · 3 sesiones semanales · 100 % online</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </header>

        <!-- ===================== CIFRAS ===================== -->
        <section class="py-5 bg-body-tertiary" id="cifras">
            <div class="container">
                <div class="row g-4 text-center">
                    <div class="col-12 col-sm-6 col-lg-3">
                        <h2 class="display-4 fw-bold text-primary mb-0">+3.200</h2>
                        <p class="text-secondary mb-0">estudiantes formados en 14 ciudades</p>
                    </div>
                    <div class="col-12 col-sm-6 col-lg-3">
                        <h2 class="display-4 fw-bold text-success mb-0">94 %</h2>
                        <p class="text-secondary mb-0">mejoraron su puntaje en el simulacro</p>
                    </div>
                    <div class="col-12 col-sm-6 col-lg-3">
                        <h2 class="display-4 fw-bold text-warning mb-0">48</h2>
                        <p class="text-secondary mb-0">docentes de planta</p>
                    </div>
                    <div class="col-12 col-sm-6 col-lg-3">
                        <h2 class="display-4 fw-bold text-danger mb-0">12</h2>
                        <p class="text-secondary mb-0">semanas por cohorte</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- ===================== AVISO ===================== -->
        <div class="container py-4">
            <div class="alert alert-info d-flex align-items-start gap-3 shadow-sm" role="alert">
                <i class="bi bi-info-circle-fill fs-4"></i>
                <div class="flex-grow-1">
                    <h2 class="h5 alert-heading mb-1">¡Inscripciones abiertas para la cohorte de febrero!</h2>
                    <p class="mb-0">
                        Los cupos se asignan por orden de pago. Escribe a
                        <a href="#contacto" class="alert-link">admisiones@rutuni.edu.co</a>
                        para recibir la ficha de matrícula.
                    </p>
                </div>
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Cerrar"></button>
            </div>
        </div>

        <!-- ===================== PROGRAMAS ===================== -->
        <section class="py-5" id="programas">
            <div class="container">
                <div class="row mb-5">
                    <div class="col-12 col-lg-8">
                        <span class="badge text-bg-primary mb-2">Programas</span>
                        <h2 class="fw-bold">Elige tu ruta de preparación</h2>
                    </div>
                    <div class="col-12 col-lg-4">
                        <p class="text-secondary mb-0">
                            Todos los programas son virtuales, con asesoras de planta
                            y horarios compatibles con el colegio.
                        </p>
                    </div>
                </div>

                <div class="row g-4">
                    <div class="col-12 col-md-6 col-lg-4 d-flex">
                        <article class="card h-100 w-100 shadow-sm border-0 tarjeta-programa">
                            <div class="card-body d-flex flex-column p-4">
                                <span class="badge text-bg-success align-self-start mb-3">Más solicitado</span>
                                <h3 class="card-title h4">Ruta Saber 11</h3>
                                <p class="card-text flex-grow-1 text-secondary">
                                    Intensivo de 12 semanas en matemáticas, lectura crítica,
                                    química e inglés, con simulacros semanales.
                                </p>
                                <ul class="list-group list-group-flush mb-3">
                                    <li class="list-group-item px-0">3 sesiones semanales en vivo</li>
                                    <li class="list-group-item px-0">Materiales incluidos</li>
                                    <li class="list-group-item px-0">Grupo de máximo 25 estudiantes</li>
                                </ul>
                                <div class="d-flex justify-content-between align-items-center mt-auto">
                                    <span class="h4 mb-0">$380.000 <small class="text-secondary">/ mes</small></span>
                                    <button class="btn btn-primary" data-bs-toggle="modal"
                                            data-bs-target="#modalInscripcion">Inscribirme</button>
                                </div>
                            </div>
                        </article>
                    </div>

                    <div class="col-12 col-md-6 col-lg-4 d-flex">
                        <article class="card h-100 w-100 shadow-sm border-0 tarjeta-programa">
                            <div class="card-body d-flex flex-column p-4">
                                <span class="badge text-bg-info align-self-start mb-3">Nuevo</span>
                                <h3 class="card-title h4">Lectura y escritura</h3>
                                <p class="card-text flex-grow-1 text-secondary">
                                    Taller de 8 semanas para mejorar el componente comunicativo
                                    del Icfes y aprender a escribir ensayos de opinión.
                                </p>
                                <ul class="list-group list-group-flush mb-3">
                                    <li class="list-group-item px-0">Talleres de escritura creativa</li>
                                    <li class="list-group-item px-0">Corrección personalizada</li>
                                    <li class="list-group-item px-0">2 sesiones semanales</li>
                                </ul>
                                <div class="d-flex justify-content-between align-items-center mt-auto">
                                    <span class="h4 mb-0">$240.000 <small class="text-secondary">/ mes</small></span>
                                    <button class="btn btn-outline-primary" data-bs-toggle="modal"
                                            data-bs-target="#modalInscripcion">Inscribirme</button>
                                </div>
                            </div>
                        </article>
                    </div>

                    <div class="col-12 col-md-6 col-lg-4 d-flex">
                        <article class="card h-100 w-100 shadow-sm border-0 tarjeta-programa">
                            <div class="card-body d-flex flex-column p-4">
                                <span class="badge text-bg-warning text-dark align-self-start mb-3">Cupo limitado</span>
                                <h3 class="card-title h4">Orientación universitaria</h3>
                                <p class="card-text flex-grow-1 text-secondary">
                                    Acompañamiento para elegir carrera y preparar tu carta de
                                    motivación y las pruebas de admisión de cada universidad.
                                </p>
                                <ul class="list-group list-group-flush mb-3">
                                    <li class="list-group-item px-0">6 sesiones individuales</li>
                                    <li class="list-group-item px-0">Mapa de universidades de Colombia</li>
                                    <li class="list-group-item px-0">1 sesión semanal</li>
                                </ul>
                                <div class="d-flex justify-content-between align-items-center mt-auto">
                                    <span class="h4 mb-0">$180.000 <small class="text-secondary">/ mes</small></span>
                                    <button class="btn btn-outline-primary" data-bs-toggle="modal"
                                            data-bs-target="#modalInscripcion">Inscribirme</button>
                                </div>
                            </div>
                        </article>
                    </div>
                </div>
            </div>
        </section>

        <!-- ===================== TESTIMONIOS ===================== -->
        <section class="py-5" id="testimonios">
            <div class="container">
                <h2 class="fw-bold text-center mb-5">Lo que dicen nuestros estudiantes</h2>

                <div id="carruselTestimonios" class="carousel slide" data-bs-ride="carousel"
                     data-bs-interval="6000" data-bs-touch="true">
                    <div class="carousel-indicators">
                        <button type="button" data-bs-target="#carruselTestimonios" data-bs-slide-to="0"
                                class="active" aria-current="true" aria-label="Testimonio 1"></button>
                        <button type="button" data-bs-target="#carruselTestimonios" data-bs-slide-to="1"
                                aria-label="Testimonio 2"></button>
                        <button type="button" data-bs-target="#carruselTestimonios" data-bs-slide-to="2"
                                aria-label="Testimonio 3"></button>
                    </div>

                    <div class="carousel-inner">
                        <div class="carousel-item active">
                            <div class="row justify-content-center">
                                <div class="col-12 col-lg-8">
                                    <figure class="text-center p-4 bg-body-tertiary rounded-4">
                                        <blockquote class="blockquote fs-5 mb-4">
                                            "Subí 120 puntos en el simulacro. Lo que más me sirvió fue
                                            aprender a organizar el tiempo, no solo los temas."
                                        </blockquote>
                                        <figcaption class="d-flex align-items-center justify-content-center gap-3">
                                            <i class="bi bi-person-circle-fill fs-2 text-primary"></i>
                                            <span class="text-start">
                                                <strong>Mariana Ospina</strong><br>
                                                <small class="text-secondary">Grado 11 · Medellín</small>
                                            </span>
                                        </figcaption>
                                    </figure>
                                </div>
                            </div>
                        </div>

                        <div class="carousel-item">
                            <div class="row justify-content-center">
                                <div class="col-12 col-lg-8">
                                    <figure class="text-center p-4 bg-body-tertiary rounded-4">
                                        <blockquote class="blockquote fs-5 mb-4">
                                            "Los profesores responden los mensajes el mismo día. Eso no lo
                                            había visto en ningún otro preuniversitario."
                                        </blockquote>
                                        <figcaption class="d-flex align-items-center justify-content-center gap-3">
                                            <i class="bi bi-person-circle-fill fs-2 text-success"></i>
                                            <span class="text-start">
                                                <strong>Kevin Restrepo</strong><br>
                                                <small class="text-secondary">Grado 11 · Pereira</small>
                                            </span>
                                        </figcaption>
                                    </figure>
                                </div>
                            </div>
                        </div>

                        <div class="carousel-item">
                            <div class="row justify-content-center">
                                <div class="col-12 col-lg-8">
                                    <figure class="text-center p-4 bg-body-tertiary rounded-4">
                                        <blockquote class="blockquote fs-5 mb-4">
                                            "Con la orientación profesional decidí estudiar ingeniería. Estaba
                                            entre tres opciones y terminé escogiendo la correcta."
                                        </blockquote>
                                        <figcaption class="d-flex align-items-center justify-content-center gap-3">
                                            <i class="bi bi-person-circle-fill fs-2 text-warning"></i>
                                            <span class="text-start">
                                                <strong>Sofía Cárdenas</strong><br>
                                                <small class="text-secondary">Grado 10 · Bogotá</small>
                                            </span>
                                        </figcaption>
                                    </figure>
                                </div>
                            </div>
                        </div>
                    </div>

                    <button class="carousel-control-prev" type="button"
                            data-bs-target="#carruselTestimonios" data-bs-slide="prev">
                        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                        <span class="visually-hidden">Testimonio anterior</span>
                    </button>
                    <button class="carousel-control-next" type="button"
                            data-bs-target="#carruselTestimonios" data-bs-slide="next">
                        <span class="carousel-control-next-icon" aria-hidden="true"></span>
                        <span class="visually-hidden">Testimonio siguiente</span>
                    </button>
                </div>
            </div>
        </section>

        <!-- ===================== PREGUNTAS ===================== -->
        <section class="py-5 bg-body-tertiary" id="preguntas">
            <div class="container">
                <div class="row">
                    <div class="col-12 col-lg-4 mb-4 mb-lg-0">
                        <span class="badge text-bg-secondary mb-2">FAQ</span>
                        <h2 class="fw-bold">Preguntas frecuentes</h2>
                        <p class="text-secondary">
                            ¿No encuentras tu duda? Escríbenos y te respondemos en menos de 24 horas hábiles.
                        </p>
                        <a href="#contacto" class="btn btn-outline-primary mt-2">Ir al formulario de contacto</a>
                    </div>

                    <div class="col-12 col-lg-8">
                        <div class="accordion" id="acordeonPreguntas">
                            <div class="accordion-item">
                                <h3 class="accordion-header">
                                    <button class="accordion-button" type="button" data-bs-toggle="collapse"
                                            data-bs-target="#pregunta1" aria-expanded="true" aria-controls="pregunta1">
                                        ¿Necesito tener un buen puntaje para entrar?
                                    </button>
                                </h3>
                                <div id="pregunta1" class="accordion-collapse collapse show"
                                     data-bs-parent="#acordeonPreguntas">
                                    <div class="accordion-body">
                                        No. La primera semana es de diagnóstico para conocer tu punto de partida
                                        y armar un plan personalizado. Solo condicionamos la carga horaria
                                        semanal que puedas comprometer.
                                    </div>
                                </div>
                            </div>

                            <div class="accordion-item">
                                <h3 class="accordion-header">
                                    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
                                            data-bs-target="#pregunta2" aria-expanded="false" aria-controls="pregunta2">
                                        ¿Las clases son en vivo o grabadas?
                                    </button>
                                </h3>
                                <div id="pregunta2" class="accordion-collapse collapse"
                                     data-bs-parent="#acordeonPreguntas">
                                    <div class="accordion-body">
                                        Son en vivo por videollamada y además quedan grabadas durante 6 meses.
                                        Si no puedes asistir, puedes enviar tu pregunta por el chat del
                                        curso y la responden al día siguiente.
                                    </div>
                                </div>
                            </div>

                            <div class="accordion-item">
                                <h3 class="accordion-header">
                                    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
                                            data-bs-target="#pregunta3" aria-expanded="false" aria-controls="pregunta3">
                                        ¿Qué pasa si no alcanzo a entregar un trabajo?
                                    </button>
                                </h3>
                                <div id="pregunta3" class="accordion-collapse collapse"
                                     data-bs-parent="#acordeonPreguntas">
                                    <div class="accordion-body">
                                        Tienes hasta 48 horas para entregar después de la fecha límite.
                                        Cada asesor puede activar dos extensiones por cohorte, siempre
                                        que avises con tiempo.
                                    </div>
                                </div>
                            </div>

                            <div class="accordion-item">
                                <h3 class="accordion-header">
                                    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
                                            data-bs-target="#pregunta4" aria-expanded="false" aria-controls="pregunta4">
                                        ¿Ofrecen beca o descuentos?
                                    </button>
                                </h3>
                                <div id="pregunta4" class="accordion-collapse collapse"
                                     data-bs-parent="#acordeonPreguntas">
                                    <div class="accordion-body">
                                        Sí. Hay dos modalidades: beca por rendimiento académico
                                        (top 10 del cohorte) y descuento del 20 % para estudiantes de
                                        municipios con difícil acceso a internet.
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- ===================== CONTACTO ===================== -->
        <section class="py-5" id="contacto">
            <div class="container">
                <div class="row g-4 g-lg-5">
                <aside class="col-12 col-lg-5">
                        <span class="badge text-bg-secondary mb-2">Contacto</span>
                        <h2 class="fw-bold mb-3">¿Tienes dudas? Escríbenos</h2>
                        <p class="text-secondary mb-4">
                            Nuestro equipo de admisiones responde en menos de 24 horas hábiles y en
                            horario extendido para zonas rurales.
                        </p>

                        <ul class="list-unstyled d-grid gap-3">
                            <li class="d-flex gap-3">
                                <i class="bi bi-envelope-fill text-primary fs-5"></i>
                                <div>
                                    <strong>Correo</strong><br>
                                    <a href="mailto:admisiones@rutuni.edu.co">admisiones@rutuni.edu.co</a>
                                </div>
                            </li>
                            <li class="d-flex gap-3">
                                <i class="bi bi-telephone-fill text-primary fs-5"></i>
                                <div>
                                    <strong>Teléfono</strong><br>
                                    <a href="tel:+573001234567">+57 300 123 4567</a>
                                </div>
                            </li>
                            <li class="d-flex gap-3">
                                <i class="bi bi-geo-alt-fill text-primary fs-5"></i>
                                <div>
                                    <strong>Sede</strong><br>
                                    Medellín (ant.), con clases online a todo Colombia
                                </div>
                            </li>
                        </ul>

                        <div class="mt-4">
                            <a href="https://wa.me/573001234567" class="btn btn-success" rel="noopener">
                                <i class="bi bi-whatsapp me-2"></i>Escríbenos por WhatsApp
                            </a>
                        </div>
                    </aside>

                    <div class="col-12 col-lg-7">
                        <div class="card border-0 shadow-sm">
                            <div class="card-body p-4 p-lg-5">
                                <form id="formularioContacto" novalidate>
                                    <div class="row g-3">
                                        <div class="col-12 col-md-6">
                                            <label for="nombre" class="form-label">
                                                Nombre completo <span class="text-danger" aria-hidden="true">*</span>
                                            </label>
                                            <input type="text" class="form-control" id="nombre" name="nombre"
                                                   placeholder="Ej. Valentina Gómez" autocomplete="name"
                                                   required minlength="3">
                                            <div class="invalid-feedback">Escribe tu nombre (mínimo 3 letras).</div>
                                        </div>

                                        <div class="col-12 col-md-6">
                                            <label for="correo" class="form-label">
                                                Correo electrónico <span class="text-danger" aria-hidden="true">*</span>
                                            </label>
                                            <input type="email" class="form-control" id="correo" name="correo"
                                                   placeholder="tu@correo.com" autocomplete="email" required>
                                            <div class="invalid-feedback">
                                                Revisa el correo: debe tener el formato nombre@dominio.com
                                            </div>
                                        </div>

                                        <div class="col-12 col-md-6">
                                            <label for="telefono" class="form-label">Teléfono (opcional)</label>
                                            <input type="tel" class="form-control" id="telefono" name="telefono"
                                                   placeholder="+57 300 123 4567" autocomplete="tel"
                                                   pattern="[0-9+ ]{7,15}">
                                            <div class="invalid-feedback">
                                                Entre 7 y 15 caracteres: solo números, espacios y el signo +.
                                            </div>
                                        </div>

                                        <div class="col-12 col-md-6">
                                            <label for="grado" class="form-label">
                                                Grado en el que estás <span class="text-danger" aria-hidden="true">*</span>
                                            </label>
                                            <select class="form-select" id="grado" name="grado" required>
                                                <option value="" selected disabled>Elegir una opción</option>
                                                <option value="9">Grado 9</option>
                                                <option value="10">Grado 10</option>
                                                <option value="11">Grado 11</option>
                                                <option value="otro">Otro</option>
                                            </select>
                                            <div class="invalid-feedback">Selecciona tu grado actual.</div>
                                        </div>

                                        <div class="col-12">
                                            <label for="programa" class="form-label">
                                                Programa de interés <span class="text-danger" aria-hidden="true">*</span>
                                            </label>
                                            <select class="form-select" id="programa" name="programa" required>
                                                <option value="" selected disabled>Elegir un programa</option>
                                                <option>Ruta Saber 11</option>
                                                <option>Lectura y escritura</option>
                                                <option>Orientación universitaria</option>
                                            </select>
                                            <div class="invalid-feedback">Elige el programa que te interesa.</div>
                                        </div>

                                        <div class="col-12">
                                            <label for="mensaje" class="form-label">
                                                Mensaje <span class="text-danger" aria-hidden="true">*</span>
                                            </label>
                                            <textarea class="form-control" id="mensaje" name="mensaje" rows="4"
                                                      placeholder="Cuéntanos tu caso..." required minlength="20"></textarea>
                                            <div class="form-text">Mínimo 20 caracteres.</div>
                                            <div class="invalid-feedback">
                                                Escribe al menos 20 caracteres para que podamos ayudarte bien.
                                            </div>
                                        </div>

                                        <div class="col-12">
                                            <div class="form-check">
                                                <input class="form-check-input" type="checkbox" id="acepto" required>
                                                <label class="form-check-label" for="acepto">
                                                    Acepto el tratamiento de mis datos y las
                                                    <a href="#" class="link-primary">condiciones del programa</a>.
                                                </label>
                                                <div class="invalid-feedback">
                                                    Debes aceptar para poder enviar la solicitud.
                                                </div>
                                            </div>
                                        </div>

                                        <div class="col-12 col-lg-6">
                                            <div class="form-check form-switch">
                                                <input class="form-check-input" type="checkbox" role="switch"
                                                       id="whatsapp" checked>
                                                <label class="form-check-label" for="whatsapp">
                                                    Prefiero que me escriban por WhatsApp
                                                </label>
                                            </div>
                                        </div>

                                        <div class="col-12 col-lg-6">
                                            <label for="ciudad" class="form-label">Ciudad</label>
                                            <div class="input-group">
                                                <span class="input-group-text"><i class="bi bi-geo-alt"></i></span>
                                                <input type="text" class="form-control" id="ciudad" name="ciudad"
                                                       placeholder="Medellín" list="listaCiudades">
                                                <datalist id="listaCiudades">
                                                    <option value="Bogotá"></option>
                                                    <option value="Medellín"></option>
                                                    <option value="Cali"></option>
                                                    <option value="Bucaramanga"></option>
                                                </datalist>
                                            </div>
                                        </div>

                                        <div class="col-12">
                                            <div class="d-flex flex-wrap gap-2 pt-2">
                                                <button type="submit" class="btn btn-primary btn-lg px-4">
                                                    <i class="bi bi-send me-2"></i>Enviar solicitud
                                                </button>
                                                <button type="reset" class="btn btn-outline-secondary btn-lg">Limpiar</button>
                                            </div>
                                            <p class="form-text mt-3">
                                                Los campos marcados con <span class="text-danger">*</span> son obligatorios.
                                            </p>
                                        </div>
                                    </div>
                                </form>

                                <div class="alert alert-success d-none" id="avisoExito" role="status" tabindex="-1">
                                    <h3 class="h5 alert-heading"><i class="bi bi-check-circle me-2"></i>¡Recibimos tu mensaje!</h3>
                                    <p class="mb-0" id="textoExito">
                                        Te responderemos a tu correo en menos de 24 horas hábiles.
                                    </p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

    </main>

    <!-- ===================== FOOTER ===================== -->
    <footer class="footer-borde bg-body-tertiary py-5 mt-5">
        <div class="container">
            <div class="row g-4">
                <div class="col-12 col-md-4">
                    <a class="d-inline-flex align-items-center gap-2 mb-3 text-decoration-none" href="#inicio">
                        <i class="bi bi-compass fs-3 text-primary"></i>
                        <span class="fw-bold fs-5">RutaUni</span>
                    </a>
                    <p class="text-secondary">
                        Preuniversitario virtual para estudiantes de grado 10 y 11 en Colombia.
                        Acompañamiento desde 2019.
                    </p>
                    <div class="d-flex gap-2">
                        <a href="#" class="btn btn-sm btn-outline-secondary rounded-circle" aria-label="Instagram de RutaUni">
                            <i class="bi bi-instagram" aria-hidden="true"></i>
                        </a>
                        <a href="#" class="btn btn-sm btn-outline-secondary rounded-circle" aria-label="TikTok de RutaUni">
                            <i class="bi bi-tiktok" aria-hidden="true"></i>
                        </a>
                        <a href="#" class="btn btn-sm btn-outline-secondary rounded-circle" aria-label="YouTube de RutaUni">
                            <i class="bi bi-youtube" aria-hidden="true"></i>
                        </a>
                    </div>
                </div>

                <div class="col-6 col-md-2 offset-md-1">
                    <h2 class="h6 text-uppercase text-secondary">Programas</h2>
                    <ul class="list-unstyled d-grid gap-2">
                        <li><a class="link-secondary" href="#programas">Ruta Saber 11</a></li>
                        <li><a class="link-secondary" href="#programas">Lectura y escritura</a></li>
                        <li><a class="link-secondary" href="#programas">Orientación universitaria</a></li>
                    </ul>
                </div>

                <div class="col-6 col-md-2">
                    <h2 class="h6 text-uppercase text-secondary">Recursos</h2>
                    <ul class="list-unstyled d-grid gap-2">
                        <li><a class="link-secondary" href="#preguntas">Preguntas frecuentes</a></li>
                        <li><a class="link-secondary" href="mailto:admisiones@rutuni.edu.co">admisiones@rutuni.edu.co</a></li>
                        <li><a class="link-secondary" href="tel:+573001234567">+57 300 123 4567</a></li>
                    </ul>
                </div>

                <div class="col-12 col-md-3">
                    <h2 class="h6 text-uppercase text-secondary">Horario de atención</h2>
                    <p class="text-secondary small mb-2">
                        Lunes a viernes, 7:00 a. m. – 8:00 p. m.<br>
                        Sábados, 8:00 a. m. – 2:00 p. m.
                    </p>
                    <p class="small mb-0">
                        <i class="bi bi-geo-alt me-1"></i>Medellín, Colombia · Cobertura nacional
                    </p>
                </div>
            </div>

            <hr class="my-4">

            <div class="row align-items-center g-3">
                <div class="col-12 col-md-6">
                    <p class="small text-secondary mb-0">© 2026 RutaUni. Proyecto educativo de ejemplo.</p>
                </div>
                <div class="col-12 col-md-6">
                    <ul class="list-inline d-flex flex-wrap justify-content-md-end gap-3 mb-0 small">
                        <li class="list-inline-item"><a class="link-secondary" href="#">Términos</a></li>
                        <li class="list-inline-item"><a class="link-secondary" href="#">Privacidad</a></li>
                        <li class="list-inline-item"><a class="link-secondary" href="#">Contáctanos</a></li>
                    </ul>
                </div>
            </div>
        </div>
    </footer>

    <!-- ===================== MODAL ===================== -->
    <div class="modal fade" id="modalInscripcion" tabindex="-1"
         aria-labelledby="tituloModal" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered modal-lg">
            <div class="modal-content">
                <div class="modal-header">
                    <h2 class="modal-title h4" id="tituloModal">Solicitar cupo</h2>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Cerrar"></button>
                </div>

                <div class="modal-body">
                    <p class="text-secondary">
                        Completa tus datos y nuestro equipo te contacta en menos de 24 horas para
                        confirmar el cupo y enviarte la ficha de matrícula.
                    </p>

                    <form id="formularioModal" novalidate>
                        <div class="row g-3">
                            <div class="col-12 col-md-6">
                                <label for="modalNombre" class="form-label">Nombre completo</label>
                                <input type="text" class="form-control" id="modalNombre" required>
                            </div>
                            <div class="col-12 col-md-6">
                                <label for="modalCorreo" class="form-label">Correo</label>
                                <input type="email" class="form-control" id="modalCorreo" required>
                            </div>
                            <div class="col-12">
                                <label for="modalPrograma" class="form-label">Programa</label>
                                <select class="form-select" id="modalPrograma" required>
                                    <option value="" selected disabled>Elegir un programa</option>
                                    <option>Ruta Saber 11</option>
                                    <option>Lectura y escritura</option>
                                    <option>Orientación universitaria</option>
                                </select>
                            </div>
                        </div>
                    </form>

                    <div class="alert alert-primary d-flex gap-2 mb-0 mt-3" role="note">
                        <i class="bi bi-info-circle-fill"></i>
                        <div class="small">
                            Al enviar aceptas que te contactemos por teléfono o correo.
                            No compartimos tus datos con terceros.
                        </div>
                    </div>
                </div>

                <div class="modal-footer">
                    <button type="button" class="btn btn-outline-secondary" data-bs-dismiss="modal">Cancelar</button>
                    <button type="submit" form="formularioModal" class="btn btn-primary">
                        <i class="bi bi-send me-2"></i>Enviar solicitud
                    </button>
                </div>
            </div>
        </div>
    </div>

    <script src="js/mi-script.js"></script>
</body>
</html>
```

## `css/estilos.css`

```css
/* ============================================================
   RutaUni · Estilos personalizados
   Se carga DESPUÉS de Bootstrap, por eso gana en los empates
   ============================================================ */

/* ---------- 1. Identidad de color ---------- */
:root {
    --rutuni-azul: #1f3a8a;
    --rutuni-lima: #a3e635;
    --rutuni-naranja: #f97316;

    --bs-primary: var(--rutuni-azul);
    --bs-link-color: var(--rutuni-azul);
    --bs-link-hover-color: #16306f;

    --bs-body-font-family: system-ui, -apple-system, "Segoe UI", Roboto,
                            "Helvetica Neue", Arial, sans-serif;
}

/* ---------- 2. Detalles propios ---------- */

/* En móvil los textos largos (correos, URLs) se parten antes de provocar un
   desplazamiento horizontal de toda la página. Ojo: `anywhere`, no
   `break-word`, porque es el único que reduce también el ancho mínimo de las
   celdas de una rejilla. */
body {
    overflow-wrap: anywhere;
    word-break: break-word;
}

.rounded-4 {
    border-radius: 1.25rem !important;
}

.hero-degradado {
    background-image:
        radial-gradient(circle at 15% 20%, rgba(163, 230, 53, .25), transparent 45%),
        radial-gradient(circle at 85% 10%, rgba(249, 115, 22, .30), transparent 40%),
        linear-gradient(135deg, var(--rutuni-azul) 0%, #2b1a6b 100%);
}

.tarjeta-programa {
    border-top: 4px solid var(--rutuni-azul);
    transition: transform .2s ease, box-shadow .2s ease;
}

.tarjeta-programa:hover,
.tarjeta-programa:focus-within {
    transform: translateY(-4px);
    box-shadow: 0 1rem 1.5rem rgba(0, 0, 0, .12);
}

.footer-borde {
    border-top: 4px solid transparent;
    border-image: linear-gradient(90deg, var(--rutuni-lima), var(--rutuni-naranja), var(--rutuni-azul)) 1;
}

/* ---------- 3. Modo oscuro ---------- */
[data-bs-theme="dark"] {
    --rutuni-azul: #93c5fd;
    --rutuni-lima: #bef264;
    --rutuni-naranja: #fdba74;

    --bs-link-color: #93c5fd;
    --bs-link-hover-color: #bfdbfe;
}

[data-bs-theme="dark"] .hero-degradado {
    background-image:
        radial-gradient(circle at 15% 20%, rgba(163, 230, 53, .15), transparent 45%),
        radial-gradient(circle at 85% 10%, rgba(249, 115, 22, .18), transparent 40%),
        linear-gradient(135deg, #101a3d 0%, #1a1030 100%);
}

@media (prefers-color-scheme: dark) {
    :root:not([data-bs-theme="light"]) {
        color-scheme: dark;
    }
}

/* ---------- 4. Navegación suave entre anclas ---------- */
html {
    scroll-behavior: smooth;
    scroll-padding-top: 5rem;
}

@media (prefers-reduced-motion: reduce) {
    html {
        scroll-behavior: auto;
    }
}

/* ---------- 5. Impresión ---------- */
@media print {
    .navbar,
    footer,
    .btn {
        display: none !important;
    }

    body {
        background: #fff;
        color: #000;
    }
}
```

## `js/mi-script.js`

```javascript
/* ============================================================
   RutaUni · Validación del formulario y modo oscuro
   ============================================================ */
(function () {
    'use strict';

    const formulario = document.getElementById('formularioContacto');
    const avisoExito = document.getElementById('avisoExito');
    const textoExito = document.getElementById('textoExito');

    if (formulario) {
        function validarCampo(campo) {
            const esValido = campo.checkValidity();
            campo.classList.toggle('is-invalid', !esValido);
            campo.classList.toggle('is-valid', esValido);
            return esValido;
        }

        formulario.querySelectorAll('input, select, textarea').forEach(campo => {
            campo.addEventListener('blur', () => {
                if (campo.value !== '' || campo.required) {
                    validarCampo(campo);
                }
            });

            campo.addEventListener('input', () => {
                if (campo.classList.contains('is-invalid')) {
                    validarCampo(campo);
                }
            });
        });

        formulario.addEventListener('submit', function (evento) {
            evento.preventDefault();

            const campos = Array.from(formulario.querySelectorAll('input, select, textarea'));
            const resultados = campos.map(validarCampo);
            const primerError = campos[resultados.indexOf(false)];

            if (resultados.includes(false)) {
                primerError.focus();
                return;
            }

            const nombre = formulario.nombre.value.trim().split(' ')[0];
            textoExito.textContent =
                `Gracias, ${nombre}. Te responderemos a tu correo en menos de 24 horas hábiles.`;

            formulario.classList.add('d-none');
            avisoExito.classList.remove('d-none');
            avisoExito.focus();
        });
    }

    /* --- Modal de inscripción --- */
    const modalElement = document.getElementById('modalInscripcion');

    if (modalElement) {
        const modalInscripcion = new bootstrap.Modal(modalElement);

        document.querySelectorAll('[data-bs-target="#modalInscripcion"]').forEach(boton => {
            boton.addEventListener('click', evento => {
                evento.preventDefault();
                modalInscripcion.show();
            });
        });

        const formularioModal = document.getElementById('formularioModal');
        formularioModal.addEventListener('submit', evento => {
            evento.preventDefault();

            if (!formularioModal.checkValidity()) {
                formularioModal.classList.add('was-validated');
                return;
            }

            modalInscripcion.hide();
            alert('¡Gracias! Te contactaremos en menos de 24 horas.');
            formularioModal.reset();
        });

        modalElement.addEventListener('shown.bs.modal', () => {
            document.getElementById('modalNombre').focus();
        });
    }

    /* --- Modo claro / oscuro con memoria --- */
    const botonTema = document.getElementById('botonTema');
    const iconoTema = document.getElementById('iconoTema');
    const clave = 'rutuni-tema';

    function aplicarTema(tema) {
        document.documentElement.setAttribute('data-bs-theme', tema);
        if (iconoTema) {
            iconoTema.className = tema === 'dark' ? 'bi bi-sun-fill' : 'bi bi-moon-stars-fill';
        }
        try {
            localStorage.setItem(clave, tema);
        } catch (e) { /* modo privado */ }
    }

    let temaGuardado = null;
    try {
        temaGuardado = localStorage.getItem(clave);
    } catch (e) { /* sin almacenamiento */ }

    const sistemaPrefiereOscuro = window.matchMedia('(prefers-color-scheme: dark)').matches;
    aplicarTema(temaGuardado || (sistemaPrefiereOscuro ? 'dark' : 'light'));

    if (botonTema) {
        botonTema.addEventListener('click', () => {
            const actual = document.documentElement.getAttribute('data-bs-theme');
            aplicarTema(actual === 'dark' ? 'light' : 'dark');
        });
    }
})();
```

### Estructura final de archivos

```
rutouni/
├── index.html
├── css/
│   └── estilos.css
├── js/
│   └── mi-script.js
├── img/
└── pruebas-grid.html
```

---

# 📇 Hoja de referencia rápida (cheat sheet)

## Layout y grid

| Clase | Qué hace |
|-------|----------|
| `container` | Contenedor centrado con ancho máximo |
| `container-fluid` | Contenedor al 100 % del ancho |
| `row` | Fila de columnas (aplica el gutter) |
| `col` / `col-auto` | Columna de igual ancho / según contenido |
| `col-6` | 6 de 12 partes (nunca cambia con el tamaño) |
| `col-12 col-md-6 col-lg-4` | 1 → 2 → 3 columnas (mobile-first) |
| `offset-md-2` | Empuja la columna 2 columnas hacia la derecha |
| `order-1`, `order-last` | Cambia el orden visual |
| `g-0` … `g-5` | Espacio entre columnas (gutters) |
| `gx-4`, `gy-2` | Solo horizontal / solo vertical |
| `align-items-center` | Centra verticalmente dentro de la fila |
| `justify-content-between` | Distribuye horizontalmente |

## Espaciado (0 = 0 · 1 = .25rem · 2 = .5rem · 3 = 1rem · 4 = 1.5rem · 5 = 3rem)

| Clase | Qué hace |
|-------|----------|
| `p-3` / `m-3` | Padding / margin en las 4 direcciones |
| `pt-3` `pb-3` `ps-3` `pe-3` | Solo top / bottom / izquierda / derecha |
| `px-4` / `py-5` | Solo los ejes horizontal / vertical |
| `mt-auto` | Empuja el elemento al final (muy útil en tarjetas) |
| `mb-md-4` | Aplica `mb-4` desde 768 px |
| `mx-auto` | Centra horizontalmente |

> En Bootstrap 5 **nunca** uses `ml-*`, `mr-*`, `pl-*`, `pr-*`: son de la v4. Usa `ms-*`, `me-*`, `ps-*`, `pe-*`.

## Tipografía

| Clase | Qué hace |
|-------|----------|
| `display-1` … `display-6` | Titulares gigantes (se reducen en móvil) |
| `fs-1` … `fs-6` | Tamaño de texto normal |
| `lead` | Párrafo destacado |
| `fw-bold` `fw-semibold` `fw-light` | Grosor |
| `fst-italic` | Cursiva |
| `text-center` `text-start` `text-end` | Alineación |
| `text-uppercase` `text-lowercase` | Mayúsculas / minúsculas |
| `text-truncate` | Texto cortado con puntos suspensivos |
| `lh-1` | Interlineado compacto |
| `blockquote` `figure` `figcaption` | Citas y figuras |

## Color y fondo

| Clase | Qué hace |
|-------|----------|
| `bg-primary` `bg-secondary` `bg-success` `bg-danger` `bg-warning` `bg-info` `bg-light` `bg-dark` | Fondo de tema |
| `bg-body` `bg-body-tertiary` `bg-body-secondary` | Fondos derivados del tema (ideales para alternar secciones) |
| `bg-primary-subtle` + `text-primary-emphasis` | Recuadro claro con texto legible |
| `text-primary` `text-secondary` | Color del texto |
| `text-white-50` | Blanco translúcido (bien sobre fondos oscuros) |
| `text-bg-primary` | Fondo **y** texto a la vez (base de los badges) |
| `border` `border-0` `border-top` `border-4` `border-primary` | Bordes |
| `rounded` `rounded-3` `rounded-4` `rounded-circle` `rounded-top-4` | Esquinas |
| `shadow-sm` `shadow` `shadow-lg` | Sombras |

## Display y flex

| Clase | Qué hace |
|-------|----------|
| `d-block` `d-inline-block` `d-inline` | Tipo de visualización |
| `d-none` `d-block` `d-flex` `d-grid` | Visibilidad / tipo |
| `d-none d-md-block` | Visible solo desde 768 px |
| `d-lg-none` | Oculto desde 992 px |
| `flex-column` `flex-row` | Dirección del flex |
| `flex-wrap` | Ajuste en varias líneas |
| `flex-fill` `flex-grow-1` | Ocupan el espacio sobrante |
| `gap-1` … `gap-5` | Separación entre hijos de un flex/grid |
| `justify-content-center` `-between` `-end` | Distribución horizontal |
| `align-items-center` `-start` `-end` | Alineación vertical |
| `w-100` `h-100` `vw-100` `vh-100` | Anchos y alturas |

## Componentes

| Clase | Qué hace |
|-------|----------|
| `navbar navbar-expand-lg navbar-dark sticky-top` | Barra de navegación fija |
| `navbar-toggler` + `navbar-collapse` | Menú móvil |
| `dropdown-menu` + `dropdown-toggle` | Desplegable |
| `card` + `card-body` + `card-title` + `card-text` + `card-footer` | Tarjeta |
| `card-img-top` + `card-img-overlay` | Imagen de tarjeta |
| `btn` + `btn-primary` `btn-outline-*` `btn-lg` | Botones |
| `badge` / `badge text-bg-*` | Etiqueta compacta |
| `alert alert-*` + `btn-close` | Mensaje destacado cerrable |
| `list-group` + `list-group-item` + `list-group-flush` | Listas |
| `form-control` `form-select` `form-label` `form-text` | Formularios |
| `form-check` `form-switch` `form-check-input` `form-check-label` | Casillas y radios |
| `input-group` + `input-group-text` | Campo con adorno |
| `is-invalid` `is-valid` + `invalid-feedback` | Estados de validación |
| `modal` + `modal-dialog` + `modal-header/body/footer` | Ventana emergente |
| `accordion` + `accordion-item` + `accordion-button` + `accordion-collapse` | Acordeón |
| `carousel slide` + `carousel-inner` + `carousel-item` | Carrusel |
| `offcanvas offcanvas-start` | Menú lateral |
| `toast` + `toast-container` | Notificación flotante |
| `spinner-border` `spinner-grow` | Indicador de carga |
| `placeholder` `placeholder-glow` | Esqueleto de carga |
| `progress` + `progress-bar` | Barra de progreso |
| `breadcrumb` + `breadcrumb-item` | Ruta de navegación |
| `pagination` + `page-item` + `page-link` | Paginación |
| `visually-hidden` / `visually-hidden-focusable` | Texto solo para lectores / aparece con `Tab` |
| `ratio ratio-16x9` | Contenedor con proporción fija |
| `sticky-top` / `sticky-bottom` | Fijo al hacer scroll |

## Atributos `data-bs-*`

| Atributo | Efecto |
|----------|--------|
| `data-bs-toggle="modal"` | Abre/cierra un modal |
| `data-bs-target="#id"` | El elemento afectado |
| `data-bs-dismiss="modal\|alert\|offcanvas"` | Cierra el componente |
| `data-bs-parent="#id"` | Solo un panel abierto en el acordeón |
| `data-bs-ride="carousel"` | Autorreproducción del carrusel |
| `data-bs-interval="6000"` | Milisegundos entre diapositivas |
| `data-bs-slide="prev\|next"` | Navegación del carrusel |
| `data-bs-slide-to="2"` | Ir a la diapositiva 3 |
| `data-bs-spy="scroll"` | Marca el enlace de la sección visible |
| `data-bs-theme="dark\|light"` | Fuerza el modo claro u oscuro |

## Utilidades de accesibilidad

| Clase / atributo | Para qué |
|------------------|----------|
| `visually-hidden` | Texto invisible pero leído por lectores de pantalla |
| `visually-hidden-focusable` | Visible solo cuando recibe el foco (enlaces de salto) |
| `aria-label="…"` | Nombre accesible de botones y enlaces |
| `aria-hidden="true"` | Oculta el elemento al lector (iconos decorativos) |
| `aria-current="page"` | Marca "estás aquí" en la navegación |
| `aria-expanded` / `aria-controls` | Estado y control de los desplegables |
| `alt="…"` | Texto alternativo (obligatorio en cada `<img>`) |

## JavaScript: los objetos de Bootstrap

```javascript
const modal  = new bootstrap.Modal('#miModal');   // .show() .hide() .toggle()
const tooltip = new bootstrap.Tooltip('#miTip');   // .show() .hide()
const popover = new bootstrap.Popover('#miPop');
const toast   = new bootstrap.Toast('#miToast');   // .show()
const offcanvas = new bootstrap.Offcanvas('#menu');
const Collapse = bootstrap.Collapse.getOrCreateInstance('#panel'); // .show() .hide() .toggle()
```

---

# 🏆 Retos adicionales

Después del reto del Módulo 10, estos proyectos ordenados por dificultad te mantendrán Bootstrap fresco en la memoria:

### Nivel 1 — Refuerzo (30 min cada uno)

| # | Reto | Lo que practicas |
|---|------|------------------|
| 1 | **Portafolio personal** | Navbar, Hero, grid de proyectos, footer |
| 2 | **Card de restaurante** | Card con `card-img-top`, `ratio`, badges, botón |
| 3 | **Página 404** | Centrado vertical, un botón, algo de humor |
| 4 | **Formulario de encuesta** | Todos los tipos de input + validación |

### Nivel 2 · Intermedio (1 a 2 horas)

| # | Reto | Lo que practicas |
|---|------|------------------|
| 5 | **Tienda de productos** | Grid responsive, filtros, orden de columnas |
| 6 | **Agenda de eventos** | Carrusel + acordeón + `badge` por fecha |
| 7 | **Landing de(app) aplicación** | Modo oscuro, botón de precio, tabla de planes |
| 8 | **Clon de página de noticias** | Barras laterales, `offset`, `list-group`, `sticky-top` |

### Nivel 3 · Avanzado (medio día)

| # | Reto | Lo que practicas |
|---|------|------------------|
| 9 | **Dashboard** | `table-responsive`, `sidebar` con `offcanvas`, `card` con `stat` |
| 10 | **Multilingüe** | Bootstrap no cambia solo: investiga `dir="rtl"` |
| 11 | **Sistema de diseño propio** | Variables CSS, tokens, `data-bs-theme`, documentación |
| 12 | **Modo alto contraste** | `[data-bs-theme="dark"]` con bordes marcados para baja visión |

### Retos de Buenas prácticas

| # | Reto |
|---|------|
| 13 | Pasa tu proyecto por el validador de HTML y deja **0 errores** |
| 14 | Reduce tu CSS propio a menos de 60 líneas usando más utilidades |
| 15 | Publica tu proyecto en **GitHub Pages** y comparte el enlace |
| 16 | Reconstruye un sitio real que te guste **sin mirar su código** |
| 17 | Documenta tu proyecto en un `README.md` con capturas |

---

# 📚 Recursos oficiales

### Documentación de Bootstrap (en español disponible)

| Recurso | Enlace |
|---------|--------|
| Documentación oficial 5.3 | <https://getbootstrap.com/docs/5.3/> |
| Traducción al español | <https://getbootstrap.com/docs/5.3/getting-started/translations/> |
| Ejemplos y plantillas | <https://getbootstrap.com/docs/5.3/examples/> |
| Grid (referencia completa) | <https://getbootstrap.com/docs/5.3/layout/grid/> |
| Componentes | <https://getbootstrap.com/docs/5.3/components/> |
| Utilidades (todas) | <https://getbootstrap.com/docs/5.3/utilities/> |
| Variables CSS / modo oscuro | <https://getbootstrap.com/docs/5.3/customize/css-variables/> |
| Forms (validación) | <https://getbootstrap.com/docs/5.3/forms/validation/> |
| Migación desde v4 | <https://getbootstrap.com/docs/5.3/migration/> |
| Código fuente (GitHub) | <https://github.com/twbs/bootstrap> |
| Releases y descargas | <https://github.com/twbs/bootstrap/releases> |
| Blog oficial | <https://blog.getbootstrap.com/> |

### Bootstrap Icons (los iconos de este tutorial)

| Recurso | Enlace |
|---------|--------|
| Sitio oficial | <https://icons.getbootstrap.com/> |
| Buscador por nombre | <https://icons.getbootstrap.com/#search> |

### Color y diseño

| Recurso | Enlace |
|---------|--------|
| Generador de paletas | <https://coolors.co/> |
| Contraste (WCAG) | <https://webaim.org/resources/contrastchecker/> |
| Paletas accesibles | <https://www.color-box.io/> |

### Accesibilidad y validación

| Recurso | Enlace |
|---------|--------|
| Patrones ARIA | <https://www.w3.org/WAI/ARIA/apg/> |
| Validador de HTML | <https://validator.w3.org/nu/> |
| WAVE (análisis visual) | <https://wave.webaim.org/> |
| Lighthouse (en Chrome) | Pestaña *Lighthouse* en las herramientas de desarrollo |
| Verificar colores con daltonismo | <https://www.colorjack.com/> |

### HTML y CSS (para complementar)

| Recurso | Enlace |
|---------|--------|
| MDN (la biblia del desarrollo web) | <https://developer.mozilla.org/es/> |
| Flexbox (guía interactiva) | <https://css-tricks.com/snippets/css/a-guide-to-flexbox/> |
| CSS Grid (guía interactiva) | <https://css-tricks.com/snippets/css/complete-guide-grid/> |
| Squoosh (optimizar imágenes) | <https://squoosh.app/> |

---

## 🎓 Cierre

Terminaste un sitio completo con Bootstrap 5.3.8: con navegación responsive, grid, tarjetas, formularios con validación, modal, acordeón, carrusel, footer, modo oscuro y personalización con variables CSS. **Todo eso lo hiciste escribiéndolo, no solo leyéndolo.**

Lo que te llevas de verdad no son las clases: es el **método** para elegir clases. Cuando veas un diseño y pienses *"esto son tres columnas que en móvil se apilan y en escritorio se reparten en tercios"*, ya sabes la respuesta: `col-12 col-md-6 col-lg-4`. Ese pensamiento es lo que separa a quien copia tutoriales de quien maqueta.

Ahora haz el reto del Módulo 10, y después **clona un sitio real**. Es el mejor ejercicio que existe.

¡Mucho éxito! 🚀

