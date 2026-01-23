import streamlit as st
import google.generativeai as genai
import pandas as pd
from PyPDF2 import PdfReader
from duckduckgo_search import DDGS
import urllib.parse

st.set_page_config(page_title="AKYLMAN AI", page_icon="🧠", layout="wide")

st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://cdn.dribbble.com/userupload/12560411/file/original-cb85895710c2c26fabc3ee05308be2b0.jpg?resize=1600x1200");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    .stApp h1 { color: white !important; text-shadow: 2px 2px 8px #000 !important; }
    [data-testid="stChatMessage"] p, .stMarkdown p, .stMarkdown span, li {
        color: white !important;
        text-shadow: 2px 2px 4px black !important;
        font-weight: 500 !important;
    }
    [data-testid="stSidebar"] { background-color: rgba(255, 255, 255, 0.9) !important; }
    [data-testid="stSidebar"] * { color: #1e1e1e !important; }
    [data-testid="stChatInput"] { background-color: white !important; border-radius: 15px !important; }
    [data-testid="stChatInput"] textarea { color: black !important; }
    header, [data-testid="stHeader"], [data-testid="stBottom"] > div { background: transparent !important; }
    </style>
    """, unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []
if "doc_context" not in st.session_state:
    st.session_state.doc_context = ""
if "is_pro" not in st.session_state:
    st.session_state.is_pro = False

with st.sidebar:
    st.title("🎛️ УПРАВЛЕНИЕ")
    
    CORRECT_PASSWORD = "AKYLMAN-PRO" 
    
    if not st.session_state.is_pro:
        pwd_input = st.text_input("Пароль для Pro:", type="password")
        if pwd_input == CORRECT_PASSWORD:
            st.session_state.is_pro = True
            st.rerun()
        elif pwd_input:
            st.error("Неверный пароль")
    
    if st.session_state.is_pro:
        st.success("Доступ к Pro активен ✅")
        available_modes = ["🚀 Быстрая (Flash)", "🤔 Думающая (Pro)", "💎 Plus (1.5 Pro)"]
        if st.button("Выйти из Pro"):
            st.session_state.is_pro = False
            st.rerun()
    else:
        available_modes = ["🚀 Быстрая (Flash)"]
    
    version = st.selectbox("Версия АКЫЛМАНА:", available_modes)
    
    model_mapping = {
        "🚀 Быстрая (Flash)": "gemini-1.5-flash",
        "🤔 Думающая (Pro)": "gemini-1.0-pro",
        "💎 Plus (1.5 Pro)": "gemini-1.5-pro"
    }
    
    selected_model = model_mapping[version]

    uploaded_
