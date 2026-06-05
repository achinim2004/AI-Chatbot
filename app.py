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
st.set_page_config(page_title="Nova Chat", page_icon="⚡", layout="centered")

# Inject Custom CSS for Premium Design & Google Font
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');

    /* Global font override */
    html, body, [class*="css"], .stMarkdown {
        font-family: 'Outfit', sans-serif;
    }

    /* Custom main title gradient style */
    .gradient-text {
        background: linear-gradient(135deg, #FF2E93, #7F00FF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        font-size: 2.8rem;
        margin-bottom: 0px;
        padding-bottom: 5px;
        letter-spacing: -0.5px;
    }

    /* Subtitle styling */
    .subtitle {
        color: #8A8A9D;
        font-size: 1.1rem;
        margin-top: -10px;
        margin-bottom: 30px;
        font-weight: 400;
    }

    /* Smooth animated border for Chat Input container */
    div[data-testid="stChatInput"] {
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        background-color: rgba(255, 255, 255, 0.02) !important;
        backdrop-filter: blur(12px);
        transition: all 0.3s ease-in-out;
    }

    /* Pulse effect on focus */
    div[data-testid="stChatInput"]:focus-within {
        border-color: #7F00FF !important;
        box-shadow: 0 0 18px rgba(127, 0, 255, 0.3) !important;
    }
    
    /* Sleek badge styling */
    .model-badge {
        background: rgba(127, 0, 255, 0.1);
        border: 1px solid rgba(127, 0, 255, 0.2);
        color: #C084FC;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        display: inline-block;
        margin-bottom: 25px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header layout with premium styling
st.markdown('<h1 class="gradient-text">⚡ Nova Chat</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">A lightning-fast conversational partner</p>', unsafe_allow_html=True)
st.markdown('<div class="model-badge">Model: Llama 3.3 70B (Groq API)</div>', unsafe_allow_html=True)

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
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Capture user input from the chat bar
if prompt := st.chat_input("How can I help you today?"):
    # Display and save user's message
    with st.chat_message("user"):
        st.markdown(prompt)
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