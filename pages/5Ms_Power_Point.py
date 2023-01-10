import streamlit as st

st.set_page_config(
    page_title="Microsoft Power Point",
    page_icon=":earth_africa:"
)
st.write("# The Microsoft Power Point LECTURE")

with st.expander("Introduction"):
    st.title('Microsoft PowerPoint')

    st.markdown(
        'PowerPoint is a presentation software that allows users to create and deliver dynamic and engaging slide shows. With PowerPoint, users can create professional-looking presentations that include text, graphics, images, audio, and video. Here is an overview of what PowerPoint can do:')

    st.title('Creating Slides and Layouts')
    st.markdown('To create slides and layouts in PowerPoint, follow these steps:')
    st.markdown('1. Open PowerPoint and click the "Home" tab.')
    st.markdown('2. In the "Slides" group, click the "New Slide" button to insert a new slide into the presentation.')
    st.markdown(
        '3. In the "Slides" group, click the "Slide Layout" button to choose a layout for the slide, such as "Title and Content," "Two Content," or "Comparison."')
    st.markdown('4. Use the formatting and layout tools in the "Home" tab to customize the appearance of the slide.')

with st.expander("Working with Text and Graphics"):
    st.title('Working with Text and Graphics')
    st.markdown('To work with text and graphics in PowerPoint, follow these steps:')
    st.markdown('1. Select the text or graphic you want to work with by clicking it.')
    st.markdown(
        '2. Use the formatting tools in the "Home" tab to customize the appearance of the text or graphic, such as font, size, color, or alignment.')
    st.markdown(
        '3. Use the layout tools in the "Format" tab to arrange the text or graphic on the slide, such as size, position, or wrapping.')

    st.title('Adding Media and Transitions')
    st.markdown('To add media and transitions in PowerPoint, follow these steps:')
    st.markdown(
        '1. Click the "Insert" tab and choose the type of media you want to add, such as "Pictures," "Audio," or "Video."')
    st.markdown('2. Follow the prompts to insert the media into the slide.')
    st.markdown(
        '3. Click the "Animations" tab and choose the transition you want to use for the slide, such as "Fade," "Wipe," or "Fly In."')
    st.markdown(
        '4. Use the animation tools in the "Animations" tab to customize the transition, such as duration, start, or effect options.')

    st.markdown(
        'With PowerPoint, you can create dynamic and engaging presentations that captivate your audience. PowerPoint is a powerful tool for conveying information and ideas, and it provides a range of tools and options for working with them effectively.')

with st.expander("Slide Master"):
    st.title('Slide Master in Microsoft PowerPoint')

    st.markdown(
        'A slide master is a template that defines the formatting and layout options for all the slides in a presentation in Microsoft PowerPoint. With a slide master, you can apply formatting and layout options to multiple slides at once, which saves time and ensures that your presentation looks consistent and polished. Here are some examples of what you can do with a slide master in PowerPoint:')

    st.markdown(
        '- Create and edit a slide master: To create and edit a slide master in PowerPoint, click the "View" tab and then click the "Slide Master" button. You can then use the formatting and layout tools in the "Master" tab to customize the appearance of the master slides. You can also create multiple masters for different types of slides, such as title slides, content slides, or summary slides.')
    st.markdown(
        '- Apply formatting and layout options to slides: To apply formatting and layout options to slides using a slide master in PowerPoint, click the "Slide" tab and then click the "Slide Layout" button. You can then choose a layout for the slide, such as "Title and Content," "Two Content," or "Comparison." The formatting and layout options of the slide master will be applied to the slide automatically.')
    st.markdown(
        '- Modify and update formatting and layout options: To modify and update formatting and layout options in a slide master in PowerPoint, click the "Slide Master" button and then click the "Master" tab. You can then use the formatting and layout tools in the "Master" tab to customize the appearance of the master slides. You can also click the "Apply to All" button to apply the changes to all the slides in the presentation.')

    st.markdown(
        'By using a slide master in PowerPoint, you can create consistent and professional-looking presentations that impress and engage your audience. A slide master is a powerful tool for conveying information and ideas effectively, and it provides a range of tools and options for working with them efficiently.')
    st.title('Creating and Editing Tables and Charts')
    st.markdown(
        'Tables and charts are effective tools for presenting data and information visually in PowerPoint. With tables and charts, you can create professional-looking graphics that help your audience understand and interpret data more easily. Here are some examples of what you can do with tables and charts in PowerPoint:')
    st.markdown(
        '- Create and edit tables: To create and edit tables in PowerPoint, click the "Insert" tab and then click the "Table" button. You can then use the formatting and layout tools in the "Table Tools" tab to customize the appearance and structure of the table. You can also import data from external sources, such as Excel or Access, or create pivot tables to summarize and analyze data.')
    st.markdown(
        '- Create and edit charts: To create and edit charts in PowerPoint, click the "Insert" tab and then click the "Chart" button. You can then choose the type of chart you want to create, such as a column chart, line chart, or pie chart. You can also use the formatting and layout tools in the "Chart Tools" tab to customize the appearance and data of the chart.')

    st.title('Tips for Using Slide Masters to Apply Consistent Formatting and Design Across Multiple Slides')

    st.markdown(
        'Slide masters are a powerful tool in Microsoft PowerPoint that allow you to apply consistent formatting and design across multiple slides in your presentation. Here are some tips for using slide masters effectively:')

    st.markdown('''1. Start with a blank slide master: When creating a new slide master, it is best to start with a blank slide rather than using one of the built-in templates. This will give you more control over the layout and design of your slides. 
    
    2. Use custom styles: To make it easier to apply consistent formatting to your slides, create custom styles for text, shapes, and other objects. This way, you can quickly apply your desired formatting to any element on your slides.
    
    3. Use placeholders: Placeholders are pre-defined areas on your slide master that can be used to add text, images, or other content. Using placeholders allows you to ensure that all of your slides have a consistent layout and design.
    
    4. Use slide layouts: Slide layouts are pre-defined layouts that can be applied to individual slides in your presentation. You can create custom slide layouts to suit your specific needs, or use one of the built-in layouts provided by PowerPoint.
    
    5. Keep it simple: When designing your slide master, try to keep things simple and avoid using too many different fonts, colors, or graphics. A clean, professional look is usually the best choice for business presentations.
    
    By following these tips, you can use slide masters effectively to create consistent, professional-looking presentations in PowerPoint.''')

