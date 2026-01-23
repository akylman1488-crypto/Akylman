import streamlit as st
from groq import Groq
from PyPDF2 import PdfReader
import sqlite3
import datetime
import time

class AkylmanSystem:
    def __init__(self):
        self.client = Groq(api_key=st.secrets["GROQ_API_KEY"]
        self.model_70b = "llama-3.3-70b-versatile" 
        self.model_8b = "llama-3.1-8b-instant"
            )
    def get_ai_response(self, prompt, subject, context=""):
        system_instructions = {
            "Математика": "Ты профессор математики. Используй LaTeX $x^2$.",
            "English": "You are an Oxford English Teacher. Correct grammar.",
            "История": "Ты историк. Рассказывай события как захватывающий сериал."
        }
        instr = system_instructions.get(subject, "Ты АКЫЛМАН.")
        
        try:
            response = self.client.chat.completions.create(
                model=self.model_70b,
                messages=[
                    {"role": "system", "content": f"{instr} Контекст из файлов: {context[:5000]}"},
                    {"role": "user", "content": prompt}
                ],
                stream=True
            )
            for chunk in response:
                if chunk.choices[0].delta.content:
                    yield chunk.choices[0].delta.content
        except:
            response = self.client.chat.completions.create(
                model=self.model_8b,
                messages=[{"role": "user", "content": prompt}],
                stream=True
            )
            for chunk in response:
                if chunk.choices[0].delta.content:
                    yield chunk.choices[0].delta.content

def apply_massive_styles():
    st.markdown("""
    <style>
        .stApp { background: #000000; color: #00ffcc; }
        [data-testid="stChatMessage"] { 
            border: 1px solid #00ffcc44; 
            border-radius: 20px; 
            background: rgba(0, 255, 204, 0.05); 
        }
        .stChatInputContainer textarea { border: 1px solid #00ffcc !important; }
        h1 { text-shadow: 0px 0px 15px #00ffcc; font-family: 'Courier New'; }
    </style>
    """, unsafe_allow_html=True)

def init_memory():
    conn = sqlite3.connect('akylman_v4.db', check_same_thread=False)
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS chat (role TEXT, content TEXT, sub TEXT)')
    conn.commit()
    return conn

st.set_page_config(page_title="AKYLMAN MEGA-CORE", layout="wide")
apply_massive_styles()

if "akylman" not in st.session_state:
    st.session_state.akylman = AkylmanSystem()
    st.session_state.memory = init_memory()

st.title("🧠 AKYLMAN PRESIDENTIAL AI [V4.2]")

with st.sidebar:
    st.header("Настройки")
    subj = st.selectbox("Предмет:", ["Математика", "English", "История"])
    files = st.file_uploader("Загрузи знания (PDF):", accept_multiple_files=True)
    pdf_text = ""
    if files:
        for f in files:
            reader = PdfReader(f)
            for page in reader.pages:
                pdf_text += page.extract_text()
        st.success("База знаний загружена!")
и
cursor = st.session_state.memory.cursor()
cursor.execute('SELECT role, content FROM chat WHERE sub=?', (subj,))
for r in cursor.fetchall():
    with st.chat_message(r[0]): st.markdown(r[1])

if prompt := st.chat_input("Напиши АКЫЛМАНУ..."):
    cursor.execute('INSERT INTO chat VALUES (?, ?, ?)', ("user", prompt, subj))
    st.session_state.memory.commit()
    
    with st.chat_message("user"): st.markdown(prompt)
    
    with st.chat_message("assistant"):
        res_area = st.empty()
        full_res = ""
        for chunk in st.session_state.akylman.get_ai_response(prompt, subj, pdf_text):
            full_res += chunk
            res_area.markdown(full_res + "▌")
        res_area.markdown(full_res)
        
        cursor.execute('INSERT INTO chat VALUES (?, ?, ?)', ("assistant", full_res, subj))
        st.session_state.memory.commit()
