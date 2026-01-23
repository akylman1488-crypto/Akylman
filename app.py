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
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    .stApp h1 { color: white !important; text-shadow: 2px 2px 8px #000 !important; }
    [data-testid="stChatMessage"] p, .stMarkdown p, .stMarkdown span, li {
        color: white !important;
        text-shadow: 2px 2px 4px black !important;
        font-weight: 500 !important;
    }
    [data-testid="stSidebar"] { background-color: rgba(255, 255, 255, 0.9) !important; }
    [data-testid="stSidebar"] * { color: #1e1e1e !important; }
    [data-testid="stChatInput"] { background-color: white !important; border-radius: 15px !important; }
    [data-testid="stChatInput"] textarea { color: black !important; }
    header, [data-testid="stHeader"], [data-testid="stBottom"] > div { background: transparent !important; }
    </style>
    """, unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []
if "doc_context" not in st.session_state:
    st.session_state.doc_context = ""

with st.sidebar:
    st.title("🎛️ УПРАВЛЕНИЕ")
    
    # СЕКРЕТНЫЙ ПАРОЛЬ (можешь поменять '1234' на свой)
    CORRECT_PASSWORD = "1234"
    
    user_password = st.text_input("Введите пароль для доступа к Pro:", type="password")
    
    if user_password == CORRECT_PASSWORD:
        st.success("Доступ к Pro открыт! ✅")
        available_modes = ["🚀 Быстрая (Flash)", "🤔 Думающая (Pro)", "💎 Plus (1.5 Pro)"]
    else:
        if user_password:
            st.error("Неверный пароль")
        available_modes = ["🚀 Быстрая (Flash)"]
    
    version = st.selectbox("Версия АКЫЛМАНА:", available_modes)
    
    model_mapping = {
        "🚀 Быстрая (Flash)": "gemini-1.5-flash",
        "🤔 Думающая (Pro)": "gemini-1.0-pro",
        "💎 Plus (1.5 Pro)": "gemini-1.5-pro"
    }
    
    selected_model = model_mapping[version]

    uploaded_file = st.file_uploader("Материалы", type=["pdf", "txt", "csv"])
    if uploaded_file:
        try:
            if uploaded_file.type == "application/pdf":
                reader = PdfReader(uploaded_file)
                st.session_state.doc_context = "".join([p.extract_text() for p in reader.pages])
            elif uploaded_file.type == "text/csv":
                df = pd.read_csv(uploaded_file)
                st.session_state.doc_context = df.head(50).to_string()
            else:
                st.session_state.doc_context = uploaded_file.read().decode("utf-8")
            st.success("Данные загружены")
        except Exception as e:
            st.error(f"Error: {e}")
            
    if st.button("🗑️ Очистить всё"):
        st.session_state.messages = []
        st.session_state.doc_context = ""
        st.rerun()

try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel(selected_model)
except Exception as e:
    st.error(f"Ошибка: {e}")

st.title(f"🧠 АКЫЛМАН AI ({version.split()[1]})")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if "image_url" in message:
            st.markdown(f'<img src="{message["image_url"]}" style="width:100%; border-radius:10px;">', unsafe_allow_html=True)

if prompt := st.chat_input("Напишите АКЫЛМАНУ..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        if "нарисуй" in prompt.lower():
            response_placeholder = st.empty()
            response_placeholder.markdown("🎨 Рисую...")
            clean_prompt = prompt.lower().replace("нарисуй", "").strip()
            encoded_prompt = urllib.parse.quote(clean_prompt)
            image_url = f"https://pollinations.ai/p/{encoded_prompt}?width=1024&height=1024&nologo=true"
            st.markdown(f'<img src="{image_url}" style="width:100%; border-radius:10px;">', unsafe_allow_html=True)
            full_response = f"Готово! Рисунок: {clean_prompt}"
            st.session_state.messages.append({"role": "assistant", "content": full_response, "image_url": image_url})
            response_placeholder.markdown(full_response)
        else:
            response_placeholder = st.empty()
            full_response = ""
            search_data = ""
            if any(w in prompt.lower() for w in ["найди", "новости", "инфо"]):
                try:
                    results = DDGS().text(prompt, max_results=3)
                    search_data = "\nWEB:\n" + "\n".join([r['body'] for r in results])
                except: pass

            sys_instr = f"Ты АКЫЛМАН ({version}). Помогай Исануру. КОНТЕКСТ: {st.session_state.doc_context[:10000]} {search_data}"
            
            try:
                response = model.generate_content(f"{sys_instr}\n\nUser: {prompt}", stream=True)
                for chunk in response:
                    if chunk.text:
                        full_response += chunk.text
                        response_placeholder.markdown(full_response + "▌")
                response_placeholder.markdown(full_response)
                st.session_state.messages.append({"role": "assistant", "content": full_response})
            except Exception as e:
                st.error(f"Лимит или ошибка: {e}")
