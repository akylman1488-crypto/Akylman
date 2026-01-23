import streamlit as st
import google.generativeai as genai
import pandas as pd
from PyPDF2 import PdfReader
from duckduckgo_search import DDGS
import urllib.parse

st.set_page_config(page_title="AKYLMAN AI", page_icon="🧠", layout="wide")

st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://cdn.dribbble.com/userupload/12560411/file/original-cb85895710c2c26fabc3ee05308be2b0.jpg?resize=1600x1200");
        background-size: cover; background-position: center; background-attachment: fixed;
    }
    .stApp h1 { color: white !important; text-shadow: 2px 2px 8px #000 !important; }
    [data-testid="stChatMessage"] p, .stMarkdown p, .stMarkdown span, li {
        color: white !important; text-shadow: 2px 2px 4px black !important; font-weight: 500 !important;
    }
    [data-testid="stSidebar"] { background-color: rgba(255, 255, 255, 0.9) !important; }
    [data-testid="stSidebar"] * { color: #1e1e1e !important; }
    [data-testid="stChatInput"] { background-color: white !important; border-radius: 15px !important; }
    header, [data-testid="stHeader"], [data-testid="stBottom"] > div { background: transparent !important; }
    </style>
    """, unsafe_allow_html=True)

if "messages" not in st.session_state: st.session_state.messages = []
if "doc_context" not in st.session_state: st.session_state.doc_context = ""
if "is_pro" not in st.session_state: st.session_state.is_pro = False

with st.sidebar:
    st.title("🎛️ УПРАВЛЕНИЕ")
    CORRECT_PASSWORD = "1234"
    if not st.session_state.is_pro:
        pwd = st.text_input("Пароль для Pro:", type="password")
        if pwd == CORRECT_PASSWORD:
            st.session_state.is_pro = True
            st.rerun()
    if st.session_state.is_pro:
        st.success("Доступ активен ✅")
        modes = ["🚀 Быстрая (Flash)", "🤔 Думающая (Pro)", "💎 Plus (1.5 Pro)"]
        if st.button("Выйти"): st.session_state.is_pro = False; st.rerun()
    else:
        modes = ["🚀 Быстрая (Flash)"]
    
    version = st.selectbox("Версия АКЫЛМАНА:", modes)

    model_variants = {
        "🚀 Быстрая (Flash)": ["gemini-1.5-flash", "models/gemini-1.5-flash", "gemini-1.5-flash-latest"],
        "🤔 Думающая (Pro)": ["gemini-1.0-pro", "models/gemini-pro", "gemini-pro"],
        "💎 Plus (1.5 Pro)": ["gemini-1.5-pro", "models/gemini-1.5-pro", "gemini-1.5-pro-latest"]
    }
    
    uploaded_file = st.file_uploader("Материалы", type=["pdf", "txt", "csv"])
    if uploaded_file:
        try:
            if uploaded_file.type == "application/pdf":
                reader = PdfReader(uploaded_file)
                st.session_state.doc_context = "".join([p.extract_text() for p in reader.pages])
            else: st.session_state.doc_context = uploaded_file.read().decode("utf-8")
            st.success("Готов!")
        except: st.error("Ошибка файла")
    if st.button("🗑️ Очистить"):
        st.session_state.messages = []; st.session_state.doc_context = ""; st.rerun()

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

st.title(f"🧠 АКЫЛМАН AI ({version.split()[1]})")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if "img" in msg:
            st.markdown(f'<img src="{msg["img"]}" style="width:100%; border-radius:10px;">', unsafe_allow_html=True)

if prompt := st.chat_input("Напишите АКЫЛМАНУ..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.markdown(prompt)

    with st.chat_message("assistant"):
        if "нарисуй" in prompt.lower():
            clean = prompt.lower().replace("нарисуй", "").strip() or "space cat"
            url = f"https://pollinations.ai/p/{urllib.parse.quote(clean)}?width=1024&height=1024&nologo=true"
            st.markdown(f"🎨 Рисую: **{clean}**")
            st.markdown(f'<img src="{url}" style="width:100%; border-radius:10px;">', unsafe_allow_html=True)
            st.session_state.messages.append({"role": "assistant", "content": f"Рисунок: {clean}", "img": url})
        else:
            res_box = st.empty(); full_res = ""
            search_data = ""
            if any(w in prompt.lower() for w in ["найди", "новости"]):
                try:
                    results = DDGS().text(prompt, max_results=2)
                    search_data = "\nWeb:\n" + "\n".join([r['body'] for r in results])
                except: pass
            
            instr = f"Ты АКЫЛМАН. Помогай Исануру. КОНТЕКСТ: {st.session_state.doc_context[:5000]} {search_data}"
            
            success = False
            for model_name in model_variants[version]:
                try:
                    active_model = genai.GenerativeModel(model_name)
                    response = active_model.generate_content(f"{instr}\n\nUser: {prompt}", stream=True)
                    for chunk in response:
                        if chunk.text:
                            full_res += chunk.text
                            res_box.markdown(full_res + "▌")
                    res_box.markdown(full_res)
                    st.session_state.messages.append({"role": "assistant", "content": full_res})
                    success = True
                    break
                except Exception:
                    continue
            
            if not success:
                st.error(f"Версия {version} не отвечает. Попробуй обновить страницу или выбрать другую версию в меню.")
