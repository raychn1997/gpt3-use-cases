import streamlit as st
import job_parser
import review_summarizer


PAGES = {
    'Job Parser': job_parser,
    'Review Summarizer': review_summarizer
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio('Go to', list(PAGES.keys()))
page = PAGES[selection]
page.app()
