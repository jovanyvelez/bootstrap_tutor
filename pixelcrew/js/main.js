// ===== Validación del formulario de inscripción =====
const formulario = document.getElementById('formUnete');
const mensajeExito = document.getElementById('exito');

formulario.addEventListener('submit', (evento) => {
  evento.preventDefault(); // este sitio de práctica no envía datos a ningún servidor

  if (formulario.checkValidity()) {
    formulario.reset();
    formulario.classList.remove('was-validated');
    mensajeExito.classList.remove('d-none');
    mensajeExito.focus();               // el foco va al mensaje: quien navega con
                                         // teclado o lector de pantalla se entera
  } else {
    mensajeExito.classList.add('d-none');
    formulario.classList.add('was-validated');

    // Nadie se da cuenta de un error si no lo ve. Movemos el foco al primer
    // campo inválido: el navegador lo resalta y además lo deja preparado
    // para escribir de nuevo.
    const primerError = formulario.querySelector(':invalid');
    if (primerError) primerError.focus();
  }
});

// ===== Modo claro / oscuro =====
const raiz = document.documentElement;
const botonTema = document.getElementById('themeToggle');
const iconoTema = document.getElementById('themeIcon');
const CLAVE = 'pc-tema'; // el nombre con el que guardamos la preferencia

// El tema que ya tiene el dispositivo. Se consulta, no se supone.
const consultaSistema = window.matchMedia('(prefers-color-scheme: dark)');

// Leer y guardar puede fallar en modo privado: por eso van protegidos.
function leerTemaGuardado() {
  try {
    return localStorage.getItem(CLAVE);
  } catch (error) {
    return null;
  }
}

function aplicarTema(tema, recordar) {
  raiz.setAttribute('data-bs-theme', tema);
  iconoTema.textContent = tema === 'dark' ? '☀️' : '🌙'; // el ícono muestra a qué modo cambiarás

  // Solo guardamos cuando la ELECCIÓN es de la persona. Si guardáramos el
  // tema del sistema, después no sabríamos si ella eligió o si fue el default.
  if (recordar) {
    try {
      localStorage.setItem(CLAVE, tema);
    } catch (error) {
      /* en modo privado no se guarda, pero el sitio funciona igual */
    }
  }
}

// Al cargar: primero la elección de la persona; si no hay, la del sistema.
aplicarTema(leerTemaGuardado() || (consultaSistema.matches ? 'dark' : 'light'), false);

botonTema.addEventListener('click', () => {
  const actual = raiz.getAttribute('data-bs-theme');
  aplicarTema(actual === 'dark' ? 'light' : 'dark', true);
});

// Si la persona NO ha elegido nada y cambia el tema del sistema, la seguimos.
consultaSistema.addEventListener('change', (evento) => {
  if (!leerTemaGuardado()) {
    aplicarTema(evento.matches ? 'dark' : 'light', false);
  }
});
