import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Microsoft Word",
    page_icon=":earth_africa:"
)
st.write("# The microsoft word LECTURE")
st.markdown(" ## Learning Outcomes:")

outcome = [
    "I: Ms WORD OVERVIEW ",
    "II: TABLE OF CONTENT",
    "III: MAIL MERGE",
]
for items in outcome:
    st.write(items)

with st.expander(" MS word Overview "):
    st.markdown("## MS word Overview")
    st.write("We are going to have an over view of the Ms Word Window. Take a look at its components. ")
    st.image("assets/image/ms_window.jpeg", caption="Microsoft Word Window overview", use_column_width=True)

with st.expander("Table Of Content"):
    st.markdown("### Creating TABLE OF CONTENTS")
    st.write("""
    First you have to style your document by assign the headings with styles “Heading 1, Heading 2 to Heading N.
To assign headings, you highlight the required text, then in the **_home tab_** :house:, on the **_styles group_**, 
select heading style depending on the level of heading you want to assign.
After applying  all the heading styles,  we then create the TOC.
    """)
    st.write(
        "Once your Word document is properly formatted with the Heading Styles, to make your Table of Contents, simply:")
    steps = [
        "1. Click into your document where you want your TOC",
        "2. Navigate to the References tab",
        "3. Open the Table of Content dropdown menu",
        "4. Choose Automatic Table 1 or Automatic Table 2"
    ]
    for step in steps:
        st.write(step)
    st.image("assets/image/TOTcreation.png", caption="Steps in creation of Table of Content", use_column_width=True)

    st.write(" ### To update a Table of Contents in Word, simply:")
    steps = [
        "1. Navigate to the References tab",
        "2. Click Update Table",
        "3. Choose Update page numbers only or Update entire table",
        "4. Click OK",
    ]
    for step in steps:
        st.write(step)

with st.expander(" MAIL MERGE"):
    st.markdown("### CREATING A MAIL MERGE")
    st.write(" **What is MAIL MERGE?**")
    st.write(
        "A mail merge lets you create personalized documents that are automatically customized on a recipient-by-recipient basis.")
    st.write(" Mail merge can be used to create custom messages automatically")
    st.write("What you can do with Mail Merge")
    mail = [
        "Marketing emails.",
        "Newsletters.",
        "Custom catalogs.",
        "Form letters",
    ]

    for m in mail:
        st.write("* Create: ", m)
    st.write("---")
    st.write("#### To create a mail merge you need two components:")
    components = {
        "**_Template File_**": "The document that holds the message you’ll be sending out (like a letter or an email). It specifies the places where the personalization data will go. And that data (names, addresses, etc.) is fetched from a data file.",
        "**_Data File_**": "A data source like a Microsoft Excel spreadsheet or a Google Sheets file. Each cell in the data file contains different information (first name, last name, email address, etc.) that will be placed in your template file in the corresponding space."
    }
    for key, value in components.items():
        st.write(key)
        st.write(value)

    st.write("Create a Template file: An Official Letter")
    st.image("assets/image/templatefile.png", caption="Template File", use_column_width=True)

    st.write("___")
    st.write(
        "**Data file** is our source of info to be included in the mail. This can be achieved using excel, outlook address or created in Ms Word")
    st.write("For this lecture, we are going to create it from Ms Word.")
    st.write(" #### Create a new mail merge list:")
    mail_list = [

        "1: Go to File > New > Blank Document.",

        "2: Choose Select Recipients > Type a New List.",

        "3: In the New Address List dialog box type recipient information in each column as appropriate. For more info on using the dialog box, see Edit Data Source.",

        "4: For each new record, select Add New.",

        "5: When you'\''re done adding all the people you want to your list, choose OK.",

        "6: In the Save Address List dialog box, give your new file a name, and then choose Save."
    ]
    for item in mail_list:
        st.write(item)

    st.write("#### Creating a recipient list: ")
    st.write(
        "On the mailing Tab, under the Mail Merge group, click _select recipients_ to chose a list from pre defined lists or create a list from scratch")

with st.expander("Insert "):
    st.markdown("### Inserting Items in a document")
    st.write("We can insert different objects into pur document using the insert tab")
    st.write("Examples of objects:")
    objects = ["Tables", "Images", "Wordart", "Equations", "Shapes", "Charts"]

    for item in objects:
        st.write("*:", item)

    st.write("### Insert Tables")
    st.write(" A table is an object that allows the user to display data in a tabular format.")
    st.write("Tables can be created in Three major ways namely:")
    table = ["Table by grid", "Table by wizard", "Table by drawing"]
    for item in table:
        st.write(": ", item)

    st.write("#### By Grid")
    st.write("The grid may be used to create a simple / basic table.")
    st.write("For a basic table, click Insert > Table and move the cursor over the grid until you highlight the number of columns and rows you want.")
    st.image("assets/image/grid table.png", caption="Creating a table using the Grid ")

    st.write("#### By Insert Table")
    st.write("For a larger table, or to customize a table, select Insert > Table > Insert Table.")
    st.image("assets/image/insert table.png", caption="Creating a table using the insert table option")
    st.write("On clicking the insert table option an insert Table dialog box appears")
    st.image("assets/image/insertTable.png", caption="Selecting column and width")
    st.write("""From the dialog box, you can set the number of rows and columns of your table. This option also allows you to set the auto fit tables behaviour
    such as  Fixed column width , auto fit content and auto column width.""")

    st.write("#### By Drawing")
    st.write("You can also draw a table, select Insert > Table > Draw table.")
    st.image("assets/image/insert table.png", caption="Drawing your own table")
    st.write("""
    once the draw table option is selected, your pointer will change to look like a pencil, now yoo are ready to draw tables 
    of your choice. This is a more flexible option allowing you to design the tables in many different ways.
    """)

    st.markdown("## Inserting Picture into a word document:")
    st.write("To insert a picture, click the insert tab then select _Picture_ from ")

