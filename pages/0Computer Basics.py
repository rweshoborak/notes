import streamlit as st

st.set_page_config(
    page_title="Computer Basics",
    page_icon=":earth_africa:"
)
st.write("# The Computer Basics LECTURE")
st.markdown(" ## _INTRODUCTION TO COMPUTERS_ :computer:")
st.markdown("#### What is a computer!")
st.write("""Computers are electronic devices that can follow instructions to accept input, 
process the input and then produce information.
Computers are made up of two main components:
 **_Computer hardware_** and **_Computer Software_**""")

with st.expander("COMPUTER HARDWARE"):
    col1, col2 = st.columns(2)
    with col1:
        st.write("#### Hardware")
        st.write("These are the tangible parts of a computer that can be physically seen touched and felt.")
        computer_hardware = [
            "CPU: Central Processing Unit",
            "Input Unit",
            "Output Unit",
            "Storage Devices",
        ]
        for item in computer_hardware:
            st.write("*: " + item)

        st.write("**CPU**")
        st.write("pass")
    with col2:
        st.write("#### Software")
        st.write("These are the intangible components of a computer that can neither be touched nor felt.")
        computer_software=[
            "System Software",
            "Application Software",
            "Utility Software",
        ]
        for item in computer_software:
            st.write("-> "+ item)
    # with col2:
    #     st.write("#### Soft")
    #     input_unit = ["Key Board :keyboard:", "Mouse ", "Mic :mic:", "..."]
    #     for item in input_unit:
    #         st.write("-: " + item)


with st.expander("CPU"):
    st.write("None")
