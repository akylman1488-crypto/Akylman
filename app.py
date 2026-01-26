import streamlit as st
import time
from interface import AkylmanUI

ui = AkylmanUI()
ui.apply_styles()

if "messages_count" not in st.session_state:
    st.session_state.messages_count = 0
if "plus_unlocked" not in st.session_state:
    st.session_state.plus_unlocked = False
if "show_password_box" not in st.session_state:
    st.session_state.show_password_box = False

with st.sidebar:
    st.title("Управление")

    version = st.selectbox("Версия АКЫЛМАНА", ["PRO", "PLUS"])

    if version == "PLUS" and not st.session_state.plus_unlocked:
        st.session_state.show_password_box = True
    else:
        st.session_state.show_password_box = False

    lesson = st.selectbox("Выбор урока", ["English", "ICT", "Математика", "Физика", "История", "Биология"])

    model = st.selectbox("Модель", ["GPT-4o", "Claude 3.5", "Gemini 1.5 Pro", "Llama 3.1"])

    st.write("Добавить материалы:")
    st.file_uploader("", type=["pdf", "txt", "docx"])
    
    if st.button("🗑️ Очистить чат"):
        st.session_state.messages = []
        st.rerun()

if st.session_state.show_password_box:
    with st.container():
        st.markdown('<div class="password-popup">', unsafe_allow_html=True)

        cols = st.columns([0.9, 0.1])
        if cols[1].button("✖️"):
            st.session_state.show_password_box = False
            st.rerun()
            
        st.subheader("Введите пароль для PLUS")
        pwd = st.text_input("Пароль", type="password", key="plus_pwd")
        
        if st.button("Войти"):
            if pwd == "1234":
                st.session_state.plus_unlocked = True
                st.balloons() 
                st.success("Пароль верный! Доступ открыт.")
                time.sleep(2)
                st.rerun()
            else:
                st.error("Пароль не правильный!")
        
        st.markdown('</div>', unsafe_allow_html=True)

ui.render_centered_logo(version)

if version == "PRO" and st.session_state.messages_count >= 5:
    st.error("Лимит версии PRO истёк. Обновление через 12 часов.")
    st.stop()

if prompt := st.chat_input("Спроси у Акылмана..."):
    st.session_state.messages_count += 1
    st.chat_message("user").write(prompt)
    st.chat_message("assistant").write(f"Ответ по предмету {lesson}...")
