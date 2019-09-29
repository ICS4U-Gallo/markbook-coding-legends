from markbook import *
from data_managment_methods import *
import time
import os

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
		--> calculate-student-avg
		--> show-students
		--> edit-student-info\n""")

	def add_student(self):
		fields = []

		fields.append(input("Student First Name.....  "))
		fields.append(input("Student Last Name.....  "))

		student = create_student(fields[0], fields[1])

		add_student_to_classroom(student, self.data)
		
		temp_dict = self.data["student_list"][-1]
		temp_string = "\n%s %s, has been added to the class list \n" % (temp_dict["first_name"], temp_dict["last_name"])
		
		print(temp_string)

	def remove_student(self):
		
		while True:

			fields = []
		
			fields.append(input("Student First Name.... "))
			fields.append(input("Student Last Name.... "))

			for student in self.data["student_list"]:

				if student["first_name"] == fields[0] and student["last_name"] == fields[1]:
					remove_student_from_classroom(student, self.data)

					break

	def add_assignment(self):
		fields = []

		fields.append(input("Name of the assignemnt -->"))
		fields.append(input("Due date -->"))
		fields.append(input("Points the assignemnt is out of -->"))

		temp_assignnment = create_assignment(fields[0],fields[1],fields[2])

		self.data["assignment_list"].append(temp_assignnment)

	def calculate_student_avg(self):
		
		while True:
			fields = []

			fields.append(input("Student First Name -->"))
			fields.append(input("Student Last Name -->"))

			for student in self.data["student_list"]:

				if fields[0] == student["first_name"] and fields[1] == student["last_name"]:
					print(calculate_average_mark(student, self.data))
					break
			
			else:
				print("Student not found, please try again....")
				time.sleep(1)

	def generate_student_report(self):
		fields = []

		fields.append(input("Student First Name -->"))
		fields.append(input("Student Last Name -->"))

	def edit_student_info(self):
		fields = []

		fields.append(input("Student First name -->  "))
		fields.append(input("Student Last name -->  "))

		while True:

			key = input("What about the student are you altering?..... \n >fist_name..... \n >last_name......")
			value = input("What do you want it to be changed too.....")

			for i in range(len(self.data["student_list"])):

				if self.data["student_list"][i]["first_name"] == fields[0] and student["student_list"][i]["last_name"] == fields[1]:
					edit_student(self.data["student_list"][i], key, value)
					
					break
				
			else:
				print("invalid \'key\', please try \'fist_name\', or \'last_name\'.")

	def show_students(self):

		for student in self.data["student_list"]:

			print("\n",student["first_name"], student["last_name"])

	def update(self, cmd):

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

		elif cmd == "save":
			save_classroom_data(self.filename, self.data)

		elif cmd == "show-students":
			self.show_students()
		else:
			print("Unknown command..... \n")
			self.help()

session_data, filename = initialize_session()

usr_interface = user_interface_controller(session_data, filename)

print(" \n Type \"help\" and press Enter to see command list. \n")

while True:

	user_input = input()

	user_input = user_input.lower()

	if user_input == "exit":
		usr_interface.update("save")
		break

	usr_interface.update(user_input)
