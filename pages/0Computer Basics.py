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

    with col2:
        st.write("#### Software")
        st.write("These are the intangible components of a computer that can neither be touched nor felt.")
        computer_software = [
            "System Software",
            "Application Software",
            "Utility Software",
        ]
        for item in computer_software:
            st.write("-> " + item)
    # with col2:
    #     st.write("#### Soft")
    #     input_unit = ["Key Board :keyboard:", "Mouse ", "Mic :mic:", "..."]
    #     for item in input_unit:
    #         st.write("-: " + item)

with st.expander("CPU"):
    st.write("#### The CPU consists of:")
    cpu = {
        " **Control Unit**": "*Is a component of a computer's central processing unit (CPU) that directs the operation of the processor.*",
        "**Arithmetic Logic Unit**": "*Is the part of a central processing unit that carries out arithmetic and logic operations on the operands in computer instruction.*",
        "**Some Registers**": "*Is one of a small set of data holding places that are part of the computer processor.*"}
    for key, value in cpu.items():
        st.write(key)
        st.write(value)

with st.expander("Input Unit"):
    st.markdown("#### Input Devices")
    st.write("*These are devices that are used to insert  /  key in data and instruction to the computer.*")
    input_devices = {
        "Keyboard :keyboard:": "*Is an input device that allows you to enter letters, numbers and symbols into your computer*",
        "Mouse :mouse:": "*Is an input device that allows you to control the coordinates and movement of the onscreen cursor/pointer by simply moving the mouse across a flat surface with your hand.*",
        "Microphone :microphone:": "*Are input devices that take analogue sound waves and converts them into electrical signals, suitable for a computer to understand.*"}

    for keys, value in input_devices.items():
        st.write(keys)
        st.write(value)

with st.expander("Output Unit"):
    st.markdown("#### Output Devices")
    st.write("*Is any piece of computer hardware equipment which converts information into a human-perceptible form*")
    input_devices = {
        "Monitor :monitor:": "*Is an output device that displays information in pictorial or textual form.*",
        "Headphone :headphone:": "*I device that allows you to control the coordinates and movement of the onscreen cursor/pointer by simply moving the mouse across a flat surface with your hand.*",
        "Projector :projector:": "*Is an output hardware device that connects to a computer to generate sound.*",
        "Printer :printer:": "*Are input devices that take analogue sound waves and converts them into electrical signals, suitable for a computer to understand.*",
        "Speaker :speaker:": "*Is an output hardware device that connects to a computer to generate sound.*",}

    for keys, value in input_devices.items():
        st.write(keys)
        st.write(value)
