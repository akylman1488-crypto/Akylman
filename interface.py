import streamlit as st

def init_page():
    st.set_page_config(page_title="Akylman AI 2.0", page_icon="🧠")
    st.header("Akylman AI — Твой мудрый наставник")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

def display_chat():
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
