import streamlit as st
from context.engine.db import db_manager
from context.models.conversation import conversation
from context.models.message import message

def render_sidebar(chatbot):
    st.sidebar.title("Conversations")
    db = db_manager()
    session = db.get_session()

    conversations = session.query(conversation).order_by(conversation.created_at.desc()).all()

    options = {f"{conv.label}": conv.id for conv in conversations}
    selection = st.sidebar.selectbox("Select Conversation", options=list(options.keys()))
    conversation_id = options[selection]
    messages = session.query(message).filter_by(conversation_id=conversation_id).order_by(message.created_at).all()
    last_messages = messages[-10:] if len(messages) > 10 else messages

    if(len(last_messages) >= 10):
        chatbot.set_conversation_history(last_messages)

    if st.sidebar.button("New Conversation"):
        new_conv = conversation(label=f"Conversation {len(conversations) + 1}")
        session.add(new_conv)
        session.commit()
        st.session_state.conversation_id = new_conv.id
        chatbot.set_conversation_history([])
        st.rerun()

    if st.sidebar.button("Delete Conversations"):
        session.query(conversation).filter_by(id=conversation_id).delete()
        session.query(message).filter_by(conversation_id=conversation_id).delete()
        session.commit()
        st.session_state.conversation_id = None
        chatbot.set_conversation_history([])
        st.rerun()

    if "conversation_id" not in st.session_state or st.session_state.conversation_id != options[selection]:
        st.session_state.conversation_id = options[selection]
        st.rerun()

    db.close_session()