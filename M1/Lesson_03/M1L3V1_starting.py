# import packages
import streamlit as st
import pandas as pd
import re
import os


# Helper function to get dataset path
def get_dataset_path():
    # Get the current script directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the path to the CSV file
    csv_path = os.path.join(current_dir, "..", "..", "data", "customer_reviews.csv")
    return csv_path


st.title("Hello, GenAI!")
st.write("This is your GenAI-powered data processing app.")

# Layout two buttons side by side
col1, col2 = st.columns(2)

with col1:
    if st.button("Ingest Dataset"):
        pass

with col2:
    if st.button("Parse Reviews"):
        pass
