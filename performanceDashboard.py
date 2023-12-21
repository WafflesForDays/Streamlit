import streamlit as st
import time

st.title('Student Dashboard')
col1a, col2a, col3a = st.columns([0.45, 0.1, 0.45])
with col1a:
       st.subheader('Volunteer hours completed:')
with col2a:
    st.text('')
    st.text('')
    st.text('')
    st.text('40/40')
with col3a:
    for i in range(7):
        st.text('')
    progress_bar = st.progress(0)
for i in range(100):
    progress_bar.progress(i + 1)
    time.sleep(0.01)
expanderCourses = st.expander(label = 'Show Courses')
with expanderCourses:
    clicked = st.header('Top 6 courses:')



