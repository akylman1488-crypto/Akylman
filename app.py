import streamlit as st
from brain import AkylmanBrain
from PyPDF2 import PdfReader

st.set_page_config(page_title="AKYLMAN", layout="wide")

if "brain" not in st.session_state:
    st.session_state.brain = AkylmanBrain()
if "history" not in st.session_state:
    st.session_state.history = []

st.title("🧠 AKYLMAN PRESIDENTIAL AI")

with st.sidebar:
    subject = st.selectbox("Предмет:", ["Математика", "English", "История"])
    files = st.file_uploader("Загрузи PDF:", accept_multiple_files=True)
    context = ""
    if files:
        for f in files:
            pdf = PdfReader(f)
            for page in pdf.pages:
                context += page.extract_text()
        st.success("Файлы готовы!")

for msg in st.session_state.history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Спроси..."):
    st.session_state.history.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        res_area = st.empty()
        full_res = ""
        for chunk in st.session_state.brain.get_ai_response(prompt, subject, context):
            full_res += chunk
            res_area.markdown(full_res + "▌")
        res_area.markdown(full_res)
        st.session_state.history.append({"role": "assistant", "content": full_res})
