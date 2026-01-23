import streamlit as st
import google.generativeai as genai
import datetime
import pandas as pd
from PyPDF2 import PdfReader
from duckduckgo_search import DDGS

st.set_page_config(page_title="AKYLMAN AI", page_icon="🧠", layout="wide")

st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://cdn.dribbble.com/userupload/12560411/file/original-cb85895710c2c26fabc3ee05308be2b0.jpg?resize=1600x1200");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    .stApp h1 {
        color: white !important;
        text-shadow: 2px 2px 8px #000 !important;
    }
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

try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
except Exception as e:
    st.error(f"Ошибка API: {e}")

if "messages" not in st.session_state:
    st.session_state.messages = []
if "doc_context" not in st.session_state:
    st.session_state.doc_context = ""

with st.sidebar:
    st.title("🎛️ ПАНЕЛЬ УПРАВЛЕНИЯ")
    uploaded_file = st.file_uploader("Материалы для учебы", type=["pdf", "txt", "csv"])
    if uploaded_file:
        try:
            if uploaded_file.type == "application/pdf":
                reader = PdfReader(uploaded_file)
                st.session_state.doc_context = "".join([p.extract_text() for p in reader.pages])
            elif uploaded_file.type == "text/csv":
                df = pd.read_csv(uploaded_file)
                st.session_state.doc_context = df.head(50).to_string()
            else:
                st.session_state.doc_context = uploaded_file.read().decode("utf-8")
            st.success("АКЫЛМАН изучил файлы.")
        except Exception as e:
            st.error(f"Ошибка: {e}")
    
    if st.button("🗑️ Очистить всё"):
        st.session_state.messages = []
        st.session_state.doc_context = ""
        st.rerun()

st.title("🧠 АКЫЛМАН AI")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Напишите АКЫЛМАНУ..."):
    st.session_state.messages.append({"role": "user", "content":
