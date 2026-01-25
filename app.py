import streamlit as st
from brain import AkylmanBrain
from interface import AkylmanUI

# Инициализация
if "messages" not in st.session_state:
    st.session_state.messages = []
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

ui = AkylmanUI()
brain = AkylmanBrain()
ui.apply_styles()

# --- БОКОВАЯ ПАНЕЛЬ ---
with st.sidebar:
    st.markdown("### ⊞ УПРАВЛЕНИЕ")
    
    if not st.session_state.authenticated:
        password = st.text_input("Пароль для Pro:", type="password")
        if password == "AKYLMAN-PRO":
            st.session_state.authenticated = True
            st.rerun()
    else:
        st.markdown('<div class="status-box">Доступ активен ✅</div>', unsafe_allow_html=True)
        if st.button("Выйти"):
            st.session_state.authenticated = False
            st.rerun()

    level_map = {"🚀 Быстрая (Flash)": "Fast", "🧠 Думающая": "Thinking", "💎 Plus (Умная)": "Plus"}
    available_levels = list(level_map.keys()) if st.session_state.authenticated else ["🚀 Быстрая (Flash)", "🧠 Думающая"]

    level = level_map[st.selectbox("Версия АКЫЛМАНА:", available_levels)]
    subject = st.selectbox("Выбери урок:", ["Математика", "English", "IT", "Физика"])

    st.markdown("---")
    st.subheader("Материалы")
    st.file_uploader("Загрузить фото или PDF", type=["pdf", "png", "jpg"], accept_multiple_files=True)
    
    if st.button("🗑 Очистить чат"):
        st.session_state.messages = []
        st.rerun()

# --- ОСНОВНОЙ ЧАТ ---
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
            msg = "Лимит исчерпан. Пожалуйста, подождите немного! 😊" if "429" in str(e) else f"Ошибка: {e}"
            box.markdown(msg)
