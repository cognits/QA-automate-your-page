 # -*- coding: utf-8 -*-
 #arrays store data displayed when generating code
 #and showing console information
notes = [['Python and Computer Science Intro', '''Sometimes it can be 
difficult to know where to start with a computer program as there is 
so much to complete. First you must break down the problem into smaller 
pieces and tackle each as their own entity. With code you can precicely 
describe the steps required to solve the problem and these steps can be
completed by a computer! A computer is just a machine that can be 
programmed, and it can do almost anything so long as a program is 
written that can tell it what to do!
 
At first it may seem strange that we need new languanges in order to 
tell a computer what do to, but this is due to a number of inherant 
problems with languages such as English; primarily they are too ambiguous 
and verbose! So there are a number of programming languages out there to 
learn that will enable a person to write instructions, or a "program", 
that will tell a computer what to do.'''],

['Debugging', '''When using example code always test it to make sure
it works properly to begin with. If you have problems and need to debug 
your own code, just comment it out to begin with so when you get it 
working you will be able to see where you went wrong to begin with and 
learn from it. Sometimes is is also helpful when debugging code to 
introduce print statements so that you can see what variables are set 
to at various points throughout your code. This can help identify 
where the problem is.

'Debuigging Strategy:'
1) Examine error messages when programs crash
2) Work from example code
3) Make sure examples work
4) Check (print) intermediate results
5) Keep and compare old versions''']]
#the functions used in the code show what is the 
#title, the Descripsion and content stored in the arrays, so console display content
def generate_information_HTML(information_title, information_description):
    html_text_1 = '''
<div class="concept">
    <div class="concept-title">
        ''' + information_title
    html_text_2 = '''
    </div>
    <div class="concept-description">
        ''' + information_description
    html_text_3 = '''
    </div>
</div>'''
    all_html_text = html_text_1 + html_text_2 + html_text_3
    return all_html_text

def return_HTML_Information(notes):
    all_html = ''
    num = 0
    for item in notes:
        information = notes[num]
        information_html = generate_information_HTML(information[0], information[1])
        all_html = all_html + information_html
        num = num+1
    return all_html

print return_HTML_Information(notes)



