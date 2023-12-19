import streamlit as st

progress_bar = st.progress(0)
st.title('Student Dashboard')
st.header('Volunteer hours completed')
for i in range(40):
    progress_bar.progress(i + 1)
st.header('Top 6 courses:')
