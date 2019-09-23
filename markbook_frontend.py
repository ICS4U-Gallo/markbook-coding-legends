import json

def initialize_session(parser_obj_shell):
    print("""--New Session-- \n \n
    Please enter your desired class's course code... \n""")

    course_code = input("--> ")

    parser_obj_shell = parser(f"{course_code}.json")

class parser:
    def __init__(self,filename):

        self.filename = filename
        
        with open(filename, 'r') as json_file:
            self.data = json.load(json_file)

        self.student_list = self.data["student_list"]
        self.assignment_list = self.data["assignment_list"]
        self.course_code = self.data["course_code"]
        self.course_name = self.data["course_name"]
        self.period = self.data["period"]
        self.teacher = self.data["teacher"]

    def update_dict_surface_info(self, key, value):
        self.data[key] = value

    def update_dict_sub_info(self, key, value, index):
        self.data[key][index] = value

    def save_data(self):
        with open(self.filename,"w") as f:
            json.dump(self.data, f)

class print_center:
    def __init__(self):
        self.filler = None

    def help(self):
        print("""Commands List:
          > exit
          > help
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
        fields = []
        
        fields.append(input("Student First Name -->"))
        fields.append(input("Student Last Name -->"))

    def add_assignment(self):
        fields = []

        fields.append(input("Name of the assignemnt -->"))
        fields.append(input("Due date -->"))
        fields.append(input("Points the assignemnt is out of -->"))

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

        temp_dict = {
            "teacher": self.teacher,
            "course_code": self.course_code,
            "course_name": self.course_name,
            "period": self.period
        }

        with open(self.filename, "w") as f:
            json.dump(temp_dict, f)       

session_data = None

initialize_session(session_data)

pc = print_center()
print(" \n Type \"help\" and press Enter to see command list. \n")

while True:    

    user_input = input()

    user_input = user_input.lower()

    if user_input == "exit":
        break

    pc.update(user_input)
