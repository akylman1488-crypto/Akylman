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

    while True:
        try:
            user_text = interface.get_user_input()
            
            if user_text.lower() in ["выход", "exit"]:
                break
                
            history.append({"role": "user", "content": user_text})
            effects.show_loader()
            
            ai_response = brain.generate_response(history)
            effects.type_writer(f"Akylman: {ai_response}")
            
            history.append({"role": "assistant", "content": ai_response})
            storage.save_history(history)

        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()
