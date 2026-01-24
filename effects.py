import streamlit as st
import streamlit.components.v1 as components

class AkylmanFX:
    def __init__(self):
        pass

    def inject_particles(self):
        components.html("""
        <div id="particles-js" style="position: fixed; width: 100%; height: 100%; top: 0; left: 0; z-index: -1;"></div>
        <script src="https://cdn.jsdelivr.net/npm/particles.js@2.0.0/particles.min.js"></script>
        <script>
            particlesJS('particles-js', {
                "particles": {
                    "number": { "value": 50 },
                    "color": { "value": "#00ffcc" },
                    "line_linked": { "enable": true, "color": "#00ffcc", "opacity": 0.2 },
                    "move": { "enable": true, "speed": 1 }
                }
            });
        </script>
        """, height=0)

    def trigger_confetti(self):
        components.html("""
        <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
        <script>
            confetti({ particleCount: 150, spread: 70, origin: { y: 0.6 }, colors: ['#00ffcc', '#ffffff'] });
        </script>
        """, height=0)

    def play_audio(self):
        st.markdown("""<audio autoplay><source src="https://www.soundjay.com/buttons/sounds/button-3.mp3" type="audio/mpeg"></audio>""", unsafe_allow_html=True)
