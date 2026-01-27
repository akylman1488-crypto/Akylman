import streamlit as st

class AkylmanUI:
    def apply_styles(self):
        st.markdown("""
        <style>
        /* ГЛОБАЛЬНЫЙ ФОН */
        .stApp {
            background-image: url("https://cdn.dribbble.com/userupload/12560411/file/original-cb85895710c2c26fabc3ee05308be2b0.jpg?resize=1600x1200");
            background-size: cover;
            background-attachment: fixed;
        }

        /* КНОПКА САЙДБАРА */
        [data-testid="stSidebarCollapsedControl"] svg { fill: white !important; }
        header { background: transparent !important; }

        /* САЙДБАР: ЧИСТЫЙ СТИЛЬ */
        [data-testid="stSidebar"] {
            background-color: rgba(240, 242, 246, 0.95) !important;
            border-right: 1px solid rgba(0,0,0,0.1);
        }
        [data-testid="stSidebar"] h1, [data-testid="stSidebar"] label {
            color: #1e1e1e !important;
            font-weight: 800 !important;
            text-transform: uppercase;
            font-size: 0.9rem;
        }

        /* ПОЛЕ ВВОДА (CHAT INPUT) */
        .stChatInputContainer {
            background-color: white !important;
            border-radius: 25px !important;
            padding: 8px !important;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2) !important;
            border: 1px solid #eee !important;
        }
        .stChatInput textarea { color: #000 !important; }

        /* ЗАГРУЗКА ФАЙЛОВ "ПЛЮСИК" */
        [data-testid="stFileUploadDropzone"] {
            border: 3px dashed #00ffcc !important;
            background: rgba(0, 255, 204, 0.1) !important;
            border-radius: 50% !important;
            width: 80px !important;
            height: 80px !important;
            display: flex !important;
            justify-content: center !important;
            align-items: center !important;
            margin: 20px auto !important;
            transition: 0.3s;
        }
        [data-testid="stFileUploadDropzone"]:hover { transform: scale(1.1); }
        [data-testid="stFileUploadDropzone"]::before {
            content: "+";
            font-size: 50px;
            color: #00ffcc;
        }
        [data-testid="stFileUploadDropzone"] div, [data-testid="stFileUploadDropzone"] small { display: none !important; }

        /* ОКНО ПАРОЛЯ */
        .password-popup {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: white;
            padding: 40px;
            border-radius: 30px;
            box-shadow: 0 25px 60px rgba(0,0,0,0.6);
            z-index: 9999;
            width: 400px;
            text-align: center;
            border: 3px solid #00ffcc;
        }

        /* СТИЛЬ СООБЩЕНИЙ */
        [data-testid="stChatMessage"] {
            background-color: rgba(0, 0, 0, 0.7) !important;
            border-radius: 20px !important;
            color: white !important;
            margin-bottom: 15px;
        }
        </style>
        """, unsafe_allow_html=True)

    def render_header(self, version):
        st.markdown(f'''
        <div style="text-align: center; padding: 30px; background: rgba(0,0,0,0.7); border-radius: 25px; margin-bottom: 25px;">
            <div style="color: #00ffcc; font-size: 14px; font-weight: bold;">🧠 AKYLMAN AI ({version})</div>
            <div style="color: white; font-size: 48px; font-weight: 900; letter-spacing: -1px;">AKYLMAN</div>
            <div style="color: #888; font-size: 10px; letter-spacing: 5px;">PRESIDENTIAL SCHOOL</div>
        </div>
        ''', unsafe_allow_html=True)
