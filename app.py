import streamlit as st
from groq import Groq
import sqlite3
import datetime

conn = sqlite3.connect('memory.db', check_same_thread=False)
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS chat (role TEXT, content TEXT)')
conn.commit()
=
st.set_page_config(page_title="AKYLMAN HYBRID", layout="wide")
st.markdown("""
<style>
    .stApp { background: #000000; }
    [data-testid="stChatMessage"] { 
        background: rgba(0, 255, 204, 0.05) !important; 
        border: 1px solid #00ffcc !important; 
        border-radius: 15px !important;
    }
    h1 { color: #00ffcc !important; text-shadow: 0px 0px 15px #00ffcc; }
    p, span, li { color: #e0e0e0 !important; }
</style>
""", unsafe_allow_html=True)

st.components.v1.html("""
<script>
    alert("Исанур, гибридный интеллект АКЫЛМАН активирован!");
</script>
""", height=0)

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.title("🧠 AKYLMAN HYBRID-CORE")
st.write("Система: Python (Logic) | SQL (Memory) | CSS (UI) | JS (Alerts)")

c.execute('SELECT * FROM chat')
history = c.fetchall()
for r in history:
    with st.chat_message(r[0]): st.markdown(r[1])

if prompt := st.chat_input("Напиши АКЫЛМАНУ..."):
    c.execute('INSERT INTO chat VALUES (?, ?)', ("user", prompt))
    conn.commit()
    with st.chat_message("user"): st.markdown(prompt)
    
    with st.chat_message("assistant"):
        res_area = st.empty()
        full_response = ""
        try:
            chat = client.chat.completions.create(
                model="llama3-8b-8192",
                messages=[{"role": "user", "content": prompt}],
                stream=True
            )
            for chunk in chat:
                if chunk.choices[0].delta.content:
                    full_response += chunk.choices[0].delta.content
                    res_area.markdown(full_response + "▌")
            res_area.markdown(full_response)

            c.execute('INSERT INTO chat VALUES (?, ?)', ("assistant", full_response))
            conn.commit()
        except Exception as e:
            st.error(f"Ошибка: {e}")
