import streamlit as st

st.set_page_config(layout="wide")

col1,col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Wang Yanghuijing")
    content = """"
    Hi, I am Leo, I am a python programmer.I graduated in 2024 with 
    Computer Science major from the University of Victoria.
    
    """
    st.info(content)