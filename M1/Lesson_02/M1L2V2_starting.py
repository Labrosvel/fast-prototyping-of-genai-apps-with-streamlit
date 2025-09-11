# import packages
from dotenv import load_dotenv
from openai import OpenAI
import streamlit as st

# load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
client = OpenAI()

st.title("Hello, GenAI!")
st.write("This is your first Streamlit app.")

response = client.responses.create(
    model="gpt-4.1-mini",
    input=[{"role": "user", "content": "Explain generative AI in one sentence."}],
    temperature=0.7,  # A bit of creativity
    max_output_tokens=100,  # Limit response length
)

st.write(response.output_text)
