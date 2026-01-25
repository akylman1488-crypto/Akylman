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
        header[data-testid="stHeader"] { background-color: rgba(0,0,0,0) !important; }
        header [data-testid="stHeaderActionElements"] { display: none !important; }
        footer { visibility: hidden; }

        [data-testid="stSidebar"] { background-color: #f0f2f6 !important; }
        
        [data-testid="stSidebar"] h3, 
        [data-testid="stSidebar"] p, 
        [data-testid="stSidebar"] label {
            color: #000000 !important;
            font-weight: 700 !important;
        }

        /* ПАРОЛЬ — ТЕКСТ И ГЛАЗИК БЕЛЫЕ */
        [data-testid="stSidebar"] div[data-baseweb="input"] {
            background-color: #1e1e1e !important;
            border: none !important;
            border-radius: 10px !important;
        }
        [data-testid="stSidebar"] div[data-baseweb="input"] input {
            color: #ffffff !important;
            -webkit-text-fill-color: #ffffff !important;
        }
        [data-testid="stSidebar"] div[data-baseweb="input"] svg {
            fill: #ffffff !important;
        }

        /* ВЫБОР МОДЕЛИ И УРОКА — СТРОГО ЧЁРНЫЙ ТЕКСТ */
        [data-testid="stSidebar"] div[data-baseweb="select"] > div {
            background-color: #ffffff !important;
            border: none !important;
            border-radius: 10px !important;
        }
        /* Убираем все наслоения белого цвета для этих полей */
        [data-testid="stSidebar"] div[data-baseweb="select"] span,
        [data-testid="stSidebar"] div[data-baseweb="select"] p,
        [data-testid="stSidebar"] div[data-baseweb="select"] div {
            color: #000000 !important;
            -webkit-text-fill-color: #000000 !important;
        }
        [data-testid="stSidebar"] div[data-baseweb="select"] svg {
            fill: #000000 !important;
        }

        /* ЗАГРУЗКА ФАЙЛОВ — БЕЛЫЙ ТЕКСТ */
        [data-testid="stFileUploadDropzone"] {
            background-color: #1e1e1e !important;
            border: none !important;
            border-radius: 10px !important;
        }
        [data-testid="stFileUploadDropzone"] p, 
        [data-testid="stFileUploadDropzone"] span,
        [data-testid="stFileUploadDropzone"] div {
            color: #ffffff !important;
            -webkit-text-fill-color: #ffffff !important;
        }
        
        /* КНОПКА ОЧИСТИТЬ ЧАТ — БЕЛЫЙ ТЕКСТ */
        [data-testid="stSidebar"] .stButton button {
            background-color: #1e1e1e !important;
            border: none !important;
            width: 100%;
        }
        [data-testid="stSidebar"] .stButton button p,
        [data-testid="stSidebar"] .stButton button span {
            color: #ffffff !important;
            -webkit-text-fill-color
