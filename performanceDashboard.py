import streamlit as st

st.title('Student Dashboard')
courses = st.number_input('How many courses do you have this semester?')
for i in range(courses):
    st.slider(f'What is your average in your period {i} class', min_value = 0, max_value = 100)

