import streamlit as st

class AkylmanUI:
    def apply_styles(self):
        st.markdown("""
        <style>
        .stApp {
            background-image: url("https://cdn.dribbble.com/userupload/12560411/file/original-cb85895710c2c26fabc3ee05308be2b0.jpg?resize=1600x1200");
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
        }

        footer {
            visibility: hidden;
            height: 0px;
        }
        
        header {
            visibility: hidden;
        }

        .block-container {
            padding-bottom: 0px;
        }

        [data-testid="stSidebar"] {
            background-color: #f0f2f6 !important;
            border-right: 1px solid #ddd;
        }
        
        [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3, 
        [data-testid="stSidebar"] p, [data-testid="stSidebar"] label {
            color: #000000 !important;
            font-weight: 700 !important;
        }

        [data-testid="stSidebar"] div[data-baseweb="input"],
        [data-testid="stSidebar"] div[data-baseweb="select"] > div {
            background-color: #ffffff !important;
            border: none !important;
            border-radius: 10px !important;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05) !important;
        }

        [data-testid="stSidebar"] input, 
        [data-testid="stSidebar"] div[data-baseweb="select"] span {
            color: #000000 !important; 
            font-weight: 500 !important;
        }
        
        [data-testid="stSidebar"] svg {
            fill: #000000 !important;
        }

        [data-testid="stChatMessage"] {
            background-color: rgba(0, 0, 0, 0.75) !important;
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 15px;
        }
        [data-testid="stChatMessage"] p, 
        [data-testid="stChatMessage"] div {
            color: #ffffff !important;
        }

        .stButton>button {
            background-color: #ffffff !important;
            color: #000000 !important;
            border: none !important;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }

        .stChatInputContainer {
            background-color: rgba(255,255,255,0.95) !important;
            border-radius: 12px;
            padding-bottom: 10px;
            margin-bottom: 10px;
        }
        </style>
        """, unsafe_allow_html=True)

    def render_centered_logo(self, level_name):
        st.markdown(f'''
        <div style="text-align: center; padding: 40px; background: rgba(0,0,0,0.6); border-radius: 20px; margin-bottom: 20px; border: 1px solid rgba(255,255,255,0.1);">
            <div style="color: #00ffcc; font-size: 18px; font-weight: bold;">🧠 AKYLMAN AI ({level_name})</div>
            <div style="color: white; font-size: 50px; font-weight: 900; margin: 10px 0;">AKYLMAN</div>
            <div style="color: #ccc; letter-spacing: 4px; font-size: 11px;">PRESIDENTIAL SCHOOL</div>
        </div>
        ''', unsafe_allow_html=True)
