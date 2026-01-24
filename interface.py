import streamlit as st

class AkylmanUI:
    def apply_styles(self):
        st.markdown("""
        <style>
        /* 1. ФОН ВСЕГО ПРИЛОЖЕНИЯ */
        .stApp {
            background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS8FHqLyGvth07EBwzDTKirjRPMJbVOxPZbBZFMGNu3EG8NY_dGK3llTrzE&s=10");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }

        /* 2. СИНЯЯ ЗОНА (Боковая панель): Делаем весь текст ЧЕРНЫМ навсегда */
        [data-testid="stSidebar"] {
            background-color: #f0f2f6 !important;
            border-right: 1px solid #ddd;
        }
        
        [data-testid="stSidebar"] p, 
        [data-testid="stSidebar"] span, 
        [data-testid="stSidebar"] label, 
        [data-testid="stSidebar"] div {
            color: #000000 !important; /* Черный текст */
            font-weight: 500;
        }

        /* Исправляем цвет заголовка в боковой панели */
        .sidebar-title {
            color: #000000 !important;
            font-size: 22px;
            font-weight: bold;
            margin-bottom: 15px;
        }

        /* 3. ЖЕЛТАЯ И КРАСНАЯ ЗОНЫ (Сообщения): Делаем одинаковый фон */
        /* Стиль для сообщений пользователя (Желтая зона) и ИИ (Красная зона) */
        [data-testid="stChatMessage"] {
            background-color: rgba(100, 100, 100, 0.7) !important; /* Серый полупрозрачный фон */
            border-radius: 15px !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            margin-bottom: 10px !important;
            padding: 15px !important;
        }

        /* Текст внутри сообщений всегда белый для контраста с серым фоном */
        [data-testid="stChatMessage"] p {
            color: #ffffff !important;
            font-size: 1.1rem !important;
        }

        /* 4. ЦЕНТРАЛЬНЫЙ ЛОГОТИП */
        .logo-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            background: rgba(0, 0, 0, 0.6);
            padding: 25px;
            border-radius: 20px;
            margin: 20px auto;
            max-width: 700px;
        }
        
        .logo-text {
            color: white !important;
            font-size: 45px;
            font-weight: 900;
        }

        /* 5. ПОЛЕ ВВОДА */
        .stChatInputContainer {
            border: 2px solid #000000 !important;
            border-radius: 10px !important;
            background: white !important;
        }
        
        .stChatInputContainer textarea {
            color: black !important;
        }
        </style>
        """, unsafe_allow_html=True)

    def render_centered_logo(self, level_name):
        st.markdown(f"""
        <div class="logo-container">
            <div style="color: #00ffcc; font-size: 22px;">🧠 AKYLMAN AI ({level_name})</div>
            <div class="logo-text">AKYLMAN</div>
            <div style="color: #ccc; letter-spacing: 4px; font-size: 12px;">PRESIDENTIAL SCHOOL</div>
        </div>
        """, unsafe_allow_html=True)
