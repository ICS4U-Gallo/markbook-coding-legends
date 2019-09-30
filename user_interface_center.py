from markbook import *
from data_managment_methods import *
import time
import os

clear = lambda: os.system("clear")

class user_interface_controller:
	"""Class obj that interacts with the user to fufill requests"""

	def __init__(self, class_data, filename):
		self.filename = filename
		self.data = class_data

	def help(self):
		print("""\nCommands List:
		--> exit
		--> help
		--> save
		--> add-student
		--> remove-student
		--> add-assignment
		--> add-student-mark
		--> calculate-student-avg
		--> show-students
		--> edit-student-info\n""")

	def add_student(self):
		fields = []

		fields.append(input("\nStudent First Name.....  "))
		fields.append(input("\nStudent Last Name.....  "))

		student = create_student(fields[0], fields[1])

		add_student_to_classroom(student, self.data)
		
		temp_dict = self.data["student_list"][-1]
		temp_string = "\n%s %s, has been added to the class list \n" % (temp_dict["first_name"], temp_dict["last_name"])
		
		print(temp_string)

	def remove_student(self):
		
		def temp_func(first_name, last_name):
			for student in self.data["student_list"]:
				if student["first_name"] == fields[0] and student["last_name"] == fields[1]:
					remove_student_from_classroom(student, self.data)
					return True
		while True:

			fields = []

			
			fields.append(input("\nStudent First Name.... "))
			fields.append(input("\nStudent Last Name.... "))

			if temp_func(fields[0], fields[1]) is True:
				break

	def add_assignment(self):
		fields = []

		fields.append(input("\nName of the assignemnt -->"))
		fields.append(input("\nDue date -->"))
		fields.append(input("\nPoints the assignemnt is out of -->"))

		temp_assignnment = create_assignment(fields[0],fields[1],fields[2])

		self.data["assignment_list"].append(temp_assignnment)

	def add_student_mark(self):
		def temp_func(first_name, last_name):

			i = 0

			for student in self.data["student_list"]:
				
				if student["first_name"] == first_name and student["last_name"] == last_name:
					return i, True 
				i += 1

			else:
				return -1, False
		
		def temp_func1(assignment_name, student):
			
			i = 0

			for task in student["assignment_list"]:
				if task["name"] == assignment_name:
					return i, True
				i += 1
			
			else:
				return -1, False
			
			
		while True:

			fields = []

			fields.append(input("\nStudent's first name...  "))
			fields.append(input("\nStudent's last name... "))
			fields.append(input("\nFor what assignment...  "))
			fields.append(input("\nWhat mark his he/she recieve...  "))
		
			student_index, boolean = temp_func(fields[0],fields[1])

			if boolean is True:
				
				assignment_index, boolean = temp_func1(fields[2])
				
				if boolean is True:
					add_student_mark(self.data["student_list"][student_index]["assignemnt_list"][assignment_index])
				
				else:
					print("\nThe assignment's name does not exist...en")
			else:
				print("\nThat student does not exist...")
	
	def calculate_student_avg(self):
		def temp_func(first_name, last_name):
			""" A temp function used for breaking from a nested for loop, within a while loop
			
			Args:
				-fist_name
				-second_name
			
			Returns:
				boolean for breaking
				"""
			
			for student in self.data["student_list"]:

					if first_name == student["first_name"] and last_name == student["last_name"]:
						msg = "\nRyan has a %s avg" % calculate_average_mark(student, self.data)
						print(msg)
						break
		while True:
			
			#If the user cannot pick a student, because non exist, break from the loop
			if self.data["student_list"] == []:
				break

			fields = []
			print("\nTo leave this menu enter \"exit\".")

			
			fields.append(input("\nStudent First Name -->"))
			
			#The user can enter a exit command to leave at any time.
			if fields[-1] == "exit" or fields[-1] == "exit":
				break

			fields.append(input("\nStudent Last Name -->"))

			if fields[-1] == "exit" or fields[-1] == "leave":
				break
			
			#To check for student existance, a nested for loop prevents breaking from inside the second layer
			if temp_func(fields[0], fields[1]) is True:
				break		
		
			else:
				print("Student not found, please try again....")
				
	def edit_student_info(self):
		"""Edits a specified student's info using key/value input pairs
		Args:
			-None
		"""
		fields = []

		fields.append(input("Student First name -->  "))
		fields.append(input("Student Last name -->  "))

		while True:

			key = input("What about the student are you altering? first_name? Or last_name......")
			value = input("What do you want it to be changed too.....")

			for i in range(len(self.data["student_list"])):

				if self.data["student_list"][i]["first_name"] == fields[0] and self.data["student_list"][i]["last_name"] == fields[1]:
					edit_student(self.data["student_list"][i], key, value)
					
					break
				
			else:
				print("invalid \'key\', please try \'fist_name\', or \'last_name\'.")

	def show_students(self):
		"""Prints every student within the present student list (self.data["student_list"])"""
		
		for student in self.data["student_list"]:

			print("\n",student["first_name"], student["last_name"])

	def update(self, cmd):
		"""Used to route the general input stream into the user_interface_center 
		Args:
			-user command -> cmd
		
		Returns:
			-None
		"""

		if cmd == "help":
			self.help()
		
		elif cmd == "add-student":
			self.add_student()

		elif cmd == "remove-student":
			self.remove_student()

		elif cmd == "add-assignment":
			self.add_assignment()

		elif cmd == "calculate-student-avg":
			self.calculate_student_avg()

		elif cmd == "generate-student-report":
			self.generate_student_report()

		elif cmd == "edit-student-info":
			self.edit_student_info()

		elif cmd == "add-student-mark":
			self.add_student_info()

		elif cmd == "save":
			save_classroom_data(self.filename, self.data)

		elif cmd == "show-students":
			self.show_students()
		else:
			print("Unknown command..... \n")
			self.help()
