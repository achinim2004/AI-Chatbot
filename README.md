# 💬 Nova Chat

A modern, lightweight, and interactive web-based AI Chatbot built using **Streamlit** and powered by the **Google Gemini API** (using the `gemini-1.5-flash` model). This chatbot supports conversation memory (chat history) and real-time streaming-like user experience.

---

## 🚀 Live Demo
🌐 **[View Live Demo](https://your-live-demo-link.streamlit.app)** *(Replace this URL with your actual deployed Streamlit Cloud URL)*

---

## ✨ Features
* 🧠 **Conversation Memory:** Remembers past messages in the current session so you can have back-and-forth conversations.
* ⚡ **Fast & Responsive:** Utilizes `gemini-1.5-flash` for super-fast response generation.
* 🎨 **Clean UI:** Built with Streamlit's native chat elements for a clean and responsive messaging interface.
* 🇱🇰 **Localizations:** Customized prompts and error descriptions in Sinhala.
* 🛡️ **Robust Error Handling:** Detects API rate limits (HTTP 429) and displays clear instructions for the user.

---

## 🛠️ Tech Stack
* **Framework:** [Streamlit](https://streamlit.io/)
* **AI Model:** [Google Gemini API](https://ai.google.dev/) (`gemini-1.5-flash`)
* **Environment Management:** `python-dotenv`

---

## ⚙️ Installation & Setup

Follow these steps to run the project locally on your machine:

### 1. Clone or Open the Directory
Navigate to your project folder:
```bash
cd d:/Web_Projects/AI_Chatbot
```

### 2. Set Up a Virtual Environment (Optional but Recommended)
Create and activate a virtual environment to manage dependencies:

* **Windows:**
  ```powershell
  python -m venv venv
  .\venv\Scripts\activate
  ```
* **Mac/Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Install Dependencies
Install all the required python packages:
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory (already done for this project) and add your Google Gemini API key:
```env
GEMINI_API_KEY=your_actual_api_key_here
```
> ⚠️ **Important:** Do not commit your `.env` file containing your API key to public repositories. Make sure it is added to your `.gitignore`.

### 5. Run the Chatbot
Start the Streamlit development server:
```bash
streamlit run app.py
```

Streamlit will launch a local development server and open the app in your default web browser (typically at `http://localhost:8501`).

---

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).
