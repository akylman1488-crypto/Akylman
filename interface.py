import streamlit as st

class AkylmanUI:
    def apply_styles(self):
        st.markdown("""
        <style>
        .stApp {
            background-image: url("https://abrakadabra.fun/uploads/posts/2022-02/1643881418_3-abrakadabra-fun-p-belii-fon-bez-nichego-na-ves-5.jpg");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }

        [data-testid="stSidebar"] {
            background-color: #f0f2f6 !important;
            border-right: 1px solid #ddd;
        }

        .logo-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            background: rgba(0, 0, 0, 0.6);
            padding: 30px;
            border-radius: 25px;
            margin: 20px auto;
            max-width: 600px;
        }
        
        .logo-text {
            color: white;
            font-size: 50px;
            font-weight: 900;
            text-shadow: 2px 2px 15px #000;
        }

        /* ЧЕРНЫЕ КРАЯ ДЛЯ ПОЛЯ ВВОДА */
        .stChatInputContainer {
            border: 3px solid #000000 !important;
            border-radius: 15px !important;
            background: white !important;
        }

        .stChatInputContainer textarea {
            color: black !important;
        }
        </style>
        """, unsafe_allow_html=True)

    def render_centered_logo(self, level_name):
        st.markdown(f"""
        <div class="logo-container">
            <div style="color: #00ffcc; font-size: 25px;">🧠 AKYLMAN AI ({level_name})</div>
            <div class="logo-text">AKYLMAN</div>
            <div style="color: #ccc; letter-spacing: 5px;">PRESIDENTIAL SCHOOL</div>
        </div>
        """, unsafe_allow_html=True)
