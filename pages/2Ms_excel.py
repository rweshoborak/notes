import streamlit as st

st.set_page_config(
    page_title="Microsoft Excel",
    page_icon=":earth_africa:"
)
st.write("# The microsoft word LECTURE")
st.markdown(" ## Learning Outcomes:")

advance_excel_topics = {
    1: 'Pivot Tables',
    2: 'Vlookup',
    3: 'Hlookup',
    4: 'Data Validation',
    5: 'Conditional Formatting',

}
st.write("In this Article we will learn the following:")
for key, value in advance_excel_topics.items():
    st.write(key, value)

with st.expander("Cell referencing"):
    st.title('Cell Referencing in Microsoft Excel')

    st.markdown(
        'Cell referencing is a way to refer to the value or formula in a cell in Excel. There are two main types of cell references: relative and absolute. Here is a brief overview of each:')

    st.markdown('''
    1. Relative cell references: A relative cell reference refers to a cell in relation to the current cell. For example, if you are in cell A1 and you reference cell B1, this is a relative reference because it is one cell to the right of the current cell. If you copy and paste this formula to a different cell, the reference will change to reflect the new location.
    
    2. Absolute cell references: An absolute cell reference refers to a specific cell, regardless of the current location. To create an absolute cell reference, you can use a "$" symbol before the column letter or row number. For example, "$A$1" is an absolute reference to cell A1. If you copy and paste this formula to a different cell, the reference will not change.
    
    3. Mixed referencing: Mixed cell references contain both absolute and relative elements. For example, "$A1" is a mixed reference to cell A1, with the column letter being absolute and the row number being relative. Mixed references are useful when you want to refer to a specific column or row, but want the reference to adjust based on the row or column of the formula or function.

    Cell referencing is a powerful tool that allows you to create dynamic formulas and perform calculations on data in different cells. I hope this helps! Let me know if you have any questions.
    
    ''')
    # youtube_icon = '<img src="https://upload.wikimedia.org/wikipedia/commons/e/e1/YouTube_play_buttom_icon_%282013-2017%29.svg" alt="YouTube icon" width="30" height="30">'

    # Add the YouTube link
    youtube_link = 'https://youtu.be/LFIykJmL4M8'

    # Display the link with the YouTube icon
    st.markdown(f'[Click here to watch the video]({youtube_link})', unsafe_allow_html=True)

    # st.markdown('To watch this video on YouTube, click the YouTube icon:')
    #
    # st.markdown('[![YouTube Icon](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/YouTube_Logo_2017.svg/1200px-YouTube_Logo_2017.svg.png)](https://youtu.be/LFIykJmL4M8)')

with st.expander("Pivot Tables"):
    steps_to_create_pivot_table = {
        1: 'Select the data that you want to include in the pivot table.',
        2: 'Go to the Insert tab and click on the Pivot Table button.',
        3: 'In the Create PivotTable dialog box, choose where you want to place the pivot table and click OK.',
        4: 'The PivotTable Field List will appear on the right side of the worksheet.',
        5: 'From the PivotTable Field List, drag the fields that you want to include in the pivot table to the designated areas in the layout section.',
        6: 'You can then rearrange and manipulate the data in the pivot table by dragging the fields to different areas, filtering and sorting the data, and adding calculations and summary functions.'
    }
    st.write(
        """A pivot table is a powerful tool in Excel that allows you to quickly summarize and analyze large sets of data. It allows you to rearrange and manipulate the data in a variety of ways, such as by sorting, filtering, and grouping, to get a better understanding of the data and identify trends and patterns.""")
    st.write("#### To create a pivot table in Excel, you need to follow these steps:")
    for key, value in steps_to_create_pivot_table.items():
        st.write(key, value)

