import streamlit as st
from groq import Groq

class AkylmanBrain:
    def __init__(self):
        self.client = Groq(api_key=st.secrets["GROQ_API_KEY"])

    def get_ai_response(self, prompt, subject, context=""):
        sys_msg = f"Ты АКЫЛМАН, помощник Исанура по предмету {subject}. Знания из PDF: {context[:3000]}"
        try:
            chat = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile", 
                messages=[
                    {"role": "system", "content": sys_msg},
                    {"role": "user", "content": prompt}
                ],
                stream=True
            )
            for chunk in chat:
                if chunk.choices[0].delta.content:
                    yield chunk.choices[0].delta.content
        except Exception as e
            try:
                chat_fast = self.client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=[
                        {"role": "system", "content": sys_msg},
                        {"role": "user", "content": prompt}
                    ],
                    stream=True
                )
                for chunk in chat_fast:
                    if chunk.choices[0].delta.content:
                        yield chunk.choices[0].delta.content
            except Exception as e2:
                yield f"Ошибка API: {str(e2)}"
