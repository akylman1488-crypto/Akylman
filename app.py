import streamlit as st
import pandas as pd
from PyPDF2 import PdfReader
from groq import Groq
from duckduckgo_search import DDGS
import urllib.parse
import datetime

st.set_page_config(page_title="AKYLMAN PRO", layout="wide")

if "messages" not in st.session_state: st.session_state.messages = []
if "doc_context" not in st.session_state: st.session_state.doc_context = ""

try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except:
    st.error("Ошибка: Проверь GROQ_API_KEY в Secrets!")

st.markdown("""
<style>
[data-testid="stAppViewContainer"] { background: #0e1117; color: white; }
[data-testid="stSidebar"] { background: #262730; }
.stChatMessage { border-radius: 10px; border: 1px solid #333; margin: 5px; }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.title("🧠 АКЫЛМАН")

    uploaded_files = st.file_uploader("Загрузи учебники (PDF):", accept_multiple_files=True)
    if uploaded_files:
        text = ""
        for f in uploaded_files:
            if f.name.endswith(".pdf"):
                reader = PdfReader(f)
                for page in reader.pages:
                    text += page.extract_text()
        st.session_state.doc_context = text
        st.success("Файлы изучены!")

    if st.button("Очистить чат"):
        st.session_state.messages = []
        st.rerun()

st.title("АКЫЛМАН PRESIDENTIAL AI")

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])
        if "img" in m: st.image(m["img"])

if prompt := st.chat_input("Напиши сообщение..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.markdown(prompt)

    with st.chat_message("assistant"):
        if "нарисуй" in prompt.lower():
            subject = prompt.lower().replace("нарисуй", "").strip()
            img_url = f"https://pollinations.ai/p/{urllib.parse.quote(subject)}?width=1024&height=1024&nologo=true"
            st.image(img_url)
            st.session_state.messages.append({"role": "assistant", "content": f"Готово: {subject}", "img": img_url})
        else:
            web_info = ""
            if any(x in prompt.lower() for x in ["найди", "кто", "новости"]):
                try:
                    search = DDGS().text(prompt, max_results=2)
                    web_info = "\nИНТЕРНЕТ:\n" + "\n".join([r['body'] for r in search])
                except: pass

            full_instr = f"Ты АКЫЛМАН. Помогай Исануру. Знания из файлов: {st.session_state.doc_context[:5000]}. {web_info}"
            res_box = st.empty()
            full_text = ""
            
            try:
                completion = client.chat.completions.create(
                    model="llama3-8b-8192",
                    messages=[{"role": "system", "content": full_instr}, {"role": "user", "content": prompt}],
                    stream=True
                )
                for chunk in completion:
                    if chunk.choices[0].delta.content:
                        full_text += chunk.choices[0].delta.content
                        res_box.markdown(full_text + "▌")
                res_box.markdown(full_text)
                st.session_state.messages.append({"role": "assistant", "content": full_text})
            except Exception as e:
                st.error(f"Ошибка Groq: {e}")
