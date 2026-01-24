import streamlit as st
import base64

class AkylmanUI:
    def __init__(self):
        self.primary_color = "#00ffcc"
        self.secondary_color = "#0099ff"
        self.bg_color = "#050505"
        self.sidebar_color = "#0a0a0a"

    def get_base_css(self):
        return f"""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700;900&family=Rajdhani:wght@300;500;700&display=swap');

            :root {{
                --primary: {self.primary_color};
                --secondary: {self.secondary_color};
                --bg: {self.bg_color};
                --sidebar: {self.sidebar_color};
            }}

            .stApp {{
                background-color: var(--bg);
                font-family: 'Rajdhani', sans-serif;
            }}

            [data-testid="stSidebar"] {{
                background-color: var(--sidebar);
                border-right: 1px solid rgba(0, 255, 204, 0.1);
                box-shadow: 10px 0 30px rgba(0,0,0,0.5);
            }}

            h1, h2, h3 {{
                font-family: 'Orbitron', sans-serif !important;
                color: var(--primary) !important;
                text-transform: uppercase;
                letter-spacing: 2px;
                text-shadow: 0 0 15px rgba(0, 255, 204, 0.4);
            }}

            p, div, label, span {{
                color: #e0e0e0;
                font-size: 1.05rem;
            }}

            /* CHAT MESSAGES STYLING */
            [data-testid="stChatMessage"] {{
                background: rgba(255, 255, 255, 0.03);
                border: 1px solid rgba(255, 255, 255, 0.05);
                border-radius: 15px;
                padding: 15px;
                margin-bottom: 15px;
                transition: all 0.3s ease;
                backdrop-filter: blur(10px);
