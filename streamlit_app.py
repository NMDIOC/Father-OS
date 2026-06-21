import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="FATHER-OS: ENGINE V5",
    page_icon="🖥️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

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
        }

        .bar-fill {
            height: 100%;
            background: var(--neon-green);
            width: 0%; /* Controlado estrictamente por JS */
        }

        .bar-fill.critical {
            background: var(--neon-red);
            box-shadow: 0 0 10px var(--neon-red);
        }

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
        }
    </style>
</head>
<body>

    <canvas id="bg-canvas"></canvas>

    <div class="interface-container">
        <header>
            <h1>[ STREAMLIT_CORE_v5.0: HARDWARE_ANIMATION_FORCED ]</h1>
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

        <div class="terminal" id="terminal-output"></div>
    </div>

    <script>
        // Matrix Background
        const canvas = document.getElementById('bg-canvas');
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

        // MOTOR DE ANIMACIÓN POR SOFTWARE (JAVASCRIPT STEPPER)
        let currentPct = 0;
        function animateBars() {
            if (currentPct <= 100) {
                // Inteligencia frena en 80
                if (currentPct <= 80) {
                    document.getElementById('bar-int').style.width = currentPct + "%";
                }
                // Las otras dos avanzan hasta 100
                document.getElementById('bar-payaso').style.width = currentPct + "%";
                document.getElementById('bar-molestoso').style.width = currentPct + "%";
                
                currentPct += 1.5; // Velocidad del incremento por cuadro
                requestAnimationFrame(animateBars);
            }
        }

        // Ejecutar animación tras un breve delay de carga estable
        setTimeout(() => {
            requestAnimationFrame(animateBars);
        }, 400);

        setTimeout(typeTerminal, 600);

        const terminalText = [
            "> Inicializando subsistema de análisis de estadísticas familiares...",
            "> Procesando datos de entrada...",
            "> [ALERTA] Desbordamiento de enteros detectado en el parámetro: MOLESTOSO.",
            "> Reconfigurando búfer para admitir magnitudes superiores a 999...",
            "> Corrigiendo cadenas de caracteres: 'PAGASO' -> 'PAYASO'...",
            "> Forzando renderizado secuencial de barras por software...",
            "> Datos validados correctamente.\n",
            "--------------------------------------------------",
            "SISTEMA DE SEGURIDAD NÚCLEO: ESPERA ESTABLECIDA",
            "--------------------------------------------------\n",
            "> Esperando inyección del bloque de texto final...",
            "> Listo para procesar la cadena de desencriptación personalizada."
        ];

        let lineIndex = 0;
        let charIndex = 0;
        const terminal = document.getElementById('terminal-output');

        function typeTerminal() {
            if (lineIndex < terminalText.length) {
                let currentLine = terminalText[lineIndex];
                if (charIndex < currentLine.length) {
                    terminal.innerHTML += currentLine.charAt(charIndex);
                    charIndex++;
                    setTimeout(typeTerminal, 15); 
                } else {
                    terminal.innerHTML += "\\n";
                    lineIndex++;
                    charIndex = 0;
                    setTimeout(typeTerminal, 150); 
                }
                terminal.scrollTop = terminal.scrollHeight;
            }
        }
    </script>
</body>
</html>
"""

components.html(father_os_interface, height=1000, scrolling=False)
