from markbook import *
import json

def initialize_session(parser_obj_shell):

    while True:

        req = input("Do you want to load previous session \"o\" or \"c\" create a new classroom? -->")

        if  req == "o" or req == "O":

            code = input("What is the courses\' code? -->  ") + ".json"

            markbook = markbook_setup(code)

            parser_obj_shell = parser(code)

            break

        if req =="c" or req == "C":

            code = input("What is the course code of the classroom you would like to load? -->  ") + ".json"

            parser_obj_shell = parser(code)

            break

        else:
            print("Error - unknown request, enter either \"o\", or \"c\".")

class parser:
    def __init__(self,filename):

        self.filename = filename
        
        with open(self.filename, 'r') as json_file:
            self.data = json.load(json_file)

    def save_data(self):
        with open(self.filename,"w") as f:
            json.dump(self.data, f)

class input_center:
    def __init__(self, parser_obj):
        self.parser = parser_obj

    def help(self):
        print("""Commands List:
          > exit
          > help
          > save
          > add-student
          > remove-student
          > add-assignment
          > calculate-student-avg
          > generate-student-report \n""")

    def add_student(self):
        fields = []

        fields.append(input("Student First Name -->"))
        fields.append(input("Student Last Name -->"))

    def remove_student(self):
        
        while True:

            fields = []
        
            fields.append(input("Student First Name -->"))
            fields.append(input("Student Last Name -->"))

            for student in self.parser.student_list:

                if student["first_name"] == fields[0] and student["last_name"] == fields[1]:
                    remove_student_from_classroom(student, self.parser.data)

    def add_assignment(self):
        fields = []

        fields.append(input("Name of the assignemnt -->"))
        fields.append(input("Due date -->"))
        fields.append(input("Points the assignemnt is out of -->"))

        temp_assignnment = create_assignment(fields[0],fields[1],fields[2])

        self.parser.data["assignment_list"].append(temp_assignnment)

    def calculate_student_avg(self):
        fields = []

        fields.append(input("Student First Name -->"))
        fields.append(input("Student Last Name -->"))

    def generate_student_report(self):
        fields = []

        fields.append(input("Student First Name -->"))
        fields.append(input("Student Last Name -->"))

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

        elif cmd == "save":
            self.parser.save_data()

        else:
            print("Unknown command..... \n")
            self.help()

class markbook_setup:
    def __init__(self, filename):

        self.filename = filename
        self.wait_seconds = 2

        print("Initializing Markbook, fill in requests fields.")
        time.sleep(self.wait_seconds)

        self.teacher = input("Teacher -->  ")
        time.sleep(self.wait_seconds)

        self.course_code = input("Course Code -->  ")
        time.sleep(self.wait_seconds)

        self.course_name = input("Course Name -->  ")
        time.sleep(self.wait_seconds)

        self.period = input("What period is it -->  ")
        time.sleep(self.wait_seconds + 2)

        classroom = create_classroom(self.course_code, self.course_name, self.period, self.teacher)

        with open(self.filename, "w") as f:
            json.dump(classroom, f)       

session_data = None

initialize_session(sesssion_data)

pc = input_center(session_data)

print(" \n Type \"help\" and press Enter to see command list. \n")

while True:    

    user_input = input()

    user_input = user_input.lower()

    if user_input == "exit":
        session_data.save_data()
        break

    pc.update(user_input)
