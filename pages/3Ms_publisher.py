import streamlit as st
st.set_page_config(
    page_title="Microsoft Publisher",
    page_icon=":earth_africa:"
)
st.write("# The Microsoft Publisher LECTURE")

with st.expander("Course overview"):
    st.title('Learning Outcomes')

    st.markdown('In a Microsoft Publisher course, students may be able to achieve the following learning outcomes:')

    st.markdown('- Understand the features and capabilities of Microsoft Publisher, and be able to use the software to create professional-quality documents such as brochures, flyers, and business cards.')
    st.markdown('- Learn how to use templates, master pages, and custom styles to create consistent and professional-looking documents.')
    st.markdown('- Use text formatting tools and techniques to create and edit text in Publisher, including font, size, color, and alignment.')
    st.markdown('- Import and manipulate graphics, including images, shapes, and clip art, and apply effects such as shadows, reflections, and 3D rotation.')
    st.markdown('- Create and customize charts and diagrams, including line graphs, bar charts, and pie charts, and add data labels, legends, and gridlines.')
    st.markdown('- Create and edit tables, including merging and splitting cells, inserting and deleting rows and columns, and applying formatting to specific cells or ranges.')
    st.markdown('- Use mail merge and collaboration features to create and customize documents for mass mailings or to work on documents with other users.')
    st.markdown('- Print and export documents to other formats, such as PDF, HTML, and JPG, and share them with others or upload them to the web.')
    st.markdown('- Customize documents using a range of options, including creating custom shapes, adding custom effects and animations, and creating custom templates and styles.')

with st.expander("Templates Master Page and Custom Style"):
    st.title('Using Templates, Master Pages, and Custom Styles in Microsoft Publisher')

    st.markdown('Publisher provides a range of tools and options for creating and formatting documents, including templates, master pages, and custom styles. Here is an overview of how to use these features in Publisher:')

    st.title('Using Templates')
    st.markdown('Publisher comes with a wide range of templates that users can customize to create various types of documents. To use a template in Publisher, follow these steps:')
    st.markdown('1. Open Publisher and select "File > New" to open the "New Publication" window.')
    st.markdown('2. In the "New Publication" window, select the "Templates" tab.')
    st.markdown('3. Browse through the available templates and select the one you want to use. You can also use the search bar to find a specific template.')
    st.markdown('4. Click "Create" to open the template in Publisher.')
    st.markdown('5. Customize the template by adding or editing the text, graphics, and other elements as needed. You can use the various formatting tools and options in Publisher to make your document look the way you want.')
    st.markdown('6. When you are finished, save your document by selecting "File > Save As" and giving it a name.')

    st.title('Using Master Pages')
    st.markdown('Publisher allows users to create a master page, which is a template that defines the layout and design elements that will be applied to all pages in a document. To create a master page in Publisher, follow these steps:')
    st.markdown('1. Open a document in Publisher and select "View > Master Pages" to open the "Master Pages" window.')
    st.markdown('2. In the "Master Pages" window, click the "New Master Page" button to create a new master page.')
    st.markdown('3. Use the formatting tools and options in Publisher to design the layout and appearance of your master page. You can add text, graphics, and other elements to the page as needed.')
    st.markdown('4. When you are finished, click the "Close Master Pages" button to return to your document.')
    st.markdown('5. To apply your master page to the pages in your document, select "Page Design > Apply Master Page" and choose the master page you want to use.')

    st.title('Using Custom Styles')
    st.markdown('Publisher allows users to create custom styles, which are pre-defined formatting options that can be applied to text, graphics, and other elements in a document. To create a custom style in Publisher, follow these steps:')
    st.markdown('1. Open a document in Publisher and select "Format > Styles" to open the "Styles" window.')
    st.markdown('2. In the "Styles" window, click the "New Style" button to create a new style.')
    st.markdown('3. In the "Create New Style" window, give your style a name and use the formatting options to define the style. You can set options such as font, size, color, alignment, and more.')
    st.markdown('4. When you are finished, click "OK" to close the "Create New Style" window.')
    st.markdown('5. To apply your custom style to an element in your document, select the element and then click the style in the "Styles" window.')
    st.markdown('6. To modify an existing custom style, select the style in the "Styles" window and click the "Modify" button. Make your changes in the "Modify Style" window and click "OK" to save them.')

    st.markdown('By using templates, master pages, and custom styles, you can save time and effort when creating and formatting documents in Publisher. These features can help you create professional-quality documents that are consistent and visually appealing.')

