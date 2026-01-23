import streamlit as st
import pandas as pd
from PyPDF2 import PdfReader
from openai import OpenAI
from duckduckgo_search import DDGS
import urllib.parse
import time
import datetime

st.set_page_config(page_title="AKYLMAN ULTIMATE AI", page_icon="🧠", layout="wide")

st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://cdn.dribbble.com/userupload/12560411/file/original-cb85895710c2c26fabc3ee05308be2b0.jpg?resize=1600x1200");
        background-size: cover; background-position: center; background-attachment: fixed;
    }
    .stApp h1 { color: white !important; text-shadow: 4px 4px 15px #000 !important; font-family: 'Arial Black', sans-serif; }
    [data-testid="stChatMessage"] { background-color: rgba(15, 15, 15, 0.8) !important; border-radius: 25px !important; border: 1px solid #ff4b4b !important; }
    [data-testid="stChatMessage"] p, .stMarkdown, span, li { color: #f0f0f0 !important; font-size: 1.1rem !important; }
    [data-testid="stSidebar"] { background: rgba(255, 255, 255, 0.98) !important; border-right: 3px solid #ff4b4b !important; }
    .stChatInputContainer { padding-bottom: 20px !important; }
    .stButton>button { background: linear-gradient(45deg, #1e1e1e, #ff4b4b); color: white; border: none; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

if "messages" not in st.session_state: st.session_state.messages = []
if "doc_context" not in st.session_state: st.session_state.doc_context = ""
if "is_pro" not in st.session_state: st.session_state.is_pro = False
if "counter" not in st.session_state: st.session_state.counter = 0

try:
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=st.secrets["OPENROUTER_API_KEY"],
    )
except:
    st.error("Критическая ошибка: Проверь OPENROUTER_API_KEY в Secrets!")

with st.sidebar:
    st.image("https://img.icons8.com/fluency/144/artificial-intelligence.png", width=100)
    st.title("УПРАВЛЕНИЕ")

    with st.expander("🔑 АКЦИВАЦИЯ PRO"):
        pwd = st.text_input("Пароль:", type="password")
        if pwd == "1234":
            st.session_state.is_pro = True
            st.success("PRO РЕЖИМ ВКЛЮЧЕН")
    
    st.divider()

if st.session_state.is_pro:
        v_mode = st.selectbox("Версия интеллекта:", ["💎 Ультра (Llama 3.1)", "🚀 Скорость (Mistral)", "⚡ Флэш (Gemini)"])
        model_id = {
            "💎 Ультра (Llama 3.1)": "meta-llama/llama-3.1-8b-instruct:free",
            "🚀 Скорость (Mistral)": "mistralai/mistral-7b-instruct:free",
            "⚡ Флэш (Gemini)": "google/gemini-flash-1.5-8b"
        }[v_mode]
    else:
        model_id = "mistralai/mistral-7b-instruct:free"
        st.warning("Доступен только базовый интеллект")
    
    st.divider()

with st.expander("📁 БАЗА ЗНАНИЙ"):
        up_file = st.file_uploader("Загрузи PDF/TXT для АКЫЛМАНА", type=["pdf", "txt"])
        if up_file:
            try:
                if up_file.type == "application/pdf":
                    reader = PdfReader(up_file)
                    st.session_state.doc_context = " ".join([p.extract_text() for p in reader.pages])
                else:
                    st.session_state.doc_context = up_file.read().decode()
                st.success("Файл успешно изучен!")
            except:
                st.error("Ошибка при чтении файла")

with st.expander("🎨 СТУДИЯ РИСОВАНИЯ"):
        style = st.selectbox("Стиль:", ["Anime", "Cyberpunk", "Photorealistic", "Digital Art", "Sketch"])
        aspect = st.radio("Формат:", ["1:1", "16:9"])
    
    if st.button("🗑️ ОЧИСТИТЬ ВСЁ"):
        st.session_state.messages = []
        st.session_state.doc_context = ""
        st.rerun()

st.title("🧠 AKYLMAN ULTIMATE AI")

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])
        if "img" in m:
            st.image(m["img"], use_container_width=True)

if prompt := st.chat_input("Спроси у АКЫЛМАНА..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.markdown(prompt)

    with st.chat_message("assistant"):
        if "нарисуй" in prompt.lower():
            # Логика рисования
            subject = prompt.lower().replace("нарисуй", "").strip()
            draw_prompt = f"{subject}, {style} style, masterpiece, high quality"
            url = f"https://pollinations.ai/p/{urllib.parse.quote(draw_prompt)}?width=1024&height=1024&nologo=true"
            st.image(url, caption=f"Результат: {subject}")
            st.session_state.messages.append({"role": "assistant", "content": f"Готово! Рисунок на тему: {subject}", "img": url})
        else:
            web_data = ""
            if any(k in prompt.lower() for k in ["найди", "новости", "кто"]):
                try:
                    search = DDGS().text(prompt, max_results=3)
                    web_data = "\nWEB-ИНФО:\n" + "\n".join([s['body'] for s in search])
                except: pass

            full_instr = f"Ты - АКЫЛМАН. Помогай Исануру. Текст из файлов: {st.session_state.doc_context[:3000]}. {web_data}"
            
            res_area = st.empty(); full_text = ""
            try:
                resp = client.chat.completions.create(
                    model=model_id,
                    messages=[{"role": "system", "content": full_instr}, {"role": "user", "content": prompt}],
                    stream=True
                )
                for chunk in resp:
                    if chunk.choices[0].delta.content:
                        full_text += chunk.choices[0].delta.content
                        res_area.markdown(full_text + "▌")
                res_area.markdown(full_text)
                st.session_state.messages.append({"role": "assistant", "content": full_text})
                st.session_state.counter += len(full_text.split())
            except Exception as e:
                st.error("Упс! Эта модель сейчас спит. Переключись на 'Скорость (Mistral)' в боковом меню.")

st.divider()
c1, c2, c3 = st.columns(3)
with c1: st.info(f"📍 Статус: {'PRO' if st.session_state.is_pro else 'FREE'}")
with c2: st.info(f"📊 Слов сегодня: {st.session_state.counter}")
with c3: st.info(f"📅 Дата: {datetime.date.today()}")
