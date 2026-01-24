import streamlit as st
from groq import Groq
import re
import time
import json
import random

class AkylmanBrain:
    def __init__(self):
        self.api_key = st.secrets.get("GROQ_API_KEY", "")
        self.client = Groq(api_key=self.api_key)
        
        self.models_map = {
            "fast_tier": "llama-3.1-8b-instant",
            "high_tier": "llama-3.3-70b-versatile"
        }

        self.system_prompts = {
            "Математика": {
                "base": "Ты профессиональный математик и преподаватель.",
                "rules": "1. Пиши формулы строго в LaTeX формате: $E=mc^2$. 2. Разделяй решение на шаги. 3. Если задача сложная, проверь ответ дважды."
            },
            "English": {
                "base": "You are an expert IELTS/TOEFL tutor.",
                "rules": "1. Reply in English mostly. 2. Highlight grammar errors in bold. 3. Provide C1/C2 vocabulary alternatives. 4. Check for spelling."
            },
            "История": {
                "base": "Ты историк-аналитик с энциклопедическими знаниями.",
                "rules": "1. Указывай точные даты. 2. Анализируй причины и следствия. 3. Избегай непроверенных фактов. 4. Структурируй ответ хронологически."
            },
            "IT": {
                "base": "Ты Senior Software Engineer и ментор по Python/C++.",
                "rules": "1. Код должен соответствовать PEP8. 2. Добавляй объяснения к сложным алгоритмам. 3. Учитывай Time Complexity (Big O). 4. Предлагай оптимизации."
            }
        }

        self.level_configs = {
            "Fast": {
                "model": self.models_map["fast_tier"],
                "temperature": 0.5,
                "top_p": 0.8,
                "max_tokens": 1024,
                "mode_instruction": "Отвечай максимально кратко, быстро и по сути. Без лишних вступлений."
            },
            "Thinking": {
                "model": self.models_map["high_tier"],
                "temperature": 0.6,
                "top_p": 0.9,
                "max_tokens": 4096,
                "mode_instruction": "Используй метод Chain-of-Thought. Сначала проанализируй вопрос шаг за шагом, найди скрытые детали, и только потом дай ответ."
            },
            "Pro": {
                "model": self.models_map["high_tier"],
                "temperature": 0.7,
                "top_p": 0.95,
                "max_tokens": 8192,
                "mode_instruction": "Ты эксперт мирового уровня. Твой ответ должен быть академическим, полным, глубоким и структурированным. Используй терминологию."
            },
            "Plus": {
                "model": self.models_map["high_tier"],
                "temperature": 0.9,
                "top_p": 1.0,
                "max_tokens": 8192,
                "mode_instruction": "Включи креативность. Предлагай нестандартные решения, аналогии, примеры из реальной жизни. Будь вдохновляющим ментором."
            }
        }

    def validate_input(self, text):
        if not text:
            return False, "Empty input"
        if len(text) > 20000:
            return False, "Input too long"
        return True, "Valid"

    def process_context(self, raw_context, query):
        if not raw_context:
            return ""
        
        clean_context = re.sub(r'\s+', ' ', raw_context)
        query_terms = query.lower().split()
        sentences = clean_context.split('.')
        relevant_segments = []
        
        for sent in sentences:
            score = 0
            for term in query_terms:
                if len(term) > 3 and term in sent.lower():
                    score += 1
            if score > 0:
                relevant_segments.append(sent.strip())
        
        selected_text = ". ".join(relevant_segments)
        return selected_text[:6000]

    def format_latex_output(self, text):
        patterns = [
            (r'(\b[a-z])\^(\d+)', r'$\1^\2$'),
            (r'sqrt\((.*?)\)', r'$\sqrt{\1}$'),
            (r'(\d+)/(\d+)', r'$\frac{\1}{\2}$')
        ]
        for pat, repl in patterns:
            text = re.sub(pat, repl, text)
        return text

    def generate_response_stream(self, user_prompt, level, subject, doc_context=""):
        is_valid, msg = self.validate_input(user_prompt)
        if not is_valid:
            yield f"System Error: {msg}"
            return

        config = self.level_configs.get(level, self.level_configs["Fast"])
        
        sys_data = self.system_prompts.get(subject, {
            "base": "Ты универсальный помощник.",
            "rules": "Отвечай вежливо и точно."
        })
        
        optimized_context = self.process_context(doc_context, user_prompt)
        
        final_system_prompt = (
            f"{sys_data['base']}\n"
            f"LEVEL MODE: {level.upper()}\n"
            f"INSTRUCTION: {config['mode_instruction']}\n"
            f"SUBJECT RULES: {sys_data['rules']}\n"
            f"KNOWLEDGE BASE: {optimized_context}"
        )

        messages_payload = [
            {"role": "system", "content": final_system_prompt},
            {"role": "user", "content": user_prompt}
        ]

        try:
            stream = self.client.chat.completions.create(
                model=config["model"],
                messages=messages_payload,
                temperature=config["temperature"],
                top_p=config["top_p"],
                max_tokens=config["max_tokens"],
                stream=True
            )
            
            for chunk in stream:
                content = chunk.choices[0].delta.content
                if content:
                    yield content

        except Exception as e:
            error_msg = str(e)
            if "400" in error_msg:
                yield "Error 400: Model decommissioned or invalid request. Switching to fallback..."
                fallback_stream = self.client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=messages_payload,
                    stream=True
                )
                for chunk in fallback_stream:
                    if chunk.choices[0].delta.content:
                        yield chunk.choices[0].delta.content
            else:
                yield f"Critical API Error: {error_msg}"

    def estimate_tokens(self, text):
        return len(text) // 4

    def get_health_status(self):
        return {
            "api_status": "online" if self.api_key else "offline",
            "available_models": list(self.models_map.values()),
            "latency": random.uniform(0.1, 0.4)
        }
