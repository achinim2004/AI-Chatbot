import streamlit as st
import google.generativeai as genai
import os

# 1. Attempt to get the API Key from Streamlit Secrets (for Cloud deployment)
# 2. If not found, fall back to .env file (for local development)
if "GEMINI_API_KEY" in st.secrets:
    api_key = st.secrets["GEMINI_API_KEY"]
else:
    from dotenv import load_dotenv
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")

# Configure the Streamlit page layout
st.set_page_config(page_title="Nova Chat", page_icon="💬")
st.title("💬 Nova Chat")

# Configure the Gemini model
if api_key:
    genai.configure(api_key=api_key)
    # Using the standard gemini-1.5-flash model
    model = genai.GenerativeModel("gemini-1.5-flash")
else:
    # Error message if the API key is not configured anywhere
    st.error("API Key not found! Please check your Secrets or .env file.")
    st.stop()

# Initialize chat history to store messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display all messages from the chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).markdown(msg["content"])

# Capture user input from the chat bar
if prompt := st.chat_input("How can I help you today?"):
    # Display and save user's message
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Generate response from Gemini API
    try:
        # Request content from the model
        response = model.generate_content(prompt)
        
        # Display assistant's response
        with st.chat_message("assistant"):
            st.markdown(response.text)
        
        # Save assistant's response to history
        st.session_state.messages.append({"role": "assistant", "content": response.text})
        
    except Exception as e:
        # Error handling for API issues
        st.error(f"An error occurred: {e}")