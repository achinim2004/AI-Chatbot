import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# API key eka load karanna
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

st.set_page_config(page_title="Gemini Chatbot", page_icon="💬")
st.title("💬 My Gemini Chatbot")

# Model eka setup
if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
else:
    st.error("API Key eka .env file eke naha! Poddak check karanna.")

# History eka save karanna
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat message eka pennanna
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).markdown(msg["content"])

# User input eka
if prompt := st.chat_input("Monawada ahanne?"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # AI eke uththara eka
    response = model.generate_content(prompt)
    with st.chat_message("assistant"):
        st.markdown(response.text)
    st.session_state.messages.append({"role": "assistant", "content": response.text})