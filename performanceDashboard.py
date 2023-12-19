import streamlit as st
import time

st.title('Student Dashboard')
st.header('Volunteer hours completed:')
st.text('40/40')
progress_bar = st.progress(0)
for i in range(100):
    progress_bar.progress(i + 1)
    time.sleep(0.01)
st.header('Top 6 courses:')
