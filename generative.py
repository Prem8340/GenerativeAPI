"""
pip install virtualenv
python -m venv myenv
myenv\Scripts\activate
"""

import streamlit as st
import openai

# set you API key
#openai.api_key=st.secrets["openai_api"]
openai.api_key="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"

st.title("Generative AI")

# input text box
prompt=st.text_area("Enter a prompt:")
def generate_text(prompt):
    response=openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1200
    )
    return response.choices[0].text

# button to generate text
if st.button("Generate"):
    if prompt:
        generate_text=generate_text(prompt)
        st.write("Generate Text")
        st.write(generate_text)
    else: 
        st.warning("Please enter your prompt")   





