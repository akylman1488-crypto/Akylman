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

    level_map = {
        "🚀 Быстрая (Flash)": "Fast", 
        "🧠 Думающая": "Thinking", 
        "💎 Pro": "Pro", 
        "🔥 Plus": "Plus"
    }

    if password == "":
        st.info("Введите пароль для Pro версий")
        available_levels = ["🚀 Быстрая (Flash)", "🧠 Думающая"]
    elif password == "AKYLMAN-PRO":
        st.success("✅ ДОСТУП АКТИВИРОВАН")
        available_levels = list(level_map.keys())
        fx.trigger_confetti() # Если хочешь эффект конфетти при успехе
    else:
        st.error("❌ НЕ УДАЛОСЬ: Неверный пароль")
        available_levels = ["🚀 Быстрая (Flash)", "🧠 Думающая"]
    
    st.markdown("---")

    selected_ver = st.selectbox("Версия АКЫЛМАНА:", available_levels)
    level = level_map[selected_ver]

    subject = st.selectbox("Выбери урок:", ["Математика", "English", "Информатика", "Физика", "История"])

    st.markdown("---")
    st.subheader("Материалы")
    uploaded_file = st.file_uploader("Drag and drop file here", type=["pdf", "txt", "csv"])
    
    if st.button("🗑 Очистить чат"):
        db.clear_session_memory(st.session_state.sid)
        st.rerun()
