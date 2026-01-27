import streamlit as st

class AkylmanUI:
    def apply_styles(self):
        st.markdown("""
        <style>
        /* ФОН И ОБЩИЕ НАСТРОЙКИ */
        .stApp {
            background-image: url("https://cdn.dribbble.com/userupload/12560411/file/original-cb85895710c2c26fabc3ee05308be2b0.jpg?resize=1600x1200");
            background-size: cover;
            background-attachment: fixed;
        }
        
        /* БЕЛАЯ СТРЕЛКА САЙДБАРА */
        [data-testid="stSidebarCollapsedControl"] svg { fill: white !important; color: white !important; }
        header { background: transparent !important; }
        footer { visibility: hidden; }

        /* САЙДБАР КАК У МЕНЯ */
        [data-testid="stSidebar"] {
            background-color: #f0f2f6 !important;
            border-right: 1px solid #e0e0e0;
        }
        [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h3, [data-testid="stSidebar"] label, [data-testid="stSidebar"] p {
            color: #000000 !important;
            font-weight: 700 !important;
        }

        /* ПОЛЕ ВВОДА СООБЩЕНИЯ */
        .stChatInputContainer {
            background-color: rgba(255, 255, 255, 0.95) !important;
            border-radius: 20px !important;
            border: 1px solid rgba(0,0,0,0.1) !important;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1) !important;
            padding: 5px !important;
        }
        .stChatInput textarea { color: black !important; }

        /* ЗАГРУЗКА ФАЙЛОВ "ПЛЮСИК" */
        [data-testid="stFileUploadDropzone"] {
            border: 3px dashed #00ffcc !important;
            background: rgba(0, 255, 204, 0.05) !important;
            border-radius: 50% !important;
            width: 80px !important;
            height: 80px !important;
            display: flex !important;
            justify-content: center !important;
            align-items: center !important;
            margin: 20px auto !important;
        }
        [data-testid="stFileUploadDropzone"]::before {
            content: "+";
            font-size: 45px;
            color: #00ffcc;
            font-weight: bold;
        }
        [data-testid="stFileUploadDropzone"] div, [data-testid="stFileUploadDropzone"] small, [data-testid="stFileUploadDropzone"] span {
            display: none !important;
        }

        /* МОДАЛЬНОЕ ОКНО ПАРОЛЯ */
        .password-popup {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background-color: white;
            padding: 30px;
            border-radius: 25px;
            box-shadow: 0 20px 50px rgba(0,0,0,0.5);
            z-index: 9999;
            width: 350px;
            text-align: center;
            border: 2px solid #00ffcc;
        }
        </style>
        """, unsafe_allow_html=True)

    def render_centered_logo(self, level_name):
        st.markdown(f'''
        <div style="text-align: center; padding: 30px; background: rgba(0,0,0,0.7); border-radius: 20px; margin-bottom: 20px; border: 1px solid rgba(255,255,255,0.1);">
            <div style="color: #00ffcc; font-size: 14px; font-weight: bold; letter-spacing: 1px;">🧠 AKYLMAN AI ({level_name})</div>
            <div style="color: white; font-size: 45px; font-weight: 900; margin: 5px 0; line-height: 1;">AKYLMAN</div>
            <div style="color: #aaa; font-size: 10px; letter-spacing: 4px; font-weight: 300;">PRESIDENTIAL SCHOOL</div>
        </div>
        ''', unsafe_allow_html=True)
