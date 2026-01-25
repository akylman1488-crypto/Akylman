import streamlit as st

class AkylmanUI:
    def apply_styles(self):
        st.markdown("""
        <style>
        /* 1. БЕЛЫЙ ФОН ВСЕГО САЙТА */
        .stApp {
            background-image: url("https://abrakadabra.fun/uploads/posts/2022-02/1643881418_3-abrakadabra-fun-p-belii-fon-bez-nichego-na-ves-5.jpg");
            background-size: cover;
            background-attachment: fixed;
        }

        /* 2. ВЕРХНЯЯ ПОЛОСА: Белая */
        header[data-testid="stHeader"] {
            background-color: #ffffff !important;
        }

        /* 3. БОКОВАЯ ПАНЕЛЬ (Синяя зона на чертеже) */
        [data-testid="stSidebar"] {
            background-color: #f0f2f6 !important; /* Светло-серый фон */
            border-right: 2px solid #000000;
        }

        /* ТЕКСТ В ПАНЕЛИ: СДЕЛАЛ ЧЕРНЫМ */
        [data-testid="stSidebar"] p, 
        [data-testid="stSidebar"] span, 
        [data-testid="stSidebar"] label, 
        [data-testid="stSidebar"] h3 {
            color: #000000 !important;
            font-weight: bold !important;
        }

        /* ПОЛЯ ВВОДА В ПАНЕЛИ */
        [data-testid="stSidebar"] input, 
        [data-testid="stSidebar"] select,
        [data-testid="stSidebar"] div[data-baseweb="select"] {
            background-color: #ffffff !important;
            color: #000000 !important;
            border: 1px solid #000000 !important;
        }

        /* Кнопки Очистить/Выйти */
        [data-testid="stSidebar"] button {
            background-color: #000000 !important;
            color: #ffffff !important;
            border-radius: 8px !important;
        }

        /* 4. ОСНОВНОЙ ЧАТ */
        [data-testid="stChatMessage"] {
            background-color: #ffffff !important;
            border: 1px solid #ddd !important;
            border-radius: 15px !important;
        }
        [data-testid="stChatMessage"] p { color: #000000 !important; }

        /* Поле ввода внизу */
        .stChatInputContainer {
            border: 2px solid #000000 !important;
            background: #ffffff !important;
        }
        </style>
        """, unsafe_allow_html=True)

    def render_centered_logo(self, level_name):
        st.markdown(f'''
        <div style="text-align: center; background: rgba(255,255,255,0.9); padding: 20px; border-radius: 20px; border: 1px solid #000; margin-bottom: 20px;">
            <div style="color: #000; font-size: 18px;">🧠 AKYLMAN AI ({level_name})</div>
            <div style="color: #000; font-size: 40px; font-weight: 900;">AKYLMAN</div>
            <div style="color: #666; letter-spacing: 5px; font-size: 10px;">PRESIDENTIAL SCHOOL</div>
        </div>
        ''', unsafe_allow_html=True)
