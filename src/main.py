from context.views.sidebar import render_sidebar
from context.views.chat import render_chat
import streamlit as st
from utils.chatbot import Chatbot
chatbot = Chatbot()

render_sidebar(chatbot)
render_chat(chatbot)