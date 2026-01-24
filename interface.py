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

        /* 2. ЗЕЛЕНАЯ ОБЛАСТЬ (Верх и Низ): Делаем БЕЛЫМ */
        header[data-testid="stHeader"], 
        footer, 
        .stApp > header {
            background-color: #ffffff !important;
            color: #000000 !important;
        }

        /* 3. СИНЯЯ ОБЛАСТЬ (Кнопки Share, Github и др.): Делаем ЧЕРНЫМ */
        [data-testid="stToolbar"], 
        .stActionButton, 
        button[title="View source on GitHub"],
        [data-testid="stStatusWidget"] {
            background-color: #000000 !important;
            color: #ffffff !important;
            border-radius: 5px;
        }
        
        /* Исправляем цвет иконок в синей области, чтобы они были видны на черном */
        [data-testid="stToolbar"] svg {
            fill: #ffffff !important;
        }

        /* 4. СИНЯЯ ЗОНА (Боковая панель): Текст белый, как ты просил ранее */
        [data-testid="stSidebar"] {
            background-color: rgba(20, 30, 45, 0.9) !important;
        }
        
        [data-testid="stSidebar"] * {
            color: #ffffff !important;
        }

        /* 5. СООБЩЕНИЯ: Одинаковый фон для Красной и Желтой зоны */
        [data-testid="stChatMessage"] {
            background-color: rgba(60, 60, 60, 0.8) !important;
            border-radius: 12px !important;
            margin-bottom: 10px !important;
        }

        /* 6. ПОЛЕ ВВОДА: Черные края */
        .stChatInputContainer {
            border: 2px solid #000000 !important;
            background: #ffffff !important;
        }
        </style>
        """, unsafe_allow_html=True)

    def render_centered_logo(self, level_name):
        st.markdown(f"""
        <div style="display: flex; flex-direction: column; align-items: center; background: rgba(0, 0, 0, 0.7); padding: 20px; border-radius: 20px; margin: 10px auto; max-width: 600px;">
            <div style="color: #00ffcc; font-size: 20px; font-weight: bold;">🧠 AKYLMAN AI ({level_name})</div>
            <div style="color: white; font-size: 40px; font-weight: 900;">AKYLMAN</div>
            <div style="color: #aaa; letter-spacing: 5px; font-size: 10px;">PRESIDENTIAL SCHOOL</div>
        </div>
        """, unsafe_allow_html=True)
