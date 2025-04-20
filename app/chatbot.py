import streamlit as st


HIDDEN_PROMPT_TEMPLATE = "Отвечай так, будто ты в роли {}."


def render_chat_history():
    """ Отрисовка истории сообщений в чате. """
    for message in st.session_state.chat_dialogue:
        with st.chat_message(message["role"] if message["role"] != "system" else "assistant"):
            st.markdown(message["content"])

def handle_user_input():
    """ Обработка ввода пользователя. """
    user_input = st.chat_input("Type your question here to talk to Gemini")
    if user_input:
        # Добавляем скрытый промпт только если роль не "user"
        if st.session_state.role == "user":
            full_input = user_input
        else:
            hidden_prompt = HIDDEN_PROMPT_TEMPLATE.format(st.session_state.role)
            full_input = f"{hidden_prompt}\n{user_input}"

        st.session_state.chat_dialogue.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        generate_assistant_response(full_input)

def generate_assistant_response(user_message):
    """ Генерация ответа от нейросети. """
    message_placeholder = st.empty()
    full_response = ""

    # Формируем строку диалога
    string_dialogue = "\n".join([f"{msg['role'].capitalize()}: {msg['content']}"
                                 for msg in st.session_state.chat_dialogue if msg["role"] != "system"])

    # Добавляем последний запрос пользователя
    string_dialogue += f"\nUser: {user_message}"

    # Вызываем модель
    output = st.session_state.llm.generate_content(string_dialogue)
    generated_text = output.text if output else ""

    # Проверяем, что модель вернула текст
    if not generated_text:
        return

    for item in generated_text:
        full_response += item
        message_placeholder.markdown(full_response + "▌")

    message_placeholder.markdown(full_response)
    st.session_state.chat_dialogue.append({"role": "assistant", "content": full_response})