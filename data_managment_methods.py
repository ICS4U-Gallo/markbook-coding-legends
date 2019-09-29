import os
import time
import json
from markbook import *

clear = lambda: os.system("clear")

def initialize_session():
	"""Either creates a classroom, or loads a previous one from a json file

	Args:
		None
	
	Returns:
		-The new or old JSON file name with .json file notation
		-A dictionary of all the working classroom data
	"""

	clear()

	while True:

		req = input("""\nWould you like to \"create\" a new classroom.
Open a pre-existing one with \"open\".
Delete a pre-existing class with \"remove\".
Or \"list\" all existing classrooms......  """)

		if req == "open" or req == "Open":
			filename = input("\nWhat is the courses\' code......  ") + ".json"

			try:
				class_data = load_classroom_data(filename), filename
				return class_data

			except:
				print("\nUnable to find the course code.....\n") 

		elif req == "create" or req == "Create":

			filename = input("\nWhat is the course code of the classroom you would like to create......  ") + ".json"

			classroom = initialize_markbook(filename)
			
			return classroom, filename

		elif req == "list" or req == "List":

			if os.listdir("classes") == []:
				print("\nThere are no files to delete\n")

			else:
				for f in os.listdir("classes"):
					
					slice_range = len(f) - 5 #slicing off the .json (char length of 5)
					print(f"\n-{f[0:slice_range]}")

		elif req == "remove" or req == "Remove":
			
			while True:
				
				req = input("\nTo leave this action enter \"exit\", select a filename for deletion, or \"list\" to see all classes...\n\n")

				
				if req == "exit" or req == "Exit":
					break 

				elif os.listdir("classes") ==  []:
					print("No files to remove......")
	
				elif req == "list" or req == "List":
					for f in os.listdir("classes"):
						slice_range = len(f) - 5 #slicing off the .json (char length of 5)
						print(f"\n-{f[0:slice_range]}")

				else:
					filename = "%s.json" % (req)

					if filename in os.listdir("classes"):
					
						remove_path = "classes/%s" % (filename)
					
						os.remove(remove_path)

						print("removed " + req)
		else:
			print("Error - unknown request, enter either \"open\", \"create\", \"list\", or \"remove\".")

def initialize_markbook(filename):
	"""Creates a new classroom dictionary by interfacing with the user

	Args:
		None
	
	Returns:
		-A dictionary of classroom data
	"""

	wait_seconds = 0

	print("\nInitializing Markbook, fill in requests fields.")
	time.sleep(wait_seconds)

	teacher = input("\nTeacher...  ")
	time.sleep(wait_seconds)

	course_code = input("\nCourse Code...  ")
	time.sleep(wait_seconds)

	course_name = input("\nCourse Name...  ")
	time.sleep(wait_seconds)

	period = input("\nWhat period is it...  ")
	time.sleep(wait_seconds)

	classroom = create_classroom(course_code, course_name, period, teacher)

	path = "classes/%s" % (filename)

	with open(path, "w") as f:
		json.dump(classroom, f)

	return classroom

def load_classroom_data(filename):
	"""Returns a classroom json file

	Args:
		JSON filename
	
	Return:
		-the json data
	"""

	path = "classes/%s" % (filename)

	with open(path, 'r') as json_file:
		return json.load(json_file)

def save_classroom_data(filename, data):
