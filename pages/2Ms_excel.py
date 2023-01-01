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
    4: 'Index Match',
    5: 'Macros',
    6: 'Data Validation',
    7: 'Conditional Formatting',
    8: 'Power Query',
    9: 'Power Pivot',
    10: 'Power BI'
}
st. write("In this Article we will learn the following:")
for key , value in advance_excel_topics.items():
    st.write(key , value)


with st.expander("Pivot Tables"):
    steps_to_create_pivot_table = {
    1: 'Select the data that you want to include in the pivot table.',
    2: 'Go to the Insert tab and click on the Pivot Table button.',
    3: 'In the Create PivotTable dialog box, choose where you want to place the pivot table and click OK.',
    4: 'The PivotTable Field List will appear on the right side of the worksheet.',
    5: 'From the PivotTable Field List, drag the fields that you want to include in the pivot table to the designated areas in the layout section.',
    6: 'You can then rearrange and manipulate the data in the pivot table by dragging the fields to different areas, filtering and sorting the data, and adding calculations and summary functions.'
}
    st.write("""A pivot table is a powerful tool in Excel that allows you to quickly summarize and analyze large sets of data. It allows you to rearrange and manipulate the data in a variety of ways, such as by sorting, filtering, and grouping, to get a better understanding of the data and identify trends and patterns.""")
    st.write("#### To create a pivot table in Excel, you need to follow these steps:")
    for key ,value in steps_to_create_pivot_table.items():
         st.write(key, value)

with st.expander("Vlookup"):
    st.title('VLOOKUP Function in Excel')

    st.markdown('VLOOKUP is a function in Excel that allows you to look up and retrieve data from a table or range of cells based on a specific value. It stands for "vertical lookup."')

    st.markdown('The syntax for the VLOOKUP function is as follows:')

    st.code('=VLOOKUP(lookup_value, table_array, col_index_num, [range_lookup])')

    st.markdown('The `lookup_value` is the value that you want to look up in the table or range. The `table_array` is the table or range of cells that contains the data you want to retrieve. The `col_index_num` is the column number in the table that contains the data you want to retrieve. The `range_lookup` is an optional argument that specifies whether you want to find an exact match or an approximate match for the `lookup_value`. If you specify `TRUE` or omit the `range_lookup` argument, the function will find the closest match that is less than or equal to the `lookup_value`. If you specify `FALSE`, the function will only return a result if it finds an exact match.')

    st.title('Example of VLOOKUP Function in Excel')

    st.markdown('Imagine you have a table with two columns: "Product" and "Price." You want to look up the price of a specific product in the table and return it in a cell. You could use the VLOOKUP function to do this.')

    st.markdown('Here is the formula you could use:')

    st.code('=VLOOKUP("Product A", A1:B10, 2, TRUE)')

    st.markdown('In this example, "Product A" is the `lookup_value`, A1:B10 is the `table_array`, 2 is the `col_index_num`, and `TRUE` is the `range_lookup`. This formula will look for the value "Product A" in the first column of the table (the "Product" column) and return the corresponding value in the second column (the "Price" column).')

    st.markdown('The VLOOKUP function is a useful tool for quickly retrieving data from a table or range of cells. It can save you a lot of time and effort compared to manually searching for values in a large dataset.')


