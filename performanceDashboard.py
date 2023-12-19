import streamlit as st
import time

col1, col2 = st.columns(2)
st.set_page_config(layout = "wide")
st.title('Student Dashboard')
col1.header('Volunteer hours completed:')
col1.text('40/40')
progress_bar = col2.progress(0, use_column_width = True)
for i in range(100):
    progress_bar.progress(i + 1)
    time.sleep(0.01)
col1.header('Top 6 courses:')

