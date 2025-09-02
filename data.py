# hello_app.py

import streamlit as st

# Title of the app
st.title("👋 Hello Streamlit!")

# Text input
name = st.text_input("Enter your name:")

# Button and response
if st.button("Say Hello"):
    if name:
        st.success(f"Hello, {name}! Welcome to Streamlit. 🎉")
    else:
        st.warning("Please enter your name first.")
