import streamlit as st
from groq import Groq

class AkylmanBrain:
    def __init__(self):
        self.client = Groq(api_key=st.secrets["GROQ_API_KEY"])
        self.levels = {
            "Fast": {"model": "llama-3.1-8b-instant", "temp": 0.6, "top_p": 0.9},
            "Thinking": {"model": "llama-3.3-70b-versatile", "temp": 0.5, "top_p": 0.8},
            "Pro": {"model": "llama-3.3-70b-versatile", "temp": 0.7, "top_p": 1.0},
            "Plus": {"model": "llama-3.3-70b-versatile", "temp": 0.9, "top_p": 1.0}
        }

    def generate(self, prompt, level, subject, context):
        config = self.levels.get(level, self.levels["Fast"])
        
        system_prompts = {
            "Fast": "Отвечай максимально кратко и быстро.",
            "Thinking": "Рассуждай пошагово. Сначала проанализируй вопрос, потом дай ответ.",
            "Pro": f"Ты эксперт в области {subject}. Давай глубокий научный ответ.",
            "Plus": "Будь креативным, предлагай необычные идеи и примеры."
        }

        try:
            stream = self.client.chat.completions.create(
                model=config["model"],
                messages=[
                    {"role": "system", "content": f"{system_prompts[level]} Контекст: {context}"},
                    {"role": "user", "content": prompt}
                ],
                temperature=config["temp"],
                top_p=config["top_p"],
                stream=True
            )
            return stream
        except Exception as e:
            st.error(f"Error in Brain: {e}")
            return None