with st.expander("Vlookup"):
    st.title('VLOOKUP Function in Excel')

    st.markdown(
        'VLOOKUP is a function in Excel that allows you to look up and retrieve data from a table or range of cells based on a specific value. It stands for "vertical lookup."')

    st.markdown('The syntax for the VLOOKUP function is as follows:')

    st.code('=VLOOKUP(lookup_value, table_array, col_index_num, [range_lookup])')

    st.markdown(
        'The `lookup_value` is the value that you want to look up in the table or range. The `table_array` is the table or range of cells that contains the data you want to retrieve. The `col_index_num` is the column number in the table that contains the data you want to retrieve. The `range_lookup` is an optional argument that specifies whether you want to find an exact match or an approximate match for the `lookup_value`. If you specify `TRUE` or omit the `range_lookup` argument, the function will find the closest match that is less than or equal to the `lookup_value`. If you specify `FALSE`, the function will only return a result if it finds an exact match.')

    st.title('Example of VLOOKUP Function in Excel')

    st.markdown(
        'Imagine you have a table with two columns: "Product" and "Price." You want to look up the price of a specific product in the table and return it in a cell. You could use the VLOOKUP function to do this.')

    st.markdown('Here is the formula you could use:')

    st.code('=VLOOKUP("Product A", A1:B10, 2, TRUE)')

    st.markdown(
        'In this example, "Product A" is the `lookup_value`, A1:B10 is the `table_array`, 2 is the `col_index_num`, and `TRUE` is the `range_lookup`. This formula will look for the value "Product A" in the first column of the table (the "Product" column) and return the corresponding value in the second column (the "Price" column).')

    st.markdown(
        'The VLOOKUP function is a useful tool for quickly retrieving data from a table or range of cells. It can save you a lot of time and effort compared to manually searching for values in a large dataset.')

with st.expander(" Hlookup"):
    st.title('HLOOKUP Function in Excel')

    st.markdown(
        'HLOOKUP is a function in Excel that allows you to look up and retrieve data from a table or range of cells based on a specific value. It stands for "horizontal lookup."')

    st.markdown(
        'The syntax for the HLOOKUP function is similar to the VLOOKUP function, with a few differences. The syntax is as follows:')

    st.code('=HLOOKUP(lookup_value, table_array, row_index_num, [range_lookup])')

    st.markdown(
        "The `lookup_value` is the value that you want to look up in the table or range. The `table_array` is the table or range of cells that contains the data you want to retrieve. The `row_index_num` is the row number in the table that contains the data you want to retrieve. The `range_lookup` is an optional argument that specifies whether you want to find an exact match or an approximate match for the `lookup_value`. If you specify `TRUE` or omit the `range_lookup")

    st.title('Example of HLOOKUP Function in Excel')

    st.markdown(
        'Imagine you have a table with two rows: "Product" and "Price." You want to look up the price of a specific product in the table and return it in a cell. You could use the HLOOKUP function to do this.')

    st.markdown('Here is the formula you could use:')

    st.code('=HLOOKUP("Product A", A1:B2, 2, TRUE)')

    st.markdown(
        'In this example, "Product A" is the `lookup_value`, A1:B2 is the `table_array`, 2 is the `row_index_num`, and `TRUE` is the `range_lookup`. This formula will look for the value "Product A" in the first row of the table (the "Product" row) and return the corresponding value in the second row (the "Price" row).')

with st.expander("Data Entry Form"):
    st.title('Data Entry Forms in Excel')

    st.markdown(
        'Data entry forms in Excel allow you to enter data into a spreadsheet using a more user-friendly interface. They can be especially useful for entering large amounts of data, as they provide an organized and structured way to enter the data.')

    st.markdown('To create a data entry form in Excel, follow these steps:')

    st.markdown('1. Open the spreadsheet that you want to create the data entry form for.')
    st.markdown('2. Go to the "Data" tab in the ribbon and click the "Form" button.')
    st.markdown('3. A data entry form will open up, with a field for each column in the spreadsheet.')
    st.markdown('4. Enter the data into the fields as desired, and use the "New" button to add a new record.')
    st.markdown(
        '5. Use the "Find Prev" and "Find Next" buttons to navigate between records, and use the "Delete" button to delete a record.')
    st.markdown('6. When you are finished, click the "Close" button to close the data entry form.')

