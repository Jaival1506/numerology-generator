import streamlit as st
from main import generate_numerology_report

st.title("Numerology Generator")

first = st.text_input("First Name")
middle = st.text_input("Middle Name")
last = st.text_input("Last Name")
birth_year = st.number_input("Birth Year", min_value=1900, max_value=2100, step=1)

if st.button("Generate Report"):
    if not (first and middle and last):
        st.error("Please enter First, Middle, and Last name.")
    else:
        file_buffer = generate_numerology_report(first, middle, last, birth_year)
        st.download_button(
            label="Download Excel",
            data=file_buffer,
            file_name="numerology_report.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )