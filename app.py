import streamlit as st
from groq import Groq
import os
import datetime
import pandas as pd
from PyPDF2 import PdfReader
from duckduckgo_search import DDGS

st.set_page_config(page_title="AKYLMAN AI", page_icon="🧠", layout="wide")

st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://cdn.dribbble.com/userupload/12560411/file/original-cb85895710c2c26fabc3ee05308be2b0.jpg?resize=1600x1200");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    .stApp h1 {
        color: white !important;
        -webkit-text-fill-color: white !important;
        text-shadow: 2px 2px 8px #000 !important;
    }

    [data-testid="stChatMessage"] div, 
    [data-testid="stChatMessage"] p, 
    .stMarkdown p, 
    .stMarkdown span,
    [data-testid="stChatMessage"] li {
        color: white !important;
        -webkit-text-fill-color: white !important;
        text-shadow: 2px 2px 4px black !important;
        font-weight: 500 !important;
    }

    [data-testid="stSidebar"] {
        background-color: rgba(255, 255, 255, 0.9) !important;
        backdrop-filter: blur(10px);
    }
    
    [data-testid="stSidebar"] * {
        color: #1e1e1e !important;
    }

    [data-testid="stChatInput"] {
        background-color: white !important;
        border-radius: 15px !important;
        border: 2px solid #4A90E2 !important;
    }
    
    [data-testid="stChatInput"] textarea {
        color: black !important;
        -webkit-text-fill-color: black !important;
    }

    header, [data-testid="stHeader"], [data-testid="stBottom"] > div {
        background: transparent !important;
    }

    .stButton>button {
        border-radius: 20px;
        background-color: #4A90E2;
        color: white;
        transition: 0.3s;
    }
    </style>

    <script>
    function applyStyles() {
        const doc = window.parent.document;
        const elements = doc.querySelectorAll('[data-testid="stChatMessage"] p, [data-testid="stChatMessage"] li');
        elements.forEach(el => {
            el.style.color = 'white';
            el.style.webkitTextFillColor = 'white';
        });
    }
    setInterval(applyStyles, 1000);
    </script>
    """, unsafe_allow_html=True)

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

if "messages" not in st.session_state:
    st.session_state.messages = []
if "doc_context" not in st.session_state:
    st.session_state.doc_context = ""

with st.sidebar:
    st.title("🎛️ ПАНЕЛЬ УПРАВЛЕНИЯ")
    st.markdown("---")
    uploaded_file = st.file_uploader("Загрузить материалы для учебы (PDF/TXT/CSV)", type=["pdf", "txt", "csv"])
    
    if uploaded_file:
        try:
            if uploaded_file.type == "application/pdf":
                reader = PdfReader(uploaded_file)
                st.session_state.doc_context = "КОНТЕКСТ УЧЕБНОГО ПОСОБИЯ:\n" + "".join([p.extract_text() for p in reader.pages])
            elif uploaded_file.type == "text/csv":
                df = pd.read_csv(uploaded_file)
                st.session_state.doc_context = "ДАННЫЕ ДЛЯ АНАЛИЗА:\n" + df.head(30).to_string()
            else:
                st.session_state.doc_context = uploaded_file.read().decode("utf-8")
            st.success("Данные успешно интегрированы в память АКЫЛМАН.")
        except Exception as e:
            st.error(f"Ошибка загрузки: {e}")

    st.markdown("---")
    if st.button("🗑️ Очистить память и чат"):
        st.session_state.messages = []
        st.session_state.doc_context = ""
        st.rerun()

st.title("🧠 АКЫЛМАН AI")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Напишите сообщение АКЫЛМАН..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""
        
        search_context = ""
        if any(word in prompt.lower() for word in ["найди", "новости", "информация", "реальном времени", "узнай"]):
            with st.spinner("АКЫЛМАН подключается к глобальной сети..."):
                try:
                    results = DDGS().text(prompt, max_results=4)
                    search_context = "\nАКТУАЛЬНЫЕ ДАННЫЕ ИЗ СЕТИ:\n" + "\n".join([r['body'] for r in results])
                except:
                    pass

        system_msg = (
            "Твое имя — АКЫЛМАН. Ты — высокоинтеллектуальный ИИ нового поколения, созданный Исануром. "
            "Твои ключевые характеристики: "
            "1. ВЫСШИЙ УРОВЕНЬ МЫШЛЕНИЯ: Анализируй задачи глубоко, логично и последовательно. "
            "2. ЭМПАТИЯ: Будь вежливым, умей соболезновать и поддерживать пользователя эмоционально. "
            "3. ПОМОЩНИК В УЧЕБЕ: Мастерски помогай с уроками, объясняй сложные темы, решай задачи. "
            "4. МУЛЬТИЯЗЫЧНОСТЬ: Всегда отвечай строго на том языке, на котором к тебе обратились. "
            "5. РЕАЛЬНОЕ ВРЕМЯ: Используй предоставленные данные из интернета для актуальных ответов. "
            f"КОНТЕКСТ ДАННЫХ: {st.session_state.doc_context[:7500]} {search_context} "
            "Если лимит запросов исчерпан, вежливо попроси пользователя подождать 60 секунд."
        )
        
        try:
            msgs = [{"role": "system", "content": system_msg}] + st.session_state.messages
            completion = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=msgs,
                stream=True,
                temperature=0.6
            )
            
            for chunk in completion:
                if chunk.choices[0].delta.content:
                    full_response += chunk.choices[0].delta.content
                    response_placeholder.markdown(full_response + "▌")
            
            response_placeholder.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            
        except Exception as e:
            if "rate_limit" in str(e).lower():
                st.error("Уважаемый пользователь, АКЫЛМАН сейчас обрабатывает большой объем данных. Пожалуйста, подождите 60 секунд, прежде чем мы продолжим нашу беседу. Благодарю за терпение.")
            else:
                st.error(f"Произошла техническая заминка: {e}")
