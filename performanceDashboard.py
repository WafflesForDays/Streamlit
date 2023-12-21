import streamlit as st
import time
from st_circular_progress import CircularProgress

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
    for i in range(3):
        st.text('')
    progress_bar = st.progress(0)
for i in range(100):
    progress_bar.progress(i + 1)
    time.sleep(0.01)
expanderCourses = st.expander(label = 'Show Courses')
with expanderCourses:
    clicked = st.header('Top 6 courses:')
    col1b, col2b, col3b = st.columns(3)
    with col1b:
        Math1 = CircularProgress(
            label="Advanced functions",
            value=96,
            key="Math1",
            color = "blue")
        
        Math1.st_circular_progress()

        English = CircularProgress(
            label="English",
            value=95,
            key="English",
            color = "red")
        
        English.st_circular_progress()

    with col2b:
        Math2 = CircularProgress(
            label="Calculus and Vectors",
            value=96,
            key="Math2",
            color = "blue")
        
        Math2.st_circular_progress()

        Physics = CircularProgress(
            label = "Physics",
            value = 96,
            key = "Physics",
            color = "orange")
        
        Physics.st_circular_progress()

    with col3b:
        cs = CircularProgress(
            label = "Computer Science",
            value = 100,
            key = "cs",
            color = "green")
        
        cs.st_circular_progress()

        Business = CircularProgress(
            label = "International Business",
            value = 100,
            key = "Business",
            color = "yellow")
        
        Business.st_circular_progress() 


