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
    
    level = level_map[st.selectbox("Версия АКЫЛМАНА:", available_levels)]
    subject = st.selectbox("Выбери урок:", ["Математика", "English", "IT", "Физика"])

ui.render_centered_logo(level)

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Напишите АКЫЛМАНУ..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        full_res = ""
        box = st.empty()
        
        try:
            for chunk in brain.generate_response_stream(prompt, level, subject):
                if isinstance(chunk, str):
                    full_res += chunk
                    box.markdown(full_res + "▌")

            st.session_state.messages.append({"role": "assistant", "content": full_res})
            box.markdown(full_res)
            
        except Exception as e:
            if "limit" in str(e).lower() or "429" in str(e):
                error_msg = "Извините, на сегодня мои лимиты исчерпаны. Пожалуйста, подождите немного или попробуйте позже. Я обязательно помогу вам, как только отдохну! 😊"
            else:
                error_msg = f"Произошла ошибка: {str(e)}. Попробуйте обновить страницу."
            
            box.markdown(error_msg)
            st.session_state.messages.append({"role": "assistant", "content": error_msg})
