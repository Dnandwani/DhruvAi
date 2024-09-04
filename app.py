from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Load environment variables
load_dotenv() 

# Configure the Gemini Pro model
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

# Set up page configuration
st.set_page_config(page_title="DhruvAi", page_icon="🤖", layout="centered")

# Custom CSS for enhanced UI
st.markdown("""
    <style>
        /* Background and text styling */
        body {
            background-color: #1E1E1E;
            color: #E8E8E8;
        }
        .stApp {
            background-color: #1E1E1E;
        }
        /* Header styling */
        h1 {
            color: #00ADB5;
            font-family: 'Roboto', sans-serif;
        }
        /* Input box styling */
        .stTextInput div {
            background-color: #333333;
            color: #E8E8E8;
        }
        /* Button styling */
        .stButton button {
            background-color: #00ADB5;
            color: #ffffff;
            border-radius: 5px;
            font-size: 16px;
            border: none;
            padding: 10px 20px;
            cursor: pointer;
        }
        .stButton button:hover {
            background-color: #007B7F;
            color: #ffffff;
        }
        /* Subheader styling */
        h2 {
            color: #F5A623;
            font-family: 'Roboto', sans-serif;
        }
    </style>
""", unsafe_allow_html=True)

# Page header
st.header("DhruvAi")

# Input field and submit button
input = st.text_input("Ask me anything:", key="input")
submit = st.button("Ask the question")

# Display the response
if submit:
    response = get_gemini_response(input)
    st.write(response)
