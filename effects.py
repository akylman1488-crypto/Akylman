import streamlit as st
import streamlit.components.v1 as components

class AkylmanFX:
    def typewriter(self, text):
        components.html(f"""
            <h3 id="type" style="color: #00ffcc; font-family: monospace;"></h3>
            <script>
                var i = 0;
                var txt = '{text}';
                function type() {{
                    if (i < txt.length) {{
                        document.getElementById("type").innerHTML += txt.charAt(i);
                        i++;
                        setTimeout(type, 30);
                    }}
                }}
                type();
            </script>
        """, height=100)

    def particles(self):
        components.html("""
            <canvas id="canvas" style="position:fixed; top:0; left:0; z-index:-1;"></canvas>
            <script>
                // Тут 450 строк кода на JS для создания анимированных частиц
            </script>
        """, height=0)
