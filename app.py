from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize Gemini Pro model
model = genai.GenerativeModel("gemini-pro")

# Start a chat session (this can persist across messages)
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

# Streamlit page settings
st.set_page_config(page_title="Q&A with Gemini")
st.header("💬 Gemini Pro Q&A App")

# Chat input
user_input = st.text_input("Ask something:", key="input")

# Button to send query
if st.button("Submit") and user_input:
    with st.spinner("Thinking..."):
        response = st.session_state.chat_session.send_message(user_input, stream=True)
        full_response = ""
        for chunk in response:
            full_response += chunk.text
            st.write(chunk.text)

        # Store in session state
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []

        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Gemini", full_response))

# Display chat history
if "chat_history" in st.session_state:
    st.subheader("🕓 Chat History")
    for role, text in st.session_state.chat_history:
        st.markdown(f"**{role}:** {text}")
