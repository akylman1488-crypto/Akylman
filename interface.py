import streamlit as st

class AkylmanUI:
    def apply_styles(self):
        st.markdown("""
        <style>
        /* 1. ФОН САЙТА */
        .stApp {
            background-image: url("https://cdn.dribbble.com/userupload/12560411/file/original-cb85895710c2c26fabc3ee05308be2b0.jpg?resize=1600x1200");
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
        }

        /* 2. УПРАВЛЕНИЕ ХЕДЕРОМ И ФУТЕРОМ */
        header[data-testid="stHeader"] {
            background-color: rgba(0,0,0,0) !important;
        }
        header [data-testid="stHeaderActionElements"] {
            display: none !important;
        }
        footer { visibility: hidden; }

        /* 3. БОКОВАЯ ПАНЕЛЬ (СВЕТЛО-СЕРАЯ) */
        [data-testid="stSidebar"] {
            background-color: #f0f2f6 !important;
        }
        
        [data-testid="stSidebar"] h3, 
        [data-testid="stSidebar"] p, 
        [data-testid="stSidebar"] label {
            color: #000000 !important;
            font-weight: 700 !important;
        }

        /* 4. ПОЛЕ ПАРОЛЯ (КРАСНАЯ ОБЛАСТЬ): ТЕКСТ БЕЛЫЙ */
        [data-testid="stSidebar"] div[data-baseweb="input"] {
            background-color: #1e1e1e !important;
            border: none !important;
            border-radius: 10px !important;
        }
        [data-testid="stSidebar"] input {
            color: #ffffff !important;
        }

        /* 5. ВЫБОР МОДЕЛИ И УРОКА (СИНЯЯ ОБЛАСТЬ): ТЕКСТ ЧЕРНЫЙ */
        /* Принудительно задаем черный цвет для текста в селектах */
        [data-testid="stSidebar"] div[data-baseweb="select"] > div {
            background-color: #ffffff !important;
            border: none !important;
            border-radius: 10px !important;
        }
        
        /* Основной текст в поле выбора */
        [data-testid="stSidebar"] div[data-baseweb="select"] [data-testid="stMarkdownContainer"] p,
        [data-testid="stSidebar"] div[data-baseweb="select"] span {
            color: #000000 !important;
            font-weight: 600 !important;
        }

        /* Цвет текста в выпадающем списке при нажатии */
        div[data-baseweb="popover"] li {
            color: #000000 !important;
        }
        
        /* Иконки (стрелочки и глаз) */
        [data-testid="stSidebar"] svg {
            fill: #000000 !important;
        }

        /* 6. ЧАТ И СООБЩЕНИЯ */
        [data-testid="stChatMessage"] {
            background-color: rgba(0, 0, 0, 0.75) !important;
            border-radius: 15px;
        }
        [data-testid="stChatMessage"] p {
            color: #ffffff !important;
        }

        .stChatInputContainer {
            background-color: rgba(255,255,255,0.95) !important;
            border-radius: 12px;
        }
        </style>
        """, unsafe_allow_html=True)

    def render_centered_logo(self, level_name):
        st.markdown(f'''
        <div style="text-align: center; padding: 40px; background: rgba(0,0,0,0.6); border-radius: 20px; margin-bottom: 20px; border: 1px solid rgba(255,255,255,0.1);">
            <div style="color: #00ffcc; font-size: 18px; font-weight: bold;">🧠 AKYLMAN AI ({level_name})</div>
            <div style="color: white; font-size: 50px; font-weight: 900; margin: 10px 0;">AKYLMAN</div>
            <div style="color: #ccc; letter-spacing: 4px; font-size: 11px;">PRESIDENTIAL SCHOOL</div>
        </div>
        ''', unsafe_allow_html=True)
