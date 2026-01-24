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
            }}

            [data-testid="stChatMessage"]:hover {{
                border-color: var(--primary);
                box-shadow: 0 0 15px rgba(0, 255, 204, 0.1);
                transform: translateX(5px);
            }}

            [data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] p {{
                font-family: 'Rajdhani', sans-serif;
                font-weight: 500;
                line-height: 1.6;
            }}

            /* INPUT FIELD STYLING */
            .stChatInputContainer textarea {{
                background-color: #000 !important;
                color: var(--primary) !important;
                border: 1px solid rgba(0, 255, 204, 0.3) !important;
                border-radius: 10px !important;
                font-family: 'Rajdhani', monospace !important;
                font-size: 1.1rem !important;
            }}
            
            .stChatInputContainer textarea:focus {{
                border-color: var(--primary) !important;
                box-shadow: 0 0 20px rgba(0, 255, 204, 0.2) !important;
            }}

            /* BUTTONS STYLING */
            .stButton > button {{
                background: linear-gradient(135deg, rgba(0, 255, 204, 0.1) 0%, rgba(0, 153, 255, 0.1) 100%);
                border: 1px solid var(--primary);
                color: var(--primary);
                font-family: 'Orbitron', sans-serif;
                font-weight: 700;
                border-radius: 8px;
                transition: 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
                text-transform: uppercase;
            }}

            .stButton > button:hover {{
                background: var(--primary);
                color: #000;
                box-shadow: 0 0 30px var(--primary);
                transform: scale(1.05);
            }}

            /* UPLOAD STYLING */
            [data-testid="stFileUploader"] section {{
                background: rgba(0,0,0,0.5);
                border: 1px dashed var(--secondary);
            }}

            /* CUSTOM SCROLLBAR */
            ::-webkit-scrollbar {{
                width: 10px;
                background: #000;
            }}
            ::-webkit-scrollbar-thumb {{
                background: linear-gradient(to bottom, var(--primary), var(--secondary));
                border-radius: 5px;
            }}

            /* ANIMATIONS */
            @keyframes pulse-glow {{
                0% {{ box-shadow: 0 0 5px var(--primary); }}
                50% {{ box-shadow: 0 0 20px var(--primary), 0 0 10px var(--secondary); }}
                100% {{ box-shadow: 0 0 5px var(--primary); }}
            }}
            
            .status-online {{
                display: inline-block;
                width: 10px;
                height: 10px;
                background-color: #0f0;
                border-radius: 50%;
                box-shadow: 0 0 10px #0f0;
                margin-right: 10px;
            }}
        </style>
        """

    def apply_styles(self):
        st.markdown(self.get_base_css(), unsafe_allow_html=True)

    def render_header(self, title, subtitle):
        st.markdown(f"""
        <div style="text-align: center; margin-bottom: 40px; border-bottom: 1px solid #333; padding-bottom: 20px;">
            <h1 style="font-size: 3.5rem; margin: 0;">{title}</h1>
            <p style="color: #0099ff; font-family: 'Orbitron'; letter-spacing: 5px; margin-top: -10px;">{subtitle}</p>
            <div style="margin-top: 10px;">
                <span class="status-online"></span> <span style="font-size: 0.8rem; color: #666;">SYSTEM ONLINE</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    def render_level_selector_style(self):
        # Custom CSS for the level selection radio buttons to look like cards
        st.markdown("""
        <style>
        div[role="radiogroup"] > label > div:first-of-type {
            display: none;
        }
        div[role="radiogroup"] {
            flex-direction: column;
            gap: 10px;
        }
        div[role="radiogroup"] label {
            background: rgba(255,255,255,0.05);
            padding: 15px;
            border-radius: 10px;
            border: 1px solid #333;
            cursor: pointer;
            transition: 0.3s;
            text-align: center;
            font-family: 'Orbitron';
        }
        div[role="radiogroup"] label:hover {
            border-color: #00ffcc;
            background: rgba(0, 255, 204, 0.1);
        }
        div[role="radiogroup"] label[data-checked="true"] {
            background: linear-gradient(90deg, #00ffcc 0%, #0099ff 100%);
            color: #000 !important;
            font-weight: bold;
            border: none;
            box-shadow: 0 0 15px #00ffcc;
        }
        div[role="radiogroup"] label[data-checked="true"] p {
            color: #000 !important;
        }
        </style>
        """, unsafe_allow_html=True)

    def render_message_loader(self):
        st.markdown("""
        <div style="display: flex; align-items: center; gap: 10px; padding: 20px; color: #00ffcc;">
            <div style="width: 20px; height: 20px; border: 2px solid #00ffcc; border-top: 2px solid transparent; border-radius: 50%; animation: spin 1s linear infinite;"></div>
            <span style="font-family: 'Orbitron';">NEURAL PROCESSING...</span>
        </div>
        <style>
            @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
        </style>
        """, unsafe_allow_html=True)
