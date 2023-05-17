import streamlit as st

# Header
st.header('Info about data')
st.header('Data description')

# Application title
st.title('Mi primer app con streamlit')

sidebar = st.sidebar
sidebar.title('This is lateral sidebar')
sidebar.write('Input elements')

st.write("""

Este es un simple ejemplo de una app para predecir

¡Esta app predice mis datos!
 """)

 


