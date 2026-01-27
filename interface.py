import streamlit as st

class AkylmanUI:
    def apply_styles(self):
        st.markdown("""
        <style>
        /* 1. ФОН */
        .stApp {
            background-image: url("https://cdn.dribbble.com/userupload/12560411/file/original-cb85895710c2c26fabc3ee05308be2b0.jpg?resize=1600x1200");
            background-size: cover;
            background-attachment: fixed;
        }

        /* 2. ТЕМНЫЙ САЙДБАР С БЕЛЫМ ТЕКСТОМ */
        [data-testid="stSidebar"] {
            background-color: #1e1e1e !important;
            border-right: 1px solid #333;
        }
        [data-testid="stSidebar"] h1, [data-testid="stSidebar"] p, [data-testid="stSidebar"] label, [data-testid="stSidebar"] span {
            color: #ffffff !important;
        }

        /* 3. ИСПРАВЛЕНИЕ: ЗАГРУЗКА ФАЙЛОВ - ЧЁРНЫЙ ТЕКСТ */
        [data-testid="stFileUploadDropzone"] {
            background-color: #ffffff !important; /* Белый фон блока */
            border: 2px dashed #00ffcc !important;
            border-radius: 15px !important;
            padding: 10px !important;
        }
        /* Делаем весь текст внутри загрузчика ЧЁРНЫМ */
        [data-testid="stFileUploadDropzone"] div,
        [data-testid="stFileUploadDropzone"] span,
        [data-testid="stFileUploadDropzone"] small,
        [data-testid="stFileUploadDropzone"] p {
            color: #000000 !important;
            -webkit-text-fill-color: #000000 !important;
            font-weight: 600 !important;
            display: block !important; /* Возвращаем отображение текста */
        }
        /* Иконка загрузки тоже черная */
        [data-testid="stFileUploadDropzone"] svg {
            fill: #000000 !important;
        }

        /* 4. ЧАТ И ПОЛЕ ВВОДА */
        [data-testid="stChatMessage"] {
            background-color: rgba(0, 0, 0, 0.8) !important;
            border-radius: 15px;
            border: 1px solid rgba(255,255,255,0.1);
        }
        [data-testid="stChatMessage"] p { color: white !important; }
        
        .stChatInputContainer {
            background-color: white !important;
            border-radius: 20px !important;
        }
        .stChatInput textarea { color: black !important; }
        
        /* Скрываем лишнее */
        header { background: transparent !important; }
        footer { visibility: hidden; }
        [data-testid="stSidebarCollapsedControl"] svg { fill: white !important; }
        </style>
        """, unsafe_allow_html=True)

    def render_header(self, version):
        st.markdown(f'''
        <div style="text-align: center; padding: 30px; background: rgba(0,0,0,0.6); border-radius: 20px; margin-bottom: 20px;">
            <div style="color: #00ffcc; font-size: 14px; font-weight: bold;">🧠 AKYLMAN AI ({version})</div>
            <div style="color: white; font-size: 45px; font-weight: 900;">AKYLMAN</div>
        </div>
        ''', unsafe_allow_html=True)
