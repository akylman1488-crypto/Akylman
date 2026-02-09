import google.generativeai as genai
import config

genai.configure(api_key=config.GOOGLE_API_KEY)

def generate_response(history):
    model = genai.GenerativeModel(
        model_name=config.MODEL_NAME,
        system_instruction=config.SYSTEM_PROMPT
    )
    
    formatted_history = []
    for msg in history[:-1]:
        role = "user" if msg["role"] == "user" else "model"
        formatted_history.append({"role": role, "parts": [msg["content"]]})
    
    chat_session = model.start_chat(history=formatted_history)
    
    try:
        last_message = history[-1]["content"]
        response = chat_session.send_message(last_message)
        return response.text
    except Exception as e:
        return f"Ошибка: {str(e)}"
