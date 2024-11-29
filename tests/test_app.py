import streamlit as st

if "counter" not in st.session_state:
    st.session_state.counter = 0

if st.button("mais"):
    st.session_state.counter += 1   
if st.button("menos"):
    st.session_state.counter -= 1
st.header(f"This page has run {st.session_state.counter} times.")
