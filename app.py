import streamlit as st
from brain import AkylmanBrain
from interface import AkylmanUI
from storage import AkylmanStorage
from effects import AkylmanFX
from PyPDF2 import PdfReader

st.set_page_config(page_title="AKYLMAN PRO", layout="wide")

if "brain" not in st.session_state:
    st.session_state.brain = AkylmanBrain()
    st.session_state.ui = AkylmanUI()
    st.session_state.db = AkylmanStorage()
    st.session_state.fx = AkylmanFX()
    st.session_state.sid = None

ui = st.session_state.ui
brain = st.session_state.brain
db = st.session_state.db
fx = st.session_state.fx

ui.apply_styles()
fx.inject_particles()

st.title("AKYLMAN PRO")

with st.sidebar:
    subject = st.selectbox("SUBJECT", ["Математика", "English", "IT"])
    level = st.radio("LEVEL", ["Fast", "Thinking", "Pro", "Plus"])
    if not st.session_state.sid:
        st.session_state.sid = db.create_session(subject, level)
    
    files = st.file_uploader("Upload PDF", accept_multiple_files=True)
    if files:
        for f in files:
            reader = PdfReader(f)
            text = "".join([p.extract_text() for p in reader.pages])
            db.save_document(f.name, text)

hist = db.get_chat_history(st.session_state.sid)
for m in hist:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

if p := st.chat_input("Write command..."):
    db.save_message(st.session_state.sid, "user", p)
    with st.chat_message("user"):
        st.markdown(p)

    with st.chat_message("assistant"):
        full_res = ""
        placeholder = st.empty()
        ctx = db.get_full_knowledge_context()
        
        # Исправленный цикл для вывода только текста
        for chunk in brain.generate_response_stream(p, level, subject, ctx):
            if isinstance(chunk, str):
                full_res += chunk
                placeholder.markdown(full_res + "▌")
        
        placeholder.markdown(full_res)
        db.save_message(st.session_state.sid, "assistant", full_res, level)