with st.expander("Working with Text"):
    st.title('Advanced Text Formatting Options in Microsoft Publisher')

    st.markdown('Publisher provides a range of advanced text formatting options that allow users to customize the appearance and layout of their text. Here are some examples of the advanced text formatting options available in Publisher:')

    st.markdown('- Text wrapping: Publisher allows users to wrap text around graphics, shapes, and other elements in a document. To wrap text around an element, select the element and then choose from the text wrapping options in the "Format" tab, such as "Square," "Tight," or "Through."')
    st.markdown('- Columns: Publisher allows users to create multi-column layouts in their documents. To create columns, select the text you want to place in the columns and then click the "Columns" button in the "Page Design" tab. You can then choose the number of columns you want and customize the column width and spacing as needed.')
    st.markdown('- Text effects: Publisher provides a range of text effects that can be applied to text, such as shadow, reflection, and 3D rotation. To apply a text effect, select the text you want to format and then click the "Text Effects" button in the "Format" tab. You can then choose from the available effects and customize the options as needed.')
    st.markdown('- Text styles: Publisher allows users to create and apply custom text styles, which are pre-defined formatting options that can be applied to text with a single click. To create a text style, select the text you want to format and then click the "Create a Style" button in the "Styles" window. You can then give your style a name and use the formatting options to define the style.')
    st.markdown('- Text alignment: Publisher allows users to align text horizontally or vertically within a text box or other element. To align text, select the text and then use the alignment options in the "Format" tab, such as "Left," "Center," or "Justify." You can also use the "Text Direction" button to set the text direction, such as left-to-right or top-to-bottom.')
    st.markdown('- Text spacing: Publisher allows users to adjust the spacing between lines of text and between paragraphs. To adjust text spacing, select the text and then use the "Line Spacing" and "Paragraph Spacing" options in the "Format" tab. You can also use the "Space Before" and "Space After" options to adjust the spacing before and after the text.')

    st.markdown('These are just a few examples of the advanced text formatting options available in Publisher. By using these options, you can customize the appearance and layout of your text to create professional-quality documents that meet your specific needs and requirements.')

    st.title('Working with Text Boxes')
    st.markdown('Once you have created a text box in Publisher, you can work with it in various ways. Here are some examples:')
    st.markdown('- Resizing and moving text boxes: To resize a text box, select it and then click and drag one of the handles on the sides or corners. To move a text box, select it and then click and drag it to a new location. You can also use the "Size and Position" window in the "Format" tab to set the size and position of a text box more precisely.')
    st.markdown('- Linking text boxes: Publisher allows users to link text boxes together, which means that the text will flow from one text box to the next as you add or delete text. To link text boxes, select one of the text boxes and then click the "Link Text Boxes" button in the "Format" tab. Then click the other text box you want to link to.')
    st.markdown('- Grouping text boxes: Publisher allows users to group text boxes together, which means that they will move and resize as a unit. To group text boxes, select the text boxes you want to group and then click the "Group" button in the "Format" tab. You can then use the handles on the grouped text boxes to resize and move them as a unit.')
    st.markdown('- Adding text flow: Publisher allows users to add text flow between text boxes, which means that the text will automatically wrap from one text box to the next as you type. To add text flow between text boxes, select the first text box and then click the "Add Text Flow" button in the "Format" tab. Then click the second text box you want to flow to.')
    st.markdown('- Adding text wrap: Publisher allows users to wrap text around text boxes, which means that the text will automatically flow around the edges of the text box as you type. To add text wrap to a text box, select the text box and then click the "Text Wrapping" button in the "Format" tab. You can then choose from the available text wrapping options, such as "Square," "Tight," or "Through."')

    st.markdown('By creating and working with text boxes in Publisher, you can create documents with custom layouts and text flow that meet your specific needs and requirements. Text boxes are a useful and flexible tool for organizing and formatting text in your documents.')

    st.title('Using Text Effects and Text Wrapping')

    st.markdown('Publisher allows users to apply text effects and text wrapping to enhance the appearance and layout of their documents. Text effects are visual enhancements that can be applied to text, such as shadow, reflection, and 3D rotation. Text wrapping is a feature that allows text to flow around or behind graphics, shapes, and other elements in a document. Here is an overview of how to use text effects and text wrapping in Publisher:')

    st.title('Using Text Effects')
    st.markdown('To apply a text effect in Publisher, follow these steps:')
    st.markdown('1. Open a document in Publisher and select the text you want to format.')
    st.markdown('2. Click the "Text Effects" button in the "Format" tab.')
    st.markdown('3. In the "Text Effects" window, choose the type of effect you want to apply, such as "Shadow," "Reflection," or "3D Rotation."')
    st.markdown('4. Use the options in the "Text Effects" window to customize the effect, such as the color, size, and direction.')
    st.markdown('5. When you are finished, click "OK" to close the "Text Effects" window.')

    st.title('Using Text Wrapping')
    st.markdown('To wrap text around an element in Publisher, follow these steps:')
    st.markdown('1. Open a document in Publisher and insert the element you want to wrap text around, such as a graphic or shape.')
    st.markdown('2. Select the element and then click the "Text Wrapping" button in the "Format" tab.')
    st.markdown('3. In the "Text Wrapping" window, choose the type of text wrapping you want to use, such as "Square," "Tight," or "Through."')
    st.markdown('4. Use the options in the "Text Wrapping" window to customize the text wrapping, such as the distance between the text and the element.')
    st.markdown('5. When you are finished, click "OK" to close the "Text Wrapping" window.')

    st.markdown('By using text effects and text wrapping in Publisher, you can add visual interest and polish to your documents. Text effects and text wrapping can help you create professional-quality documents that are eye-catching and engaging.')


