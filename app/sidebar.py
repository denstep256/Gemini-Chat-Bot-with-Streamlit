import streamlit as st
from app.AImodel import gemini_MODELS


def render_sidebar():
    """ Отрисовка боковой панели с выбором модели и роли. """
    st.sidebar.header("Чат-бот Gemini")
    selected_model = st.sidebar.selectbox('Выберите модель Gemini:', list(gemini_MODELS.keys()))
    st.session_state.llm = gemini_MODELS[selected_model]

    roles = ['user', 'assistant', 'customer', 'support', 'expert', 'friend']
    selected_role = st.sidebar.selectbox('Выберите роль:', roles)

    if selected_role != st.session_state.role:
        st.session_state.role = selected_role
        if selected_role != "user":  # Сообщение о смене роли не добавляется для "user"
            st.session_state.chat_dialogue.append(
                {"role": "system", "content": f"Модель теперь будет в роли {selected_role}."}
            )