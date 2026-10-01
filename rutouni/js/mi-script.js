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
