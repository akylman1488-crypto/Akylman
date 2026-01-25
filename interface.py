import streamlit as st

class AkylmanUI:
    def apply_styles(self):
        st.markdown("""
        <style>
        /* 1. ФОН САЙТА (Твоя ссылка) */
        .stApp {
            background-image: url("https://cdn.dribbble.com/userupload/12560411/file/original-cb85895710c2c26fabc3ee05308be2b0.jpg?resize=1600x1200");
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
        }

        /* 2. ЗЕЛЕНАЯ ЗОНА (Боковая панель): СВЕТЛО-СЕРЫЙ ФОН */
        [data-testid="stSidebar"] {
            background-color: #e0e2e6 !important; /* Светло-серый */
            border-right: 1px solid #ccc;
        }

        /* Текст в боковой панели (Заголовки): Черный */
        [data-testid="stSidebar"] h1, 
        [data-testid="stSidebar"] h2, 
        [data-testid="stSidebar"] h3, 
        [data-testid="stSidebar"] p, 
        [data-testid="stSidebar"] label {
            color: #000000 !important;
            font-weight: 600 !important;
        }

        /* 3. КРАСНАЯ ЗОНА (Поля ввода): ТЕКСТ ЧЕРНЫЙ */
        [data-testid="stSidebar"] input, 
        [data-testid="stSidebar"] div[data-baseweb="select"] > div {
            background-color: #ffffff !important;
            color: #000000 !important; /* Текст черный */
            border: 1px solid #000000 !important;
            border-radius: 8px !important;
        }
        /* Цвет текста внутри выпадающего списка */
        [data-testid="stSidebar"] div[data-baseweb="select"] span {
            color: #000000 !important;
        }

        /* 4. СИНЯЯ ЗОНА (Сообщения): ТЕКСТ БЕЛЫЙ */
        [data-testid="stChatMessage"] {
            background-color: rgba(0, 0, 0, 0.7) !important; /* Темная подложка */
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 15px;
        }
        
        [data-testid="stChatMessage"] p, 
        [data-testid="stChatMessage"] li, 
        [data-testid="stChatMessage"] div {
            color: #ffffff !important; /* Текст белый */
        }

        /* Зеленая плашка "Доступ активен" */
        .status-box {
            background-color: #d4edda;
            color: #155724 !important;
            padding: 10px;
            border-radius: 8px;
            text-align: center;
            border: 1px solid #c3e6cb;
            margin-bottom: 10px;
            font-weight: bold;
        }

        /* Кнопки в панели */
        .stButton>button {
            background-color: #ffffff !important;
            color: #000000 !important;
            border: 1px solid #000000 !important;
        }

        /* Поле ввода сообщения внизу */
        .stChatInputContainer {
            background-color: rgba(255, 255, 255, 0.9) !important;
            border-radius: 10px;
        }
        </style>
        """, unsafe_allow_html=True)

    def render_centered_logo(self, level_name):
        st.markdown(f'''
        <div style="text-align: center; padding: 40px; background: rgba(0,0,0,0.6); border-radius: 20px; margin-bottom: 20px;">
            <div style="color: #00ffcc; font-size: 18px; font-weight: bold;">🧠 AKYLMAN AI ({level_name})</div>
            <div style="color: white; font-size: 50px; font-weight: 900; margin: 10px 0;">AKYLMAN</div>
            <div style="color: #ddd; letter-spacing: 4px; font-size: 11px;">PRESIDENTIAL SCHOOL</div>
        </div>
        ''', unsafe_allow_html=True)
