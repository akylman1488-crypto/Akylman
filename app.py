import streamlit as st
import brain
import behavior
import storage

def main():
    import interface
    interface.init_page()
    
    if not st.session_state.messages:
        opener = behavior.get_opener()
        st.session_state.messages.append({"role": "assistant", "content": opener})
        storage.save_history(st.session_state.messages)

    interface.display_chat()

    if prompt := st.chat_input("Напиши что-нибудь..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            response = brain.generate_response(st.session_state.messages)
            st.markdown(response)
        
        st.session_state.messages.append({"role": "assistant", "content": response})
        storage.save_history(st.session_state.messages)

if __name__ == "__main__":
    main()
