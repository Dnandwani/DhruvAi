from dotenv import load_dotenv
load_dotenv()  
import streamlit as st
import os
import google.generativeai as genai




genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel(model_name="gemini-2.5-pro")
chat = model.start_chat(history=[])


if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display previous chat messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input box
user_input = st.chat_input("Enter your message")

if user_input:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get model response
    response = model.invoke(user_input)
    bot_reply = response.content if hasattr(response, "content") else str(response)

    # Show assistant message
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    with st.chat_message("assistant"):
        st.markdown(bot_reply)


st.set_page_config(page_title="Dhruv Ai")

custom_html = """
<style>
    .main-title {
        width: 100%;
        text-align: center;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-weight: 800;
        font-size: 75px;
        background: linear-gradient(90deg, #4285F4, #8E44AD, #E91E63, #FF5252);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-top: 10px;
        margin-bottom: 10px;
    }
</style>

<div class="main-title">
    DhruvAi
</div>
"""
st.markdown(custom_html, unsafe_allow_html=True)



user_input = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    full_response = ""
    for chunk in response:
        full_response += chunk.text
    return full_response

if submit and user_input:
    st.subheader("The Response is")
    answer = get_gemini_response(user_input)
    st.write(answer)
