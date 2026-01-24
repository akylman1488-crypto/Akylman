import streamlit as st

class AkylmanUI:
    def apply_styles(self):
        st.markdown("""
        <style>
        /* Установка фона по твоей ссылке */
        .stApp {
            background-image: url("https://abrakadabra.fun/uploads/posts/2022-02/1643881418_3-abrakadabra-fun-p-belii-fon-bez-nichego-na-ves-5.jpg");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }

        /* Светлая боковая панель */
        [data-testid="stSidebar"] {
            background-color: #f0f2f6 !important;
            border-right: 1px solid #ddd;
        }

        .sidebar-title {
            color: #333;
            font-size: 24px;
            font-weight: bold;
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 20px;
        }

        /* Центрирование логотипа */
        .logo-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            margin-top: 30px;
            background: rgba(0, 0, 0, 0.4); /* Затемнение под текстом для читаемости */
            padding: 20px;
            border-radius: 20px;
        }
        
        .logo-text {
            color: white;
            font-size: 50px;
            font-weight: 900;
            letter-spacing: 3px;
            text-shadow: 2px 2px 10px rgba(0,0,0,0.8);
        }

        /* ПОЛЕ ВВОДА С ЧЕРНЫМИ КРАЯМИ */
        .stChatInputContainer {
            border: 2px solid #000000 !important; /* Черные края */
            border-radius: 12px !important;
            background-color: rgba(255, 255, 255, 0.9) !important;
            padding: 5px !important;
        }
        
        .stChatInputContainer textarea {
            color: #000 !important;
        }

        /* Стиль кнопок */
        .stButton>button {
            border-radius: 10px;
            border: 1px solid #000;
        }
        </style>
        """, unsafe_allow_html=True)

    def render_centered_logo(self, level_name):
        st.markdown(f"""
        <div class="logo-container">
            <div style="color: #00ffcc; font-size: 30px; font-weight: bold; margin-bottom: 10px;">
                🧠 AKYLMAN AI ({level_name})
            </div>
            <div class="logo-text">AKYLMAN</div>
            <div style="color: #eee; letter-spacing: 5px; font-size: 14px;">
                PRESIDENTIAL SCHOOL
            </div>
        </div>
        """, unsafe_allow_html=True)
