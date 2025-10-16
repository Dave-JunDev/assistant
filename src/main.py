import streamlit as st

from context.views.sidebar import render_sidebar
from context.views.chat import render_chat
from utils.chatbot import Chatbot
from context.engine.db import db_manager

chatbot = Chatbot()
db = db_manager()
db.init_db()

render_sidebar(chatbot, db)
render_chat(chatbot, db)