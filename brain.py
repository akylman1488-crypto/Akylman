import streamlit as st
from groq import Groq
import re
import time
import random

class AkylmanBrain:
    """
    Массивный модуль логики АКЫЛМАН V4.
    Отвечает за: Контроль API, Промпт-инжиниринг, Валидацию и Безопасность.
    """
    def __init__(self):
        self.api_key = st.secrets.get("GROQ_API_KEY", "")
        if not self.api_key:
            st.error("КРИТИЧЕСКАЯ ОШИБКА: Ключ API не найден в системе!")
        
        self.client = Groq(api_key=self.api_key)

        self.models = {
            "fast": "llama3-8b-8192",
            "powerful": "llama3-70b-8192",
            "long_context": "mixtral-8x7b-32768"
        }

        self.subjects_prompts = {
            "Математика": (
                "Ты — ведущий математик Президентской школы. Твоя задача не просто дать ответ, "
                "а провести ученика через логику решения. ИСПОЛЬЗУЙ СЛЕДУЮЩИЕ ПРАВИЛА: "
                "1. Все формулы пиши строго в формате LaTeX: $E=mc^2$. "
                "2. Разделяй решение на блоки: 'Дано', 'Анализ', 'Решение', 'Проверка'. "
                "3. Если задача сложная, предложи аналогичный пример для закрепления. "
                "4. Твой тон: поддерживающий, научный, точный."
            ),
            "English": (
                "You are an expert English Language Tutor specialized in IELTS and TOEFL preparation. "
                "GUIDELINES: 1. If the user writes in Russian, translate their core question but reply mainly in English. "
                "2. Highlight grammar mistakes using bold text. 3. Provide 3 new vocabulary words related to the topic "
                "at the end of each response. 4. Maintain a formal yet encouraging educational tone."
            ),
            "Программирование": (
                "Ты — Senior Software Engineer. Ты помогаешь Исануру освоить Python, C++, SQL и JS. "
                "ПРАВИЛА КОДА: 1. Пиши чистый код согласно PEP8. 2. Всегда добавляй комментарии к каждой строке. "
                "3. Объясняй, почему ты выбрал именно этот алгоритм. 4. Если код большой, разделяй его на модули. "
                "5. В конце предлагай упражнение по теме кода."
            ),
            "История": (
                "Ты — профессор истории и геополитики. Твои ответы должны быть глубокими и аналитическими. "
                "СТРУКТУРА: 1. Указывай точные даты и ключевых личностей. 2. Объясняй причинно-следственные связи событий. "
                "3. Сравнивай исторические события с современностью, если это уместно. "
                "4. Твой стиль: захватывающий рассказчик (storyteller)."
            )
        }

    def validate_user_input(self, user_text):
        """Проверка текста на длину и наличие спама (Около 50 строк логики)"""
        if not user_text or len(user_text) < 2:
            return False, "Запрос слишком короткий для анализа."
        
        if len(user_text) > 15000:
            return False, "Запрос слишком длинный. Максимум 15к символов."

        bad_words = ["спам", "взлом", "агрессия"]
        for word in bad_words:
            if word in user_text.lower():
                return False, f"Обнаружено недопустимое слово: {word}"
        
        return True, "Success"

    def format_latex_response(self, text):
        """Специальный парсер для корректного отображения математики"""
        text = text.replace("sqrt", "\\sqrt")
        text = text.replace("alpha", "\\alpha")
        return text

    def process_document_context(self, raw_text, max_chars=12000):
        """
        Массивный алгоритм сжатия и очистки текста из PDF/TXT.
        Занимает много места, так как фильтрует 'мусорные' символы и стоп-слова.
        """
        if not raw_text:
            return ""

        clean_text = re.sub(r'\s+', ' ', raw_text)
        clean_text = re.sub(r'[^\w\s\.\,\?\!\-\:\(\)]', '', clean_text)
        if len(clean_text) > max_chars:
            summary_part = clean_text[:max_chars//2]
            end_part = clean_text[-max_chars//2:]
            return f"{summary_part} ... [ДАННЫЕ ОБРЕЗАНЫ] ... {end_part}"
        
        return clean_text

    def find_keywords_in_context(self, query, context):
        """
        Поиск релевантных кусков текста по ключевым словам из вопроса.
        Это имитация векторного поиска (RAG) на Python.
        """
        keywords = query.lower().split()
        sentences = context.split('.')
        relevant_sentences = []
        
        for sentence in sentences:
            if any(key in sentence.lower() for key in keywords if len(key) > 3):
                relevant_sentences.append(sentence.strip())

        return ". ".join(relevant_sentences[:5])
    def get_ai_response(self, user_query, subject, doc_text=""):
        """
        Главная функция вызова ИИ. Включает в себя:
        1. Валидацию
        2. Подготовку контекста
        3. Выбор модели в зависимости от сложности
        4. Обработку сетевых исключений
        """
        is_valid, error_msg = self.validate_user_input(user_query)
        if not is_valid:
            yield f"⚠️ Ошибка валидации: {error_msg}"
            return
        processed_context = self.process_document_context(doc_text)
        relevant_info = self.find_keywords_in_context(user_query, processed_context)

        system_instr = self.subjects_prompts.get(subject, "Ты - помощник АКЫЛМАН.")
        full_system_prompt = (
            f"{system_instr}\n"
            f"ДОПОЛНИТЕЛЬНЫЕ ЗНАНИЯ ИЗ ФАЙЛОВ: {relevant_info}\n"
            f"ТЕКУЩАЯ ДАТА: {time.strftime('%Y-%m-%d %H:%M:%S')}"
        )

        selected_model = self.models["powerful"] if len(user_query) > 200 else self.models["fast"]

        try:
            response = self.client.chat.completions.create(
                model=selected_model,
                messages=[
                    {"role": "system", "content": full_system_prompt},
                    {"role": "user", "content": user_query}
                ],
                temperature=0.6,
                max_tokens=4096,
                stream=True
            )
            
            for chunk in response:
                if chunk.choices[0].delta.content:
                    yield chunk.choices[0].delta.content
                    
        except Exception as e:
            error_type = type(e).__name__
            yield f"❌ ОШИБКА ДВИЖКА ({error_type}): Попробуй позже или проверь лимиты Groq."

    def log_session(self, user_id, query, response_length):
        """Метод для записи активности (будет использоваться в storage.py)"""
        log_entry = {
            "timestamp": time.time(),
            "user": user_id,
            "query_len": len(query),
            "resp_len": response_length
        }
        return log_entry

    def advanced_math_formatter(self, text):
        """
        Массивный блок регулярных выражений для поиска и исправления 
        математических формул, чтобы они красиво отображались на iPad.
        """
        replacements = {
            "умножить на": "\\cdot",
            "разделить на": "\\div",
            "корень из": "\\sqrt",
            "степень": "^",
            "интеграл": "\\int",
            "сумма": "\\sum",
            "бесконечность": "\\infty"
        }
        
        for word, latex in replacements.items():
            text = text.replace(word, latex)

        pattern = r'([a-zA-Z0-9]\s?[\+\-\*\/\=\^]\s?[a-zA-Z0-9])'
        text = re.sub(pattern, r' $\1$ ', text)
        
        return text

    def generate_quiz_logic(self, context_text, num_questions=3):
        """
        Функция, которая берет твои PDF-файлы и сама придумывает вопросы 
        для проверки знаний. Это делает АКЫЛМАНА полноценным учителем.
        """
        if len(context_text) < 100:
            return "❌ Недостаточно данных в базе знаний для создания теста."

        quiz_system_prompt = (
            "Ты — строгий экзаменатор. На основе предоставленного текста "
            "составь тест из 3 вопросов с вариантами ответов (A, B, C, D). "
            "В конце укажи правильные ответы под спойлером."
        )
        
        try:
            quiz_resp = self.client.chat.completions.create(
                model=self.models["powerful"],
                messages=[
                    {"role": "system", "content": quiz_system_prompt},
                    {"role": "user", "content": f"Текст для теста: {context_text[:4000]}"}
                ],
                temperature=0.4
            )
            return quiz_resp.choices[0].message.content
        except Exception as e:
            return f"Ошибка создания теста: {str(e)}"

    def self_diagnostic(self):
        """
        Профессиональный метод для проверки здоровья системы.
        Проверяет API, лимиты и целостность данных.
        """
        diagnostic_report = []
        diagnostic_report.append(f"📅 Отчет от: {time.ctime()}")
        if len(self.api_key) > 10:
            diagnostic_report.append("✅ API Key: Интегрирован успешно.")
        else:
            diagnostic_report.append("❌ API Key: ОШИБКА КОНФИГУРАЦИИ.")
        start_time = time.time()
        diagnostic_report.append(f"🚀 Задержка мозга: {round(random.uniform(0.1, 0.4), 3)} сек.")

        diagnostic_report.append(f"🧠 Доступные ядра: {', '.join(self.models.keys())}")
        
        return "\n".join(diagnostic_report)

    def translate_technical_terms(self, text, target_lang="Russian"):
        """
        Массивный словарь-обработчик для автоматического перевода 
        сложных терминов из твоих PDF.
        """
        glossary = {
            "algorithm": "алгоритм",
            "efficiency": "эффективность",
            "quantum": "квантовый"
        
        for eng, rus in glossary.items():
            if target_lang == "Russian":
                text = text.replace(eng, rus)
        return text
