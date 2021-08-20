import streamlit as st
from utility.helper import apikey
import openai


def get_pros_and_cons(text):
    # Authentication
    openai.api_key = apikey
    openai.Engine.list()

    # Prompt writing
    separator = '#########'
    newline = '\n'
    instruction = 'Please summarize the pros and cons for the product above, ' \
                  'but please do not repeat the same point twice:'
    prompt = text + separator + newline + instruction

    # Call the API
    completion = openai.Completion.create(engine='davinci-instruct-beta',
                                          temperature=0.3,
                                          prompt=prompt,
                                          max_tokens=300)
    result = completion['choices'][0]['text']

    return result


def app():
    # A text area where text can be input manually
    text = st.text_area('Reviews:', '', key='text', height=600)
    button = st.button('Analyze')
    if button:
        st.write(get_pros_and_cons(text))
