import streamlit as st
from groq import Groq
import os

def get_groq_client():
    # If client is already set, display "Change API" button in sidebar and return client
    if "groq_client" in st.session_state and st.session_state.groq_client is not None:
        if st.sidebar.button("Reset / Change API Key"):
            st.session_state.groq_client = None
            st.session_state.messages = []  # Reset messages for privacy
            st.rerun()
        return st.session_state.groq_client

    # 1. Attempt to get the backend API Key from Streamlit Secrets or .env (default for free trial)
    backend_key = None
    try:
        if "GROQ_API_KEY" in st.secrets:
            backend_key = st.secrets["GROQ_API_KEY"]
    except Exception:
        pass

    if not backend_key:
        from dotenv import load_dotenv
        load_dotenv()
        backend_key = os.getenv("GROQ_API_KEY")

    # Render selector on the main page
    st.subheader("Select an API option to begin:")
    api_choice = st.radio(
        "Option:",
        ["Try Free Trial", "Use Your Own Groq API Key"],
        label_visibility="collapsed"
    )

    if api_choice == "Use Your Own Groq API Key":
        user_key = st.text_input("Enter your Groq API Key:", type="password")
        submit_button = st.button("Submit Key")
        
        if submit_button and user_key:
            st.session_state.groq_client = Groq(api_key=user_key)
            st.rerun()
        else:
            st.stop()  # Wait for user input
    else:
        # Free Trial Option
        submit_button = st.button("Start Chatting (Free Trial)")
        if submit_button:
            if backend_key:
                st.session_state.groq_client = Groq(api_key=backend_key)
                st.rerun()
            else:
                st.error("Free trial key is not configured. Please enter your own API key.")
                st.stop()
        else:
            st.stop()  # Wait for user to click the start button
