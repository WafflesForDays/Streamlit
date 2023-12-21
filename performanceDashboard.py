import streamlit as st
import time

st.title('Student Dashboard')
col1, col2, col3 = st.beta_columns([6, 1, 6])
with col1:
    st.text('')
with col2:
    st.header('Volunteer hours completed:')
    st.text('40/40')
with col3:
    for i in range(7):
        st.text('')
    progress_bar = st.progress(0)
for i in range(100):
    progress_bar.progress(i + 1)
    time.sleep(0.01)
expanderCourses = st.expander(label = 'Show Courses')
with expanderCourses:
    clicked = col1.header('Top 6 courses:')



