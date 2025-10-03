from model import Student
from managment import Student_manager
import csv

def test_init() :
    data = Student("mehrab","khanmohammadi","Male","0860761156","09365604375","programmer.py.mail@gmail.com")
    assert data.name == "mehrab"
    assert data.lastname == "khanmohammadi"
    assert data.email == "programmer.py.mail@gmail.com"

def test_fullname() :
    data = Student("mehrab","khanmohammadi","male","1234567890","09123265329")
    assert data.fullname() == "mehrab khanmohammadi"

def test_to_dict() :
    data = Student("mehrab","khanmohammadi","male","1234567890","09154035679")
    dict_data = data.to_dict()
    assert "id" in dict_data
    assert isinstance(dict_data["id"],str)
    assert dict_data["name"] == "mehrab"
    assert dict_data["phone"] == "09154035679"

def test_add_student(tmp_path,monkeypatch) :
    new_path = tmp_path / "data.csv"

    manager = Student_manager(path_file=str(new_path))
    student = Student("mehrab","khanmohammadi","male","1234567898","09154138288")
    manager.add_student(student)
    with open(new_path,"r",encoding="utf-8") as r :
        data = csv.DictReader(r)
        list_data = list(data)
    assert len(list_data) == 1
    assert list_data[0]["name"] == "mehrab"
    assert list_data[0]["phone"] == "09154138288"







