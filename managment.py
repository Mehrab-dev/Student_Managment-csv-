import csv
from model import Student
import os
import re


class Student_manager :
    def __init__(self,path_file:str) :
        self.path_file = path_file
        if not os.path.exists(self.path_file) :
            with open(self.path_file,"w",encoding="utf-8") as w :
                writer = csv.DictWriter(w,fieldnames=["id","name","lastname","gender","national_code","phone","email","gpa"],delimiter=",")
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

    def gpa_students(self) :
        average = []
        with open(self.path_file,"r",encoding="utf-8") as a :
            reader = list(csv.DictReader(a))
            for i in reader :
                if i.get("gpa") :
                    try :
                        average.append(float(i["gpa"]))
                    except ValueError :
                        pass
        return sum(average) / len(average) if average else 0

    def highest_gpa(self) :
        students = []
        with open(self.path_file,"r",encoding="utf-8") as h :
            reader = list(csv.DictReader(h))
            for i in reader :
                if i.get("gpa").strip() :
                    try :
                        students.append(float(i["gpa"]))
                    except ValueError :
                        pass
        if not students :
            return 0
        return max(students)


    def update_student(self,phone:str,name:str=None,lastname:str=None,gender:str=None,national_code:str=None,email:str=None,gpa:str=None) :
        updated = False
        with open(self.path_file,"r",encoding="utf-8") as u :
            reader = list(csv.DictReader(u))
            for i in reader :
                if i["phone"] == phone :
                    if name is not None :
                        i["name"] = name
                    if lastname is not None :
                        i["lastname"] = lastname
                    if gender is not None :
                        i["gender"] = gender
                    if national_code is not None :
                        if re.fullmatch(r"\d{10}",national_code) :
                            i["national_code"] = national_code
                        else :
                            raise ValueError("the new national code is invalid")
                    if email is not None :
                        if re.fullmatch(r"[a-zA-Z0-9._]+@gmail\.com$",email) :
                            i["email"] = email
                        else :
                            raise ValueError("the new email is invalid")
                    if gpa is not None :
                        i["avg"] = str(float(gpa))
                    updated = True
                    break
        if not updated :
            return "student not found with this mobile phone"
        with open(self.path_file,"w",encoding="utf-8",newline="") as a :
            writer = csv.DictWriter(a,fieldnames=reader[0].keys())
            writer.writeheader()
            writer.writerows(reader)
        return "the desired student is information was updated"

    def min_gpa(self) :
        all_gpa = []
        with open(self.path_file,"r",encoding="utf-8") as m :
            reader = list(csv.DictReader(m))
            for i in reader :
                if i.get("gpa") :
                    try :
                        all_gpa.append(float(i["gpa"]))
                    except ValueError :
                        pass
        if not all_gpa :
            return "no grade has been recorded"
        return min(all_gpa)