with st.expander(" Hlookup"):

    st.title('HLOOKUP Function in Excel')

    st.markdown('HLOOKUP is a function in Excel that allows you to look up and retrieve data from a table or range of cells based on a specific value. It stands for "horizontal lookup."')

    st.markdown('The syntax for the HLOOKUP function is similar to the VLOOKUP function, with a few differences. The syntax is as follows:')

    st.code('=HLOOKUP(lookup_value, table_array, row_index_num, [range_lookup])')

    st.markdown("The `lookup_value` is the value that you want to look up in the table or range. The `table_array` is the table or range of cells that contains the data you want to retrieve. The `row_index_num` is the row number in the table that contains the data you want to retrieve. The `range_lookup` is an optional argument that specifies whether you want to find an exact match or an approximate match for the `lookup_value`. If you specify `TRUE` or omit the `range_lookup")

    st.title('Example of HLOOKUP Function in Excel')

    st.markdown('Imagine you have a table with two rows: "Product" and "Price." You want to look up the price of a specific product in the table and return it in a cell. You could use the HLOOKUP function to do this.')

    st.markdown('Here is the formula you could use:')

    st.code('=HLOOKUP("Product A", A1:B2, 2, TRUE)')

    st.markdown('In this example, "Product A" is the `lookup_value`, A1:B2 is the `table_array`, 2 is the `row_index_num`, and `TRUE` is the `range_lookup`. This formula will look for the value "Product A" in the first row of the table (the "Product" row) and return the corresponding value in the second row (the "Price" row).')

with st.expander(" Data Validation"):

    st.title('Data Validation in Excel')

    st.markdown('Data validation is a feature in Excel that allows you to control the type of data that can be entered in a cell or range of cells. It helps you ensure that the data in your spreadsheet is accurate and consistent.')

    st.markdown('To set up data validation in Excel, follow these steps:')

    st.markdown('1. Select the cells or range of cells that you want to apply data validation to.')
    st.markdown('2. Go to the "Data" tab in the ribbon and click the "Data Validation" button.')
    st.markdown('3. In the "Data Validation" dialog box, select the "Settings" tab.')
    st.markdown('4. Under the "Allow" dropdown, choose the type of data that you want to allow in the selected cells. For example, you can choose "Whole Number" to only allow whole numbers, or "Decimal" to allow decimal values.')
    st.markdown('5. Optional: Under the "Data" tab, you can also set up a custom error message or warning to display if someone tries to enter invalid data. You can also specify a formula to validate the data based on a custom rule.')
    st.markdown('6. Click "OK" to apply the data validation.')

    st.title('Example of Data Validation in Excel')

    st.markdown('Imagine you have a spreadsheet with a column for employee IDs. You want to ensure that only numeric values are entered in this column. You can use data validation to do this.')

    st.markdown('To set up data validation for the employee ID column, follow these steps:')

    st.markdown('1. Select the cells in the employee ID column.')
    st.markdown('2. Go to the "Data" tab in the ribbon and click the "Data Validation" button.')
    st.markdown('3. In the "Data Validation" dialog box, select the "Settings" tab.')
    st.markdown('4. Under the "Allow" dropdown, choose "Whole Number" to only allow whole numbers in the employee ID cells.')
    st.markdown('5. Optional: Under the "Error Alert" tab, you can set up a custom error message to display if someone tries to enter a non-numeric value. You can also specify whether you want to show an error message or warning, and whether you want to allow the user to cancel the entry or not.')
    st.markdown('6. Click "OK" to apply the data validation.')

    st.markdown('Now, if someone tries to enter a non-numeric value in an employee ID cell, they will see an error message or warning. This helps you ensure that only numeric values are entered in the employee ID column.')

with st.expander("Data Entry Form"):
    st.title('Data Entry Forms in Excel')

    st.markdown('Data entry forms in Excel allow you to enter data into a spreadsheet using a more user-friendly interface. They can be especially useful for entering large amounts of data, as they provide an organized and structured way to enter the data.')

    st.markdown('To create a data entry form in Excel, follow these steps:')

    st.markdown('1. Open the spreadsheet that you want to create the data entry form for.')
    st.markdown('2. Go to the "Data" tab in the ribbon and click the "Form" button.')
    st.markdown('3. A data entry form will open up, with a field for each column in the spreadsheet.')
    st.markdown('4. Enter the data into the fields as desired, and use the "New" button to add a new record.')
    st.markdown('5. Use the "Find Prev" and "Find Next" buttons to navigate between records, and use the "Delete" button to delete a record.')
    st.markdown('6. When you are finished, click the "Close" button to close the data entry form.')