with st.expander("Working with SmartArt and Shapes"):
    st.title('Working with SmartArt and Shapes')
    st.markdown(
        'SmartArt and shapes are powerful tools for adding visual interest and meaning to presentations in PowerPoint. With SmartArt and shapes, you can create graphics that convey information and ideas in a clear and concise way. Here are some examples of what you can do with SmartArt and shapes in PowerPoint:')
    st.markdown(
        '- Create and edit SmartArt: To create and edit SmartArt in PowerPoint, click the "Insert" tab and then click the "SmartArt" button. You can then choose from the available SmartArt categories, such as "List," "Process," or "Hierarchy." You can also use the formatting and layout tools in the "SmartArt Tools" tab to customize the appearance and data of the SmartArt.')
    st.markdown(
        '- Create and edit shapes: To create and edit shapes in PowerPoint, click the "Insert" tab and then click the "Shapes" button. You can then choose from the available shapes, or draw your own custom shapes using the drawing tools. You can also use the formatting and layout tools in the "Format" tab to customize the appearance and behavior of the shapes, such as color, size, or animation.')

    st.title('Working with Animations and Transitions')
    st.markdown(
        'Animations and transitions are powerful tools for adding visual interest and dynamics to presentations in PowerPoint. With animations and transitions, you can create engaging and interactive presentations that captivate your audience. Here are some examples of what you can do with animations and transitions in PowerPoint:')
    st.markdown(
        '- Create and edit animations: To create and edit animations in PowerPoint, click the "Animations" tab and then click the "Animation Pane" button. You can then choose the type of animation you want to use, such as "Entrance," "Exit," or "Emphasis." You can also use the animation tools in the "Animations" tab to customize the duration, start, and effect options of the animations.')
    st.markdown(
        '- Create and edit transitions: To create and edit transitions in PowerPoint, click the "Transitions" tab and then click the "Transition to This Slide" button. You can then choose the type of transition you want to use, such as "Fade," "Wipe," or "Fly In." You can also use the transition tools in the "Transitions" tab to customize the duration, sound, and effect options of the transitions.')

    st.title('Collaborating and Sharing Presentations')
    st.markdown(
        'PowerPoint provides a range of tools and options for collaborating and sharing presentations with others. With these tools, you can work on presentations with colleagues, clients, or classmates, and share your ideas and feedback in real time. Here are some examples of what you can do with collaboration and sharing tools in PowerPoint:')
    st.markdown(
        '- Collaborate on presentations online: To collaborate on presentations online in PowerPoint, click the "File" tab and then click the "Share" button. You can then invite others to collaborate on the presentation using their email addresses or Microsoft accounts. You can also use the review and comment tools in the "Review" tab to track changes and provide feedback on the presentation.')
    st.markdown(
        '- Share presentations through social media: To share presentations through social media in PowerPoint, click the "File" tab and then click the "Export" button. You can then choose the "Create Handouts" option and select the "Send Handouts via Email" option. You can then enter the email addresses of the recipients and select the social media service you want to use, such as "Facebook," "Twitter," or "LinkedIn."')
    st.markdown(
        '- Publish and present presentations online: To publish and present presentations online in PowerPoint, click the "File" tab and then click the "Publish" button. You can then choose the "Create a Video" option and select the "Create a Video" option. You can then choose the video quality and duration, and click "Create Video" to publish the presentation as a video file. You can then share the video file online or embed it in a website or blog.')

    st.markdown(
        'By learning and using the advanced features in PowerPoint, you can create and deliver professional-quality presentations that engage and inform your audience. PowerPoint is a powerful tool for conveying information and ideas, and it provides a range of tools and options for working with them effectively.')

