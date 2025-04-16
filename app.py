from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure API
genai.configure(api_key=GOOGLE_API_KEY)

# Load model
model = genai.GenerativeModel("gemini-pro")

# Streamlit UI
st.set_page_config(page_title="Gemini Pro QA")
st.title("💬 Chat with Gemini Pro")

# User input
user_input = st.text_input("Ask me anything:")

# Generate response
if st.button("Send") and user_input:
    try:
        response = model.generate_content(user_input)
        st.markdown("### 🤖 Response")
        st.write(response.text)
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
