import streamlit as st

class AkylmanUI:
    def apply_styles(self):
        st.markdown("""
        <style>
        /* 1. ОБЩИЙ ФОН */
        .stApp {
            background-image: url("https://cdn.dribbble.com/userupload/12560411/file/original-cb85895710c2c26fabc3ee05308be2b0.jpg?resize=1600x1200");
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
        }

        /* 2. КНОПКА ПАНЕЛИ (Стрелочка >>) */
        /* Делаем хедер прозрачным, чтобы кнопка была видна на фоне */
        header[data-testid="stHeader"] {
            background-color: rgba(0,0,0,0) !important;
        }
        header [data-testid="stHeaderActionElements"] {
            display: none !important;
        }
        footer { visibility: hidden; }

        /* 3. БОКОВАЯ ПАНЕЛЬ (Светло-серая) */
        [data-testid="stSidebar"] {
            background-color: #f0f2f6 !important;
        }
        
        /* ВЕСЬ ТЕКСТ В ПАНЕЛИ — ЧЁРНЫЙ */
        [data-testid="stSidebar"] * {
            color: #000000 !important;
        }

        /* 4. ПОЛЕ ПАРОЛЯ (Чёрный фон, Белый текст) */
        [data-testid="stSidebar"] div[data-baseweb="input"] {
            background-color: #1e1e1e !important;
            border: none !important;
            border-radius: 10px !important;
        }
        /* Внутри пароля текст должен остаться белым для контраста */
        [data-testid="stSidebar"] div[data-baseweb="input"] input {
            color: #ffffff !important;
            -webkit-text-fill-color: #ffffff !important;
        }

        /* 5. ВЫБОР МОДЕЛИ И УРОКА (Белый фон, Чёрный текст) */
        [data-testid="stSidebar"] div[data-baseweb="select"] > div {
            background-color: #ffffff !important;
            border: none !important;
            border-radius: 10px !important;
        }
        
        /* Текст внутри выпадающих списков */
        [data-testid="stSidebar"] [data-testid="stWidgetLabel"] p,
        [data-testid="stSidebar"] div[data-baseweb="select"] span,
        [data-testid="stSidebar"] div[data-baseweb="select"] p {
            color: #000000 !important;
            font-weight: 700 !important;
        }
        
        /* Иконки и стрелочки — Чёрные */
        [data-testid="stSidebar"] svg {
            fill: #000000 !important;
        }

        /* 6. ЧАТ (Белый текст на тёмном фоне) */
        [data-testid="stChatMessage"] {
            background-color: rgba(0, 0, 0, 0.75) !important;
            border-radius: 15px;
        }
        [data-testid="stChatMessage"] p {
            color: #ffffff !important;
        }

        /* Поле ввода внизу */
        .stChatInputContainer {
            background-color: rgba(255,255,255,0.95) !important;
            border-radius: 12px;
        }
        .stChatInputContainer textarea {
            color: #000000 !important;
        }
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
