import streamlit as st
import streamlit.components.v1 as components
import base64

class AkylmanEffects:
    def __init__(self):
        pass

    def trigger_audio_notification(self, sound_type="success"):
        sounds = {
            "success": "https://www.soundjay.com/buttons/sounds/button-16.mp3",
            "error": "https://www.soundjay.com/buttons/sounds/button-10.mp3",
            "message": "https://www.soundjay.com/buttons/sounds/button-3.mp3"
        }
        url = sounds.get(sound_type)
        st.components.v1.html(f"""
            <audio autoplay>
                <source src="{url}" type="audio/mpeg">
            </audio>
        """, height=0)

    def inject_confetti(self):
        components.html("""
            <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
            <script>
                confetti({
                    particleCount: 150,
                    spread: 70,
                    origin: { y: 0.6 },
                    colors: ['#00f2fe', '#4facfe', '#ffffff']
                });
            </script>
        """, height=0)

    def text_to_speech(self, text):
        clean_text = text.replace('"', "'").replace('\n', ' ')
        components.html(f"""
            <script>
                var msg = new SpeechSynthesisUtterance("{clean_text}");
                msg.lang = 'ru-RU';
                msg.rate = 1.0;
                window.speechSynthesis.speak(msg);
            </script>
        """, height=0)

    def terminal_typing_effect(self, element_id, text, speed=50):
        clean_text = text.replace('"', "'").replace('\n', ' ')
        components.html(f"""
            <div id="{element_id}" style="font-family: monospace; color: #00ffcc;"></div>
            <script>
                var i = 0;
                var txt = "{clean_text}";
                function typeWriter() {{
                    if (i < txt.length) {{
                        document.getElementById("{element_id}").innerHTML += txt.charAt(i);
                        i++;
                        setTimeout(typeWriter, {speed});
                    }}
                }}
                typeWriter();
            </script>
        """, height=400)

    def inject_custom_cursor(self):
        st.markdown("""
            <style>
                * { cursor: url('https://cur.cursors-4u.net/cursors/cur-2/cur116.cur'), auto !important; }
            </style>
        """, unsafe_allow_html=True)

    def dynamic_title_pulse(self):
        components.html("""
            <script>
                var titles = ["AKYLMAN V4", "SYSTEM READY", "HELLO ISANUR"];
                var i = 0;
                setInterval(function() {
                    document.title = titles[i % titles.length];
                    i++;
                }, 2000);
            </script>
        """, height=0)

    def scroll_to_bottom(self):
        components.html("""
            <script>
                var scrollTarget = window.parent.document.querySelector('.main');
                scrollTarget.scrollTop = scrollTarget.scrollHeight;
            </script>
        """, height=0)

    def alert_notification(self, message):
        components.html(f"""
            <script>
                alert("{message}");
            </script>
        """, height=0)

    def particles_background(self):
        components.html("""
            <div id="particles-js" style="position: fixed; width: 100vw; height: 100vh; top: 0; left: 0; z-index: -1;"></div>
            <script src="https://cdn.jsdelivr.net/npm/particles.js@2.0.0/particles.min.js"></script>
            <script>
                particlesJS('particles-js', {
                    "particles": {
                        "number": { "value": 80 },
                        "color": { "value": "#00f2fe" },
                        "shape": { "type": "circle" },
                        "opacity": { "value": 0.5 },
                        "size": { "value": 3 },
                        "line_linked": { "enable": true, "distance": 150, "color": "#00f2fe", "opacity": 0.4, "width": 1 }
                    }
                });
            </script>
        """, height=0)
