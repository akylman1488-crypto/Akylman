import streamlit as st

class AkylmanUI:
    def apply_styles(self):
        st.markdown("""
        <style>
        /* ГЛОБАЛЬНЫЙ ФОН (твоя новая ссылка) */
        .stApp {
            background-image: url("https://abrakadabra.fun/uploads/posts/2022-02/1643881418_3-abrakadabra-fun-p-belii-fon-bez-nichego-na-ves-5.jpg");
            background-size: cover;
            background-attachment: fixed;
        }

        /* ЗЕЛЕНАЯ ЗОНА: Белый верх и низ */
        header[data-testid="stHeader"], footer {
            background-color: #ffffff !important;
        }

        /* СИНЯЯ ЗОНА (Кнопки вверху): Черный фон */
        [data-testid="stToolbar"] {
            background-color: #000000 !important;
            border-radius: 8px;
        }
        [data-testid="stToolbar"] svg { fill: white !important; }

        /* БОКОВАЯ ПАНЕЛЬ: Темная, как на образце */
        [data-testid="stSidebar"] {
            background-color: #262730 !important;
            border-right: 1px solid #444;
        }

        /* Весь текст в панели — белый */
        [data-testid="stSidebar"] p, [data-testid="stSidebar"] span, 
        [data-testid="stSidebar"] label, [data-testid="stSidebar"] h3 {
            color: #ffffff !important;
            font-weight: 500 !important;
        }

        /* Кнопки в панели: Прозрачные с белой рамкой */
        [data-testid="stSidebar"] .stButton>button {
            background-color: transparent !important;
            color: white !important;
            border: 1px solid #ffffff !important;
            border-radius: 8px !important;
            width: 100%;
        }

        /* Зеленая плашка "Доступ активен" */
        .status-box {
            background-color: rgba(144, 238, 144, 0.2);
            border: 1px solid #90ee90;
            color: #90ee90 !important;
            padding: 10px;
            border-radius: 8px;
            text-align: center;
            margin-bottom: 15px;
            font-weight: bold;
        }

        /* Поля выбора и ввода в темной панели */
        [data-testid="stSidebar"] div[role="listbox"], 
        [data-testid="stSidebar"] input {
            background-color: #1e1e1e !important;
            color: white !important;
            border: 1px solid #555 !important;
        }

        /* Сообщения в чате: Темно-серый фон */
        [data-testid="stChatMessage"] {
            background-color: rgba(50, 50, 50, 0.9) !important;
            border-radius: 15px !important;
        }
        [data-testid="stChatMessage"] p { color: white !important; }

        /* Поле ввода внизу: Черная рамка */
        .stChatInputContainer {
            border: 2px solid #000000 !important;
            background: white !important;
        }
        </style>
        """, unsafe_allow_html=True)

    def render_centered_logo(self, level_name):
        st.markdown(f'''
        <div style="display: flex; flex-direction: column; align-items: center; background: rgba(0,0,0,0.7); padding: 25px; border-radius: 20px; margin: 15px auto; max-width: 650px; text-align: center;">
            <div style="color: #00ffcc; font-size: 20px; font-weight: bold;">🧠 AKYLMAN AI ({level_name})</div>
            <div style="color: white; font-size: 45px; font-weight: 900; margin: 5px 0;">AKYLMAN</div>
            <div style="color: #aaa; letter-spacing: 5px; font-size: 11px;">PRESIDENTIAL SCHOOL</div>
        </div>
        ''', unsafe_allow_html=True)
