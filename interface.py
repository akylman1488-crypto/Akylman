import streamlit as st

class AkylmanUI:
    def apply_styles(self):
        st.markdown("""
        <style>
        /* 1. ОБЩИЙ БЕЛЫЙ ФОН САЙТА */
        .stApp {
            background-color: #ffffff !important;
        }

        /* 2. БОКОВАЯ ПАНЕЛЬ: Светлая с черным текстом */
        [data-testid="stSidebar"] {
            background-color: #f1f3f6 !important;
            border-right: 1px solid #ddd;
        }

        /* Текст в панели — ПРИНУДИТЕЛЬНО ЧЕРНЫЙ */
        [data-testid="stSidebar"] p, 
        [data-testid="stSidebar"] span, 
        [data-testid="stSidebar"] label, 
        [data-testid="stSidebar"] h3 {
            color: #000000 !important;
            font-weight: 700 !important;
        }

        /* Поля выбора и ввода */
        [data-testid="stSidebar"] select, 
        [data-testid="stSidebar"] input,
        [data-testid="stSidebar"] div[data-baseweb="select"] {
            background-color: #ffffff !important;
            color: #000000 !important;
            border: 1px solid #000000 !important;
            border-radius: 10px !important;
        }

        /* Зеленая плашка статуса */
        .status-box {
            background-color: #d4edda;
            color: #155724 !important;
            padding: 10px;
            border-radius: 10px;
            text-align: center;
            border: 1px solid #c3e6cb;
            margin-bottom: 10px;
        }

        /* 3. КРУТОЙ ФОН ДЛЯ СООБЩЕНИЙ (твоя ссылка) */
        [data-testid="stChatMessage"] {
            background-image: url("https://cdn.dribbble.com/userupload/12560411/file/original-cb85895710c2c26fabc3ee05308be2b0.jpg?resize=1600x1200") !important;
            background-size: cover !important;
            background-position: center !important;
            border-radius: 20px !important;
            border: 1px solid rgba(255,255,255,0.2) !important;
            margin-bottom: 15px !important;
            padding: 20px !important;
            box-shadow: 0 4px 15px rgba(0,0,0,0.3) !important;
        }

        /* Текст внутри сообщений — белый на синем фоне */
        [data-testid="stChatMessage"] p, 
        [data-testid="stChatMessage"] li {
            color: #ffffff !important;
            font-size: 17px !important;
            text-shadow: 1px 1px 2px black;
        }

        /* 4. ПОЛЕ ВВОДА ВНИЗУ */
        .stChatInputContainer {
            border: 2px solid #000000 !important;
            background-color: #ffffff !important;
            border-radius: 15px !important;
        }
        </style>
        """, unsafe_allow_html=True)

    def render_centered_logo(self, level_name):
        st.markdown(f'''
        <div style="display: flex; flex-direction: column; align-items: center; margin-bottom: 30px;">
            <div style="background-image: url('https://cdn.dribbble.com/userupload/12560411/file/original-cb85895710c2c26fabc3ee05308be2b0.jpg?resize=1600x1200'); 
                        background-size: cover; padding: 40px; border-radius: 30px; text-align: center; border: 2px solid #000; width: 100%; max-width: 700px;">
                <div style="color: #00ffcc; font-size: 20px; font-weight: bold;">🧠 AKYLMAN AI ({level_name})</div>
                <div style="color: white; font-size: 55px; font-weight: 900; margin: 10px 0; text-shadow: 2px 2px 5px #000;">AKYLMAN</div>
                <div style="color: #eee; letter-spacing: 7px; font-size: 12px;">PRESIDENTIAL SCHOOL</div>
            </div>
        </div>
        ''', unsafe_allow_html=True)
