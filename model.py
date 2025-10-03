import uuid
import re


class Student :
    def __init__(self,name:str,lastname:str,gender:str,national_code:str,phone:str,email:str=None) :
        self.id = uuid.uuid4()
        self.name = name
        self.lastname = lastname
        self.gender = gender
        match = re.fullmatch(r"\d{10}",national_code)
        if not match :
            raise ValueError("invalid national code")
        self.national_code = national_code
        match = re.fullmatch(r"09\d{9}",phone)
        if not match :
            raise ValueError("invalid phone number")
        self.phone = phone
        if email is not None :
            match = re.fullmatch(r"[a-zA-Z0-9_.]+@gmail\.com$",email)
            if not match :
                raise ValueError("invalid email")
            self.email = email
        else :
            self.email = ""

    def fullname(self) :
        return f"{self.name} {self.lastname}"

    def to_dict(self) :
        return {
            "id":str(self.id),
            "name":self.name,
            "lastname":self.lastname,
            "gender":self.gender,
            "national_code":self.national_code,
            "phone":self.phone,
            "email":self.email
        }


