from model import Student
from managment import Student_manager
import argparse

parser = argparse.ArgumentParser(description="Student Managment CSV")
sub_parser = parser.add_subparsers(dest="command")

add = sub_parser.add_parser("a",help="add student")
add.add_argument("--p",required=True,help="file save path csv")
add.add_argument("name",help="student firs name")
add.add_argument("lastname",help="student last name")
add.add_argument("gender",choices=["male","female"],help="student gender")
add.add_argument("national_code",help="student national code")
add.add_argument("phone",help="student phone")
add.add_argument("--email",required=False,help="student email")
add.add_argument("--gpa",required=False,help="student is GPA")

list_data = sub_parser.add_parser("l",help="list all student in csv file")
list_data.add_argument("--p",required=True,help="file address for list students",type=str)

search_data = sub_parser.add_parser("ser",help="to search for the desired student")
search_data.add_argument("--p",required=True,help="the path to the desired file",type=str)
search_data.add_argument("--nc",required=True,help="national code for search")

delete = sub_parser.add_parser("del",help="to delete a student")
delete.add_argument("--p",required=True,help="path to remove a student",type=str)
delete.add_argument("--ph",required=True,help="phone number to remove a student")

gpa = sub_parser.add_parser("gpa",help="calculating GPA")
gpa.add_argument("--p",required=True,help="file path",type=str)

highest_gpa = sub_parser.add_parser("hg",help="calculating highest GPA")
highest_gpa.add_argument("--p",required=True,help="file path csv")

update = sub_parser.add_parser("up",help="update information student")
update.add_argument("--p",required=True,type=str,help="file path for update")
update.add_argument("--ph",required=True,help="key to search for the desired student")
update.add_argument("--name",required=False,help="student new name")
update.add_argument("--lname",required=False,help="student new lastname")
update.add_argument("--gen",required=False,help="student gender")
update.add_argument("--ncode",required=False,help="student new national code")
update.add_argument("--email",required=False,help="student new email")
update.add_argument("--gpa",required=False,help="student new gpa")

min_gpa = sub_parser.add_parser("min_gpa",help="to calculate the lowest gpa")
min_gpa.add_argument("--p",required=True,help="file path",type=str)


args = parser.parse_args()


if args.command == "a" :
    data = Student(name=args.name,lastname=args.lastname,gender=args.gender,national_code=args.national_code,phone=args.phone,email=args.email,
                   gpa=args.gpa)
    manage = Student_manager(args.p)
    manage.add_student(data)
if args.command == "l" :
    manage = Student_manager(path_file=args.p)
    print(manage.list_student())
if args.command == "ser" :
    manage = Student_manager(path_file=args.p)
    print(manage.search_student_with_ncode(args.nc))
if args.command == "del" :
    manage = Student_manager(path_file=args.p)
    print(manage.delete_student_with_phone(args.ph))
if args.command == "avg" :
    manage = Student_manager(path_file=args.p)
    print(manage.avg_students())
if args.command == "hg" :
    manage = Student_manager(path_file=args.p)
    print(manage.highest_gpa())
if args.command == "up" :
    manage = Student_manager(path_file=args.p)
    print(manage.update_student(phone=args.ph,name=args.name,lastname=args.lname,gender=args.gen,national_code=args.ncode,
                                email=args.email,gpa=args.gpa))
if args.command == "min_gpa" :
    manage = Student_manager(path_file=args.p)
    print(manage.min_gpa())