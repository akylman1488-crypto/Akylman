import streamlit as st
from groq import Groq

class AkylmanBrain:
    def __init__(self):
        self.api_key = st.secrets["GROQ_API_KEY"]
        self.client = Groq(api_key=self.api_key)
        
        self.level_configs = {
            "Fast": {"model": "llama-3.1-8b-instant", "temp": 0.5},
            "Thinking": {"model": "llama-3.3-70b-versatile", "temp": 0.3},
            "Pro": {"model": "llama-3.3-70b-versatile", "temp": 0.7},
            "Plus": {"model": "llama-3.3-70b-versatile", "temp": 1.0}
        }

    def generate_response_stream(self, prompt, level, subject, context=""):
        config = self.level_configs.get(level, self.level_configs["Fast"])
        try:
            stream = self.client.chat.completions.create(
                model=config["model"],
                messages=[
                    {"role": "system", "content": f"Ты АКЫЛМАН. Предмет: {subject}. Контекст: {context}"},
                    {"role": "user", "content": prompt}
                ],
                temperature=config["temp"],
                stream=True
            )
            for chunk in stream:
                if chunk.choices[0].delta.content:
                    yield chunk.choices[0].delta.content
        except Exception as e:
            yield f"Ошибка API: {str(e)}"
