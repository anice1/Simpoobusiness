import streamlit as st
import pandas as pd
import numpy as np

"""# A prototype for SimpooBusiness item recoginition app"""

# Project Description:
'''
The aim of this project is to enable _SimpooBusiness_ identify and validate customer image uploads.
'''
st.file_uploader("Upload an image to classify", type=["jpg", "png"])
st.balloons()


model = st.sidebar.selectbox("Select a problem", ("Sim-Sim", "Face Classification"))
if model == "Sim-Sim":
    st.sidebar.subheader(model)
    st.write("Model name:", model)
    st.markdown("""Sim-Sim is a prototype for item recognition.""")
elif model == "Random Forest":
    st.subheader("Random Forest Model")
    st.markdown("""
    This model is a probabilistic approach to classifying images. It is a non-linear classifier that uses a random forest to map the image data to a probability distribution.
    The random forest is a classification algorithm that uses a collection of decision trees to classify the data.
    The random forest is a classification algorithm that uses a collection of decision trees to classify the data.
    """)

col1, col2, col3 = st.columns(3)

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")


def form_callback():
    st.write(st.session_state.my_slider)
    st.write(st.session_state.my_checkbox)

with st.form(key='my_form'):
    slider_input = st.slider('My slider', 0, 10, 5, key='my_slider')
    checkbox_input = st.checkbox('Yes or No', key='my_checkbox')
    submit_button = st.form_submit_button(label='Submit', on_click=form_callback)