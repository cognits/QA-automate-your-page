import os
import os.path
import webbrowser

HTML_HEAD = """
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Generator</title>
        <link rel="stylesheet" type="text/css" href="styles.css">
    </head>
"""

HTML_BODY = """
    <body>
        <article>
            <h2>Programming</h2>
            <p>Programming is the process
             of taking an algorithm and encoding
             it into a notation, a programming language,
             so that it can be executed by a computer.
             Although many programming languages and many different
             types of computers exist, the important first step is
             the need to have the solution. Without an algorithm
             there can be no program.</p>
        </article>
        <article>
            <h2>Functions</h2>
            <p>Functions are "self contained" modules of
            code that accomplish a specific task.
            Functions usually "take in" data, process
            it, and "return" a result. Once a function is
            written, it can be used over and over and over 
            again. Functions can be "called" from the
            inside of other functions.</p>
        </article>
        <article>
            <h2>Variables</h2>
            <p>In computer programming, a variable or scalar is a storage
            location paired with an associated symbolic name (an identifier),
            which contains some known or unknown quantity
            or information referred to as a value.</p>
        </article>
        <article>
            <h2>Loops</h2>
            <p>In computer programming, a loop is a sequence of instructions
            that iscontinually repeated until a certain condition is reached. </p>
        </article>
        <article>
            <h2>Python Lists</h2>
            <p>The list is a most versatile datatype available in Python
            which can be written as a list of comma-separated values (items)
            between square brackets.Important thing about a list is that
            items in a list need not be of the same type.</p>
        </article>
        <article>
            <h2>Python dictionaries</h2>
            <p>Each key is separated from its value by a colon (:),
            the items are separated by commas, and the whole thing
            is enclosed in curly braces. An empty dictionary without
            any items is written with just two curly braces, like this: {}.</p>
            <p>Keys are unique within a dictionary while values may not be.
            The values of a dictionary can be of any type, but the keys must be
            of an immutable data type such as strings, numbers, or tuples.</p>
        </article>
    </body>
</html>
"""
HTML_STRUCTURE = [HTML_HEAD, HTML_BODY]

def html_exist():
    return os.path.isfile('index.html')

def creating_html():
    html_file = open('index.html','w')
    html_file.close()

def recording_info(structure_html):
    html_writing = open('index.html', 'a')
    for structure in structure_html:
        html_writing.write(structure)
    html_writing.close

def open_page():
    webbrowser.open('index.html')

def creating_functions():
    exist_page = html_exist()

    if exist_page == True:
        print ""
        print "    The html file already exist"
        print ""
    raw_input("    Press enter")
    creating_html()
    recording_info(HTML_STRUCTURE)
    print HTML_HEAD, HTML_BODY
    open_page()

creating_functions()

