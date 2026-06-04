import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API Key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Page Config
st.set_page_config(page_title="Gemini Chatbot", page_icon="💬")
st.title("💬 My Gemini Chatbot")

# Setup Model
if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
else:
    st.error("API Key not found in .env file!")
    st.stop()

# Initialize Chat Session (Memory)
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# Display Chat History
for msg in st.session_state.chat.history:
    st.chat_message(msg.role).markdown(msg.parts[0].text)

# User Input
if prompt := st.chat_input("Monawada ahanne?"):
    st.chat_message("user").markdown(prompt)

    # Get AI Response
    try:
        with st.spinner("Gemini hithamin inne..."):
            response = st.session_state.chat.send_message(prompt)
            
        with st.chat_message("assistant"):
            st.markdown(response.text)
            
    except Exception as e:
        if "429" in str(e):
            st.error("Quota error: API key limit eka panala. Tikak wela idala aye try karanna!")
        else:
            st.error(f"Error ekak awa: {e}")