import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Page configuration
st.set_page_config(page_title="Gemini Chatbot", page_icon="💬")
st.title("💬 My Gemini Chatbot")

# Model setup
if api_key:
    genai.configure(api_key=api_key)
    # Using 1.5-flash as it is more stable for free tier
    model = genai.GenerativeModel("gemini-1.5-flash")
else:
    st.error("API Key not found in .env file!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).markdown(msg["content"])

# React to user input
if prompt := st.chat_input("How can I help you today?"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Get AI response
    try:
        response = model.generate_content(prompt)
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        st.error(f"An error occurred: {e}")