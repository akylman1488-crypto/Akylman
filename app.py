import streamlit as st
import time
import datetime
from openai import OpenAI 
from interface import AkylmanUI

# --- НАСТРОЙКИ ---
st.set_page_config(page_title="AKYLMAN AI", page_icon="🧠", layout="wide")

# !!! ВСТАВЬ СЮДА СВОЙ API КЛЮЧ !!!
# Если ключа нет, бот будет предупреждать об этом.
MY_API_KEY = "sk-..." 

ui = AkylmanUI()
ui.apply_styles()

# --- ИНИЦИАЛИЗАЦИЯ ---
if "messages" not in st.session_state: st.session_state.messages = []
if "plus_unlocked" not in st.session_state: st.session_state.plus_unlocked = False
if "pro_count" not in st.session_state: st.session_state.pro_count = 0
if "pro_limit_time" not in st.session_state: st.session_state.pro_limit_time = None

client = None
if MY_API_KEY != "sk-AIzaSyDbJ0E5vDZrGw3C14zFkZjJ0RUx1ClLXHA":
    try:
        client = OpenAI(api_key=MY_API_KEY)
    except:
        pass

with st.sidebar:
    st.title("🔐 Доступ")
    pwd = st.text_input("Пароль для Plus", type="password")
    if pwd == "7777":
        st.session_state.plus_unlocked = True
        st.success("✅ Пароль верный")
    elif pwd:
        st.error("❌ Неверно")

    st.write("---")

    opts = ["Думающая", "Быстрая", "PRO"]
    if st.session_state.plus_unlocked: opts.append("PLUS")
    version = st.selectbox("Версия", opts)
    
    lesson = st.selectbox("Предмет", ["English", "ICT", "Математика", "Физика", "История", "Биология"])
    
    st.write("Материалы:")
    st.file_uploader("Загрузить файл", type=["pdf", "docx", "txt"]) 
    
    if st.button("🗑️ Очистить"):
        st.session_state.messages = []
        st.rerun()

ui.render_header(version)

if version == "PRO":
    if st.session_state.pro_limit_time:
        diff = datetime.datetime.now() - st.session_state.pro_limit_time
        if diff.total_seconds() < 36000: # 10 часов
            hours = 10 - int(diff.total_seconds()/3600)
            st.error(f"⛔ Лимит PRO исчерпан. Ждите {hours} ч.")
            st.stop()
        else:
            st.session_state.pro_count = 0
            st.session_state.pro_limit_time = None
            
    if st.session_state.pro_count >= 5:
        st.session_state.pro_limit_time = datetime.datetime.now()
        st.error("⛔ Вы задали 5 вопросов. Лимит PRO исчерпан на 10 часов.")
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

        ai_model = "gpt-4o-mini" # Стандартная быстрая
        if version == "Думающая": ai_model = "gpt-4o"
        elif version == "PRO": ai_model = "gpt-4o"
        elif version == "PLUS": ai_model = "gpt-4o" 

        system_msg = f"Ты Akylman AI, помощник для Presidential School. Твой предмет сейчас: {lesson}. Отвечай полезно и четко."

        if client:
            try:
                stream = client.chat.completions.create(
                    model=ai_model,
                    messages=[
                        {"role": "system", "content": system_msg},
                        {"role": "user", "content": prompt}
                    ],
                    stream=True
                )

                for chunk in stream:
                    if chunk.choices[0].delta.content is not None:
                        full_response += chunk.choices[0].delta.content
                        message_placeholder.markdown(full_response + "▌")
                
                message_placeholder.markdown(full_response)
                
            except Exception as e:
                st.error(f"Ошибка API: {e}")
                full_response = "Произошла ошибка соединения с мозгом ИИ."
        else:
            full_response = "⚠️ Чтобы я мог давать реальные ответы, вставь API Key в код (строка `MY_API_KEY`)."
            message_placeholder.warning(full_response)

    st.session_state.messages.append({"role": "assistant", "content": full_response})

    if version == "PRO" and st.session_state.pro_count >= 5:
        time.sleep(1)
        st.rerun()
