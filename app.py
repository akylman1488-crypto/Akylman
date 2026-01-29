import streamlit as st
import time
import datetime
from openai import OpenAI
from interface import AkylmanUI

st.set_page_config(page_title="AKYLMAN AI", page_icon="🧠", layout="wide")

MY_API_KEY = "sk-AIzaSyDbJ0E5vDZrGw3C14zFkZjJ0RUx1ClLXHA" 

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
    st.title("🔐 Доступ")
    pwd_input = st.text_input("Пароль для Plus", type="password")
    
    if pwd_input == "7777":
        st.session_state.plus_unlocked = True
        st.success("✅ Пароль верный")
    elif pwd_input:
        st.error("❌ Пароль неверен")

    st.write("---")
    
    version_options = ["Думающая", "Быстрая", "PRO"]
    if st.session_state.plus_unlocked:
        version_options.append("PLUS")
        
    version = st.selectbox("Версия АКЫЛМАНА", version_options)
    lesson = st.selectbox("Предмет", ["English", "ICT", "Математика", "Физика", "История", "Биология"])
    
    st.write("Материалы:")
    st.file_uploader("Загрузить файл", type=["pdf", "docx", "txt"])
    
    if st.button("🗑️ Очистить"):
        st.session_state.messages = []
        st.rerun()

ui.render_header(version)

if version == "PRO":
    if st.session_state.pro_limit_time:
        elapsed = datetime.datetime.now() - st.session_state.pro_limit_time
        if elapsed.total_seconds() < 36000:
            hours_left = 10 - int(elapsed.total_seconds() / 3600)
            st.error(f"⛔ Лимит PRO исчерпан. Доступ через {hours_left} ч.")
            st.stop()
        else:
            st.session_state.pro_count = 0
            st.session_state.pro_limit_time = None
            
    if st.session_state.pro_count >= 5:
        st.session_state.pro_limit_time = datetime.datetime.now()
        st.error("⛔ Лимит (5 вопросов) исчерпан на 10 часов.")
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
        message_placeholder = st.empty()
        full_response = ""
        
        selected_model = "gpt-4o-mini"
        if version == "Думающая" or version == "PRO" or version == "PLUS":
            selected_model = "gpt-4o"
            
        if MY_API_KEY == "sk-...":
             full_response = "⚠️ Пожалуйста, добавьте API Key в код (строка 9), чтобы я мог отвечать."
             message_placeholder.warning(full_response)
        else:
            try:
                client = OpenAI(api_key=MY_API_KEY)
                stream = client.chat.completions.create(
                    model=selected_model,
                    messages=[
                        {"role": "system", "content": f"Ты учитель по предмету {lesson}."},
                        {"role": "user", "content": prompt}
                    ],
                    stream=True
                )
                for chunk in stream:
                    if chunk.choices[0].delta.content:
                        full_response += chunk.choices[0].delta.content
                        message_placeholder.markdown(full_response + "▌")
                message_placeholder.markdown(full_response)
            except Exception as e:
                full_response = f"Ошибка: {e}"
                message_placeholder.error(full_response)

    st.session_state.messages.append({"role": "assistant", "content": full_response})
    
    if version == "PRO" and st.session_state.pro_count >= 5:
        time.sleep(1)
        st.rerun()
