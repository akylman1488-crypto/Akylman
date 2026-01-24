import streamlit as st
import streamlit.components.v1 as components
import json

class AkylmanFX:
    def __init__(self):
        self.success_color = "#00ffcc"
        self.error_color = "#ff4b4b"
        self.info_color = "#0099ff"

    def inject_particles(self):
        components.html("""
        <div id="particles-container" style="position: fixed; width: 100vw; height: 100vh; top: 0; left: 0; z-index: -1; pointer-events: none;"></div>
        <script src="https://cdn.jsdelivr.net/npm/particles.js@2.0.0/particles.min.js"></script>
        <script>
            particlesJS('particles-container', {
                "particles": {
                    "number": { "value": 80, "density": { "enable": true, "value_area": 800 } },
                    "color": { "value": "#00ffcc" },
                    "shape": { "type": "circle" },
                    "opacity": { "value": 0.2, "random": true },
                    "size": { "value": 3, "random": true },
                    "line_linked": { "enable": true, "distance": 150, "color": "#00ffcc", "opacity": 0.1, "width": 1 },
                    "move": { "enable": true, "speed": 2, "direction": "none", "random": false, "straight": false, "out_mode": "out", "bounce": false }
                },
                "interactivity": {
                    "detect_on": "canvas",
                    "events": { "onhover": { "enable": true, "mode": "grab" }, "onclick": { "enable": true, "mode": "push" } },
                    "modes": { "grab": { "distance": 140, "line_linked": { "opacity": 1 } } }
                },
                "retina_detect": true
            });
        </script>
        """, height=0)

    def play_audio(self, event_type="message"):
        sounds = {
            "message": "https://www.soundjay.com/buttons/sounds/button-3.mp3",
            "success": "https://www.soundjay.com/buttons/sounds/button-16.mp3",
            "error": "https://www.soundjay.com/buttons/sounds/button-10.mp3",
            "typing": "https://www.soundjay.com/communication/sounds/typewriter-key-1.mp3"
        }
        url = sounds.get(event_type)
        components.html(f"""
            <audio autoplay>
                <source src="{url}" type="audio/mpeg">
            </audio>
        """, height=0)

    def trigger_confetti(self):
        components.html("""
        <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
        <script>
            var count = 200;
            var defaults = { origin: { y: 0.7 }, colors: ['#00ffcc', '#0099ff', '#ffffff'] };
            function fire(particleRatio, opts) {
                confetti(Object.assign({}, defaults, opts, {
                    particleCount: Math.floor(count * particleRatio)
                }));
            }
            fire(0.25, { spread: 26, startVelocity: 55 });
            fire(0.2, { spread: 60 });
            fire(0.35, { spread: 100, decay: 0.91, scalar: 0.8 });
            fire(0.1, { spread: 120, startVelocity: 25, decay: 0.92, scalar: 1.2 });
            fire(0.1, { spread: 120, startVelocity: 45 });
        </script>
        """, height=0)

    def terminal_text(self, text, element_id="term"):
        safe_text = json.dumps(text)
        components.html(f"""
        <div id="{element_id}" style="font-family: 'Courier New', monospace; color: #00ffcc; padding: 10px; border-left: 2px solid #00ffcc;"></div>
        <script>
            let i = 0;
            const txt = {safe_text};
            const speed = 20;
            function typeWriter() {{
                if (i < txt.length) {{
                    document.getElementById("{element_id}").innerHTML += txt.charAt(i);
                    i++;
                    setTimeout(typeWriter, speed);
                }}
            }}
            typeWriter();
        </script>
        """, height=150)

    def scroll_to_bottom(self):
        components.html("""
        <script>
            window.parent.document.querySelector('.main').scrollTo({
                top: window.parent.document.querySelector('.main').scrollHeight,
                behavior: 'smooth'
            });
        </script>
        """, height=0)

    def inject_glow_cursor(self):
        st.markdown("""
        <style>
            * { cursor: crosshair !important; }
            .stApp::before {
                content: '';
                position: fixed;
                top: 0; left: 0;
                width: 100%; height: 100%;
                background: radial-gradient(circle at var(--x, 50%) var(--y, 50%), rgba(0,255,204,0.05) 0%, transparent 50%);
                pointer-events: none;
                z-index: 9999;
            }
        </style>
        <script>
            const app = window.parent.document.querySelector('.stApp');
            window.parent.document.addEventListener('mousemove', e => {
                app.style.setProperty('--x', e.clientX + 'px');
                app.style.setProperty('--y', e.clientY + 'px');
            });
        </script>
        """, unsafe_allow_html=True)

    def show_toast(self, message, type="info"):
        colors = {"info": "#0099ff", "success": "#00ffcc", "error": "#ff4b4b"}
        color = colors.get(type, "#fff")
        components.html(f"""
        <div id="toast" style="position: fixed; top: 20px; right: 20px; background: {color}; color: black; padding: 10px 20px; border-radius: 5px; font-family: sans-serif; font-weight: bold; z-index: 10000; animation: slideIn 0.5s ease-out;">
            {message}
        </div>
        <style>
            @keyframes slideIn { from { transform: translateX(100%); } to { transform: translateX(0); } }
        </style>
        <script>
            setTimeout(() => {{ document.getElementById('toast').style.display = 'none'; }}, 3000);
        </script>
        """, height=0)
