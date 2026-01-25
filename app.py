import streamlit as st
from brain import AkylmanBrain
from interface import AkylmanUI
from storage import AkylmanStorage
from effects import AkylmanFX

if "messages" not in st.session_state:
    st.session_state.messages = []

if "init" not in st.session_state:
    st.session_state.brain = AkylmanBrain()
    st.session_state.ui = AkylmanUI()
    st.session_state.db = AkylmanStorage()
    st.session_state.fx = AkylmanFX()
    st.session_state.init = True

ui, brain, db, fx = st.session_state.ui, st.session_state.brain, st.session_state.db, st.session_state.fx
ui.apply_styles()

with st.sidebar:
    st.markdown("### ⚙️ УПРАВЛЕНИЕ")
    password = st.text_input("Пароль для Pro:", type="password")
    
    level_map = {"🚀 Быстрая (Flash)": "Fast", "🧠 Думающая": "Thinking", "💎 Pro": "Pro", "🔥 Plus": "Plus"}
    
    if password == "AKYLMAN-PRO":
        st.success("✅ ДОСТУП АКТИВИРОВАН")
        available_levels = list(level_map.keys())
    else:
        available_levels = ["🚀 Быстрая (Flash)", "🧠 Думающая"]
    
    selected_ver = st.selectbox("Версия АКЫЛМАНА:", available_levels)
    level = level_map[selected_ver]
    subject = st.selectbox("Выбери урок:", ["Математика", "English", "IT", "Физика"])

    st.markdown("---")
    st.subheader("Материалы")
    uploaded_files = st.file_uploader(
        "Загрузить фото или PDF", 
        type=["pdf", "png", "jpg", "jpeg", "txt"], 
        accept_multiple_files=True,
        key="file_manager" # Добавил ключ для стабильности
    )
    
    if st.button("🗑 Очистить чат"):
        st.session_state.messages = []
        st.rerun()

ui.render_centered_logo(level)

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

if prompt := st.chat_input("Напишите АКЫЛМАНУ..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        res = ""
        box = st.empty()
        try:
            for chunk in brain.generate_response_stream(prompt, level, subject):
                if isinstance(chunk, str):
                    res += chunk
                    box.markdown(res + "▌")
            st.session_state.messages.append({"role": "assistant", "content": res})
            box.markdown(res)
        except Exception as e:
            msg = "Извините, лимит исчерпан. Подождите немного! 😊" if "429" in str(e) else f"Ошибка: {e}"
            box.markdown(msg)
