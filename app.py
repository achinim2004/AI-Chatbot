import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

st.set_page_config(page_title="Gemini Chatbot", page_icon="💬")
st.title("💬 My Gemini Chatbot")

if api_key:
    genai.configure(api_key=api_key)
    # 1.5 Flash use karamu
    model = genai.GenerativeModel("gemini-1.5-flash")
else:
    st.error("API Key eka .env file eke naha!")

# User input eka
if prompt := st.chat_input("Monawada ahanne?"):
    st.chat_message("user").markdown(prompt)
    
    # AI response (History eka yawanne nathuwa direct ahanawa)
    try:
        response = model.generate_content(prompt)
        with st.chat_message("assistant"):
            st.markdown(response.text)
    except Exception as e:
        st.error(f"Error ekak awa: {e}")