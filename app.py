import streamlit as st
from brain import AkylmanBrain
from interface import AkylmanInterface
from storage import AkylmanStorage
from effects import AkylmanEffects
from PyPDF2 import PdfReader

if "brain" not in st.session_state:
    st.session_state.brain = AkylmanBrain()
if "ui" not in st.session_state:
    st.session_state.ui = AkylmanInterface()
if "db" not in st.session_state:
    st.session_state.db = AkylmanStorage()
if "fx" not in st.session_state:
    st.session_state.fx = AkylmanEffects()
if "doc_text" not in st.session_state:
    st.session_state.doc_text = ""

ai = st.session_state.brain
ui = st.session_state.ui
db = st.session_state.db
fx = st.session_state.fx

ui.apply_base_theme()
ui.inject_glass_morphism()
fx.particles_background()
fx.dynamic_title_pulse()

ui.render_sidebar_header()
with st.sidebar:
    subject = st.selectbox("ВЫБЕРИ ПРЕДМЕТ:", ["Математика", "English", "История", "Программирование"])
    
    with st.expander("📂 ЗАГРУЗКА ЗНАНИЙ"):
        uploaded_files = st.file_uploader("PDF/TXT файлы:", accept_multiple_files=True)
        if uploaded_files:
            combined_text = ""
            for f in uploaded_files:
                if f.name.endswith(".pdf"):
                    pdf = PdfReader(f)
                    for page in pdf.pages:
                        combined_text += page.extract_text()
                else:
                    combined_text += f.read().decode()
            st.session_state.doc_text = combined_text
            db.save_document("current_session", combined_text)
            st.success("База знаний обновлена!")

    if st.button("🧹 ОЧИСТИТЬ ИСТОРИЮ"):
        db.clear_subject_history(subject)
        fx.trigger_audio_notification("error")
        st.rerun()

ui.create_subject_tabs(subject)
stats = db.get_stats()
ui.render_info_metrics(stats['messages'], stats['subjects'], "ONLINE")

history = db.get_history(subject)
for msg in history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Введите ваш вопрос..."):
    db.save_message(subject, "user", prompt)
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        ui.animate_loading()
        fx.trigger_audio_notification("message")
        
        full_response = ""
        res_container = st.empty()

        for chunk in ai.get_ai_response(prompt, subject, st.session_state.doc_text):
            full_response += chunk
            res_container.markdown(full_response + "▌")
        
        res_container.markdown(full_response)
        db.save_message(subject, "assistant", full_response)
        
        if "тест" in prompt.lower() or "экзамен" in prompt.lower():
            fx.inject_confetti()

    fx.scroll_to_bottom()
