/* ============================================================
   Tutorial Bootstrap 5.3.8 · Comportamiento de la versión web
   Sin dependencias: el sitio funciona aunque falle el CDN.
   ============================================================ */
(function () {
    'use strict';

    /* ---------------- Tema claro / oscuro ---------------- */

    var botonTema = document.getElementById('botonTema');
    var iconoTema = document.getElementById('iconoTema');
    var claveTema = 'tutorial-tema';

    function aplicarTema(tema) {
        document.documentElement.setAttribute('data-bs-theme', tema);
        if (iconoTema) {
            iconoTema.className = tema === 'dark' ? 'bi bi-sun-fill' : 'bi bi-moon-stars-fill';
        }
        try {
            localStorage.setItem(claveTema, tema);
        } catch (e) { /* modo privado */ }
    }

    if (botonTema) {
        botonTema.addEventListener('click', function () {
            var actual = document.documentElement.getAttribute('data-bs-theme');
            aplicarTema(actual === 'dark' ? 'light' : 'dark');
        });
    }

    /* ---------------- Índice lateral en móvil ---------------- */

    var panelIndice = document.getElementById('panelIndice');
    var botonIndice = document.getElementById('botonIndice');

    function cerrarIndice() {
        if (!panelIndice) return;
        panelIndice.classList.remove('abierto');
        document.body.classList.remove('oculto-indice');
        if (botonIndice) botonIndice.setAttribute('aria-expanded', 'false');
    }

    if (botonIndice && panelIndice) {
        botonIndice.addEventListener('click', function () {
            var abierto = panelIndice.classList.toggle('abierto');
            document.body.classList.toggle('oculto-indice', abierto);
            botonIndice.setAttribute('aria-expanded', abierto ? 'true' : 'false');
        });

        panelIndice.addEventListener('click', function (evento) {
            if (evento.target.closest('a')) cerrarIndice();
        });

        document.addEventListener('keydown', function (evento) {
            if (evento.key === 'Escape') cerrarIndice();
        });
    }

    /* ---------------- Botón «copiar» ---------------- */

    document.addEventListener('click', function (evento) {
        var boton = evento.target.closest('.btn-copiar');
        if (!boton) return;

        var bloque = boton.closest('.bloque-codigo');
        var codigo = bloque ? bloque.querySelector('code') : null;
        if (!codigo) return;

        var texto = codigo.innerText;
        var original = boton.innerHTML;

        function confirmar(ok) {
            boton.innerHTML = ok ? '✓ Copiado' : 'No se pudo copiar';
            boton.classList.toggle('copiado', ok);
            setTimeout(function () {
                boton.innerHTML = original;
                boton.classList.remove('copiado');
            }, 1800);
        }

        if (navigator.clipboard && navigator.clipboard.writeText) {
            navigator.clipboard.writeText(texto).then(
                function () { confirmar(true); },
                function () { confirmar(seleccionar(texto)); }
            );
        } else {
            confirmar(seleccionar(texto));
        }
    });

    function seleccionar(texto) {
        var area = document.createElement('textarea');
        area.value = texto;
        area.setAttribute('readonly', '');
        area.style.position = 'fixed';
        area.style.opacity = '0';
        document.body.appendChild(area);
        area.select();
        var ok = false;
        try { ok = document.execCommand('copy'); } catch (e) { ok = false; }
        document.body.removeChild(area);
        return ok;
    }

    /* ---------------- Resaltado suave de sintaxis ---------------- */

    var PALETA = {
        etiqueta: 'var(--bs-danger)',
        atributo: 'var(--bs-success)',
        valor: 'var(--bs-info)',
        cadena: 'var(--bs-warning)',
        comentario: 'var(--bs-secondary-color)'
    };

    function pintar(txt, color) {
        return txt ? '<span style="color:' + color + '">' + txt + '</span>' : txt;
    }

    /* Colorea una etiqueta ya escapada. Se recorre carácter a carácter para no
       volver a analizar el marcado que vamos insertando (si se usara replace
       en cadena, los <span> generados también se colorearían entre sí). */
    function colorearEtiqueta(tag) {
        var salida = '';
        var i = 0;
        var apertura = /^(&lt;\/?)([\w:-]+)/.exec(tag);

        if (apertura) {
            salida += pintar(apertura[1] + apertura[2], PALETA.etiqueta);
            i = apertura[0].length;
        }

        while (i < tag.length) {
            if (tag[i] === ' ') {
                salida += ' ';
                i += 1;
                continue;
            }

            var igual = tag.indexOf('=', i);
            var fin = tag.length;

            if (igual !== -1) {
                var comilla = tag[igual + 1];
                if (comilla === '"' || comilla === "'") {
                    var cierre = tag.indexOf(comilla, igual + 2);
                    fin = cierre === -1 ? tag.length : cierre + 1;
                }
            }

            var trozo = tag.slice(i, fin);

            if (igual !== -1 && igual < fin) {
                salida += pintar(trozo.slice(0, igual - i), PALETA.atributo);
                salida += pintar(trozo.slice(igual - i), PALETA.valor);
            } else {
                salida += pintar(trozo, PALETA.etiqueta);
            }

            i = fin;
        }

        return salida;
    }

    function resaltar(bloque) {
        var pre = bloque.querySelector('pre');
        var code = bloque.querySelector('code');
        if (!pre || !code || code.dataset.resaltado) return;

        var lenguaje = (pre.className || '').trim();
        if (['html', 'xml'].indexOf(lenguaje) === -1) return;

        // El texto plano se escapa primero: así el innerHTML de abajo no
        // interpreta el código como HTML real.
        var texto = code.textContent
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;');

        texto = texto
            .replace(/&lt;!--[\s\S]*?--&gt;/g, function (comentario) {
                return pintar(comentario, PALETA.comentario);
            })
            .replace(/&lt;\/?[\w:-]+[^]*?&gt;/g, colorearEtiqueta);

        code.innerHTML = texto;
        code.dataset.resaltado = '1';
    }

    var bloques = document.querySelectorAll('.bloque-codigo');
    for (var i = 0; i < bloques.length; i++) {
        resaltar(bloques[i]);
    }

    /* ---------------- Buscador ---------------- */

    var buscador = document.getElementById('buscador');
    var resultados = document.getElementById('resultadosBusqueda');
    var article = document.getElementById('contenido-tutorial');

    if (buscador && article) {
        var secciones = Array.prototype.slice.call(article.querySelectorAll('h1, h2, h3'));

        function sinAcento(txt) {
            return txt.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
        }

        function escapar(txt) {
            return txt.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
        }

        // Guarda el título limpio de cada encabezado y recompone el enlace "#"
        var titulosLimpios = secciones.map(function (seccion) {
            var enlace = seccion.querySelector('.ancla-enlace');
            return {
                nodo: seccion,
                ancla: seccion.id,
                prefijo: enlace ? enlace.outerHTML : ''
            };
        });

        function pintar(termino) {
            var objetivo = sinAcento(termino);
            var coincidencias = 0;

            titulosLimpios.forEach(function (item) {
                var titulo = item.nodo.textContent.replace(/^#/, '').trim();
                var posicion = sinAcento(titulo).indexOf(objetivo);

                if (posicion === -1) {
                    item.nodo.innerHTML = item.prefijo + escapar(titulo);
                    return;
                }

                coincidencias++;
                var antes = titulo.slice(0, posicion);
                var durante = titulo.slice(posicion, posicion + termino.length);
                var despues = titulo.slice(posicion + termino.length);

                item.nodo.innerHTML = item.prefijo + escapar(antes) +
                    '<mark class="marcado">' + escapar(durante) + '</mark>' +
                    escapar(despues);
            });

            if (resultados) {
                resultados.textContent = termino.length < 2 ? '' :
                    (coincidencias === 0 ? 'Sin coincidencias' :
                     coincidencias === 1 ? '1 coincidencia' :
                     coincidencias + ' coincidencias');
            }

            return coincidencias;
        }

        buscador.addEventListener('input', function () {
            pintar(buscador.value.trim());
        });

        buscador.addEventListener('keydown', function (evento) {
            if (evento.key !== 'Escape') return;
            buscador.value = '';
            pintar('');
            buscador.blur();
        });

        document.addEventListener('keydown', function (evento) {
            if (evento.key === '/' && document.activeElement !== buscador &&
                /^(INPUT|TEXTAREA|SELECT)$/.test(document.activeElement.tagName) === false) {
                evento.preventDefault();
                buscador.focus();
            }
        });
    }

    /* ---------------- Barra de progreso y botón "volver arriba" ---------------- */

    var progreso = document.getElementById('progreso');
    var botonArriba = document.getElementById('botonArriba');

    function alDesplazar() {
        var alto = document.documentElement.scrollHeight - window.innerHeight;
        var porcentaje = alto > 0 ? (window.scrollY / alto) * 100 : 0;
        if (progreso) progreso.style.width = porcentaje.toFixed(2) + '%';
        if (botonArriba) botonArriba.hidden = window.scrollY < 400;
    }

    var pendiente;
    window.addEventListener('scroll', function () {
        if (pendiente) return;
        pendiente = requestAnimationFrame(function () {
            alDesplazar();
            pendiente = null;
        });
    }, { passive: true });
    alDesplazar();

    if (botonArriba) {
        botonArriba.addEventListener('click', function () {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    /* ---------------- Índice activo (scroll-spy) ---------------- */

    var enlacesIndice = Array.prototype.slice.call(document.querySelectorAll('.enlace-indice'));

    if (enlacesIndice.length && 'IntersectionObserver' in window) {
        var porAncla = {};
        enlacesIndice.forEach(function (enlace) {
            porAncla[enlace.getAttribute('href').slice(1)] = enlace;
        });

        var visibles = {};

        var observador = new IntersectionObserver(function (entradas) {
            entradas.forEach(function (entrada) {
                visibles[entrada.target.id] = entrada.isIntersecting
                    ? entrada.intersectionRatio
                    : 0;
            });

            var mejor = null;
            var mejorProporcion = 0;
            Object.keys(visibles).forEach(function (clave) {
                if (visibles[clave] > mejorProporcion) {
                    mejorProporcion = visibles[clave];
                    mejor = clave;
                }
            });

            enlacesIndice.forEach(function (e) { e.classList.remove('activo'); });

            if (mejor && porAncla[mejor]) {
                porAncla[mejor].classList.add('activo');
                var caja = porAncla[mejor].getBoundingClientRect();
                var panel = document.getElementById('panelIndice');
                if (panel && (caja.top < 70 || caja.bottom > window.innerHeight - 40)) {
                    panel.scrollTop += caja.top - window.innerHeight / 2;
                }
            }
        }, { rootMargin: '-15% 0px -70% 0px', threshold: [0, .25, .5, 1] });

        Object.keys(porAncla).forEach(function (ancla) {
            var elemento = document.getElementById(ancla);
            if (elemento) observador.observe(elemento);
        });
    }

    /* ---------------- Navegación anterior / siguiente ---------------- */

    var navModulos = document.querySelector('.nav-modulos');

    function crearEnlace(ancla, texto, etiqueta) {
        var a = document.createElement('a');
        a.href = '#' + ancla;
        var small = document.createElement('small');
        small.textContent = etiqueta;
        var strong = document.createElement('strong');
        strong.textContent = texto;
        a.appendChild(small);
        a.appendChild(strong);
        a.className = etiqueta === 'Siguiente' ? 'siguiente' : '';
        return a;
    }

    if (navModulos) {
        // Los módulos pueden ser <h1> (RutaUni) o <h2> (PixelCrew): buscamos
        // por el texto, no por el nivel.
        var modulos = Array.prototype.slice.call(
            document.querySelectorAll('#contenido-tutorial > h1, #contenido-tutorial > h2')
        ).filter(function (titulo) {
            return /^M[oó]dulo/i.test(titulo.textContent.replace(/^#/, '').trim());
        }).map(function (titulo) {
            return { ancla: titulo.id, texto: titulo.textContent.replace(/^#/, '').trim() };
        });

        if (modulos.length) {
            var enlaceAnterior = crearEnlace(modulos[0].ancla, modulos[0].texto, 'Anterior');
            var enlaceSiguiente = crearEnlace(
                modulos.length > 1 ? modulos[1].ancla : modulos[0].ancla,
                modulos.length > 1 ? modulos[1].texto : 'Volver al inicio',
                'Siguiente'
            );
            navModulos.appendChild(enlaceAnterior);
            navModulos.appendChild(enlaceSiguiente);

            var indiceActual = -1;

            function actualizarModulo() {
                var limite = window.innerHeight * 0.35;
                var nuevo = 0;

                modulos.forEach(function (modulo, i) {
                    var elemento = document.getElementById(modulo.ancla);
                    if (elemento && elemento.getBoundingClientRect().top <= limite) nuevo = i;
                });

                if (nuevo === indiceActual) return;
                indiceActual = nuevo;

                var previo = modulos[indiceActual];
                var prox = modulos[indiceActual + 1];

                enlaceAnterior.querySelector('strong').textContent = previo.texto;
                enlaceAnterior.href = '#' + previo.ancla;
                enlaceAnterior.querySelector('small').textContent =
                    indiceActual === 0 ? 'Empezaste aquí' : 'Anterior';

                if (prox) {
                    enlaceSiguiente.querySelector('strong').textContent = prox.texto;
                    enlaceSiguiente.href = '#' + prox.ancla;
                    enlaceSiguiente.querySelector('small').textContent = 'Siguiente';
                    enlaceSiguiente.removeAttribute('aria-disabled');
                    enlaceSiguiente.classList.remove('inactivo');
                } else {
                    enlaceSiguiente.querySelector('strong').textContent =
                        'Código completo del proyecto';
                    enlaceSiguiente.href = '#-código-completo-del-proyecto';
                    enlaceSiguiente.querySelector('small').textContent = 'Siguiente';
                }
            }

            var pendienteModulo;
            window.addEventListener('scroll', function () {
                if (pendienteModulo) return;
                pendienteModulo = requestAnimationFrame(function () {
                    actualizarModulo();
                    pendienteModulo = null;
                });
            }, { passive: true });

            actualizarModulo();
        }
    }

})();
