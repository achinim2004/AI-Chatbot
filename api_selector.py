import streamlit as st
from groq import Groq
import os

def get_groq_client():
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

    # Render selector in sidebar
    st.sidebar.title("API Configuration")
    api_choice = st.sidebar.radio(
        "Choose your API option:",
        ["Try Free Trial", "Use Your Own Groq API Key"]
    )

    api_key = None

    if api_choice == "Use Your Own Groq API Key":
        # Text input field for user's key
        user_key = st.sidebar.text_input("Enter your Groq API Key:", type="password")
        if user_key:
            api_key = user_key
        else:
            st.sidebar.warning("Please enter your Groq API Key to proceed.")
            st.stop()
    else:
        # Fallback to the developer's backend key for Free Trial
        if backend_key:
            api_key = backend_key
        else:
            st.sidebar.error("Free trial key is not configured. Please enter your own API key.")
            st.stop()

    # Return the initialized Groq client
    return Groq(api_key=api_key)
