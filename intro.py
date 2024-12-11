import streamlit as st

st.title("Hello Streamlit!")
st.write("This is a basic test app and its working fine now.")

agree = st.checkbox("I agree with Subash")

if agree:
    st.write("Great!")