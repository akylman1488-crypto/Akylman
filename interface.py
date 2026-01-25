import streamlit as st

class AkylmanUI:
    def apply_styles(self):
        st.markdown("""
        <style>
        /* 1. БЕЛЫЙ ФОН САЙТА */
        .stApp {
            background-image: url("https://abrakadabra.fun/uploads/posts/2022-02/1643881418_3-abrakadabra-fun-p-belii-fon-bez-nichego-na-ves-5.jpg");
            background-size: cover;
            background-attachment: fixed;
        }

        /* 2. ВЕРХНЯЯ ПАНЕЛЬ: Чисто белая */
        header[data-testid="stHeader"] {
            background-color: #ffffff !important;
        }

        /* 3. БОКОВАЯ ПАНЕЛЬ: Тот самый темно-синий/черный цвет */
        [data-testid="stSidebar"] {
            background-color: #262730 !important;
            min-width: 300px !important;
        }

        /* Текст в панели: Белый и четкий */
        [data-testid="stSidebar"] p, [data-testid="stSidebar"] span, 
        [data-testid="stSidebar"] label, [data-testid="stSidebar"] h3 {
            color: #ffffff !important;
            font-size: 16px !important;
        }

        /* Поля ввода и выбора в панели: Белый фон, черный текст */
        [data-testid="stSidebar"] input, 
        [data-testid="stSidebar"] select,
        [data-testid="stSidebar"] div[data-baseweb="select"] {
            background-color: #ffffff !important;
            color: #000000 !important;
            border-radius: 10px !important;
        }

        /* Зеленая плашка "Доступ активен" */
        .status-box {
            background-color: #d4edda;
            border: 1px solid #c3e6cb;
            color: #155724 !important;
            padding: 10px;
            border-radius: 8px;
            text-align: center;
            margin-bottom: 15px;
            font-weight: bold;
        }

        /* Кнопки "Выйти" и "Очистить": Белая рамка */
        .stButton>button {
            background-color: transparent !important;
            color: white !important;
            border: 1px solid #ffffff !important;
            border-radius: 8px !important;
        }

        /* Окно загрузки файлов в темной панели */
        [data-testid="stFileUploader"] section {
            background-color: #ffffff !important;
            color: #000000 !important;
            border-radius: 10px !important;
        }

        /* 4. ЧАТ: Сообщения на белом фоне */
        [data-testid="stChatMessage"] {
            background-color: #f0f2f6 !important;
            border-radius: 15px !important;
            border: 1px solid #ddd !important;
        }
        
        [data-testid="stChatMessage"] p {
            color: #000000 !important;
        }

        /* Поле ввода сообщения: Черная рамка */
        .stChatInputContainer {
            border: 2px solid #000000 !important;
            background: #ffffff !important;
        }
        </style>
        """, unsafe_allow_html=True)

    def render_centered_logo(self, level_name):
        st.markdown(f'''
        <div style="display: flex; flex-direction: column; align-items: center; background: rgba(50, 50, 50, 0.8); padding: 25px; border-radius: 20px; margin: 10px auto; max-width: 650px;">
            <div style="color: #00ffcc; font-size: 18px; font-weight: bold;">🧠 AKYLMAN AI ({level_name})</div>
            <div style="color: white; font-size: 42px; font-weight: 900; margin: 5px 0;">AKYLMAN</div>
            <div style="color: #ccc; letter-spacing: 5px; font-size: 10px;">PRESIDENTIAL SCHOOL</div>
        </div>
        ''', unsafe_allow_html=True)
