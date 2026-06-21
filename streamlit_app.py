import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="FATHER-OS: SYSTEM UNLOCKED",
    page_icon="🖥️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Ocultar elementos de interfaz nativos de Streamlit
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {
            padding-top: 0rem;
            padding-bottom: 0rem;
            padding-left: 0rem;
            padding-right: 0rem;
        }
        iframe {
            display: block;
            border: none;
        }
    </style>
""", unsafe_allow_html=True)

father_os_interface = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <style>
        :root {
            --neon-green: #00ff66;
            --neon-red: #ff3333;
            --dark-bg: #0a0a0f;
            --panel-bg: rgba(16, 16, 24, 0.85);
            --text-color: #e0e0e6;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            background-color: var(--dark-bg);
            color: var(--text-color);
            font-family: 'Courier New', Courier, monospace;
            overflow: hidden;
            height: 100vh;
            width: 100vw;
        }

        #bg-canvas {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 1;
            opacity: 0.15;
        }

        .interface-container {
            position: relative;
            z-index: 2;
            display: grid;
            grid-template-columns: 1.2fr 2fr;
            grid-template-rows: auto 1fr;
            gap: 20px;
            height: 100vh;
            padding: 20px;
        }

        header {
            grid-column: 1 / span 2;
            background: var(--panel-bg);
            border: 1px solid var(--neon-green);
            padding: 15px;
            text-align: center;
            box-shadow: 0 0 15px rgba(0, 255, 102, 0.2);
        }

        .blink {
            animation: blinker 1s linear infinite;
        }
        @keyframes blinker { 50% { opacity: 0; } }

        .panel {
            background: var(--panel-bg);
            border: 1px solid rgba(0, 255, 102, 0.3);
            padding: 20px;
            border-radius: 4px;
            display: flex;
            flex-direction: column;
            gap: 22px;
        }

        .stats-title {
            color: var(--neon-green);
            font-size: 1.2rem;
            border-bottom: 1px dashed rgba(0, 255, 102, 0.5);
            padding-bottom: 5px;
        }

        .stat-row {
            display: flex;
            flex-direction: column;
            gap: 6px;
        }

        .stat-header {
            display: flex;
            justify-content: space-between;
            font-size: 0.9rem;
        }

        .bar-container {
            width: 100%;
            background: #1a1a26;
            height: 18px;
            border: 1px solid rgba(255,255,255,0.1);
            overflow: hidden;
        }

        .bar-fill {
            height: 100%;
            background: var(--neon-green);
            width: 0%;
        }

        .bar-fill.critical {
            background: var(--neon-red);
            box-shadow: 0 0 10px var(--neon-red);
        }

        @keyframes fillTo80 { 0% { width: 0%; } 100% { width: 80%; } }
        @keyframes fillTo100 { 0% { width: 0%; } 100% { width: 100%; } }

        #bar-int { animation: fillTo80 2.5s cubic-bezier(0.1, 0.85, 0.25, 1) forwards; }
        #bar-payaso { animation: fillTo100 2.5s cubic-bezier(0.1, 0.85, 0.25, 1) forwards; }
        #bar-molestoso { animation: fillTo100 2.5s cubic-bezier(0.1, 0.85, 0.25, 1) forwards; }

        .string-value {
            color: #00ffff;
            font-weight: bold;
            padding: 2px 5px;
            background: rgba(0, 255, 255, 0.1);
            border: 1px solid rgba(0, 255, 255, 0.3);
            width: fit-content;
            margin-top: 2px;
        }

        .terminal {
            background: #050508;
            border: 1px solid var(--neon-green);
            font-family: 'Courier New', monospace;
            padding: 25px;
            overflow-y: auto;
            white-space: pre-wrap;
            color: #fff;
            box-shadow: inset 0 0 15px rgba(0,0,0,0.9);
            font-size: 1.05rem;
            line-height: 1.5;
            cursor: text;
        }

        /* corrección estricta de visibilidad para el input */
        #terminal-key-input {
            background: transparent !important;
            border: none !important;
            color: #00ffff !important;
            caret-color: #00ffff !important;
            font-family: 'Courier New', monospace !important;
            font-size: 1.05rem !important;
            outline: none !important;
            width: 180px !important;
            height: 24px !important;
            display: inline-block !important;
            padding: 0 5px !important;
        }
    </style>
</head>
<body>

    <canvas id="bg-canvas"></canvas>

    <div class="interface-container">
        <header>
            <h1>[ STREAMLIT_CORE_v6.1: DECRYPTION_PATCH_APPLIED ]</h1>
            <p>ESTADO_DEL_NÚCLEO: <span class="blink" style="color: var(--neon-green);">DYNAMIC_OK</span> | ID: PAPÁ_MAIN</p>
        </header>

        <div class="panel">
            <h2 class="stats-title">> MÉTRICAS_DE_RENDIMIENTO</h2>
            
            <div class="stat-row">
                <div class="stat-header">
                    <label>INTELIGENCIA:</label>
                    <span>80/100</span>
                </div>
                <div class="bar-container"><div class="bar-fill" id="bar-int"></div></div>
            </div>

            <div class="stat-row">
                <div class="stat-header">
                    <label>MODO ADAPTATIVO:</label>
                </div>
                <div class="string-value">"Adaptate TU !"</div>
            </div>

            <div class="stat-row">
                <div class="stat-header">
                    <label>NIVEL DE PAYASO:</label>
                    <span>100/100</span>
                </div>
                <div class="bar-container"><div class="bar-fill" id="bar-payaso"></div></div>
            </div>

            <div class="stat-row">
                <div class="stat-header" style="color: var(--neon-red);">
                    <label>MOLESTOSO:</label>
                    <span class="blink">999/100 [CRITICAL]</span>
                </div>
                <div class="bar-container"><div class="bar-fill critical" id="bar-molestoso"></div></div>
            </div>
        </div>

        <div class="terminal" id="terminal-container">
            <div id="terminal-output"></div>
            
            <div id="terminal-input-row" style="display: none; margin-top: 15px;">
                <span style="color: var(--neon-green); font-weight: bold;">> INTRODUCE LA CLAVE DE 7 DÍGITOS:</span> 
                <input type="text" id="terminal-key-input" maxlength="7" autocomplete="off" autofocus>
            </div>

            <div id="decryption-result" style="display: none; margin-top: 30px; border-top: 1px dashed #00ffff; padding-top: 20px; text-align: center;">
                <p style="color: #00ffff; font-size: 0.85rem; font-family: monospace; margin-bottom: 10px;">[ TRANSMISIÓN DESENCRIPTADA ]</p>
                <h1 style="color: #00ff66; font-size: 4rem; font-family: monospace; text-shadow: 0 0 25px rgba(0,255,102,0.7); animation: blinker 1.5s linear infinite;">BIEN :)</h1>
            </div>
        </div>
    </div>

    <script>
        const canvas = document.getElementById('bg-canvas');
        if (canvas) {
            const ctx = canvas.getContext('2d');
            function resizeCanvas() {
                canvas.width = window.innerWidth;
                canvas.height = window.innerHeight;
            }
            resizeCanvas();
            window.addEventListener('resize', resizeCanvas);

            const letters = '0123456789SYSTEMINITIALIZINGCORESTREAMLITOPTIMIZED';
            const fontSize = 14;
            const columns = canvas.width / fontSize;
            const drops = Array(Math.floor(columns)).fill(1);

            function drawMatrix() {
                ctx.fillStyle = 'rgba(10, 10, 15, 0.05)';
                ctx.fillRect(0, 0, canvas.width, canvas.height);
                ctx.fillStyle = '#00ff66';
                ctx.font = fontSize + 'px monospace';

                for (let i = 0; i < drops.length; i++) {
                    const text = letters[Math.floor(Math.random() * letters.length)];
                    ctx.fillText(text, i * fontSize, drops[i] * fontSize);
                    if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) {
                        drops[i] = 0;
                    }
                    drops[i]++;
                }
            }
            setInterval(drawMatrix, 33);
        }

        const terminalText = [
            "> Inicializando subsistema de análisis de estadísticas familiares...",
            "> Procesando datos de entrada...",
            "> [ALERTA] Desbordamiento de enteros detectado en el parámetro: MOLESTOSO.",
            "> Reconfigurando búfer para admitir magnitudes superiores a 999...",
            "> Corrigiendo cadenas de caracteres: 'PAGASO' -> 'PAYASO'...",
            "> Desplegando animaciones nativas CSS via GPU...",
            "> Datos validados correctamente.\\n",
            "--------------------------------------------------",
            "SISTEMA DE SEGURIDAD NÚCLEO: ENCRIPTADO ACTIVADO",
            "--------------------------------------------------\\n",
            "> El núcleo principal requiere autenticación externa de 7 dígitos.",
            "> Completa el protocolo inferior para generar la firma criptográfica..."
        ];

        let lineIndex = 0;
        let charIndex = 0;

        function typeTerminal() {
            const terminal = document.getElementById('terminal-output');
            const container = document.getElementById('terminal-container');
            if (!terminal || !container) return;

            if (lineIndex < terminalText.length) {
                let currentLine = terminalText[lineIndex];
                if (charIndex < currentLine.length) {
                    terminal.innerHTML += currentLine.charAt(charIndex);
                    charIndex++;
                    setTimeout(typeTerminal, 12); 
                } else {
                    terminal.innerHTML += "\\n";
                    lineIndex++;
                    charIndex = 0;
                    setTimeout(typeTerminal, 120); 
                }
                container.scrollTop = container.scrollHeight;
            } else {
                const inputRow = document.getElementById('terminal-input-row');
                const keyInput = document.getElementById('terminal-key-input');
                if (inputRow && keyInput) {
                    inputRow.style.display = 'block';
                    keyInput.focus();
                }
            }
        }
        setTimeout(typeTerminal, 400);

        setTimeout(() => {
            const keyInput = document.getElementById('terminal-key-input');
            const container = document.getElementById('terminal-container');
            
            if (container && keyInput) {
                container.addEventListener('click', () => keyInput.focus());
                
                keyInput.addEventListener('keydown', function(e) {
                    if (e.key === 'Enter') {
                        const val = this.value.trim();
                        let termOut = document.getElementById('terminal-output');
                        
                        if (val === '9991100') {
                            document.getElementById('terminal-input-row').style.display = 'none';
                            termOut.innerHTML += "\\n\\n> [OK] FIRMA CORRECTA RECONOCIDA.\\n> COMPILANDO DIRECTIVA FINAL...";
                            
                            setTimeout(() => {
                                document.getElementById('decryption-result').style.display = 'block';
                                container.scrollTop = container.scrollHeight;
                            }, 1000);
                        } else {
                            termOut.innerHTML += `\\n\\n> [ERROR] CLAVE "${val}" CORRUPTA o RECHAZADA.\\n> Acceso denegado. Introduce el código correcto del protocolo.`;
                            this.value = '';
                            container.scrollTop = container.scrollHeight;
                        }
                    }
                });
            }
        }, 800);
    </script>
</body>
</html>
"""

