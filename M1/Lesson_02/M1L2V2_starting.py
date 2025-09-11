# import packages
from dotenv import load_dotenv
from openai import OpenAI
import streamlit as st


@st.cache_data
def get_response(user_prompt, temperature):
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[{"role": "user", "content": user_prompt}],  # Prompt
        temperature=temperature,  # A bit of creativity
        max_output_tokens=100,  # Limit response length
    )
    return response


# load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
client = OpenAI()

st.title("Hello, GenAI!")
st.write("This is your first Streamlit app.")

# Add a text input box for the user prompt
user_prompt = st.text_input(
    "Enter your prompt:", "Explain generative AI in one sentence."
)

# Add a slier for temperature
temperature = st.slider(
    "Model temperature:",
    min_value=0.0,
    max_value=1.0,
    value=0.7,
    step=0.01,
    help="Controls reandomness: 0 = deterministic, 1 = very creative",
)

with st.spinner("AI is working..."):
    response = get_response(user_prompt, temperature)

    # print the response from OpenAI
    st.write(response.output_text)
