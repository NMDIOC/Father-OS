import streamlit as st
import streamlit.components.v1 as components

# 1. Configuración de la aplicación Streamlit
st.set_page_config(
    page_title="FATHER-OS: CORE SYSTEM",
    page_icon="🖥️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Inyección de CSS para ocultar elementos nativos de Streamlit (Header, Footer, Padding)
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

# 3. Interfaz de Alto Impacto (HTML5 Canvas + CSS Grid + JS Engine)
father_os_interface = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <style>
        :root {
            --neon-green: #00ff66;
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
            grid-template-columns: 1fr 2fr;
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
            gap: 20px;
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
            gap: 8px;
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
            width: 0%; 
            transition: width 2.5s cubic-bezier(0.1, 1, 0.1, 1);
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
            <h1>[ STREAMLIT_CORE_v4.0: ACCESO INTEGRAL ]</h1>
            <p>ESTADO_DEL_NÚCLEO: <span class="blink" style="color: var(--neon-green);">DYNAMIC_OK</span> | MÓDULO: PAPÁ_MAIN</p>
        </header>

        <!-- PANEL DE ATRIBUTOS -->
        <div class="panel">
            <h2 class="stats-title">> COMPILACIÓN_DE_MÉTRICAS</h2>
            
            <div class="stat-row">
                <label>SABIDURÍA / LÓGICA APLICADA:</label>
                <div class="bar-container"><div class="bar-fill" data-width="98%"></div></div>
            </div>
            <div class="stat-row">
                <label>RESOLUCIÓN DE PROBLEMAS FAMILIARES:</label>
                <div class="bar-container"><div class="bar-fill" data-width="100%"></div></div>
            </div>
            <div class="stat-row">
                <label>INGENIERÍA GASTRONÓMICA / ASADOS:</label>
                <div class="bar-container"><div class="bar-fill" data-width="95%"></div></div>
            </div>
            <div class="stat-row">
                <label>SOPORTE Y OPTIMIZACIÓN CONTINUA:</label>
                <div class="bar-container"><div class="bar-fill" data-width="97%"></div></div>
            </div>
        </div>

        <!-- TERMINAL DE COMANDOS CRÍPTICOS -->
        <div class="terminal" id="terminal-output"></div>
    </div>

    <script>
        // Matrix Render Engine
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

        // Activación de barras de carga
        window.onload = () => {
            setTimeout(() => {
                document.querySelectorAll('.bar-fill').forEach(bar => {
                    bar.style.width = bar.getAttribute('data-width');
                });
            }, 300);
            typeTerminal();
        };

        // Secuencia de desencriptación en terminal
        const terminalText = [
            "> Inicializando entorno de ejecución Python 3.11...",
            "> Cargando dependencias: Streamlit (v1.35), NumPy, CoreFamiliar...",
            "> Estableciendo conexión segura con el nodo raíz: PAPÁ...",
            "> [OK] Conexión establecida bajo protocolo criptográfico.",
            "> Extrayendo bloque de datos confidenciales de la memoria flash...",
            "> Desencriptando transmisión... Por favor, espere.\n",
            "--------------------------------------------------",
            "  SISTEMA CENTRAL: ¡FELIZ DÍA DEL PADRE!",
            "--------------------------------------------------\n",
            "Papá:",
            "Este entorno fue programado y optimizado específicamente",
            "para reconocer tu impacto en mi código de vida.",
            "Gracias por ser la guía estructural, el soporte técnico",
            "en los momentos difíciles y la lógica detrás de mis pasos.",
            "Tu arquitectura como padre no tiene bugs.",
            "\n> Proceso finalizado. El sistema continuará ejecutándose en bucle indefinido."
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
                    setTimeout(typeTerminal, 20); 
                } else {
                    terminal.innerHTML += "\\n";
                    lineIndex++;
                    charIndex = 0;
                    setTimeout(typeTerminal, 180); 
                }
                terminal.scrollTop = terminal.scrollHeight;
            }
        }
    </script>
</body>
</html>
"""

# 4. Renderizado del componente a pantalla completa dentro del Viewport
components.html(father_os_interface, height=1000, scrolling=False)
