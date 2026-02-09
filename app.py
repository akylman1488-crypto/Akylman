import brain
import storage
import interface
import effects
import behavior

def main():
    interface.print_header()
    
    history = storage.load_history()
    
    if not history:
        opener = behavior.get_opener()
        effects.type_writer(f"Akylman: {opener}")
        history.append({"role": "assistant", "content": opener})
        storage.save_history(history)
    else:
        last_role = history[-1]["role"]
        if last_role == "user":
            effects.show_loader()
            response = brain.generate_response(history)
            effects.type_writer(f"Akylman: {response}")
            history.append({"role": "assistant", "content": response})
            storage.save_history(history)
        else:
            effects.type_writer("Akylman: Я помню, на чем мы остановились. Продолжим?")

    while True:
        try:
            user_text = interface.get_user_input()
            
            if user_text.lower() in ["выход", "exit", "quit"]:
                effects.type_writer("Akylman: Хорошо, я на связи. До встречи!")
                break
                
            if user_text.lower() == "/reset":
                storage.clear_history()
                history = []
                effects.type_writer("Akylman: Память очищена. Начнем с чистого листа!")
                continue

            history.append({"role": "user", "content": user_text})
            storage.save_history(history)

            effects.show_loader()
            
            ai_response = brain.generate_response(history)
            
            effects.type_writer(f"Akylman: {ai_response}")
            
            history.append({"role": "assistant", "content": ai_response})
            storage.save_history(history)

        except KeyboardInterrupt:
            print("\n")
            effects.type_writer("Akylman: Экстренное завершение. Я сохраню контекст.")
            break

if __name__ == "__main__":
    main()
