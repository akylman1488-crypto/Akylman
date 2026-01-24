import streamlit as st
from brain import AkylmanBrain
from interface import AkylmanUI
from storage import AkylmanStorage
from effects import AkylmanFX
from PyPDF2 import PdfReader

# 1. Инициализация систем
if "init" not in st.session_state:
    st.session_state.brain = AkylmanBrain()
    st.session_state.ui = AkylmanUI()
    st.session_state.db = AkylmanStorage()
    st.session_state.fx = AkylmanFX()
    st.session_state.session_id = None
    st.session_state.init = True

ui, brain, db, fx = st.session_state.ui, st.session_state.brain, st.session_state.db, st.session_state.fx

# 2. Настройка интерфейса
ui.apply_styles()
fx.inject_particles()
ui.render_header("AKYLMAN PRO", "PRESIDENTIAL AI SYSTEM")

# 3. Боковая панель
with st.sidebar:
    st.header("CORE CONFIG")
    subject = st.selectbox("SUBJECT", ["Математика", "English", "История", "IT"])
    ui.render_level_selector_style()
    level = st.radio("INTELLIGENCE LEVEL", ["Fast", "Thinking", "Pro", "Plus"])
    
    if st.session_state.session_id is None:
        st.session_state.session_id = db.create_session(subject, level)
    
    with st.expander("KNOWLEDGE UPLOAD"):
        files = st.file_uploader("Upload PDF", accept_multiple_files=True)
        if files:
            for f in files:
                pdf = PdfReader(f)
                text = "".join([p.extract_text() for p in pdf.pages])
                if db.save_document(f.name, text):
                    fx.show_toast(f"File {f.name} indexed!", "success")

# 4. Чат и логика
history = db.get_chat_history(st.session_state.session_id)
for m in history:
    with st.chat_message(m["role"]): st.markdown(m["content"])

if prompt := st.chat_input("Enter command..."):
    db.save_message(st.session_state.session_id, "user", prompt)
    with st.chat_message("user"): st.markdown(prompt)
    
    with st.chat_message("assistant"):
        ui.render_message_loader()
        context = db.get_full_knowledge_context()
        full_res = ""
        placeholder = st.empty()
        
        for chunk in brain.generate_response_stream(prompt, level, subject, context):
            full_res += chunk
            placeholder.markdown(full_res + "▌")
        
        placeholder.markdown(full_res)
        db.save_message(st.session_state.session_id, "assistant", full_res, level)
        fx.play_audio("message")
        fx.scroll_to_bottom()
