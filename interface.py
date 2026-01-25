import streamlit as st

class AkylmanUI:
    def apply_styles(self):
        st.markdown("""
        <style>
        /* 1. ФОН И КНОПКА ПАНЕЛИ */
        .stApp {
            background-image: url("https://cdn.dribbble.com/userupload/12560411/file/original-cb85895710c2c26fabc3ee05308be2b0.jpg?resize=1600x1200");
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
        }
        header[data-testid="stHeader"] { background-color: rgba(0,0,0,0) !important; }
        header [data-testid="stHeaderActionElements"] { display: none !important; }
        footer { visibility: hidden; }

        /* 2. БОКОВАЯ ПАНЕЛЬ */
        [data-testid="stSidebar"] { background-color: #f0f2f6 !important; }
        
        /* Заголовки — Чёрные */
        [data-testid="stSidebar"] h3, 
        [data-testid="stSidebar"] p, 
        [data-testid="stSidebar"] label {
            color: #000000 !important;
            font-weight: 700 !important;
        }

        /* 3. ПАРОЛЬ — ТЕКСТ БЕЛЫЙ */
        [data-testid="stSidebar"] div[data-baseweb="input"] {
            background-color: #1e1e1e !important;
            border: none !important;
            border-radius: 10px !important;
        }
        [data-testid="stSidebar"] div[data-baseweb="input"] input {
            color: #ffffff !important;
            -webkit-text-fill-color: #ffffff !important;
        }

        /* 4. ВЫБОР МОДЕЛИ И УРОКА — ТЕКСТ ТОЛЬКО ЧЁРНЫЙ */
        [data-testid="stSidebar"] div[data-baseweb="select"] > div {
            background-color: #ffffff !important;
            border: none !important;
            border-radius: 10px !important;
        }
        /* Принудительно черный цвет для текста в селектах */
        [data-testid="stSidebar"] div[data-baseweb="select"] span,
        [data-testid="stSidebar"] div[data-baseweb="select"] p,
        [data-testid="stSidebar"] div[data-baseweb="select"] div {
            color: #000000 !important;
            -webkit-text-fill-color: #000000 !important;
        }

        /* 5. КРАСНАЯ ЗОНА (ЗАГРУЗКА И ОЧИСТКА) — ТЕКСТ БЕЛЫЙ */
        [data-testid="stFileUploadDropzone"] {
            background-color: #1e1e1e !important;
            border: none !important;
            border-radius: 10px !important;
        }
        [data-testid="stFileUploadDropzone"] p, 
        [data-testid="stFileUploadDropzone"] span,
        [data-testid="stFileUploadDropzone"] div {
            color: #ffffff !important; /* ТУТ БЕЛЫЙ */
            -webkit-text-fill-color: #ffffff !important;
        }
        
        [data-testid="stSidebar"] .stButton button {
            background-color: #1e1e1e !important;
            border: none !important;
            width: 100%;
        }
        /* Текст внутри кнопки очистки */
        [data-testid="stSidebar"] .stButton button p,
        [data-testid="stSidebar"] .stButton button div {
            color: #ffffff !important; /* ТУТ БЕЛЫЙ */
            -webkit-text-fill-color: #ffffff !important;
        }

        /* Чат */
        [data-testid="stChatMessage"] { background-color: rgba(0, 0, 0, 0.75) !important; border-radius: 15px; }
        [data-testid="stChatMessage"] p { color: #ffffff !important; }
        .stChatInputContainer { background-color: rgba(255,255,255,0.95) !important; border-radius: 12px; }
        
        /* Иконки — Чёрные там, где белый фон */
        [data-testid="stSidebar"] svg { fill: #000000 !important; }
        /* Иконки внутри темных кнопок — Белые */
        [data-testid="stSidebar"] .stButton button svg { fill: #ffffff !important; }
        </style>
        """, unsafe_allow_html=True)

    def render_centered_logo(self, level_name):
        st.markdown(f'''
        <div style="text-align: center; padding: 40px; background: rgba(0,0,0,0.6); border-radius: 20px; margin-bottom: 20px;">
            <div style="color: #00ffcc; font-size: 18px; font-weight: bold;">🧠 AKYLMAN AI ({level_name})</div>
            <div style="color: white; font-size: 50px; font-weight: 900; margin: 10px 0;">AKYLMAN</div>
            <div style="color: #ccc; letter-spacing: 4px; font-size: 11px;">PRESIDENTIAL SCHOOL</div>
        </div>
        ''', unsafe_allow_html=True)
