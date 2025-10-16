import streamlit as st
from context.engine.db import db_manager
from context.models.conversation import conversation
from context.models.message import message
from utils.chatbot import Chatbot

def render_chat(chatbot : Chatbot, db : db_manager):
    st.title("Chat Interface")
    session = db.get_session()

    conversation_id = st.session_state.get("conversation_id", None)
    messages = session.query(message).filter_by(conversation_id=st.session_state.conversation_id).order_by(message.created_at).all()

    for msg in messages:
        with st.chat_message(msg.role):
            st.markdown(msg.content)

    if user_input := st.chat_input("Type your message here..."):
        st.chat_message("user").markdown(user_input)
        user_msg = message(content=user_input, role="user", conversation_id=conversation_id)
        session.add(user_msg)
        session.commit()

            # Here you would typically call your assistant model to get a response
        assistant_response = chatbot.get_response(user_input)
        with st.chat_message("assistant"):
            st.markdown(assistant_response)
        assistant_msg = message(content=assistant_response, role="assistant", conversation_id=conversation_id)
        session.add(assistant_msg)
        session.commit()
        st.rerun()

    db.close_session()