components.html(father_os_interface, height=520, scrolling=False)


# =============================================================================
# MOTOR DE LA BÚSQUEDA DEL TESORO (INTEGRADO BAJO EL IFRAME)
# =============================================================================

st.markdown("---")
st.markdown("<h2 style='color: #00ff66; font-family: monospace; text-align: center;'>[ ACCESO A SUBRUTINA: BÚSQUEDA DEL TESORO ]</h2>", unsafe_allow_html=True)

if 'hunt_level' not in st.session_state:
    st.session_state['hunt_level'] = 1

quiz_data = {
    1: {
        "rango": "MEDIO",
        "pregunta": "Un bate y una pelota cuestan $1.10 en total. El bate cuesta $1.00 más que la pelota. ¿Cuánto cuesta la pelota?",
        "instruccion": "Responde solo con el valor numérico decimal (ej: 0.50).",
        "soluciones": ["0.05", ".05"],
        "fail_hint": "Si pensaste en 0.10, la diferencia sería de $0.90, no de $1.00. Revisa el álgebra elemental."
    },
    2: {
        "rango": "MEDIO",
        "pregunta": "Si 5 máquinas hacen 5 artículos en 5 minutos, ¿cuánto tiempo tardan 100 máquinas en hacer 100 artículos?",
        "instruccion": "Responde solo con el número entero de minutos.",
        "soluciones": ["5"],
        "fail_hint": "La tasa de producción es constante. Cada máquina tarda 5 minutos en hacer un artículo de forma independiente."
    },
    3: {
        "rango": "MEDIO",
        "pregunta": "En un lago hay un parche de nenúfares que duplica su tamaño cada día. Si tarda 48 días en cubrir todo el lago, ¿cuántos días tarda en cubrir exactamente la mitad?",
        "instruccion": "Responde solo con el número entero de días.",
        "soluciones": ["47"],
        "fail_hint": "Si se duplica cada día, el día anterior al final (48 - 1) estaba exactamente a la mitad."
    },
    4: {
        "rango": "MEDIO",
        "pregunta": "Divide 30 por 0.5 y súmale 10. ¿Cuál es el resultado final?",
        "instruccion": "Responde solo con el número entero resultante.",
        "soluciones": ["70"],
        "fail_hint": "Dividir por 0.5 es matemáticamente equivalente a multiplicar por 2. No es lo mismo que dividir entre 2."
    },
    5: {
        "rango": "MEDIO",
        "pregunta": "Un granjero tiene 17 ovejas. Todas menos 9 mueren debido a un error de ejecución en el servidor. ¿Cuántas ovejas vivas le quedan?",
        "instruccion": "Responde solo con el número entero.",
        "soluciones": ["9"],
        "fail_hint": "Lee la sintaxis de la frase con cuidado: 'Todas menos 9 mueren'."
    },
    6: {
        "rango": "MEDIO",
        "pregunta": "¿Cuántos ladrillos se necesitan exactamente para completar una casa de ladrillos de un solo piso?",
        "instruccion": "Responde en texto plano, minúsculas y sin puntos.",
        "soluciones": ["el ultimo", "el último"],
        "fail_hint": "Trampa lingüística. No es un cálculo de volumen, es una secuencia temporal."
    },
    7: {
        "rango": "MEDIO",
        "pregunta": "Si dos pintores pueden pintar dos habitaciones en dos horas, ¿cuántos pintores se necesitan para pintar 18 habitaciones en 18 horas?",
        "instruccion": "Responde solo con el número entero de pintores.",
        "soluciones": ["2"],
        "fail_hint": "La capacidad de procesamiento no cambia. Dos pintores siguen haciendo el mismo ratio por hora de forma lineal."
    },
    8: {
        "rango": "MEDIO",
        "pregunta": "Un avión comercial se estrella exactamente en la frontera entre Chile y Argentina. ¿En qué país se debe enterrar legalmente a los sobrevivientes?",
        "instruccion": "Responde con una frase corta en minúsculas.",
        "soluciones": ["no se entierran", "a los sobrevivientes no se les entierra", "ninguno"],
        "fail_hint": "Analiza el estado del objeto antes de aplicar la función de entierro: son sobrevivientes."
    },
    9: {
        "rango": "MEDIO",
        "pregunta": "Tengo 3 manzanas en memoria local. Si tú vienes y me quitas 2, ¿cuántas manzanas tienes tú?",
        "instruccion": "Responde solo con el número entero.",
        "soluciones": ["2"],
        "fail_hint": "La pregunta interroga sobre tus recursos asignados, no sobre los míos."
    },
    10: {
        "rango": "MEDIO",
        "pregunta": "Un caracol sube por un pozo de 10 metros. Cada día sube 3 metros, pero cada noche resbala 2 metros hacia abajo. ¿En cuántos días saldrá del pozo?",
        "instruccion": "Responde solo con el número de días.",
        "soluciones": ["8"],
        "fail_hint": "En el día 7 llega a los 8 metros. Al día 8 sube 3 metros, alcanzando los 11 metros y saliendo del pozo ANTES de que llegue la noche para resbalar."
    },
    11: {
        "rango": "DIFÍCIL",
        "pregunta": "En un cajón completamente oscuro hay 2 pares de calcetines negros y 2 pares de calcetines blancos. ¿Cuál es el número mínimo de calcetines individuales que debes extraer para asegurar con 100% de certeza que tienes al menos un par del mismo color?",
        "instruccion": "Responde solo con el número entero.",
        "soluciones": ["3"],
        "fail_hint": "Principio del palomar. Solo existen 2 estados de color posibles. Al extraer el tercero, inevitablemente colisiona con uno de los dos anteriores."
    },
    12: {
        "rango": "DIFÍCIL",
        "pregunta": "Si un reloj de pared tarda exactamente 6 segundos en dar las 6 campanadas de las 6:00, ¿cuánto tiempo tardará en dar las 12 campanadas de las 12:00?",
        "instruccion": "Responde solo con el valor decimal usando punto (ej: 12.5).",
        "soluciones": ["13.2"],
        "fail_hint": "El tiempo transcurre en los INTERVALOS entre campanadas. 6 campanadas tienen 5 intervalos (6s / 5 = 1.2s por intervalo). Calcula para 11 intervalos."
    },
    13: {
        "rango": "SUPER DIFÍCIL",
        "pregunta": "Dada la ecuación funcional f(x) + 2f(1/x) = 3x para todo x real diferente de cero. Encuentra el valor exacto de f(2).",
        "instruccion": "Responde solo con el número entero (puede incluir signo negativo si aplica).",
        "soluciones": ["-1"],
        "fail_hint": "No intentes resolver la función general f(x). Crea un sistema de ecuaciones lineales de 2x2 evaluando la expresión en x=2 y en x=1/2, luego despeja f(2)."
    }
}

