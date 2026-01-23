import streamlit as st
import pandas as pd
from PyPDF2 import PdfReader
from openai import OpenAI
from duckduckgo_search import DDGS
import urllib.parse
import time

st.set_page_config(page_title="AKYLMAN ULTIMATE", page_icon="🧠", layout="wide")

st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://cdn.dribbble.com/userupload/12560411/file/original-cb85895710c2c26fabc3ee05308be2b0.jpg?resize=1600x1200");
        background-size: cover; background-position: center; background-attachment: fixed;
    }
    .stApp h1 { color: white !important; text-shadow: 3px 3px 10px #000 !important; font-size: 3rem !important; }
    [data-testid="stChatMessage"] { background-color: rgba(0,0,0,0.6) !important; border-radius: 20px !important; margin-bottom: 10px !important; border: 1px solid rgba(255,255,255,0.1) !important; }
    [data-testid="stChatMessage"] p, .stMarkdown, span, li { color: white !important; text-shadow: 1px 1px 3px black !important; }
    [data-testid="stSidebar"] { background-color: rgba(255, 255, 255, 0.95) !important; box-shadow: 5px 0 15px rgba(0,0,0,0.5) !important; }
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; background-color: #1e1e1e; color: white; transition: 0.3s; }
    .stButton>button:hover { background-color: #ff4b4b; border: none; }
    [data-testid="stChatInput"] { background-color: white !important; border-radius: 20px !important; border: 2px solid #ff4b4b !important; }
    </style>
    """, unsafe_allow_html=True)

if "messages" not in st.session_state: st.session_state.messages = []
if "doc_context" not in st.session_state: st.session_state.doc_context = ""
if "is_pro" not in st.session_state: st.session_state.is_pro = False
if "stats" not in st.session_state: st.session_state.stats = {"words": 0, "chars": 0}

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=st.secrets["OPENROUTER_API_KEY"],
)

with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/brain.png", width=80)
    st.title("ПАНЕЛЬ АКЫЛМАНА")
    
    with st.expander("🔐 ДОСТУП PRO"):
        pwd = st.text_input("Введи пароль:", type="password")
        if pwd == "1234":
            st.session_state.is_pro = True
            st.success("Доступ открыт!")
    
    st.divider()
    
    if st.session_state.is_pro:
        v_mode = st.selectbox("Версия ИИ:", ["Mistral (Free)", "Llama 3 (Free)", "Gemini Flash (Pro)"])
        model_id = {
            "Mistral (Free)": "mistralai/mistral-7b-instruct:free",
            "Llama 3 (Free)": "meta-llama/llama-3-8b-instruct:free",
            "Gemini Flash (Pro)": "google/gemini-flash-1.5-8b"
        }[v_mode]
    else:
        model_id = "mistralai/mistral-7b-instruct:free"
        st.info("В Pro режиме больше моделей")

    st.divider()
    
    with st.expander("🎨 СТИЛЬ РИСОВАНИЯ"):
        art_style = st.radio("Выбери стиль:", ["Реализм", "Аниме", "Киберпанк", "Масло", "3D Render"])
        quality = st.select_slider("Качество:", options=["Low", "Medium", "High"])

    with st.expander("📄 ЗАГРУЗКА ЗНАНИЙ"):
        file = st.file_uploader("Загрузить PDF/TXT", type=["pdf", "txt"])
        if file:
            if file.type == "application/pdf":
                pdf = PdfReader(file)
                st.session_state.doc_context = " ".join([p.extract_text() for p in pdf.pages])
            else:
                st.session_state.doc_context = file.read().decode()
            st.success("Знания впитаны!")

    if st.button("🗑️ ОЧИСТИТЬ ПАМЯТЬ"):
        st.session_state.messages = []
        st.session_state.doc_context = ""
        st.rerun()

st.title("🧠 AKYLMAN ULTIMATE AI")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if "img" in msg:
            st.image(msg["img"], use_container_width=True, caption="Сгенерировано АКЫЛМАНОМ")

if prompt := st.chat_input("Спроси что угодно..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.markdown(prompt)

    with st.chat_message("assistant"):
        if "нарисуй" in prompt.lower():
            with st.spinner("🎨 Художник АКЫЛМАН берется за кисть..."):
                subject = prompt.lower().replace("нарисуй", "").strip()
                full_prompt = f"{subject}, style {art_style}, highly detailed, {quality} resolution"
                url = f"https://pollinations.ai/p/{urllib.parse.quote(full_prompt)}?width=1024&height=1024&nologo=true"
                st.image(url, use_container_width=True)
                st.session_state.messages.append({"role": "assistant", "content": f"Вот твой рисунок: {subject}", "img": url})
        else:
            res_box = st.empty()
            full_res = ""
            
            # Поиск в сети
            web_info = ""
            if any(x in prompt.lower() for x in ["найди", "новости", "кто такой"]):
                try:
                    search = DDGS().text(prompt, max_results=3)
                    web_info = "\nДАННЫЕ ИЗ ИНТЕРНЕТА:\n" + "\n".join([s['body'] for s in search])
                except: pass

            system_instr = f"Ты - АКЫЛМАН. Помогай Исануру. Используй знания: {st.session_state.doc_context[:4000]}. {web_info}"
            
            try:
                stream = client.chat.completions.create(
                    model=model_id,
                    messages=[{"role": "system", "content": system_instr}, {"role": "user", "content": prompt}],
                    stream=True
                )
                for chunk in stream:
                    if chunk.choices[0].delta.content:
                        full_res += chunk.choices[0].delta.content
                        res_box.markdown(full_res + "▌")
                res_box.markdown(full_res)
                st.session_state.messages.append({"role": "assistant", "content": full_res})
                
                # Функция статистики
                st.session_state.stats["words"] += len(full_res.split())
            except Exception as e:
                st.error(f"Критическая ошибка: {e}")

st.divider()
col1, col2, col3 = st.columns(3)
with col1: st.write(f"💬 Сообщений: {len(st.session_state.messages)}")
with col2: st.write(f"📝 Слов сгенерировано: {st.session_state.stats['words']}")
with col3: st.write(f"👤 Пользователь: Исанур")
