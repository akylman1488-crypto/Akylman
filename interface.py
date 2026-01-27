import streamlit as st

class AkylmanUI:
    def apply_styles(self):
        st.markdown("""
        <style>
        /* 1. ФОН ПРИЛОЖЕНИЯ */
        .stApp {
            background-image: url("https://cdn.dribbble.com/userupload/12560411/file/original-cb85895710c2c26fabc3ee05308be2b0.jpg?resize=1600x1200");
            background-size: cover;
            background-attachment: fixed;
        }

        /* 2. БОКОВАЯ ПАНЕЛЬ (САЙДБАР) - ТЁМНАЯ */
        [data-testid="stSidebar"] {
            background-color: #1e1e1e !important; /* Тёмный фон, чтобы белый текст читался */
            border-right: 1px solid #333;
        }
        
        /* ВСЕ ТЕКСТЫ В САЙДБАРЕ - БЕЛЫЕ (как ты просил в красном круге) */
        [data-testid="stSidebar"] h1, 
        [data-testid="stSidebar"] h2, 
        [data-testid="stSidebar"] h3, 
        [data-testid="stSidebar"] label, 
        [data-testid="stSidebar"] p, 
        [data-testid="stSidebar"] span {
            color: #ffffff !important;
        }
        
        /* Поля ввода в сайдбаре */
        [data-testid="stSidebar"] .stTextInput input, 
        [data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] div {
            color: black !important; /* Текст внутри полей ввода черный */
        }

        /* 3. ЧАТ (Красный круг внизу) */
        /* Сообщения пользователя и ассистента - БЕЛЫЙ ТЕКСТ */
        [data-testid="stChatMessage"] p {
            color: #ffffff !important;
            font-size: 16px;
        }
        [data-testid="stChatMessage"] {
            background-color: rgba(0, 0, 0, 0.7) !important;
            border-radius: 15px;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }

        /* 4. ПОЛЕ ВВОДА (Внизу) */
        .stChatInputContainer {
            background-color: white !important;
            border-radius: 20px !important;
            padding: 5px !important;
        }
        .stChatInput textarea {
            color: black !important;
        }

        /* 5. ЗАГРУЗКА ФАЙЛОВ "ПЛЮСИК" */
        [data-testid="stFileUploadDropzone"] {
            border: 2px dashed #00ffcc !important;
            background: rgba(255, 255, 255, 0.1) !important;
            border-radius: 50% !important;
            width: 70px !important;
            height: 70px !important;
            display: flex !important;
            justify-content: center !important;
            align-items: center !important;
            margin: 20px auto !important;
        }
        [data-testid="stFileUploadDropzone"]::before {
            content: "+";
            font-size: 40px;
            color: #00ffcc;
        }
        [data-testid="stFileUploadDropzone"] div, [data-testid="stFileUploadDropzone"] small { display: none !important; }
        
        /* Убираем верхнюю полосу и футер */
        header { background: transparent !important; }
        footer { visibility: hidden; }
        [data-testid="stSidebarCollapsedControl"] svg { fill: white !important; }
        </style>
        """, unsafe_allow_html=True)

    def render_header(self, version):
        st.markdown(f'''
        <div style="text-align: center; padding: 30px; background: rgba(0,0,0,0.6); border-radius: 20px; margin-bottom: 20px;">
            <div style="color: #00ffcc; font-size: 14px; font-weight: bold;">🧠 AKYLMAN AI ({version})</div>
            <div style="color: white; font-size: 45px; font-weight: 900; margin-top: 5px;">AKYLMAN</div>
            <div style="color: #bbb; font-size: 10px; letter-spacing: 3px;">PRESIDENTIAL SCHOOL</div>
        </div>
        ''', unsafe_allow_html=True)