with st.expander(" Data Validation"):
    st.title('Data Validation in Excel')

    st.markdown(
        'Data validation is a feature in Excel that allows you to control the type of data that can be entered in a cell or range of cells. It helps you ensure that the data in your spreadsheet is accurate and consistent.')

    st.markdown('To set up data validation in Excel, follow these steps:')

    st.markdown('1. Select the cells or range of cells that you want to apply data validation to.')
    st.markdown('2. Go to the "Data" tab in the ribbon and click the "Data Validation" button.')
    st.markdown('3. In the "Data Validation" dialog box, select the "Settings" tab.')
    st.markdown(
        '4. Under the "Allow" dropdown, choose the type of data that you want to allow in the selected cells. For example, you can choose "Whole Number" to only allow whole numbers, or "Decimal" to allow decimal values.')
    st.markdown(
        '5. Optional: Under the "Data" tab, you can also set up a custom error message or warning to display if someone tries to enter invalid data. You can also specify a formula to validate the data based on a custom rule.')
    st.markdown('6. Click "OK" to apply the data validation.')

    st.title('Example of Data Validation in Excel')

    st.markdown(
        'Imagine you have a spreadsheet with a column for employee IDs. You want to ensure that only numeric values are entered in this column. You can use data validation to do this.')

    st.markdown('To set up data validation for the employee ID column, follow these steps:')

    st.markdown('1. Select the cells in the employee ID column.')
    st.markdown('2. Go to the "Data" tab in the ribbon and click the "Data Validation" button.')
    st.markdown('3. In the "Data Validation" dialog box, select the "Settings" tab.')
    st.markdown(
        '4. Under the "Allow" dropdown, choose "Whole Number" to only allow whole numbers in the employee ID cells.')
    st.markdown(
        '5. Optional: Under the "Error Alert" tab, you can set up a custom error message to display if someone tries to enter a non-numeric value. You can also specify whether you want to show an error message or warning, and whether you want to allow the user to cancel the entry or not.')
    st.markdown('6. Click "OK" to apply the data validation.')

    st.markdown(
        'Now, if someone tries to enter a non-numeric value in an employee ID cell, they will see an error message or warning. This helps you ensure that only numeric values are entered in the employee ID column.')

with st.expander("Conditional Formatting"):
    st.title('Conditional Formatting in Microsoft Excel')

    st.markdown(
        'Conditional formatting is a powerful feature in Excel that allows you to highlight cells or ranges of cells based on specific conditions. This can be a useful way to quickly identify important data or trends in your worksheets. Here are some key points to consider when using conditional formatting:')

    st.markdown('''
    1. Setting up conditional formatting: To set up conditional formatting, select the cells or range of cells that you want to format. Then, go to the "Home" tab and click the "Conditional Formatting" button. From here, you can choose from a range of predefined formatting options or create your own custom rule.
    
    2. Applying formatting: Once you have set up your conditional formatting rule, Excel will automatically apply the formatting to the relevant cells based on the conditions you specified. You can see the formatting rules applied to a cell by selecting the cell and going to the "Conditional Formatting" button on the "Home" tab.
    
    3. Modifying and deleting rules: You can modify or delete a conditional formatting rule by selecting the cells or range of cells that have the rule applied and going to the "Conditional Formatting" button on the "Home" tab. From here, you can edit or delete the rule as needed.
    
    By using conditional formatting, you can quickly and easily highlight important data and trends in your Excel worksheets.''')

    # youtube_link = 'https://youtu.be/7iKoccSTNZA'

    # Display the link with the YouTube icon

with st.expander("Other Resources "):
    st.title('YouTube Channels to Learn Advanced Excel')

    st.markdown(
        'There are many YouTube channels that offer tutorials and lessons on advanced Excel techniques. Here are a few suggestions:')

    st.markdown('''
    1. ExcelIsFun: This channel is run by Mike "ExcelIsFun" Girvin, a Microsoft MVP who has over 25 years of experience with Excel. He offers a wide range of Excel tutorials, including advanced topics like pivot tables, macros, and financial modeling.
    
    2. MyExcelOnline: This channel is run by Excel expert Dave Bruns, who has over 20 years of experience using Excel in a variety of industries. He offers a range of Excel courses, including an advanced course that covers topics like pivot tables, macros, and data visualization.
    
    3. Excel Campus: This channel is run by Jon Acampora, a Microsoft Excel MVP who has been using Excel for over 20 years. He offers a range of Excel tutorials, including advanced topics like pivot tables, macros, and data analysis.
    
    4. Excel with Business: This channel is run by a team of Excel experts who offer a range of Excel courses and tutorials, including an advanced course that covers topics like pivot tables, macros, and data analysis.
    
    5. Tutorials Point: Is a comprehensive online learning platform that offers a wide range of tutorials and resources for Excel and other software programs.
    ''')
