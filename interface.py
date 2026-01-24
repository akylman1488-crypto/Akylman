import streamlit as st

class AkylmanUI:
    def apply_styles(self):
        st.markdown("""
        <style>
        /* Основной фон как на скрине */
        .stApp {
            background: linear-gradient(rgba(14, 38, 64, 0.8), rgba(14, 38, 64, 0.8)), 
                        url('https://images.unsplash.com/photo-1516979187457-637abb4f9353?auto=format&fit=crop&q=80');
            background-size: cover;
        }

        /* Светлая боковая панель УПРАВЛЕНИЕ */
        [data-testid="stSidebar"] {
            background-color: #f0f2f6 !important;
            border-right: 1px solid #ddd;
        }

        /* Заголовок УПРАВЛЕНИЕ */
        .sidebar-title {
            color: #333;
            font-size: 24px;
            font-weight: bold;
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 20px;
        }

        /* Логотип по центру */
        .logo-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            margin-top: 50px;
        }
        
        .logo-text {
            color: white;
            font-size: 64px;
            font-weight: 900;
            letter-spacing: 5px;
            text-shadow: 2px 2px 10px rgba(0,0,0,0.5);
            margin-top: -20px;
        }

        .sub-logo {
            color: #ccc;
            letter-spacing: 8px;
            font-size: 18px;
        }

        /* Поле ввода сообщения внизу */
        .stChatInputContainer {
            border: 2px solid #ff4b4b !important;
            border-radius: 10px !important;
        }
        </style>
        """, unsafe_allow_html=True)

    def render_centered_logo(self, level_name):
        st.markdown(f"""
        <div class="logo-container">
            <div style="font-size: 40px;">🧠 AKYLMAN AI ({level_name})</div>
            <img src="https://i.ibb.co/v4m0YmC/akylman-logo.png" width="250">
            <div class="logo-text">AKYLMAN</div>
            <div class="sub-logo">PRESIDENTIAL SCHOOL</div>
        </div>
        """, unsafe_allow_html=True)
