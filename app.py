import streamlit as st
from brain import AkylmanBrain
from interface import AkylmanUI
from storage import AkylmanStorage
from effects import AkylmanFX

st.set_page_config(page_title="AKYLMAN PRO", layout="wide")

if "init" not in st.session_state:
    st.session_state.brain = AkylmanBrain()
    st.session_state.ui = AkylmanUI()
    st.session_state.db = AkylmanStorage()
    st.session_state.fx = AkylmanFX()
    st.session_state.init = True

ui = st.session_state.ui
brain = st.session_state.brain
db = st.session_state.db
fx = st.session_state.fx

ui.apply_styles()
fx.inject_particles()

st.title("AKYLMAN PRO")

with st.sidebar:
    level = st.radio("LEVEL", ["Fast", "Thinking", "Pro", "Plus"])
    subject = st.selectbox("SUBJECT", ["Math", "English", "IT"])

if p := st.chat_input("Command..."):
    with st.chat_message("user"):
        st.markdown(p)
    
    with st.chat_message("assistant"):
        res = ""
        box = st.empty()
        for chunk in brain.generate_response_stream(p, level, subject, ""):
            if isinstance(chunk, str):
                res += chunk
                box.markdown(res + "▌")
        box.markdown(res)
        fx.play_audio()
