import streamlit as st
import pandas as pd
from PyPDF2 import PdfReader
from groq import Groq
from duckduckgo_search import DDGS
import urllib.parse
import time
import datetime
import base64

st.set_page_config(page_title="AKYLMAN ULTIMATE", page_icon="🧠", layout="wide")

if "messages" not in st.session_state: st.session_state.messages = []
if "doc_context" not in st.session_state: st.session_state.doc_context = ""
if "is_pro" not in st.session_state: st.session_state.is_pro = False
if "words" not in st.session_state: st.session_state.words = 0

try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except Exception as e:
    st.error("Ошибка ключа Groq в Secrets!")

st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), url("https://images.unsplash.com/photo-1614728263952-84ea256f9679?auto=format&fit=crop&w=1920&q=80");
    background-size: cover;
}
.stApp h1 { color: #00d2ff !important; text-shadow: 2px 2px 10px #000; text-align: center; }
[data-testid="stChatMessage"] { background: rgba(255,255,255,0.05) !important; border-radius: 15px; border-left: 5px solid #00d2ff; }
[data-testid="stSidebar"] { background: rgba(255,255,255,0.95) !important; border-right: 2px solid #00d2ff; }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.title("🛡️ ЦЕНТР УПРАВЛЕНИЯ")
    with st.expander("🔑 PRO ДОСТУП"):
        pass_input = st.text_input("Пароль:", type="password")
        if pass_input == "1234":
            st.session_state.is_pro = True
            st.success("РЕЖИМ PRO ВКЛЮЧЕН")

st.divider()
    if st.session_state.is_pro:
        m_choice = st.selectbox("Модель:", ["Llama 3 (70B)", "Llama 3 (8B)", "Mixtral 8x7b"])
        m_id = {"Llama 3 (70B)": "llama3-70b-8192", "Llama 3 (8B)": "llama3-8b-8192", "Mixtral 8x7b": "mixtral-8x7b-32768"}[m_choice]
    else:
        m_id = "llama3-8b-8192"
        st.info("Вам доступна быстрая версия 8B")

with st.expander("📚 БАЗА PDF"):
        files = st.file_uploader("Загрузи учебники:", accept_multiple_files=True, type=['pdf', 'txt'])
        if files:
            full_txt = ""
            for f in files:
                if f.name.endswith('.pdf'):
                    pdf = PdfReader(f)
                    full_txt += " ".join([p.extract_text() for p in pdf.pages])
                else: full_txt += f.read().decode()
            st.session_state.doc_context = full_txt
            st.success(f"Загружено {len(full_txt)} знаков")

if st.button("🔴 ПОЛНЫЙ СБРОС"):
        st.session_state.messages = []
        st.session_state.doc_context = ""
        st.rerun()

st.title("🧠 AKYLMAN PRESIDENTIAL AI")

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])
        if "img" in m: st.image(m["img"])

if prompt := st.chat_input("Спроси у АКЫЛМАНА..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.markdown(prompt)

    with st.chat_message("assistant"):
        if "нарисуй" in prompt.lower():
            subj = prompt.lower().replace("нарисуй", "").strip()
            url = f"https://pollinations.ai/p/{urllib.parse.quote(subj)}?width=1024&height=1024&nologo=true"
            st.image(url)
            st.session_state.messages.append({"role": "assistant", "content": f"Рисунок: {subj}", "img": url})

else:
            search_res = ""
            if any(x in prompt.lower() for x in ["найди", "кто", "новости"]):
                try: search_res = "\nИНТЕРНЕТ:\n" + "\n".join([r['body'] for r in DDGS().text(prompt, max_results=2)])
                except: pass
            
            sys_info = f"Ты АКЫЛМАН. Помогай Исануру. Твои знания: {st.session_state.doc_context[:10000]}. {search_res}"
            res_box = st.empty(); full_ans = ""
            try:
                chat = client.chat.completions.create(
                    model=m_id,
                    messages=[{"role": "system", "content": sys_info}, {"role": "user", "content": prompt}],
                    stream=True
                )
                for chunk in chat:
                    if chunk.choices[0].delta.content:
                        full_ans += chunk.choices[0].delta.content
                        res_box.markdown(full_ans + "▌")
                res_box.markdown(full_ans)
                st.session_state.messages.append({"role": "assistant", "content": full_ans})
                st.session_state.words += len(full_ans.split())
            except Exception as e:
                st.error(f"Groq Error: {e}")

st.divider()
c1, c2, c3 = st.columns(3)
with c1: st.info(f"📍 Модель: {m_id}")
with c2: st.info(f"📊 Слов сгенерировано: {st.session_state.words}")
with c3: st.info(f"👤 Пользователь: Исанур")
