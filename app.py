import streamlit as st
from brain import AkylmanBrain
from interface import AkylmanUI
from storage import AkylmanStorage
from effects import AkylmanFX

if "init" not in st.session_state:
    st.session_state.brain = AkylmanBrain()
    st.session_state.ui = AkylmanUI()
    st.session_state.db = AkylmanStorage()
    st.session_state.fx = AkylmanFX()
    st.session_state.init = True

ui, brain, db, fx = st.session_state.ui, st.session_state.brain, st.session_state.db, st.session_state.fx
ui.apply_styles()

with st.sidebar:
    st.markdown('<div class="sidebar-title">⚙️ УПРАВЛЕНИЕ</div>', unsafe_allow_html=True)

    password = st.text_input("Пароль для Pro:", type="password")

    level_map = {"🚀 Быстрая (Flash)": "Fast", "🧠 Думающая": "Thinking", "💎 Pro": "Pro", "🔥 Plus": "Plus"}
    if password == "AKYLMAN-PRO":
        available_levels = list(level_map.keys())
    else:
        available_levels = ["🚀 Быстрая (Flash)", "🧠 Думающая"]
    
    selected_ver = st.selectbox("Версия АКЫЛМАНА:", available_levels)
    level = level_map[selected_ver]

    subject = st.selectbox("Выбери урок:", ["Математика", "English", "Информатика", "Физика", "История"])

    st.markdown("---")
    st.subheader("Материалы")
    uploaded_file = st.file_uploader("Drag and drop file here", type=["pdf", "txt", "csv"])
    
    if st.button("🗑 Очистить"):
        st.rerun()

ui.render_centered_logo(level)

if prompt := st.chat_input("Напишите АКЫЛМАНУ..."):
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        res = ""
        box = st.empty()
        # Вызов ИИ из brain.py
        for chunk in brain.generate_response_stream(prompt, level, subject, ""):
            if isinstance(chunk, str):
                res += chunk
                box.markdown(res + "▌")
        box.markdown(res)
