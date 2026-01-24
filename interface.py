import streamlit as st

class AkylmanUI:
    def apply_styles(self):
        st.markdown("""
        <style>
        /* 1. ОБЩИЙ ФОН */
        .stApp {
            background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS8FHqLyGvth07EBwzDTKirjRPMJbVOxPZbBZFMGNu3EG8NY_dGK3llTrzE&s=10");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }

        /* 2. СИНЯЯ ЗОНА (Боковая панель): Делаем текст БЕЛЫМ навсегда */
        [data-testid="stSidebar"] {
            background-color: rgba(20, 30, 45, 0.8) !important; /* Делаем панель чуть темнее для белого текста */
            border-right: 1px solid #333;
        }
        
        /* Принудительный БЕЛЫЙ цвет для всех надписей в синей зоне */
        [data-testid="stSidebar"] p, 
        [data-testid="stSidebar"] span, 
        [data-testid="stSidebar"] label, 
        [data-testid="stSidebar"] div,
        .sidebar-title {
            color: #ffffff !important; 
            font-weight: 600 !important;
            text-shadow: 1px 1px 2px #000;
        }

        /* 3. СООБЩЕНИЯ (Желтая и Красная зоны): Одинаковый фон */
        [data-testid="stChatMessage"] {
            background-color: rgba(80, 80, 80, 0.85) !important; /* Серый фон как в желтой зоне */
            border-radius: 15px !important;
            border: 1px solid rgba(255, 255, 255, 0.2) !important;
            margin-bottom: 12px !important;
            padding: 15px !important;
        }

        /* Текст внутри всех сообщений всегда белый */
        [data-testid="stChatMessage"] p {
            color: #ffffff !important;
        }

        /* 4. ПОЛЕ ВВОДА С ЧЕРНЫМИ КРАЯМИ */
        .stChatInputContainer {
            border: 2px solid #000000 !important;
            border-radius: 10px !important;
            background: white !important;
        }
        
        .stChatInputContainer textarea {
            color: black !important;
        }

        /* Кнопка очистки и загрузчик */
        .stFileUploader section {
            background-color: rgba(255, 255, 255, 0.1) !important;
            border: 1px dashed white !important;
        }
        </style>
        """, unsafe_allow_html=True)

    def render_centered_logo(self, level_name):
        st.markdown(f"""
        <div style="display: flex; flex-direction: column; align-items: center; background: rgba(0, 0, 0, 0.7); padding: 20px; border-radius: 20px; margin: 10px auto; max-width: 600px; text-align: center;">
            <div style="color: #00ffcc; font-size: 20px; font-weight: bold;">🧠 AKYLMAN AI ({level_name})</div>
            <div style="color: white; font-size: 40px; font-weight: 900; margin: 5px 0;">AKYLMAN</div>
            <div style="color: #aaa; letter-spacing: 5px; font-size: 10px;">PRESIDENTIAL SCHOOL</div>
        </div>
        """, unsafe_allow_html=True)
