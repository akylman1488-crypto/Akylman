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

        /* 2. ЗЕЛЕНАЯ ОБЛАСТЬ (Верх и Низ): ВСЕГДА БЕЛЫЙ */
        header[data-testid="stHeader"], 
        footer, 
        .stApp > header {
            background-color: #ffffff !important;
            color: #000000 !important;
        }

        /* 3. СИНЯЯ ОБЛАСТЬ (Системные кнопки справа вверху): ВСЕГДА ЧЕРНЫЙ */
        [data-testid="stToolbar"], 
        [data-testid="stStatusWidget"],
        .stActionButton {
            background-color: #000000 !important;
            color: #ffffff !important;
            border-radius: 8px !important;
        }
        
        [data-testid="stToolbar"] svg {
            fill: #ffffff !important;
        }

        /* 4. БОКОВАЯ ПАНЕЛЬ (Синяя зона): ТЕКСТ ТЕПЕРЬ ВСЕГДА ЧЕРНЫЙ */
        [data-testid="stSidebar"] {
            background-color: rgba(240, 242, 246, 0.95) !important; /* Светлый фон панели */
            border-right: 1px solid #ddd;
        }
        
        /* Принудительный ЧЕРНЫЙ цвет для всех надписей в панели */
        [data-testid="stSidebar"] p, 
        [data-testid="stSidebar"] span, 
        [data-testid="stSidebar"] label, 
        [data-testid="stSidebar"] div,
        .sidebar-title {
            color: #000000 !important; 
            font-weight: 600 !important;
        }
        
        /* Поля ввода в боковой панели (белый фон, черный текст) */
        [data-testid="stSidebar"] input, 
        [data-testid="stSidebar"] select,
        [data-testid="stSidebar"] div[role="listbox"] {
            color: #000000 !important;
            background-color: #ffffff !important;
            border: 1px solid #000 !important;
        }

        /* 5. СООБЩЕНИЯ ЧАТА (Красная и Желтая зоны): ЕДИНЫЙ СЕРЫЙ ФОН */
        [data-testid="stChatMessage"] {
            background-color: rgba(60, 60, 60, 0.85) !important;
            border-radius: 15px !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
        }

        [data-testid="stChatMessage"] p {
            color: #ffffff !important;
        }

        /* 6. ПОЛЕ ВВОДА ВНИЗУ: ЧЕРНЫЕ КРАЯ */
        .stChatInputContainer {
            border: 2px solid #000000 !important;
            background: #ffffff !important;
        }
        
        .stChatInputContainer textarea {
            color: #000000 !important;
        }
        </style>
        """, unsafe_allow_html=True)

    def render_centered_logo(self, level_name):
        st.markdown(f"""
        <div style="display: flex; flex-direction: column; align-items: center; background: rgba(0, 0, 0, 0.7); padding: 25px; border-radius: 20px; margin: 10px auto; max-width: 650px; text-align: center;">
            <div style="color: #00ffcc; font-size: 22px; font-weight: bold;">🧠 AKYLMAN AI ({level_name})</div>
            <div style="color: white; font-size: 45px; font-weight: 900;
