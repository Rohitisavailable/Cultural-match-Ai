
# CultureMatch AI - Streamlit App

import streamlit as st
import requests
import os
from dotenv import load_dotenv
load_dotenv() 
QLOO_API_KEY = os.getenv("QLOO_API_KEY")
 


QLOO_BASE_URL = "https://api.qloo.com"  
HEADERS = {
    "x-api-key": QLOO_API_KEY,
    "Content-Type": "application/json"
}


def get_gpt_response(prompt):
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    if not OPENAI_API_KEY:
        return "OpenAI API key not found. Please set the OPENAI_API_KEY environment variable."

    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    json_data = {
        "model": "gpt-4",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=json_data)

    try:
        return response.json()["choices"][0]["message"]["content"]
    except (KeyError, IndexError):
        return "Error: Invalid response from GPT API. Please check your API key or request format."

# Streamlit UI
st.set_page_config(page_title="CultureMatch AI", page_icon="🌍", layout="centered")

st.markdown(
    "<h1 style='text-align: center;'>🌍 CultureMatch AI</h1>",
    unsafe_allow_html=True,
)
st.markdown("**Personalized cultural recommendations using Qloo Taste API + GPT-4**")

user_input = st.text_input("Enter your favorite artist, movie, or book:", "")
location = st.text_input("Optional: Enter your city for local suggestions", "")

if st.button("Get Cultural Match"):
    if user_input:
        prompt = f"Give personalized cultural recommendations based on the interest: '{user_input}'"
        if location:
            prompt += f" and make it relevant to the city: {location}."
        else:
            prompt += "."
        output = get_gpt_response(prompt)
        st.success(output)
    else:
        st.warning("Please enter your interest to get recommendations.")
