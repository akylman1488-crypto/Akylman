import streamlit as st

class AkylmanUI:
    def apply_styles(self):
        st.markdown("""
        <style>
        /* Общий фон */
        .stApp {
            background-image: url("https://cdn.dribbble.com/userupload/12560411/file/original-cb85895710c2c26fabc3ee05308be2b0.jpg?resize=1600x1200");
            background-size: cover;
            background-attachment: fixed;
        }

        /* ПОЛЕ ВВОДА КАК НА СКРИНШОТАХ */
        .stChatInputContainer {
            background-color: rgba(255, 255, 255, 0.95) !important;
            border-radius: 20px !important;
            padding: 10px !important;
            border: 1px solid rgba(0, 0, 0, 0.1) !important;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1) !important;
        }

        /* Настройка текста внутри поля ввода */
        .stChatInput textarea {
            color: #000000 !important;
            font-size: 16px !important;
        }

        /* Кнопка отправки (иконка стрелочки) */
        .stChatInput button svg {
            fill: #1e1e1e !important;
        }

        /* Остальные стили (Сайдбар и кнопки) */
        [data-testid="stSidebar"] { background-color: #f0f2f6 !important; }
        
        /* Загрузка ПЛЮСОМ */
        [data-testid="stFileUploadDropzone"] {
            border: 3px dashed #00ffcc !important;
            background: rgba(255,255,255,0.1) !important;
            border-radius: 50% !important;
            width: 80px !important;
            height: 80px !important;
            display: flex !important;
            justify-content: center !important;
            align-items: center !important;
            margin: 10px auto !important;
        }
        [data-testid="stFileUploadDropzone"]::before {
            content: "+";
            font-size: 40px;
            color: #00ffcc;
            font-weight: bold;
        }
        [data-testid="stFileUploadDropzone"] div, [data-testid="stFileUploadDropzone"] small, [data-testid="stFileUploadDropzone"] span {
            display: none !important;
        }

        /* Окно пароля в центре */
        .password-popup {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background-color: white;
            padding: 30px;
            border-radius: 25px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.5);
            z-index: 10000;
            width: 350px;
            text-align: center;
        }
        </style>
        """, unsafe_allow_html=True)

    def render_centered_logo(self, level_name):
        st.markdown(f'''
        <div style="text-align: center; padding: 20px; background: rgba(0,0,0,0.6); border-radius: 20px; margin-bottom: 20px;">
            <div style="color: #00ffcc; font-size: 14px; font-weight: bold;">🧠 AKYLMAN AI ({level_name})</div>
            <div style="color: white; font-size: 30px; font-weight: 900; margin: 5px 0;">AKYLMAN</div>
            <div style="color: #ccc; font-size: 10px; letter-spacing: 3px;">PRESIDENTIAL SCHOOL</div>
        </div>
        ''', unsafe_allow_html=True)
