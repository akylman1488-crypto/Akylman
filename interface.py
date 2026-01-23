import streamlit as st

class AkylmanUI:
    def apply_styles(self):
        st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
        
        .stApp { background-color: #020202; }
        
        .level-card {
            padding: 10px;
            border-radius: 10px;
            border-left: 5px solid #00ffcc;
            background: #111;
            margin-bottom: 10px;
        }

        h1 {
            font-family: 'Orbitron', sans-serif;
            color: #00ffcc;
            text-shadow: 0 0 20px #00ffcc;
        }

        .stButton>button {
            width: 100%;
            background: linear-gradient(90deg, #00ffcc, #0088ff);
            color: black;
            border: none;
            font-family: 'Orbitron';
        }

        [data-testid="stSidebar"] {
            background-color: #0a0a0a !important;
            border-right: 1px solid #333;
        }
        
        /* Здесь будет еще 400 строк CSS для кнопок, чата и анимаций */
        </style>
        """, unsafe_allow_html=True)