with st.expander("Working with Graphics"):
    st.title('Working with Graphics in Microsoft Publisher')

    st.markdown('Publisher provides a range of tools and options for working with graphics in documents. Graphics can be used to add visual interest and appeal to your documents, and Publisher provides a variety of ways to insert, format, and manipulate graphics. Here is an overview of how to work with graphics in Publisher:')

    st.title('Inserting Graphics')
    st.markdown('To insert a graphic in Publisher, follow these steps:')
    st.markdown('1. Open a document in Publisher and click the "Insert" tab.')
    st.markdown('2. In the "Illustrations" group, click the "Picture" button to open the "Insert Picture" window.')
    st.markdown('3. In the "Insert Picture" window, navigate to the location of the graphic you want to insert and select it.')
    st.markdown('4. Click "Insert" to insert the graphic into your document.')

    st.title('Formatting Graphics')
    st.markdown('Once you have inserted a graphic in Publisher, you can use the formatting tools and options to customize its appearance and layout. Here are some examples:')
    st.markdown('- Resizing and moving graphics: To resize a graphic, select it and then click and drag one of the handles on the sides or corners. To move a graphic, select it and then click and drag it to a new location. You can also use the "Size and Position" window in the "Format" tab to set the size and position of a graphic more precisely.')
    st.markdown('- Adding text wrap: Publisher allows users to wrap text around graphics, which means that the text will automatically flow around the edges of the graphic as you type. To add text wrap to a graphic, select the graphic and then click the "Text Wrapping" button in the "Format" tab. You can then choose from the available text wrapping options, such as "Square," "Tight," or "Through."')
    st.markdown('- Adding effects: Publisher allows users to apply effects to graphics, such as shadows, reflections, and 3D rotation. To add an effect to a graphic, select the graphic and then click the "Picture Effects" button in the "Format" tab. You can then choose from the available effects and customize the options as needed.')
    st.markdown('- Adjusting transparency: Publisher allows users to adjust the transparency of graphics, which means that you can make them partially transparent so that the background shows through. To adjust the transparency of a graphic, select it and then use the "Transparency" slider in the "Format" tab.')

    st.title('Manipulating Graphics')
    st.markdown('Publisher provides a range of tools and options for manipulating graphics in documents. Here are some examples:')
    st.markdown('- Grouping graphics: Publisher allows users to group graphics together, which means that they will move and resize as a unit. To group graphics, select the graphics you want to group and then click the "Group" button in the "Format" tab. You can then use the handles on the grouped graphics to resize and move them as a unit.')
    st.markdown('- Locking graphics: Publisher allows users to lock graphics in place, which means that they cannot be moved or resized accidentally. To lock a graphic, select it and then click the "Lock" button in the "Format" tab. You can unlock a graphic by clicking the "Lock" button again.')
    st.markdown('- Cropping graphics: Publisher allows users to crop graphics, which means that you can remove unwanted parts of the graphic to focus on the most important elements. To crop a graphic, select it and then click the "Crop" button in the "Format" tab. You can then click and drag the crop handles to remove parts of the graphic.')
    st.markdown('- Adding captions: Publisher allows users to add captions to graphics, which means that you can add a label or description to the graphic. To add a caption to a graphic, select it and then click the "Insert Caption" button in the "Format" tab. You can then type the caption in the "Caption" field.')
    st.markdown('- Adding hyperlinks: Publisher allows users to add hyperlinks to graphics, which means that you can create a link to a web page or other resource when the graphic is clicked. To add a hyperlink to a graphic, select it and then click the "Insert Hyperlink" button in the "Format" tab. You can then type the address of the web page or other resource in the "Address" field.')

    st.markdown('By working with graphics in Publisher, you can add visual interest and appeal to your documents and enhance their overall impact. Graphics are a powerful tool for conveying information and ideas, and Publisher provides a range of tools and options for working with them effectively.')