current_step = st.session_state['hunt_level']

if current_step <= len(quiz_data):
    node = quiz_data[current_step]
    
    st.markdown(f"""
        <div style='background-color: #101018; border: 1px solid #00ff66; padding: 20px; border-radius: 5px; margin-bottom: 15px;'>
            <span style='background-color: {"#ff3333" if node["rango"] != "MEDIO" else "#00ff66"}; color: black; padding: 2px 6px; font-weight: bold; font-family: monospace;'>
                NIVEL {current_step} - RANGO: {node["rango"]}
            </span>
            <p style='font-family: monospace; font-size: 1.1rem; margin-top: 15px; color: #ffffff;'>{node["pregunta"]}</p>
            <p style='color: #00ffff; font-family: monospace; font-size: 0.85rem;'>* Instrucción: {node["instruccion"]}</p>
        </div>
    """, unsafe_allow_html=True)
    
    user_ans = st.text_input("Introduce la clave de desencriptación:", key=f"hunt_in_{current_step}")
    
    if st.button("PROCESAR RESPUESTA ➔", key=f"btn_{current_step}"):
        clean_ans = user_ans.lower().strip()
        if clean_ans in node["soluciones"]:
            st.toast("ACCESO PERMITIDO. Cargando siguiente nodo...", icon="✅")
            st.session_state['hunt_level'] += 1
            st.rerun()
        else:
            st.error(f"ERROR DE VERIFICACIÓN. Código incorrecto.\\n\\nPISTA DEL SISTEMA: {node['fail_hint']}")
            
