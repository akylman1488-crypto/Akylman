import streamlit as st
import time
import requests 
from interface import AkylmanUI

st.set_page_config(page_title="AKYLMAN AI", page_icon="🧠")

ui = AkylmanUI()
ui.apply_styles()

if "history" not in st.session_state: st.session_state.history = []
if "msg_count" not in st.session_state: st.session_state.msg_count = 0
if "is_plus" not in st.session_state: st.session_state.is_plus = False
if "modal_open" not in st.session_state: st.session_state.modal_open = False

with st.sidebar:
    st.title("Settings")

    version = st.selectbox("Версия АКЫЛМАНА", ["PRO", "PLUS"])
    if version == "PLUS" and not st.session_state.is_plus:
        st.session_state.modal_open = True

    lesson = st.selectbox("Предмет", ["English", "ICT", "Математика", "Физика", "История", "Биология"])
    model_choice = st.selectbox("Нейросеть", ["GPT-4o", "Claude 3.5", "Llama 3.1"])
    
    st.markdown("---")
    st.write("📁 Загрузить файлы:")
    st.file_uploader("", type=["pdf", "txt", "docx"])
    
    if st.button("🗑️ Сбросить всё"):
        st.session_state.history = []
        st.session_state.msg_count = 0
        st.rerun()

if st.session_state.modal_open:
    st.markdown('<div class="password-popup">', unsafe_allow_html=True)
    if st.button("✖️", help="Закрыть"): 
        st.session_state.modal_open = False
        st.rerun()
    st.subheader("🔐 Доступ к PLUS")
    user_pwd = st.text_input("Введите секретный код", type="password")
    if st.button("АКТИВИРОВАТЬ"):
        if user_pwd == "7777": # Твой секретный пароль
            st.session_state.is_plus = True
            st.session_state.modal_open = False
            st.balloons()
            st.success("PLUS статус активирован!")
            time.sleep(2)
            st.rerun()
        else:
            st.error("Неверный код доступа")
    st.markdown('</div>', unsafe_allow_html=True)

ui.render_header(version)

if version == "PRO" and st.session_state.msg_count >= 5:
    st.error("🚫 Лимит бесплатных вопросов исчерпан. Ждите 12 часов или используйте PLUS.")
    st.stop()

for chat in st.session_state.history:
    with st.chat_message(chat["role"]):
        st.markdown(chat["content"])

if prompt := st.chat_input("Напиши свой вопрос..."):
    st.session_state.history.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        system_prompt = f"Ты - Akylman AI, эксперт по предмету {lesson}. Отвечай профессионально."

        fake_response = f"Анализирую ваш вопрос по {lesson}... Использую модель {model_choice}. Вот ваш ответ: [Здесь будет ответ от API]"
        
        for chunk in fake_response.split():
            full_response += chunk + " "
            time.sleep(0.05)
            message_placeholder.markdown(full_response + "▌")
        
        message_placeholder.markdown(full_response)
    
    st.session_state.history.append({"role": "assistant", "content": full_response})
   
    if version == "PRO":
        st.session_state.msg_count += 1