with st.expander("Advance audio and video features"):
    st.title('Advanced Audio and Video Features in Microsoft PowerPoint')

    st.markdown(
        'PowerPoint allows you to enhance your presentations with audio and video elements. Here are some advanced features you can use to make your audio and video content more effective:')
    st.markdown(
        'Insert the audio or video clip: To insert an audio or video clip into your PowerPoint presentation, go to the "Insert" tab and click the "Audio" or "Video" button. Select the clip you want to insert and click "Insert.'
        'There after, follow the following steps')

    st.markdown('''
    1. Trimming audio and video clips: You can trim audio and video clips in PowerPoint to remove any unnecessary content. To do this, select the clip and then click the "Trim" button on the "Playback" tab. You can then drag the trim handles to adjust the start and end points of the clip.
    
    2. Adding fade-in and fade-out effects: You can use fade-in and fade-out effects to smoothly transition between audio and video clips in your presentation. To do this, select the clip and then click the "Fade In" or "Fade Out" button on the "Playback" tab.
    
    3. Setting start and end points: You can set the start and end points for audio and video clips in your presentation. This allows you to play only a portion of the clip rather than the entire thing. To do this, select the clip and then click the "Start" and "End" buttons on the "Playback" tab.
    
    4. Adding captions: You can add captions to audio and video clips in your presentation to provide additional context or to make the content more accessible to viewers. To do this, select the clip and then click the "Captions" button on the "Playback" tab.
    
    5. Adding audio and video effects: You can enhance the audio and video elements in your presentation by adding effects such as volume control, fade in/out, or speed control. To do this, select the clip and then click the "Audio Effects" or "Video Effects" button on the "Playback" tab.
    
    By using these advanced audio and video features in PowerPoint, you can create more engaging and effective presentations.''')

    st.title('Tips for Using Advanced Audio and Video Features to Enhance the Impact of a Presentation')

    st.markdown('Audio and video elements can be a powerful way to enhance the impact of a presentation. Here are some tips for using advanced audio and video features effectively:')

    st.markdown('''
    1. Keep it relevant: Only use audio and video elements that are directly relevant to your presentation. Don't just include them for the sake of it.
    
    2. Keep it brief: Keep your audio and video clips as brief as possible. People's attention spans are limited, so the shorter the better.
    
    3. Use high-quality content: Use high-quality audio and video content to avoid any distractions or disruptions in your presentation.
    
    4. Use fade-in and fade-out effects: Use fade-in and fade-out effects to smoothly transition between audio and video clips. This helps to keep your presentation flowing smoothly.
    
    5. Use captions: Use captions to provide additional context or to make the content more accessible to viewers. This can be especially helpful if you are presenting in a noisy or crowded environment.
    
    By following these tips, you can use advanced audio and video features to effectively enhance the impact of your presentation.''')


with st.expander("Other Resources"):
    st.title('YouTube Channels to Learn Advanced PowerPoint')

    st.markdown('There are many YouTube channels that offer tutorials and lessons on advanced PowerPoint techniques. Here are a few suggestions:')

    st.markdown('''
    1. PowerPoint Tips: This channel is run by PowerPoint expert, Echo Swinford, who has over 20 years of experience using the software. She offers a wide range of PowerPoint tutorials, including advanced topics like slide design, animations, and using PowerPoint with other Office applications.
    
    2. PowerPoint School: This channel is run by PowerPoint expert, Rohit Srivastwa, who has over 10 years of experience using the software. He offers a range of PowerPoint courses and tutorials, including an advanced course that covers topics like slide design, animations, and working with data.
    
    3. PowerPoint Training Academy: This channel is run by PowerPoint expert, David Marcinko, who has over 20 years of experience using the software. He offers a range of PowerPoint courses and tutorials, including an advanced course that covers topics like slide design, animations, and working with data.
    
    4. PowerPoint Master: This channel is run by PowerPoint expert, Jess Stratton, who has over 20 years of experience using the software. She offers a range of PowerPoint courses and tutorials, including an advanced course that covers topics like slide design, animations, and working with data.
    
   ''')
