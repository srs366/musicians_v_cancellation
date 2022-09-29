import streamlit as st

#set page config
st.set_page_config(page_title="Background", page_icon=":tada:", layout="wide", initial_sidebar_state="expanded")

#create a title and center it
st.title("Background")

st.text("""
        Cancel culture can be defined as public backlash in relation to an offensive action. This results in calls to
        end the offender's career or cultural cachet (most often done through boycotts / seeking disciplinary action).

        Quantitative assessments of this phenomena are lacking and this project aims to provide an initial investigation
        into whether 'cancelling' is an effective course of action.
        """)

st.text("""Methodology:

    1) Defined cancellation events / dates for chosen musicans (based on domain knowledge & desk-research)
    2) Determined public sentiment (Tweet data) and music listening trends (Spotify monthly listener / radio
        play data) 6 months either side of these events
    3) Assessed whether public backlash coincided with a decrease in music consumption""")

st.text("""Data Sources:

    Streaming & radio play data were gathered from Chartmetric using their built in API. Tweets were scraped
    and then analysed for sentiment using the AI model RoBERTa.

    (RoBERTa is a model developed and trained by Meta that is specifically built for analysis of Tweets
    using self supervised Natural Language Processing""")
