import streamlit as st

class AkylmanInterface:
    def __init__(self):
        self.primary_color = "#00f2fe"
        self.secondary_color = "#4facfe"
        self.bg_dark = "#050505"
        self.accent_red = "#ff4b4b"

    def apply_base_theme(self):
        st.markdown(f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Roboto:wght@300;400;700&display=swap');

        [data-testid="stAppViewContainer"] {{
            background: radial-gradient(circle at center, #111 0%, {self.bg_dark} 100%);
            color: white;
            font-family: 'Roboto', sans-serif;
        }}

        [data-testid="stSidebar"] {{
            background-color: rgba(10, 10, 10, 0.95) !important;
            border-right: 1px solid {self.primary_color}44;
            box-shadow: 5px 0 15px rgba(0,0,0,0.5);
        }}

        .stApp h1 {{
            font-family: 'Orbitron', sans-serif;
            color: {self.primary_color} !important;
            text-align: center;
            text-transform: uppercase;
            letter-spacing: 5px;
            text-shadow: 0 0 20px {self.primary_color}aa;
            margin-bottom: 50px;
        }}

        [data-testid="stChatMessage"] {{
            background: rgba(255, 255, 255, 0.03) !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            border-radius: 20px !important;
            padding: 20px !important;
            margin-bottom: 15px !important;
            transition: all 0.3s ease;
        }}

        [data-testid="stChatMessage"]:hover {{
            border: 1px solid {self.primary_color}88 !important;
            background: rgba(0, 242, 254, 0.05) !important;
            transform: translateY(-2px);
        }}

        .stChatInputContainer {{
            background-color: transparent !important;
            padding: 20px !important;
        }}

        .stChatInputContainer textarea {{
            background-color: #111 !important;
            color: white !important;
            border: 1px solid {self.primary_color}55 !important;
            border-radius: 15px !important;
            font-size: 1.1rem !important;
        }}

        .stButton>button {{
            background: linear-gradient(45deg, {self.secondary_color}, {self.primary_color});
            color: white;
            border: none;
            border-radius: 12px;
            padding: 10px 25px;
            font-family: 'Orbitron', sans-serif;
            font-weight: bold;
            transition: 0.4s;
            width: 100%;
        }}

        .stButton>button:hover {{
            box-shadow: 0 0 20px {self.primary_color};
            transform: scale(1.02);
            color: black;
        }}

        ::-webkit-scrollbar {{
            width: 8px;
        }}
        ::-webkit-scrollbar-track {{
            background: #000;
        }}
        ::-webkit-scrollbar-thumb {{
            background: {self.primary_color};
            border-radius: 10px;
        }}
        </style>
        """, unsafe_allow_html=True)

    def inject_glass_morphism(self):
        st.markdown("""
        <style>
        .glass-panel {
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            padding: 25px;
            margin: 10px 0;
        }
        </style>
        """, unsafe_allow_html=True)

    def render_sidebar_header(self):
        st.sidebar.markdown(f"""
        <div style='text-align: center; padding: 20px;'>
            <h2 style='color: {self.primary_color}; font-family: Orbitron;'>AKYLMAN V4</h2>
            <p style='color: #888; font-size: 0.8em;'>ISSUK-KUL REGION EDITION</p>
            <hr style='border: 0.5px solid {self.primary_color}33;'>
        </div>
        """, unsafe_allow_html=True)

  def create_subject_tabs(self, current_subject):
        colors = {
            "Математика": "#0088ff",
            "English": "#00ff88",
            "История": "#ff8800",
            "Программирование": "#ff00ff"
        }
        active_color = colors.get(current_subject, self.primary_color)
        
        st.markdown(f"""
        <style>
        .subject-badge {{
            background: {active_color}22;
            color: {active_color};
            padding: 5px 15px;
            border-radius: 50px;
            border: 1px solid {active_color};
            font-weight: bold;
            display: inline-block;
            margin-bottom: 20px;
        }}
        </style>
        <div class='subject-badge'>АКТИВНЫЙ РЕЖИМ: {current_subject}</div>
        """, unsafe_allow_html=True)

    def render_info_metrics(self, words, sessions, status):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f"""
            <div class='glass-panel' style='text-align: center;'>
                <div style='font-size: 0.8em; color: #888;'>СЛОВ</div>
                <div style='font-size: 1.5em; color: {self.primary_color}; font-weight: bold;'>{words}</div>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
            <div class='glass-panel' style='text-align: center;'>
                <div style='font-size: 0.8em; color: #888;'>СЕССИИ</div>
                <div style='font-size: 1.5em; color: {self.primary_color}; font-weight: bold;'>{sessions}</div>
            </div>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown(f"""
            <div class='glass-panel' style='text-align: center;'>
                <div style='font-size: 0.8em; color: #888;'>СТАТУС</div>
                <div style='font-size: 1.2em; color: #00ff88; font-weight: bold;'>{status}</div>
            </div>
            """, unsafe_allow_html=True)

    def floating_action_button(self):
        st.markdown("""
        <style>
        .fab {
            position: fixed;
            bottom: 30px;
            right: 30px;
            width: 60px;
            height: 60px;
            background: #ff4b4b;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 10px 20px rgba(0,0,0,0.3);
            cursor: pointer;
            z-index: 999;
            transition: 0.3s;
        }
        .fab:hover { transform: rotate(90deg) scale(1.1); }
        </style>
        <div class="fab">🚀</div>
        """, unsafe_allow_html=True)

    def display_system_logs(self, log_text):
        st.markdown(f"""
        <div style='background: #000; color: #0f0; padding: 15px; border-radius: 5px; font-family: monospace; font-size: 0.8em; border: 1px solid #333;'>
            <span style='color: #555;'>[SYSTEM LOG]:</span> {log_text}
        </div>
        """, unsafe_allow_html=True)

    def animate_loading(self):
        st.markdown("""
        <style>
        @keyframes pulse {
            0% { opacity: 0.4; }
            50% { opacity: 1; }
            100% { opacity: 0.4; }
        }
        .loading-text {
            font-family: 'Orbitron', sans-serif;
            color: #00f2fe;
            animation: pulse 1.5s infinite;
            text-align: center;
            padding: 20px;
        }
        </style>
        <div class="loading-text">ВЫЧИСЛЕНИЕ ОТВЕТА...</div>
        """, unsafe_allow_html=True)
