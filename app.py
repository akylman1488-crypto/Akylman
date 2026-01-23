import streamlit as st
from groq import Groq
from PyPDF2 import PdfReader
import sqlite3

st.set_page_config(page_title="AKYLMAN PRO", layout="wide")

def get_db():
    conn = sqlite3.connect('akylman_memory.db', check_same_thread=False)
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS messages (role TEXT, content TEXT)')
    conn.commit()
    return conn, c

conn, c = get_db()

st.markdown("""
<style>
    .stApp { background-color: #050505; color: #e0e0e0; }
    h1 { color: #00ffcc; text-shadow: 0 0 15px #00ffcc; font-family: sans-serif; }
    [data-testid="stChatMessage"] { 
        background: rgba(255, 255, 255, 0.05); 
        border: 1px solid #00ffcc44; 
        border-radius: 15px; 
    }
    .stChatInputContainer textarea { border: 1px solid #00ffcc !important; }
</style>
""", unsafe_allow_html=True)

st.title("AKYLMAN V4: SYSTEM ONLINE")

api_key = st.secrets["GROQ_API_KEY"]
client = Groq(api_key=api_key)

with st.sidebar:
    st.header("DATABASE")
    uploaded_files = st.file_uploader("Upload PDF Knowledge", accept_multiple_files=True)
    knowledge_base = ""
    if uploaded_files:
        for pdf_file in uploaded_files:
            reader = PdfReader(pdf_file)
            for page in reader.pages:
                knowledge_base += page.extract_text()
        st.success("FILES INDEXED")

    if st.button("RESET MEMORY"):
        c.execute("DELETE FROM messages")
        conn.commit()
        st.rerun()

c.execute("SELECT role, content FROM messages")
for role, text in c.fetchall():
    with st.chat_message(role):
        st.markdown(text)

if prompt := st.chat_input("Enter command..."):
    c.execute("INSERT INTO messages VALUES (?, ?)", ("user", prompt))
    conn.commit()
    
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response_box = st.empty()
        full_text = ""
        
        try:
            chat_stream = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": "You are Akylman. Context: " + knowledge_base[:5000]},
                    {"role": "user", "content": prompt}
                ],
                stream=True
            )
            
            for chunk in chat_stream:
                if chunk.choices[0].delta.content:
                    full_text += chunk.choices[0].delta.content
                    response_box.markdown(full_text + "▌")
            
            response_box.markdown(full_text)
            c.execute("INSERT INTO messages VALUES (?, ?)", ("assistant", full_text))
            conn.commit()
            
        except Exception as e:
            st.error(str(e))
