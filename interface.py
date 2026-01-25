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

        /* 2. СКРЫВАЕМ ЛИШНЕЕ, НО ОСТАВЛЯЕМ КНОПКУ ПАНЕЛИ */
        /* Скрываем только элементы управления в хедере, а не весь хедер */
        header [data-testid="stHeaderActionElements"] {
            display: none;
        }
        
        /* Убираем футер (красная зона) */
        footer {
            visibility: hidden;
            height: 0px;
        }

        /* Убираем пустые отступы сверху и снизу */
        .block-container {
            padding-top: 2rem;
            padding-bottom: 0px;
        }

        /* 3. БОКОВАЯ ПАНЕЛЬ: СВЕТЛО-СЕРАЯ */
        [data-testid="stSidebar"] {
            background-color: #f0f2f6 !important;
            border-right: 1px solid #ddd;
        }
        
        [data-testid="stSidebar"] h3, 
        [data-testid="stSidebar"] p, 
        [data-testid="stSidebar"] label {
            color: #000000 !important;
            font-weight: 700 !important;
        }

        /* 4. ПОЛЯ ВВОДА (БЕЗ ЛИНИЙ) */
        [data-testid="stSidebar"] div[data-baseweb="input"],
        [data-testid="stSidebar"] div[data-baseweb="select"] > div {
            background-color: #ffffff !important;
            border: none !important;
            border-radius: 10px !important;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05) !important;
        }

        [data-testid="stSidebar"] input, 
        [data-testid="stSidebar"] div[data-baseweb="select"] span {
            color: #000000 !important; 
            font-weight: 500 !important;
        }

        /* 5. ЧАТ (БЕЛЫЙ ТЕКСТ) */
        [data-testid="stChatMessage"] {
            background-color: rgba(0, 0, 0, 0.75) !important;
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 15px;
        }
        [data-testid="stChatMessage"] p, 
        [data-testid="stChatMessage"] div {
            color: #ffffff !important;
        }

        /* Кнопки */
        .stButton>button {
            background-color: #ffffff !important;
            color: #000000 !important;
            border: none !important;
        }

        /* Инпут внизу */
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
