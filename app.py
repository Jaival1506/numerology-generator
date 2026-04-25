import streamlit as st
from main import generate_numerology_report

st.title("Numerology Generator")

st.write("Enter details to generate numerology report")

first = st.text_input("First Name")
middle = st.text_input("Middle Name")
last = st.text_input("Last Name")
birth_year = st.number_input("Birth Year", min_value=1900, max_value=2100)

if st.button("Generate Report"):

    if first and middle and last:
        file_path = generate_numerology_report(first, middle, last, birth_year)

        with open(file_path, "rb") as f:
            st.download_button(
                label="Download Excel",
                data=f,
                file_name="numerology_report.xlsx"
            )
    else:
        st.error("Please enter full name")