# coding: utf-8
sample = '''
title: Project 2 Notes

title: Breaking Problems into Smaller Pieces

definition:Computers
Computer Programs
Computer Science is how to solve problems, by breaking them into smaller pieces and making a procedure for the computer.
Programming is the core of computer science.

title:Programming tips
tips:
Computer:
Designed to do anything, universal machine, it can do any program.
Program:
Tells computer what to do
I is a series of instructions
Use precise sequence of steps
Computation (use rules of 3, convert units and consider Hz)
High-level language:
Python
Instead of running on computer , it runs on interpreter

title:Why not English?
definition: We have to use computer language, since it is less ambiguous. Verbosity is also a factor, since we need less lines to describe a step.

title: Inputs and Outputs
definition: Inputs are all the data that we are getting into our system
definition: Outputs are all the data that we pretend to get out of our system
definition: The system si the series of procedures we make to turn the input into the output
	
title:Functions
definition:
What is a function?
A function is a series of procedures within our program that will (intendedly) be used more than once.
The purpose of programming is to avoid repetition, with Functions, we can use the same procedure several times without repeating code.
definition:How to make a function?
in python we use: 
def function(input):
	pass
	return output
		
definition:When you should write a function?
Whenever we need to repeat a procedure.
definition:Why are functions so valuable.
They will help us to reduce our programming time, they avoid code repetition.


title:Loops
definition:Loops help us repeat procedures. Useful for iterative purposes.
IMAGE:https://pythonproject.files.wordpress.com/2014/02/recursion_for_while.jpg


title:Lists
definition: The list is a most versatile datatype available in Python which can be written as a list of comma-separated values (items) between square brackets. Important thing about a list is that items in a list need not be of the same type.

title:Rules of Problems
tips:
0. Don’t Panic
1. What are the Inputs
2. What are the outputs?
3. Solve the problem
Defensive Programing, avoid errors checking in cod
'''

# This function finds the start of the definitions or Concepts 
def separate_concepts(text, text_to_find):
	concept_location = []
	i = 0
	while i <len(text):
		i = text.find(text_to_find,i)
		if i != -1:
			concept_location.append(i+len(text_to_find))
		else :
			break
		i = i + len(text_to_find)
	return concept_location
#Now we will form 2 new lists with the separate_concepts function
definition_list = separate_concepts(sample,'definition:')
title_list = separate_concepts(sample,'title:')
tips_list = separate_concepts(sample,'tips:')
image_list = separate_concepts(sample,"IMAGE:")
#Now we have to find a way to "join" the 4 lists

def rename_lists(old_list,concept):
	#we will create a list of lists, to be later rearanged
	new_list = []
	for i in old_list:
		new_list.append([i,concept])
	return new_list
list_end = [len(sample)-1,'']

# list_end was made to get the end of the text
# we should join all the rename lists and later rearrange them in order
list_to_join = rename_lists(definition_list,'definition') + rename_lists (title_list,'title') + rename_lists (tips_list, 'tips') +rename_lists(image_list,'IMAGE') + [list_end]
list_to_join.sort()

#this will generate our Div containers
def div_kind(kind):
	
	if kind != 'IMAGE':
		first_part = '<div class = "%s' %(kind)
		last_part = '''" >
'''
	else:
		first_part = '<div class = "%s" ><img src="' %(kind )
		last_part = ''
	return first_part+last_part

def div_end(kind):
	if kind !='IMAGE':
	 	return '''</div>
'''
	else:
		return '''"></div>
'''
def print_html(text,concept_list):
	html_out= ''
	x = 1 # 1 will be the enclosing div 
	for i in range(0,len(concept_list)-1):
		start = concept_list[i][0]
		end = concept_list[i+1][0]-len(concept_list[i+1][1])-1
		text_to_print = text[start:end]  #It separates the text or image
		html_out = html_out + div_kind(concept_list[i][1])+ text_to_print + div_end(concept_list[i][1])
		
	return html_out
#to simplyfiy the steps, we will find <div clas = image 

html_header = """<!DOCTYPE html>
 <html>
<head>
	<meta charset="UTF-8">
	<title>Automate your page</title>
	<link rel="stylesheet" href="main.css">
<body>
"""
html_footer = """</body>		
</html>"""
print html_header + print_html(sample,list_to_join) + html_footer