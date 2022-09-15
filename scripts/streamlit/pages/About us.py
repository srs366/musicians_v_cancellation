import streamlit as st

#set page config
st.set_page_config(page_title="About us", page_icon=":tada:", layout="wide", initial_sidebar_state="expanded")

#create a title and center it
st.title("About us")

st.text("""
        This research project was conducted as part of the
        Le Wagon Data Science Bootcamp (July-September 2022)
        """)

st.text("Team Members (left to right): Stefan Sujanthakumar, Afiq Hamidon, Mischa Dhar, Huseyin Cenkci, Jiwon Shin")

# st.markdown(
# """
# <style>
# .st-fo {
#     width:400px;
#     position: center
# }
# </style>
# """,
# unsafe_allow_html=True
# )

st.text("\n\n\nWith huge thanks to Catriona Beamish, Charlotte Holcombe, Oliver Giles, Julio Quintana, and Mark Botteril")
