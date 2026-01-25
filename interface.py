import streamlit as st

class AkylmanUI:
    def apply_styles(self):
        st.markdown("""
        <style>
        /* 1. ГЛОБАЛЬНАЯ БЛОКИРОВКА ЦВЕТОВ */
        :root {
            --primary-color: #00ffcc;
        }

        /* Общий фон */
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

        /* 3. СИНЯЯ ОБЛАСТЬ (Системные кнопки): ВСЕГДА ЧЕРНЫЙ */
        [data-testid="stToolbar"], 
        [data-testid="stStatusWidget"],
        .stActionButton,
        button[title="View source on GitHub"] {
            background-color: #000000 !important;
            color: #ffffff !important;
            border-radius: 8px !important;
        }
        
        [data-testid="stToolbar"] svg {
            fill: #ffffff !important;
        }

        /* 4. БОКОВАЯ ПАНЕЛЬ (Синяя зона на схеме): ТЕКСТ ВСЕГДА БЕЛЫЙ */
        [data-testid="stSidebar"] {
            background-color: rgba(20, 30, 45, 0.95) !important;
        }
        
        /* Заставляем все надписи в панели быть белыми */
        [data-testid="stSidebar"] * {
            color: #ffffff !important;
        }
        
        /* Исправляем поля ввода в боковой панели (чтобы текст внутри был черным) */
        [data-testid="stSidebar"] input, 
        [data-testid="stSidebar"] select,
        [data-testid="stSidebar"] div[role="listbox"] {
            color: #000000 !important;
            background-color: #ffffff !important;
        }

        /* 5. СООБЩЕНИЯ (Красная и Желтая зоны): ВСЕГДА СЕРЫЙ ФОН */
        [data-testid="stChatMessage"] {
            background-color: rgba(50, 50, 50, 0.9) !important;
            border-radius: 15px !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
        }

        [data-testid="stChatMessage"] p {
            color: #ffffff !important;
        }

        /* 6. ПОЛЕ ВВОДА: ЧЕРНЫЕ КРАЯ */
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
            <div style="color: white; font-size: 45px; font-weight: 900; margin: 5px 0;">AKYLMAN</div>
            <div style="color: #aaa; letter-spacing: 5px; font-size: 11px;">PRESIDENTIAL SCHOOL</div>
        </div>
        """, unsafe_allow_html=True)
