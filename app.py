import streamlit as st
from brain import AkylmanBrain
from interface import AkylmanUI
from storage import AkylmanStorage
from effects import AkylmanFX

brain = AkylmanBrain()
ui = AkylmanUI()
db = AkylmanStorage()
fx = AkylmanFX()

ui.apply_styles()
fx.particles()

st.title("AKYLMAN PRO")

with st.sidebar:
    level = st.radio("LEVEL:", ["Fast", "Thinking", "Pro", "Plus"])
    subject = st.selectbox("SUBJECT:", ["Math", "English", "IT"])

hist = db.load_history(subject)
for _, row in hist.iterrows():
    with st.chat_message(row['role']):
        st.markdown(row['content'])

if prompt := st.chat_input("Write command..."):
    db.add_msg(level, "user", prompt, subject)
    with st.chat_message("user"): st.markdown(prompt)
    
    with st.chat_message("assistant"):
        stream = brain.generate(prompt, level, subject, "")
        full_res = st.write_stream(stream)
        db.add_msg(level, "assistant", full_res, subject)
