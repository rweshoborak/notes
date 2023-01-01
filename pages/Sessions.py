import streamlit as st
import csv

# Create an empty dictionary to store the submitted data

data = {}


# Create a form for accepting input
# # form = st.form()
# form = st.form(key='my_form')
# # Add form elements for collecting data
# session_type = st.selectbox("Type of session", ["Session A", "Session B", "Session C", "Session D"])
# session_date = st.date_input("Date of session")
# description = st.text_area("Description of what was learned")
#
# # Add a submit button
# if st.button("Submit"):
#     # Update the dictionary with the submitted data
#     data["session_type"] = session_type
#     data["session_date"] = session_date
#     data["description"] = description
#     # Display a success message
#     st.success("Thank you for submitting the form!")


#########################################################
def write_to_csv(data):
    fieldnames = ['session_type', 'session_date', 'description']
    with open('session_data.csv', 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # inserts header every time you add data " We need a way to correct that"
        # writer.writeheader()
        writer.writerow(data)


session_type = st.selectbox("Type of session", ["Session A", "Session B", "Session C", "Session D"])
session_date = st.date_input("Date of session")
description = st.text_area("Description of what was learned")

if st.button("Submit"):
    data = {'session_type': session_type, 'session_date': session_date, 'description': description}
    write_to_csv(data)
    st.write("Data saved to CSV file!")


#########################################################
# Displaying the data
#########################################################
def read_csv():
    data = []
    with open('session_data.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data


data = read_csv()


st.table(data)

