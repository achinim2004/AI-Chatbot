import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Configure the Streamlit page
st.set_page_config(page_title="Gemini Chatbot", page_icon="💬")
st.title("💬 My Gemini Chatbot")

# Model Setup
if api_key:
    genai.configure(api_key=api_key)
    # Initialize the model with the specific version
    model = genai.GenerativeModel("models/gemini-1.5-flash")
else:
    # Error handling if API key is missing
    st.error("API Key not found in .env file. Please configure it.")
    st.stop()

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages from history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).markdown(msg["content"])

# Process user input
if prompt := st.chat_input("How can I help you today?"):
    # Add user message to display and history
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Generate AI response
    try:
        # Generate content from the model
        response = model.generate_content(prompt)
        
        # Display assistant response
        with st.chat_message("assistant"):
            st.markdown(response.text)
        
        # Add assistant message to history
        st.session_state.messages.append({"role": "assistant", "content": response.text})
        
    except Exception as e:
        # Handle potential API errors
        st.error(f"An error occurred: {e}")