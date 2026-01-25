import streamlit as st

class AkylmanUI:
    def apply_styles(self):
        st.markdown("""
        <style>
        /* Фон сайта */
        .stApp {
            background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS8FHqLyGvth07EBwzDTKirjRPMJbVOxPZbBZFMGNu3EG8NY_dGK3llTrzE&s=10");
            background-size: cover;
            background-attachment: fixed;
        }

        /* ЗЕЛЕНАЯ ЗОНА: Белый верх и низ */
        header[data-testid="stHeader"], footer {
            background-color: #ffffff !important;
        }

        /* СИНЯЯ ЗОНА (Кнопки Share/GitHub): Всегда ЧЕРНЫЙ */
        [data-testid="stToolbar"] {
            background-color: #000000 !important;
            border-radius: 10px;
        }
        [data-testid="stToolbar"] svg { fill: white !important; }

        /* БОКОВАЯ ПАНЕЛЬ: Текст всегда ЧЕРНЫЙ */
        [data-testid="stSidebar"] {
            background-color: rgba(255, 255, 255, 0.9) !important;
        }
        [data-testid="stSidebar"] p, [data-testid="stSidebar"] span, 
        [data-testid="stSidebar"] label, [data-testid="stSidebar"] div {
            color: #000000 !important;
            font-weight: 600 !important;
        }

        /* Поля ввода в панели */
        [data-testid="stSidebar"] input, [data-testid="stSidebar"] select {
            color: black !important;
            background-color: white !important;
            border: 1px solid black !important;
        }

        /* СООБЩЕНИЯ (Красная/Желтая зона): Серый фон */
        [data-testid="stChatMessage"] {
            background-color: rgba(50, 50, 50, 0.8) !important;
            border-radius: 15px !important;
        }
        [data-testid="stChatMessage"] p { color: white !important; }

        /* Поле ввода сообщения: Черные края */
        .stChatInputContainer {
            border: 2px solid #000000 !important;
            background: white !important;
        }
        </style>
        """, unsafe_allow_html=True)

    def render_centered_logo(self, level_name):
        st.markdown(f'''
        <div style="display: flex; flex-direction: column; align-items: center; background: rgba(0,0,0,0.7); padding: 20px; border-radius: 20px; margin: 10px auto; max-width: 600px;">
            <div style="color: #00ffcc; font-size: 20px;">🧠 AKYLMAN AI ({level_name})</div>
            <div style="color: white; font-size: 40px; font-weight: 900;">AKYLMAN</div>
            <div style="color: #aaa; letter-spacing: 5px; font-size: 10px;">PRESIDENTIAL SCHOOL</div>
        </div>
        ''', unsafe_allow_html=True)
