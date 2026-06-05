import streamlit as st
from groq import Groq
import os

# 1. Attempt to get the API Key from Streamlit Secrets (for Cloud deployment)
# 2. If not found, fall back to .env file (for local development)
api_key = None
try:
    if "GROQ_API_KEY" in st.secrets:
        api_key = st.secrets["GROQ_API_KEY"]
except Exception:
    pass

if not api_key:
    from dotenv import load_dotenv
    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY")

# Configure the Streamlit page layout
st.set_page_config(page_title="Nova Chat", page_icon="💬")
st.title("💬 Nova Chat")

# Initialize the Groq client
if api_key:
    client = Groq(api_key=api_key)
else:
    # Error message if the API key is not configured anywhere
    st.error("Groq API Key not found! Please check your Secrets or .env file.")
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

    # Generate response from Groq API
    try:
        # Request content from Llama 3.3 on Groq
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            model="llama-3.3-70b-versatile",
        )
        
        response_text = chat_completion.choices[0].message.content
        
        # Display assistant's response
        with st.chat_message("assistant"):
            st.markdown(response_text)
        
        # Save assistant's response to history
        st.session_state.messages.append({"role": "assistant", "content": response_text})
        
    except Exception as e:
        # Error handling for API issues
        st.error(f"An error occurred: {e}")