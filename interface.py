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

        /* 2. КНОПКА ПАНЕЛИ (СДЕЛАЛ ВИДИМОЙ) */
        header[data-testid="stHeader"] {
            background-color: rgba(0,0,0,0) !important;
        }
        
        /* Скрываем только лишние иконки справа */
        header [data-testid="stHeaderActionElements"] {
            display: none !important;
        }

        footer { visibility: hidden; }

        /* 3. БОКОВАЯ ПАНЕЛЬ */
        [data-testid="stSidebar"] {
            background-color: #f0f2f6 !important;
        }
        
        [data-testid="stSidebar"] h3, 
        [data-testid="stSidebar"] p, 
        [data-testid="stSidebar"] label {
            color: #ffffff !important;
            font-weight: 700 !important;
        }

        /* 4. КРАСНАЯ ОБЛАСТЬ (ВВОД ПАРОЛЯ): ФОН ТЕМНЫЙ, ТЕКСТ БЕЛЫЙ */
        [data-testid="stSidebar"] div[data-baseweb="input"] {
            background-color: #1e1e1e !important; /* Темный фон как на фото */
            border: none !important;
            border-radius: 10px !important;
        }
        [data-testid="stSidebar"] input {
            color: #ffffff !important; /* ТЕКСТ БЕЛЫЙ */
        }

        /* 5. СИНЯЯ ОБЛАСТЬ (ВЫБОР УРОКА): ФОН СВЕТЛЫЙ, ТЕКСТ ЧЕРНЫЙ */
        [data-testid="stSidebar"] div[data-baseweb="select"] > div {
            background-color: #ffffff !important; /* Светлый фон */
            border: none !important;
            border-radius: 10px !important;
        }
        [data-testid="stSidebar"] div[data-baseweb="select"] span {
            color: #000000 !important; /* ТЕКСТ ЧЕРНЫЙ */
        }
        
        /* Иконка глаза и стрелочки */
        [data-testid="stSidebar"] svg {
            fill: #888 !important;
        }

        /* 6. ЧАТ */
        [data-testid="stChatMessage"] {
            background-color: rgba(0, 0, 0, 0.75) !important;
            border-radius: 15px;
        }
        [data-testid="stChatMessage"] p {
            color: #ffffff !important;
        }

        .stChatInputContainer {
            background-color: rgba(255,255,255,0.95) !important;
            border-radius: 12px;
        }
        </style>
        """, unsafe_allow_html=True)

    def render_centered_logo(self, level_name):
        st.markdown(f'''
        <div style="text-align: center; padding: 40px; background: rgba(0,0,0,0.6); border-radius: 20px; margin-bottom: 20px;">
            <div style="color: #00ffcc; font-size: 18px; font-weight: bold;">🧠 AKYLMAN AI ({level_name})</div>
            <div style="color: blakc; font-size: 50px; font-weight: 900; margin: 10px 0;">AKYLMAN</div>
            <div style="color: #ccc; letter-spacing: 4px; font-size: 11px;">PRESIDENTIAL SCHOOL</div>
        </div>
        ''', unsafe_allow_html=True)
