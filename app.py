import streamlit as st
import time
import datetime
from interface import AkylmanUI

st.set_page_config(page_title="AKYLMAN AI", page_icon="🧠", layout="wide")

ui = AkylmanUI()
ui.apply_styles()

if "messages" not in st.session_state:
    st.session_state.messages = []
if "plus_unlocked" not in st.session_state:
    st.session_state.plus_unlocked = False

if "pro_count" not in st.session_state:
    st.session_state.pro_count = 0
if "pro_limit_time" not in st.session_state:
    st.session_state.pro_limit_time = None

with st.sidebar:
    # 1. ПОЛЕ ПАРОЛЯ (Вверху, черный круг на скрине)
    st.title("🔐 Доступ")
    password_input = st.text_input("Введите пароль для Plus", type="password")
    
    if password_input:
        if password_input == "7777": # Твой пароль
            st.session_state.plus_unlocked = True
            st.success("✅ Пароль верный!")
        else:
            st.error("❌ Пароль неверен")

    st.write("---")

    available_versions = ["Думающая", "Быстрая", "PRO"]
    if st.session_state.plus_unlocked:
        available_versions.append("PLUS")
        
    version = st.selectbox("Версия АКЫЛМАНА", available_versions)

    lesson = st.selectbox("Предмет", ["English", "ICT", "Математика", "Физика", "История", "Биология"])


    st.write("Материалы:")
    st.file_uploader("", type=["pdf", "docx", "txt"])
    
    if st.button("🗑️ Очистить"):
        st.session_state.messages = []
        st.rerun()

ui.render_header(version)

if version == "PRO":
    if st.session_state.pro_limit_time:
        elapsed = datetime.datetime.now() - st.session_state.pro_limit_time
        if elapsed.total_seconds() < 36000: # 10 часов в секундах
            hours_left = 10 - int(elapsed.total_seconds() / 3600)
            st.error(f"⛔ Лимит версии PRO исчерпан (5 вопросов). Доступ откроется через {hours_left} ч.")
            st.stop()
        else:
            st.session_state.pro_count = 0
            st.session_state.pro_limit_time = None

    if st.session_state.pro_count >= 5:
        st.session_state.pro_limit_time = datetime.datetime.now()
        st.error("⛔ Вы задали 5 вопросов. PRO версия заблокирована на 10 часов.")
        st.stop()

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt := st.chat_input("Напиши свой вопрос..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    if version == "PRO":
        st.session_state.pro_count += 1

    with st.chat_message("assistant"):
        response_text = f"Это ответ версии **{version}** по предмету **{lesson}**. (Вопрос: {prompt})"
    
        display_placeholder = st.empty()
        full_res = ""
        for char in response_text:
            full_res += char
            time.sleep(0.02)
            display_placeholder.write(full_res + "▌")
        display_placeholder.write(full_res)
        
    st.session_state.messages.append({"role": "assistant", "content": full_res})

    if version == "PRO" and st.session_state.pro_count >= 5:
        time.sleep(2)
        st.rerun()
