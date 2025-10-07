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

def test_list_student(tmp_path) :
    fake_path = tmp_path / "data_student.csv"

    manage = Student_manager(path_file=str(fake_path))
    student = Student("mehrab","khanmohammadi","male","1234567898","09154138288")
    manage.add_student(student)

    list_data = manage.list_student()
    assert len(list_data) == 1
    assert list_data[0]["name"] == "mehrab"
    assert list_data[0]["phone"] == "09154138288"

def test_search_st_ncode(tmp_path) :
    fake_path = tmp_path / "data_student.csv"
    manage = Student_manager(path_file=str(fake_path))
    student = Student("mehrab","khanmohammadi","male","0864563024","09308438266")
    manage.add_student(student)
    search = manage.search_student_with_ncode(ncode="0864563024")
    assert search[0]["name"] == "mehrab"
    assert search[0]["lastname"] == "khanmohammadi"
    assert search[0]["national_code"] == "0864563024"

def test_delete_student(tmp_path) :
    fake_path = tmp_path / "data_student.csv"
    student = Student("ali","ghorbani","male","0942871502","09127390247")
    manage = Student_manager(path_file=str(fake_path))
    manage.add_student(student)
    manage.delete_student_with_phone(phone="09127390247")
    with open(fake_path,"r",encoding="utf-8") as d :
        data = csv.DictReader(d)
        assert len(list(data)) == 0

def test_average(tmp_path) :
    fake_path = tmp_path / "data_student.csv"
    student1 = Student("alex","teles","male","2947638996","09734268819",avg="18")
    student2 = Student("lana","delray","female","7391830289","09287165542",avg="16.48")
    manage = Student_manager(path_file=str(fake_path))
    manage.add_student(student1)
    manage.add_student(student2)
    avg = manage.avg_students()
    assert round(avg,2) == 17.24

def test_highest_average(tmp_path) :
    fake_path = tmp_path / "data_student.csv"
    student1 = Student("alex","teles","male","2947638996","09734268819",avg="18")
    student2 = Student("lana", "delray", "female", "7391830289", "09287165542", avg="16.48")
    student3 = Student("mikel","baroz","male","7319830289","09447165542",avg="19.03")
    manage = Student_manager(path_file=str(fake_path))
    manage.add_student(student1)
    manage.add_student(student2)
    manage.add_student(student3)
    h_gpa = manage.highest_gpa()
    assert h_gpa == 19.03

def test_min_gpa(tmp_path) :
    fake_path = tmp_path / "data_students.csv"
    student1 = Student("mehrab","khanmohammadi","male","0867384755","09154132425",gpa="17.45")
    student2 = Student("aide","hasanzadeh","female","0678674040","09308433030",gpa="19.29")
    manage = Student_manager(path_file=str(fake_path))
    manage.add_student(student1)
    manage.add_student(student2)
    min_gpa = manage.min_gpa()
    assert min_gpa == 17.45