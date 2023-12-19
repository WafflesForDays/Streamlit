import streamlit as st
import time

col1, col2 = st.columns(2, gap = "small")
st.set_page_config(layout = "wide")
st.title('Student Dashboard')
with col1:
    st.header('Volunteer hours completed:')
    st.text('40/40')
with col2:
    progress_bar = st.progress(0, use_column_width = True)
for i in range(100):
    progress_bar.progress(i + 1)
    time.sleep(0.01)
expanderCourses = st.expander(label = 'Show Courses')
with expanderCourses:
    clicked = col1.header('Top 6 courses:')



