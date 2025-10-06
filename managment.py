import csv
from model import Student
import os
import re


class Student_manager :
    def __init__(self,path_file:str) :
        self.path_file = path_file
        if not os.path.exists(self.path_file) :
            with open(self.path_file,"w",encoding="utf-8") as w :
                writer = csv.DictWriter(w,fieldnames=["id","name","lastname","gender","national_code","phone","email","avg"],delimiter=",")
                writer.writeheader()


    def add_student(self,student:Student) :
        with open(self.path_file,"r",encoding="utf-8") as r :
            old_data = csv.DictReader(r)
            for i in old_data :
                if i["national_code"] == student.national_code :
                    raise ValueError("national code already entered")
                if i["phone"] == student.phone :
                    raise ValueError("phone already entered")
                if student.email and i["email"] == student.email :
                    raise ValueError("email already entered")
        dict_data = student.to_dict()
        with open(self.path_file,"a",encoding="utf-8",newline="") as a :
            writer = csv.DictWriter(a,fieldnames=dict_data.keys())
            writer.writerow(dict_data)

    def list_student(self) :
        with open(self.path_file,"r",encoding="utf-8") as s :
            data = csv.DictReader(s)
            return list(data)

    def search_student_with_ncode(self,ncode) :
        s_data = []
        if not re.fullmatch(r"\d{10}",ncode) :
            raise ValueError("The national code is invalid")
        with open(self.path_file,"r",encoding="utf-8") as s :
            data = csv.DictReader(s)
            list_data = list(data)
            for i in list_data :
                if i["national_code"] == ncode :
                    s_data.append(i)
            if s_data :
                return s_data
            else :
                return "Student with this national code was not found"

    def delete_student_with_phone(self,phone) :
        new_data = []
        if not re.fullmatch(r"09\d{9}",phone) :
            return "the mobile phone is invalid"
        with open(self.path_file,"r",encoding="utf-8") as d :
            data = csv.DictReader(d)
            list_data = list(data)
            for i in list_data :
                if i["phone"] != phone :
                    new_data.append(i)
        if len(list_data) == len(new_data) :
            return "student not found"
        with open(self.path_file,"w",encoding="utf-8",newline="") as a :
            write = csv.DictWriter(a,fieldnames=list_data[0].keys())
            write.writeheader()
            write.writerows(new_data)
        return "Student successfully deleted"

    def avg_students(self) :
        average = []
        with open(self.path_file,"r",encoding="utf-8") as a :
            reader = list(csv.DictReader(a))
            for i in reader :
                if i.get("avg") :
                    try :
                        average.append(float(i["avg"]))
                    except ValueError :
                        pass
        return sum(average) / len(average) if average else 0

    def highest_gpa(self) :
        students = []
        with open(self.path_file,"r",encoding="utf-8") as h :
            reader = list(csv.DictReader(h))
            for i in reader :
                if i.get("avg").strip() :
                    try :
                        students.append(float(i["avg"]))
                    except ValueError :
                        pass
        if not students :
            return 0
        return max(students)






