import csv
from model import Student
import os

class Student_manager :
    def __init__(self,path_file:str) :
        self.path_file = path_file
        if not os.path.exists(self.path_file) :
            with open(self.path_file,"w",encoding="utf-8") as w :
                writer = csv.DictWriter(w,fieldnames=["id","name","lastname","gender","national_code","phone","email"],delimiter=",")
                writer.writeheader()


    def add_student(self,student:Student) :
        with open(self.path_file,"r",encoding="utf-8") as r :
            old_data = csv.DictReader(r)
            for i in old_data :
                if i["national_code"] == student.national_code :
                    raise ValueError("national code already entered")
                if i["phone"] == student.phone :
                    raise ValueError("phone already entered")
                if i["email"] == student.email :
                    raise ValueError("email already entered")
        dict_data = student.to_dict()
        with open(self.path_file,"a",encoding="utf-8",newline="") as a :
            writer = csv.DictWriter(a,fieldnames=dict_data.keys())
            writer.writerow(dict_data)

