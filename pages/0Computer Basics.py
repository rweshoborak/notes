import ssl

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
        st.write(
            """Hardware refers to the physical components of an ICT system. It includes devices such as computers, tablets, smartphones, printers, scanners, servers, and other types of electronic equipment. Hardware is typically classified according to its size and capabilities. For example, a personal computer is a type of hardware that is designed for use by an individual, while a server is a type of hardware that is used to store and manage data for a network of computers.""")
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
        st.write(
            """Software refers to the programs and applications that run on hardware and enable it to perform specific tasks. There are many different types of software, including operating systems, which manage the hardware and provide a platform for other software to run on; productivity tools, such as word processors and spreadsheets; and specialized software for tasks like graphic design, video editing, and gaming.""")
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

with st.expander("Data"):
    st.title("Data")
    st.write(
        """Data refers to information that is processed, stored, and transmitted using ICT. Data can take many forms, such as text, images, audio, and video. It is typically stored in digital format, and it can be accessed and manipulated using software. Data can be organized and structured in various ways, such as in a database or spreadsheet.""")

with st.expander("Networking"):
    st.title("Networking")
    st.write(
        """Networking refers to the practice of connecting computers and other devices together to facilitate communication and the sharing of resources. There are many different types of networks, ranging from small, local networks that connect devices in a single location, to large, global networks such as the Internet, which connects devices all around the world. Networking allows devices to exchange data, access shared resources, and communicate with each other.""")


with st.expander("Cloud"):
    st.title("CLOUD")
    st.write("""The Cloud refers to a network of servers that can be accessed remotely over the Internet to store, process, and transmit data, rather than relying on local hardware. Cloud computing allows users to access data and resources from any device with an Internet connection, without having to store the data locally on their own device. Instead, the data is stored on servers in a remote location, and users can access it as needed.""")

with st.expander("Cybersecurity"):
    st.title("Cybersecurity")
    st.write("""Cybersecurity refers to measures taken to protect ICT systems and networks from attacks, unauthorized access, and data breaches. Cybersecurity includes practices such as password protection, encryption, and the use of firewalls and antivirus software to prevent unauthorized access to data and systems. Cybersecurity is important because ICT systems and networks are vulnerable to attacks from hackers and other cybercriminals, who may try to steal or damage data, or disrupt the operation of the system.""")

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
        "Monitor :tv:": "*Is an output device that displays information in pictorial or textual form.*",
        "Headphone :headphone:": "*I device that allows you to control the coordinates and movement of the onscreen cursor/pointer by simply moving the mouse across a flat surface with your hand.*",
        "Projector :tv:": "*Is an output device that takes images generated by a computer or Blu-ray player and reproduce them by projection onto a screen, wall, or another surface.*",
        "Printer :printer:": "*An output device which prints a hard copy of the electronic data that is stored in the computer or any other devices.*",
        "Speaker :speaker:": "*Is an output hardware device that connects to a computer to generate sound.*", }

    for keys, value in input_devices.items():
        st.write(keys)
        st.write(value)
