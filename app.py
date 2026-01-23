import streamlit as st
import pandas as pd
from PyPDF2 import PdfReader
from groq import Groq
from duckduckgo_search import DDGS
import urllib.parse
import time
import datetime
import random

st.set_page_config(page_title="AKYLMAN ULTIMATE PRO", page_icon="🧠", layout="wide")

if "messages" not in st.session_state: st.session_state.messages = []
if "doc_context" not in st.session_state: st.session_state.doc_context = ""
if "is_pro" not in st.session_state: st.session_state.is_pro = False
if "tokens_used" not in st.session_state: st.session_state.tokens_used = 0

st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://cdn.dribbble.com/userupload/12560411/file/original-cb85895710c2c26fabc3ee05308be2b0.jpg?resize=1600x1200");
        background-size: cover; background-position: center; background-attachment: fixed;
    }
    .stApp h1 { color: #00f2fe !important; text-shadow: 0px 0px 20px #4facfe !important; font-size: 3.5rem !important; text-align: center; }
    [data-testid="stChatMessage"] { background-color: rgba(10, 10, 20, 0.85) !important; border-left: 5px solid #00f2fe !important; border-radius: 15px !important; margin: 10px 0; }
    .stMarkdown p, li, span { color: #e0e0e0 !important; font-weight: 400; line-height: 1.6; }
    [data-testid="stSidebar"] { background: rgba(0, 0, 0, 0.9) !important; border-right: 2px solid #00f2fe !important; }
    .stChatInputContainer { background: transparent !important; }
    input { background-color: #1e1e2e !important; color: white !important; border-radius: 25px !important; border: 1px solid #00f2fe !important; }
    </style>
    """, unsafe_allow_html=True)

try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except Exception as e:
    st.error(f"Ошибка ключа Groq: {e}")

with st.sidebar:
    st.image("https://img.icons8.com/nolan/128/brainstorm.png", width=100)
    st.title("АКЫЛМАН КОНТРОЛЬ")
    
    with st.expander("👤 АККАУНТ"):
        if not st.session_state.is_pro:
            user_pwd = st.text_input("Пароль доступа:", type="password")
            if user_pwd == "1234":
                st.session_state.is_pro = True
                st.success("Доступ активен!")
                st.rerun()
        else:
            st.success("СТАТУС: ПРЕЗИДЕНТСКИЙ")

st.divider()
    if st.session_state.is_pro:
        groq_model = st.selectbox("Выбери мощность:", 
            ["Llama 3 (70B) - Самая умная", "Llama 3 (8B) - Мгновенная", "Mixtral - Для задач"])
        model_id = {
            "Llama 3 (70B) - Самая умная": "llama3-70b-8192",
            "Llama 3 (8B) - Мгновенная": "llama3-8b-8192",
            "Mixtral - Для задач": "mixtral-8x7b-32768"
        }[groq_model]
    else:
        model_id = "llama3-8b-8192"
        st.info("Вам доступна версия 8B. Введите пароль для 70B.")

with st.expander("📂 БАЗА ДАННЫХ"):
        uploaded_files = st.file_uploader("Загрузи документы (PDF/TXT):", accept_multiple_files=True)
        if uploaded_files:
            full_text = ""
            for f in uploaded_files:
                if f.name.endswith(".pdf"):
                    reader = PdfReader(f)
                    full_text += " ".join([p.extract_text() for p in reader.pages])
                else:
                    full_text += f.read().decode()
            st.session_state.doc_context = full_text
            st.success(f"Изучено символов: {len(full_text)}")

with st.expander("🎨 СТУДИЯ ДИЗАЙНА"):
        st_art = st.selectbox("Стиль ИИ:", ["Цифровое искусство", "Гиперреализм", "Аниме 4K", "Чертеж", "3D Объект"])
        st_size = st.select_slider("Детализация:", options=["Normal", "HD", "Ultra"])
    
    if st.button("🔴 СБРОС СИСТЕМЫ"):
        st.session_state.messages = []
        st.session_state.doc_context = ""
        st.rerun()

st.title("🧠 AKYLMAN ULTIMATE PRO")

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])
        if "img" in m:
            st.image(m["img"], caption="Визуализация АКЫЛМАНА")

if prompt := st.chat_input("Спроси у АКЫЛМАНА..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.markdown(prompt)

    with st.chat_message("assistant"):
        if "нарисуй" in prompt.lower():
            # Мощный генератор промптов для картинок
            clean_prompt = prompt.lower().replace("нарисуй", "").strip()
            final_art_prompt = f"{clean_prompt}, style: {st_art}, {st_size} quality, masterwork"
            img_url = f"https://pollinations.ai/p/{urllib.parse.quote(final_art_prompt)}?width=1024&height=1024&nologo=true"
            st.image(img_url)
            st.session_state.messages.append({"role": "assistant", "content": f"Создано по запросу: {clean_prompt}", "img": img_url})
        else:
            web_context = ""
            if any(word in prompt.lower() for word in ["найди", "новости", "кто"]):
                try:
                    results = DDGS().text(prompt, max_results=3)
                    web_context = "\nДАННЫЕ ИЗ СЕТИ:\n" + "\n".join([r['body'] for r in results])
                except: pass

            system_msg = f"Ты АКЫЛМАН, самый умный ИИ Президентской школы. Используй этот контекст: {st.session_state.doc_context[:8000]}. {web_context}"
            
            res_box = st.empty(); full_text = ""
            try:
                chat_completion = client.chat.completions.create(
                    messages=[{"role": "system", "content": system_msg}, {"role": "user", "content": prompt}],
                    model=model_id,
                    stream=True,
                )
                for chunk in chat_completion:
                    if chunk.choices[0].delta.content:
                        full_text += chunk.choices[0].delta.content
                        res_box.markdown(full_text + "▌")
                res_box.markdown(full_text)
                st.session_state.messages.append({"role": "assistant", "content": full_text})
                st.session_state.tokens_used += len(full_text.split())
            except Exception as e:
                st.error(f"Ошибка Groq: {e}")

st.divider()
c1, c2, c3, c4 = st.columns(4)
with c1: st.write(f"📡 Движок: Groq")
with c2: st.write(f"🧩 Модель: {model_id}")
with c3: st.write(f"📊 Слов: {st.session_state.tokens_used}")
with c4: st.write(f"⏰ {datetime.datetime.now().strftime('%H:%M')}")
