import os 
import json
import pprint
import time

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
    def __init__(self,jsonfile):
        
        with open(jsonfile, "r") as json_file:
            responces = json.load(json_file)
    
    def help(self):
        print("""Commands List:
          > add-student
          > remove-student
          > add-assignment
          > calculate-student-avg
          > generate-student-report""")

    def add_student(self):

    def remove_student(self):

    def add_assignemnt(self):
    
    def calculate_student_avg(self):
    
    def generate_student_report(self):

class markbook_setup:
    def __init__(self, filename):

        self.filename = filename
        self.wait_seconds = 2

        print("Initializing Markbook, fill in requests fields.")
        time.sleep(self.wait_seconds)

        self.teacher = input("Teacher --> ")
        time.sleep(self.wait_seconds)

        self.course_code = input("Course Code --> ")
        time.sleep(self.wait_seconds)

        self.course_name = input("Course Name --> ")
        time.sleep(self.wait_seconds)

        self.period = input("What period is it --> ")
        time.sleep(self.wait_seconds + 2)

        temp_dict = {
            "teacher": self.teacher,
            "course_code": self.course_code,
            "course_name": self.course_name,
            "period": self.period
        }

        with open(self.filename, "w") as f:
            json.dump(temp_dict, f)       

while True:

    user_input = input()

    if 