with st.expander("Working with Tables"):
    st.title('Working with Tables in Microsoft Publisher')

    st.markdown('Publisher provides a range of tools and options for working with tables in documents. Tables are a useful way to organize and present data, and Publisher provides a variety of ways to create, format, and manipulate tables. Here is an overview of how to work with tables in Publisher:')

    st.title('Creating Tables')
    st.markdown('To create a table in Publisher, follow these steps:')
    st.markdown('1. Open a document in Publisher and click the "Insert" tab.')
    st.markdown('2. In the "Tables" group, click the "Table" button to open the "Insert Table" window.')
    st.markdown('3. In the "Insert Table" window, choose the number of rows and columns you want in your table.')
    st.markdown('4. Click "OK" to insert the table into your document.')

    st.title('Formatting Tables')
    st.markdown('Once you have created a table in Publisher, you can use the formatting tools and options to customize its appearance and layout. Here are some examples:')
    st.markdown('- Changing cell sizes: To change the size of a cell in a table, select the cell and then click and drag the handles on the sides or corners. You can also use the "Cell Size" window in the "Format" tab to set the size of cells more precisely.')
    st.markdown('- Changing cell borders: To change the borders of a cell in a table, select the cell and then click the "Borders" button in the "Format" tab. You can then choose from the available border options, such as "All," "Inside," or "None." You can also use the "Borders and Shading" window to customize the appearance of borders more finely.')
    st.markdown('- Changing cell shading: To change the shading of a cell in a table, select the cell and then click the "Shading" button in the "Format" tab. You can then choose from the available shading options, such as "Fill Color," "Fill Pattern," or "Fill Effects." You can also use the "Borders and Shading" window to customize the appearance of shading more finely.')
    st.markdown('- Merging and splitting cells: To merge cells in a table, select the cells and then click the "Merge Cells" button in the "Format" tab. To split a merged cell, select the cell and then click the "Split Cells" button in the "Format" tab. You can then specify the number of rows and columns you want to split the cell into.')

    st.title('Manipulating Tables')
    st.markdown('Publisher provides a range of tools and options for manipulating tables in documents. Here are some examples:')
    st.markdown('- Inserting rows and columns: To insert a row or column in a table, click the row or column where you want to insert the new one and then click the "Insert" button in the "Format" tab. You can then choose to insert a row above, row below, column left, or column right.')
    st.markdown('- Deleting rows and columns: To delete a row or column in a table, click the row or column you want to delete and then click the "Delete" button in the "Format" tab. You can then choose to delete the row, column, or both.')
    st.markdown('- Sorting data: To sort the data in a table, click the "Sort" button in the "Format" tab. You can then specify the column or columns you want to sort by, as well as the sort order (ascending or descending).')
    st.markdown('- Applying formulas: Publisher allows users to apply formulas to cells in a table, which means that you can perform calculations on the data in the table. To apply a formula to a cell, click the cell and then type the formula in the formula bar. You can use the options in the "Formulas" tab to insert functions, such as SUM, AVERAGE, and MAX.')
    st.markdown('- Adding headers and footers: Publisher allows users to add headers and footers to tables, which means that you can repeat certain rows or columns at the top or bottom of each page. To add a header or footer to a table, click the "Header & Footer" button in the "Format" tab. You can then choose the rows or columns you want to repeat and specify the repeat direction (across or down).')
    st.markdown('By working with tables in Publisher, you can organize and present data in a clear and effective way. Tables are a powerful tool for conveying information and ideas, and Publisher provides a range of tools and options for working with them effectively.')

