import streamlit as st

st.title('Student Dashboard')
st.header('Volunteer hours completed:')
st.text('40/40')
progress_bar = st.progress(0)
for i in range(40):
    progress_bar.progress(i + 1)
    time.sleep(0.1)
st.header('Top 6 courses:')
