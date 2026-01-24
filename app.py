import streamlit as st
from brain import AkylmanBrain
from interface import AkylmanUI
from storage import AkylmanStorage
from effects import AkylmanFX

st.set_page_config(page_title="AKYLMAN PRO", layout="wide")

if "init" not in st.session_state:
    st.session_state.brain = AkylmanBrain()
    st.session_state.ui = AkylmanUI()
    st.session_state.db = AkylmanStorage()
    st.session_state.fx = AkylmanFX()
    st.session_state.init = True

ui, brain, db, fx = st.session_state.ui, st.session_state.brain, st.session_state.db, st.session_state.fx
ui.apply_styles()
fx.inject_particles()

with st.sidebar:
    st.markdown("### ⚙️ УПРАВЛЕНИЕ")
    password = st.text_input("Пароль для Pro:", type="password")
    
    level_map = {"🚀 Быстрая (Flash)": "Fast", "🧠 Думающая": "Thinking", "💎 Pro": "Pro", "🔥 Plus": "Plus"}
    
    if password == "AKYLMAN-PRO":
        st.success("✅ ДОСТУП АКТИВИРОВАН")
        fx.trigger_confetti()
        available_levels = list(level_map.keys())
    elif password == "":
        available_levels = ["🚀 Быстрая (Flash)", "🧠 Думающая"]
    else:
        st.error("❌ НЕ УДАЛОСЬ: Неверный пароль")
        available_levels = ["🚀 Быстрая (Flash)", "🧠 Думающая"]
    
    selected_ver = st.selectbox("Версия АКЫЛМАНА:", available_levels)
    level = level_map[selected_ver]
    subject = st.selectbox("Выбери урок:", ["Математика", "English", "IT", "Физика"])

ui.render_centered_logo(level)

if prompt := st.chat_input("Напишите АКЫЛМАНУ..."):
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        res = ""
        placeholder = st.empty()
        for chunk in brain.generate_response_stream(prompt, level, subject):
            res += chunk
            placeholder.markdown(res + "▌")
        placeholder.markdown(res)
