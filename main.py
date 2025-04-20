from pyngrok import ngrok
import google.generativeai as genai
from app.chatbot import render_chat_history, handle_user_input
from app.setup_session import setup_session_state, send_intro_message
from config import GEMINI_TOKEN
from app.sidebar import render_sidebar
import streamlit as st


def start_ngrok():
    public_url = ngrok.connect('8501')  # Streamlit по умолчанию работает на порту 8501
    st.write(f"Твоё приложение доступно по ссылке: {public_url}")

genai.configure(api_key=GEMINI_TOKEN)

# Установка начальной конфигурации страницы
st.set_page_config(
    page_title="Gemini_chat",
    layout="wide"
)

setup_session_state()
send_intro_message()
render_sidebar()
render_chat_history()
handle_user_input()