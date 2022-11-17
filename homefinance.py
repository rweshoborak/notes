import streamlit as st

st.title("Data Science lecture")
st.sidebar.header("Module Content")
option = st.sidebar.selectbox("Topics",
                              ["Computer Essentials", "File & Folder management", "Advanced Ms Word",
                               "Advanced Ms Excel",
                               "Advanced Power Point"]
                              )
if option == "Computer Essentials":
    slide_content = st.selectbox("Chapter1 Introduction to Computers ",
                             ["Definition", "computer components",
                                                                     "Computer Hardware",
                                                                     "Input Unit", "Output Unit",
                                                                     "Computer Memory/Storage", "CPU",
                                                                     "Computer Software",
                                                                     "Computer Types", "Computer Virus"
                             ])
    st.write("---")
    if slide_content == "Definition":
        st.markdown("**Content**:")
        st.write(slide_content,":")
        st.write("""Computers are electronic devices that can
         follow instructions to accept input, 
         process the input and then produce information""")





    # st.radio("Chapter1 Introduction to Computers ", slide_content)
    # for items in slide_content:
    #     st.radio("**", items,"**")

if option == "File & Folder management":
    st.write(" Welcome Folder")
if option == "Advanced Ms Word":
    st.write(" Welcome Word")
if option == "Advanced Ms Excel":
    st.write(" Welcome to excel")
if option == "Advanced Power Point":
    st.write(" Welcome to PPT")