with st.expander("Working with Charts"):
    st.title('Working with Charts in Microsoft Publisher')

    st.markdown('Publisher provides a range of tools and options for working with charts in documents. Charts are a useful way to present data visually, and Publisher provides a variety of ways to create, format, and manipulate charts. Here is an overview of how to work with charts in Publisher:')

    st.title('Creating Charts')
    st.markdown('To create a chart in Publisher, follow these steps:')
    st.markdown('1. Open a document in Publisher and click the "Insert" tab.')
    st.markdown('2. In the "Illustrations" group, click the "Chart" button to open the "Insert Chart" window.')
    st.markdown('3. In the "Insert Chart" window, choose the type of chart you want to create, such as "Column," "Line," or "Pie."')
    st.markdown('4. Click "OK" to insert the chart into your document.')

    st.title('Formatting Charts')
    st.markdown('Once you have created a chart in Publisher, you can use the formatting tools and options to customize its appearance and layout. Here are some examples:')
    st.markdown('- Changing chart types: To change the type of a chart in Publisher, select the chart and then click the "Change Chart Type" button in the "Format" tab. You can then choose from the available chart types, such as "Column," "Line," or "Pie."')
    st.markdown('- Changing chart styles: To change the style of a chart in Publisher, select the chart and then click the "Change Chart Style" button in the "Format" tab. You can then choose from the available chart styles, such as "Style 1," "Style 2," or "Style 3."')
    st.markdown('- Changing chart layout: To change the layout of a chart in Publisher, select the chart and then click the "Layout" button in the "Format" tab. You can then choose from the available chart layouts, such as "Layout 1," "Layout 2," or "Layout 3."')
    st.markdown('- Changing chart data: To change the data in a chart in Publisher, select the chart and then click the "Data" button in the "Format" tab. You can then use the "Select Data Source" window to modify the data range and series for the chart.')

    st.title('Manipulating Charts')
    st.markdown('Publisher provides a range of tools and options for manipulating charts in documents. Here are some examples:')
    st.markdown('- Resizing and moving charts: To resize a chart in Publisher, select it and then click and drag one of the handles on the sides or corners. To move a chart, select it and then click and drag it to a new location. You can also use the "Size" and "Position" options in the "Format" tab to set the size and position of a chart more precisely.')
    st.markdown('- Adding titles and legends: To add a title or legend to a chart in Publisher, select the chart and then click the "Title" or "Legend" button in the "Format" tab. You can then type the title or legend in the corresponding field.')
    st.markdown('- Adding data labels and data table: To add data labels or a data table to a chart in Publisher, select the chart and then click the "Data Labels" or "Data Table" button in the "Format" tab. You can then choose from the available options, such as "Value," "Category," or "Series Name."')
    st.markdown('- Adding axis titles: To add axis titles to a chart in Publisher, select the chart and then click the "Axis Titles" button in the "Format" tab. You can then type the axis titles in the corresponding fields.')
    st.markdown('- Adding gridlines: To add gridlines to a chart in Publisher, select the chart and then click the "Gridlines" button in the "Format" tab. You can then choose from the available options, such as "Primary Major Horizontal," "Primary Major Vertical," or "Primary Minor Horizontal."')

    st.markdown('By working with charts in Publisher, you can present data visually in a clear and effective way. Charts are a powerful tool for conveying information and ideas, and Publisher provides a range of tools and options for working with them effectively.')