else:
    st.balloons()
    st.markdown("""
        <div style='background-color: #101018; border: 2px solid #00ff66; padding: 30px; text-align: center; border-radius: 5px;'>
            <h1 style='color: #00ff66; font-family: monospace;'>[ PROTOCOLO COMPLETADO CON ÉXITO ]</h1>
            <p style='font-family: monospace; color: #e0e0e6; font-size: 1.2rem; margin-top: 15px;'>
                Has superado todos los filtros de seguridad y trampas lógicas implementadas.
            </p>
            
            <div style='background: rgba(0, 255, 102, 0.1); border: 1px dashed #00ff66; padding: 15px; margin: 20px auto; max-width: 550px;'>
                <p style='font-family: monospace; color: #00ff66; font-size: 1.1rem; margin: 0;'>
                    🔑 CLAVE GENERADA PARA CONSOLA SUPERIOR:
                </p>
                <h2 style='font-family: monospace; color: #00ffff; letter-spacing: 5px; margin: 10px 0; font-size: 2rem;'>9991100</h2>
                <p style='font-family: monospace; color: #888899; font-size: 0.85rem; margin: 0;'>
                    Introduce este código en el prompt interactivo de la consola de arriba para revelar el mensaje final.
                </p>
            </div>
            
            <p style='font-family: monospace; color: #00ffff; font-size: 1.2rem; font-weight: bold; margin-top: 20px;'>
                TU REGALO FÍSICO ESTÁ OCULTO EN: [Escribe aquí el escondite real del regalo]
            </p>
        </div>
    """, unsafe_allow_html=True)
