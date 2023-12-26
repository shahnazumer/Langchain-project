# Q&A Chatbot

from langchain.llms import OpenAI
from dotenv import load_dotenv
import streamlit as st
import os


load_dotenv()  # take environment variables from .env.

# Function to load OpenAI model and get response
def get_openai_response(question):
    # Pass the openai_api_key as a named parameter or set it as an environment variable
    llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"), model_name="gpt-3.5-turbo-instruct", temperature=0.5)
    response = llm(question)
    return response

# Initialize our Streamlit app
st.set_page_config(page_title="Q&A")
st.header("Langchain Application")

# Get user input
input = st.text_input("Input: ", key="input")

# Get OpenAI response when the "Ask the question" button is clicked
submit = st.button("Ask the question")

# If ask button is clicked
if submit:
    # Ensure there is input before getting a response
    if input:
        st.subheader("The Response is")
        response = get_openai_response(input)
        st.write(response)
    else:
        st.warning("Please enter a question before clicking the 'Ask the question' button.")