with st.expander("Working with Mail Merge"):
    st.title('Working with Mail Merge in Microsoft Publisher')

    st.markdown('Publisher provides a range of tools and options for working with mail merge in documents. Mail merge is a process that allows users to create personalized documents, such as letters, labels, or envelopes, using data from a list or database. Here is an overview of how to work with mail merge in Publisher:')

    st.title('Creating Mail Merge Documents')
    st.markdown('To create a mail merge document in Publisher, follow these steps:')
    st.markdown('1. Open a document in Publisher and click the "Mailings" tab.')
    st.markdown('2. In the "Start Mail Merge" group, click the "Start Mail Merge" button and then choose the type of document you want to create, such as "Letters," "Labels," or "Envelopes."')
    st.markdown('3. In the "Select Recipients" group, click the "Select Recipients" button and then choose the source of your recipient list, such as "Use an Existing List" or "Type a New List."')
    st.markdown('4. Follow the prompts in the "Mail Merge" window to complete the setup of your mail merge document.')

    st.title('Formatting Mail Merge Documents')
    st.markdown('Once you have created a mail merge document in Publisher, you can use the formatting tools and options to customize its appearance and layout. Here are some examples:')
    st.markdown('- Adding merge fields: To add merge fields to a mail merge document in Publisher, click the "Insert Merge Field" button in the "Write & Insert Fields" group. You can then choose from the available merge fields, such as "First Name," "Last Name," or "Address."')
    st.markdown('- Adding rules and conditions: To add rules and conditions to a mail merge document in Publisher, click the "Rules" button in the "Write & Insert Fields" group. You can then use the "If...Then" or "Go to Next" options to specify how the document should behave based on the data in the recipient list.')
    st.markdown('- Adding personalization: To add personalization to a mail merge document in Publisher, click the "Personalize" button in the "Write & Insert Fields" group. You can then use the "Greeting Line" or "Personalized Message" options to insert personalized text into the document.')
    st.markdown('- Previewing and reviewing: To preview and review a mail merge document in Publisher, click the "Preview Results" button in the "Preview Results" group.')

    st.title('Completing Mail Merge')
    st.markdown('Once you have finished formatting and previewing your mail merge document in Publisher, you can complete the process by completing the following steps:')
    st.markdown('1. In the "Finish" group, click the "Finish & Merge" button and then choose the option you want, such as "Print," "Email," or "Word Document."')
    st.markdown('2. In the "Merge to New Document" window, select the recipients you want to include in the merge and then click "OK."')
    st.markdown('3. If you selected the "Print" option, follow the prompts in the "Print" window to print your mail merge documents.')
    st.markdown('4. If you selected the "Email" option, follow the prompts in the "E-mail" window to send your mail merge documents via email.')
    st.markdown('5. If you selected the "Word Document" option, follow the prompts in the "Save As" window to save your mail merge documents as a Word document.')

    st.markdown('By working with mail merge in Publisher, you can create personalized documents that are tailored to your audience. Mail merge is a powerful tool for personalizing communication and streamlining processes, and Publisher provides a range of tools and options for working with it effectively.')

    st.title('Finishing and Printing Mail Merge Documents')
    st.markdown('To finish and print a mail merge document in Publisher, follow these steps:')
    st.markdown('1. Review and proofread the document carefully to ensure that it is accurate and error-free.')
    st.markdown('2. Click the "Finish & Merge" button in the "Finish" group.')
    st.markdown('3. In the "Finish Merge" window, choose the options for printing or saving the merged documents.')
    st.markdown('4. Click "OK" to complete the merge process.')

    st.markdown('By working with mail merge in Publisher, you can create personalized documents quickly and efficiently. Mail merge is a powerful tool for conveying information and ideas, and Publisher provides a range of tools and options for working with it effectively.')

with st.expander("Printing and Exporting Documents"):
    st.title('Printing and Exporting Documents in Microsoft Publisher')

    st.markdown('Publisher provides a range of tools and options for printing and exporting documents to other formats. Here is an overview of how to do this in Publisher:')

    st.title('Printing Documents')
    st.markdown('To print a document in Publisher, follow these steps:')
    st.markdown('1. Open the document in Publisher and click the "File" tab.')
    st.markdown('2. In the "Info" group, click the "Print" button to open the "Print" window.')
    st.markdown('3. In the "Print" window, choose the printer, page range, and other options for printing.')
    st.markdown('4. Click "Print" to send the document to the printer.')

    st.title('Exporting Documents to Other Formats')
    st.markdown('To export a document in Publisher to another format, follow these steps:')
    st.markdown('1. Open the document in Publisher and click the "File" tab.')
    st.markdown('2. In the "Save As" group, click the "Save As" button to open the "Save As" window.')
    st.markdown('3. In the "Save As" window, choose the format you want to export to, such as "PDF," "XPS," or "JPG."')
    st.markdown('4. Click "Save" to export the document to the chosen format.')

    st.markdown('By printing and exporting documents in Publisher, you can share your documents with others in a variety of ways. Printing and exporting are important tools for conveying information and ideas, and Publisher provides a range of tools and options for working with them effectively.')
