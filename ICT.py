import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="ICT",
    page_icon=' '
)

st.write("# Welcome to ICT course")
st.markdown(" ##### What you will achieve after the courses")
bullets = ["Be able to explain the meaning of ICT and related terms",
           "Identify and explain the roles of ICT in your field",
           "Identify tools that are associated with ICT",
           "Use advanced Microsoft word features in preparing and formatting documents",
           "Use advanced Microsoft excel features in preparing, analyzing and interpreting data, prepare reports ",
           "Use advanced Microsoft power point features in preparing, formatting and presenting materials",
           "Use advanced Microsoft access features in preparing, formatting and presenting tables to users"
           ]
for i in bullets:
    st.write("*", i)
tab1, tab2, tab3, tab4 = st.tabs(["Learning Context:", "Learning Materials", "Assessment", "Reference"])

with tab1:
    st.header("Learning Context:")
    st.write(
        "The course is based on classroom lectures, guided independent work, practical illustrations, assignments, and tests. The course is planned to be interactive and the emphasis will be on learning by doing.")

with tab2:
    st.header("Learning Materials")
    materials = ["Handouts", "internet materials ", "text books"]
    for item in materials:
        st.write(item)

with tab3:
    st.header("Assessment")
    assessment = {"tests": 20, "Written paper assignments": 20, "Practical Assignments": 10, "Semester Exam ": 60}
    # for item,value in assessment:
    #     st.write(item,value)

    components.html(
        """
        <table class="table">
  <thead>
    <tr>      
      <th scope="col">ASSESSMENT METHOD</th>
      <th scope="col">% MARKS</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">TEST</th>
      <td>20%</td>
     </tr>
    <tr>
      <th scope="row">Written paper assignments </th>
      <td>10%</td>
    </tr>
    <tr>
      <th scope="row">Practical Assignments </th>
      <td>10%</td>
      
    </tr>
    <tr>
      <th scope="row">Semester Exam  </th>
      <td>60%</td>
      
    </tr>
  </tbody>
</table>
        """,
        height=600,
    )
with tab4:
    tab1, tab2 = st.tabs(['Required Readings:', "Recommended Readings"])
    with tab1:
        refs = ["(i) Peter Norton’s (2003), Introduction to Computers, Tata McGraw-Hill, New Delhi.",
                "(ii) Efraim Turban, Ephraim McLean and James Wetherbe (2001), Information Technology for Management, 2nd Edition, John Wiley, New York.",
                "(iii) Brian K. Williams, Stacey C. Sawyer and Sarah Hutchinson (1999), Using Information Technology: A Practical Introduction to Computers and Communication, 3rd Edition, Irwin McGraw-Hill, Boston."]
        for items in refs:
            st.write(items)

    with tab2:
        refs = ["(i) Stephen Doyle (2003), Computer Studies for You, Stanley Thornes (Publishers) Ltd, London.",
                "(ii) Sanjay Saxena (2001), A First Course in Computers, Vikas Publishing House PVT LTD, New Delhi. ",
                "(iii) Kenneth C. Laudon and Jane P. Laudon (2004); Management Information Systems: Managing the Digital Firm, 8th Edition, Pearson Education, New Delhi, India.",
                "(iv) James A. O’brien (2003); Introduction to Information Systems, 12th Edition, Tata McGraw-Hill Publishing Company Limited, New York.",
                "(v) Efraim Turban, Ephraim McLean and James Wetherbe (2001), Information Technology for Management, 2nd Edition, John Wiley, New York. ",
                ]
        for items in refs:
            st.write(items)


