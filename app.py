import streamlit as st
import time
from brain import AkylmanBrain
from interface import AkylmanUI

if "messages" not in st.session_state:
    st.session_state.messages = []
if "auth" not in st.session_state:
    st.session_state.auth = False

ui = AkylmanUI()
brain = AkylmanBrain()
ui.apply_styles()

with st.sidebar:
    st.markdown("### ⊞ УПРАВЛЕНИЕ")
    
    if not st.session_state.auth:
        pw = st.text_input("Пароль для Pro:", type="password")
        if pw == "AKYLMAN-PRO":
            st.session_state.auth = True
            st.balloons()
            time.sleep(1)
            st.rerun()
    else:
        st.success("Доступ активен ✅")
        if st.button("Выйти"):
            st.session_state.auth = False
            st.rerun()

    levels = {"🚀 Быстрая (Flash)": "Fast", "🧠 Думающая": "Thinking", "💎 Plus (Умная)": "Plus"}
    active_lvls = list(levels.keys()) if st.session_state.auth else ["🚀 Быстрая (Flash)", "🧠 Думающая"]
    
    ver = st.selectbox("Версия АКЫЛМАНА:", active_lvls)
    level = levels[ver]

    subject = st.selectbox("Выбери урок:", [
        "Математика", 
        "English", 
        "ICT", 
        "Физика", 
        "Биология", 
        "История"
    ])

    st.markdown("---")
    st.subheader("Материалы")
    st.file_uploader("Загрузить файлы", type=["pdf", "png", "jpg"], accept_multiple_files=True)
    
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
                res += chunk
                box.markdown(res + "▌")
            st.session_state.messages.append({"role": "assistant", "content": res})
            box.markdown(res)
        except Exception as e:
            msg = "Лимит исчерпан. Подождите немного! 😊" if "429" in str(e) else f"Ошибка: {e}"
            box.markdown(msg)
