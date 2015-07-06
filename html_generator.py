
 # -*- coding: utf-8 -*-
notes = [['Basics', '''The internet is full of lots of servers hosting web pages which are basically HTML (HyperText Markup Language) documents my browser can interpet and present to me.
 HTML is made up of Tags, Attributes and Elements. Some tags are inline and some tags are block, the latter of which essentially puts a 'box' around the content allowing for additional
 specific formatting. DIV is an example of a block element, whereas SPAN is an example of an inline element, but both are container elements. Usually an opening TAGs will need a closing
 TAG except in the case of void tags such as "img" or "br", void tags do not require a corresponding closing tag. 

HTML Tags can reference text, images, audio, video or even just plain old text - all filetypes can exist on the internet! 

Two of the most important things to remember from the first lesson
1. Computers are Stupid! Computers need very specific instructions and will perform exactly what you ask for, they cannot make intuitive guesses (Well, maybe with AI but that is waaaay out
of scope!)
2. It's ok to forget! It is not possible for everyone to remember everything, but what is important is to have knowledge of the existence of the subject matter so you know where to start
looking. 
'''],
        ['HTML' , '''HTML is at the heart of the internet and can be thought of in 4 different elements 
1.Text Content - This is what you SEE 
2. Markup - What it LOOKS LIKE 
3. Refrences - Links to images, videos or other documents. 
4. Links to other HTML Pages! 
•Web pages are made up of rectangles, but remember that not all are visible.
•HTML Controls the structure of a web page whereas CSS controls the style of the page and both are 'languages'.
•When programmers talk about the DOM they are talking about the structure of the page
•Browsers take the HTML Tag and turn them into elements of a tree
•Boxes are defined with DIV tags
•Use CLASS attributes to define styles
•HTML tags can belong to multiple classes
•Use SPAN and DIV to group related content together
'''],
        ['Boxes', '''When creating a structured document you must first divide everything up into boxes and define those boxes with DIV tags. You can also give each element a CLASS
attribute so that you can easily apply styles afterwards. Tag's can belong to multiple Classes. 

Boxes have 4 elements: 
1.Margin
2.Border
3.Padding
4.Content

 The code box-sizing:border-box will allow you to set the size of the total box including the border and margin, which makes it much easier to determine the actual size of the box rather
 than just the content. In addition, you can choose to set the size in terms of percentage of screen rather than defined pixel count!'''],
        ['CSS', '''CSS (Cascading Style Sheets) allows you to add style to the website or text and correctly structured will allow programmers to avoid repitition. We do not want to have
to repeat the same style code over and over again since it wastes time, is difficult to manage and susceptible to errors. What we want is for the code to cascade through the site and only
well structured code will allow that!

 There is a CSS library available to use by following this link.

 CSS can be stored either in the HTML or within a separate CSS file of it's own, which is usually the better option for all but the most basic of sites. If you do have a separate CSS file
 you must locate this within the same folder as the HTML file referencing it. To reference it,
 in the HEAD tag include the stylesheet "link" reference line. (Type link and hit tab!)''']

         ]



def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = '''
<div class="concept">
    <div class="concept-title">
        ''' + concept_title
    html_text_2 = '''
    </div>
    <div class="concept-description">
        ''' + concept_description
    html_text_3 = '''
    </div>
</div>'''
    
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text



def return_HTML_Text(notes):
    all_html = ''
    num = 0
    for item in notes:
        concept = notes[num]
        concept_html = generate_concept_HTML(concept[0], concept[1])
        all_html = all_html + concept_html
        num = num+1
    return all_html


print return_HTML_Text(notes)



