import streamlit as st
from utility.helper import apikey
import openai


def get_job_requirements(text):
    # Authentication
    openai.api_key = apikey
    openai.Engine.list()

    # Prompt writing
    separator = '#########'
    newline = '\n'
    instruction = 'Tell me all the skills and experience required for the job above.'
    prompt = text + newline + separator + newline + instruction

    # Call the API
    completion = openai.Completion.create(engine='davinci-instruct-beta',
                                          temperature=0.1,
                                          prompt=prompt,
                                          max_tokens=300)
    result = completion['choices'][0]['text']

    return result


def get_job_experience_year(text):
    # Authentication
    openai.api_key = apikey
    openai.Engine.list()

    # Prompt writing
    separator = '#########'
    newline = '\n'
    instruction = 'Tell me the number of years of experience required for the job above:'
    prompt = text + newline + separator + newline + instruction

    # Call the API
    completion = openai.Completion.create(engine='davinci-instruct-beta',
                                          temperature=0.1,
                                          prompt=prompt,
                                          max_tokens=30)
    result = completion['choices'][0]['text']

    return result


def app():
    # A text area where text can be input manually
    text = st.text_area('Job Ad:', '', key='text', height=600)
    button = st.button('Analyze')
    if button:
        st.write('Skills and experience required:')
        st.write(get_job_requirements(text))
        st.write('')
        st.write('Number of years of experience required: {}'.format(get_job_experience_year(text)))


