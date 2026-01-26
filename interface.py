import streamlit as st

class AkylmanUI:
    def apply_styles(self):
        st.markdown("""
        <style>
        /* Общий фон и Хедер */
        .stApp {
            background-image: url("https://cdn.dribbble.com/userupload/12560411/file/original-cb85895710c2c26fabc3ee05308be2b0.jpg?resize=1600x1200");
            background-size: cover;
            background-attachment: fixed;
        }
        
        /* Кнопка боковой панели БЕЛАЯ */
        [data-testid="stSidebarCollapsedControl"] svg { fill: white !important; }

        /* СТИЛЬ ОКНА ПАРОЛЯ (В центре) */
        .password-popup {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background-color: white;
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.5);
            z-index: 1000;
            width: 350px;
            text-align: center;
        }

        /* ЗАГРУЗКА ФАЙЛОВ В ВИДЕ ПЛЮСА */
        [data-testid="stFileUploadDropzone"] {
            border: 2px dashed #00ffcc !important;
            background: rgba(0,0,0,0.2) !important;
            border-radius: 50% !important;
            width: 80px !important;
            height: 80px !important;
            display: flex !important;
            justify-content: center !important;
            align-items: center !important;
            margin: 0 auto !important;
        }
        [data-testid="stFileUploadDropzone"]::before {
            content: "+";
            font-size: 40px;
            color: #00ffcc;
        }
        [data-testid="stFileUploadDropzone"] div, [data-testid="stFileUploadDropzone"] small {
            display: none !important; /* Скрываем текст внутри, оставляем только плюс */
        }

        /* Плавное исчезновение конфетти (через CSS анимацию) */
        .fade-out {
            animation: fadeOut 3s forwards;
        }
        @keyframes fadeOut {
            0% { opacity: 1; }
            70% { opacity: 1; }
            100% { opacity: 0; }
        }
        </style>
        """, unsafe_allow_html=True)

    def render_centered_logo(self, level_name):
        st.markdown(f'''
        <div style="text-align: center; padding: 20px; background: rgba(0,0,0,0.6); border-radius: 20px; margin-bottom: 20px;">
            <div style="color: #00ffcc; font-size: 14px; font-weight: bold;">🧠 AKYLMAN AI ({level_name})</div>
            <div style="color: white; font-size: 30px; font-weight: 900;">AKYLMAN</div>
        </div>
        ''', unsafe_allow_html=True)
