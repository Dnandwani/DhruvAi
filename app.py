from dotenv import load_dotenv
load_dotenv()  

import streamlit as st
import os
import google.generativeai as genai


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel(model_name="gemini-2.5-pro")
chat = model.start_chat(history=[])


st.set_page_config(page_title="DhruvAi")

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
