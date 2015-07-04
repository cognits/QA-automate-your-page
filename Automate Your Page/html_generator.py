"""This set of functions takes an input, notes, formatted in a list with lists containing the title and notes"""

#List
notes = ["Lists", "Lists are one of the most powerful storage containers in Python. They are a mutable structure that can hold things like variables, numbers, strings and even other lists. Individual aspects of a list can be changed while not becoming a new, copied list."], ["Index", "Indexing in lists grabs the position of an element in a list. You can using slicing with these indexes to grab certain items in a list."], ["Mutation vs Copied", "While lists can be mutated they can also be copied and will be with certain functions. When concatenating two lists a new list is created to hold the elements. Changing specific values at certain indexes or using a function such as .append mutates the list into holding new or more elements."], ["Finding Length", "To find the length of an element such as a string or list the 'len' function is used. It will return the number of items in a list or characters in a string."], ["In", "The function 'in' is used in a boolean fashion. If x can be found in y, True will be returned. Otherwise it will return False. This can be used to find a certain word in a long string or a certain element in a list."], ["Devensive Programming", "Defensive programming is the practice of desigining code so that it can deal with circumstances that were unintended and allows for the program to continue running instead of crashing."], ["Problem Solving", "Problem solving is a vital process to coding. When trying to figure out how to code or deal with a problem, you need to break it down into several steps. Figure out the input and the output. Write some pseudocode to get an idea of how to structure the code. Then you pick the foundation of the code and begin. After every part extensive testing should be done to ensure the code functions as intended."]

#Function than show the concepts
def html_note_structure(concept):
	"""Puts together a title and note into an html structure"""
	html1 = """<div class="note">
	<h3>""" + concept[0]
	html2 = """</h3>
	<p>
		""" + concept[1]
	html3 = """
	</p>
</div>

"""

	return html1 + html2 + html3

def much_html(concepts):
	"""Repeats html_note_structure until all of notes has been structured"""
	HTML = ""
	#Loop for the Concepts
	for concept in concepts:
		HTML += html_note_structure(concept)
	return HTML

#print the HTML structure in the console
print much_html(notes)