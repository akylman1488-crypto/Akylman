 import streamlit as st

class AkylmanUI:
    def apply_styles(self):
        st.markdown("""
        <style>
        /* 1. БЕЛЫЙ ФОН ВСЕГО САЙТА */
        .stApp {
            background-image: url("https://abrakadabra.fun/uploads/posts/2022-02/1643881418_3-abrakadabra-fun-p-belii-fon-bez-nichego-na-ves-5.jpg");
            background-size: cover;
            background-attachment: fixed;
        }

        /* 2. ВЕРХНЯЯ ПОЛОСА (Зеленая зона): БЕЛАЯ */
        header[data-testid="stHeader"] {
            background-color: #ffffff !important;
        }

        /* 3. БОКОВАЯ ПАНЕЛЬ (Синяя зона) */
        [data-testid="stSidebar"] {
            background-color: #f8f9fb !important; /* Светлый фон для панели */
            border-right: 1px solid #ddd;
        }

        /* ТЕКСТ В ПАНЕЛИ: ПРИНУДИТЕЛЬНО ЧЕРНЫЙ */
        [data-testid="stSidebar"] p, 
        [data-testid="stSidebar"] span, 
        [data-testid="stSidebar"] label, 
        [data-testid="stSidebar"] h3,
        [data-testid="stSidebar"] .stMarkdown {
            color: #000000 !important;
            font-weight: 600 !important;
        }

        /* ПОЛЯ ВВОДА: Белый фон, черная рамка */
        [data-testid="stSidebar"] input, 
        [data-testid="stSidebar"] select,
        [data-testid="stSidebar"] div[data-baseweb="select"] {
            background-color: #ffffff !important;
            color: #000000 !important;
            border: 1px solid #000000 !important;
            border-radius: 8px !important;
        }

        /* Кнопка Очистить и Выйти */
        .stButton>button {
            background-color: #000000 !important;
            color: #ffffff !important;
            border-radius: 8px !important;
        }

        /* Окно загрузки файлов (Материалы) */
        [data-testid="stFileUploader"] section {
            background-color: #ffffff !important;
            border: 1px dashed #000000 !important;
            color: #000000 !important;
        }

        /* 4. ЧАТ: Сообщения */
        [data-testid="stChatMessage"] {
            background-color: #ffffff !important;
            border: 1px solid #eeeeee !important;
            box-shadow: 0px 2px 5px rgba(0,0,0,0.05);
        }
        [data-testid="stChatMessage"] p { color: #000000 !important; }

        /* Поле ввода внизу */
        .stChatInputContainer {
            border: 2px solid #000000 !important;
            background: #ffffff !important;
        }
        </style>
        """, unsafe_allow_html=True)

    def render_centered_logo(self, level_name):
        st.markdown(f'''
        <div style="display: flex; flex-direction: column; align-items: center; background: rgba(255, 255, 255, 0.9); padding: 20px; border-radius: 20px; border: 1px solid #eee; margin-bottom: 20px;">
            <div style="color: #000000; font-size: 18px; font-weight: bold;">🧠 AKYLMAN AI ({level_name})</div>
            <div style="color: #000000; font-size: 40px; font-weight: 900;">AKYLMAN</div>
            <div style="color: #666; letter-spacing: 5px; font-size: 10px;">PRESIDENTIAL SCHOOL</div>
        </div>
        ''', unsafe_allow_html=True)
