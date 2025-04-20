import streamlit as st
from app.AImodel import gemini_MODELS

DEFAULT_ROLE = "user"

def setup_session_state():
    """ Инициализация session_state при первом запуске. """
    if "chat_dialogue" not in st.session_state:
        st.session_state.chat_dialogue = []
    if "llm" not in st.session_state:
        st.session_state.llm = gemini_MODELS["gemini-pro"]
    if "role" not in st.session_state:
        st.session_state.role = DEFAULT_ROLE
    if "first_message_sent" not in st.session_state:
        st.session_state.first_message_sent = False  # Флаг, чтобы бот не отвечал на "Обо мне"

def send_intro_message():
    """ Отправка сообщения 'Обо мне' при первом запуске без генерации ответа. """
    if not st.session_state.first_message_sent:
        about_message = "Я чат-бот Gemini, созданный для общения и помощи в различных вопросах."
        st.session_state.chat_dialogue.append({"role": "assistant", "content": about_message})
        st.session_state.first_message_sent = True
