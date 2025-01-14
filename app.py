from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

import streamlit as st
import os
import pathlib
import textwrap

import google.generativeai as genai

def to_markdown(text):
    text = text.replace('•', '*')
    return textwrap.indent(text, '> ')

os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load OpenAI model and get responses

def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

## initialize our streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Gemini Application")

input_text = st.text_input("Input: ", key="input")

submit = st.button("Ask the question")

## If ask button is clicked

if submit:
    response = get_gemini_response(input_text)
    st.subheader("The Response is")
    st.markdown(to_markdown(response))
