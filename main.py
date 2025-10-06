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
add.add_argument("--avg",required=False,help="student is GPA")

list_data = sub_parser.add_parser("l",help="list all student in csv file")
list_data.add_argument("--p",required=True,help="file address for list students",type=str)

search_data = sub_parser.add_parser("ser",help="to search for the desired student")
search_data.add_argument("--p",required=True,help="the path to the desired file",type=str)
search_data.add_argument("--nc",required=True,help="national code for search")

delete = sub_parser.add_parser("del",help="to delete a student")
delete.add_argument("--p",required=True,help="path to remove a student",type=str)
delete.add_argument("--ph",required=True,help="phone number to remove a student")

avg = sub_parser.add_parser("avg",help="calculating GPA")
avg.add_argument("--p",required=True,help="file path",type=str)

highest_avg = sub_parser.add_parser("ha",help="calculating highest GPA")
highest_avg.add_argument("--p",required=True,help="file path csv")

args = parser.parse_args()


if args.command == "a" :
    data = Student(name=args.name,lastname=args.lastname,gender=args.gender,national_code=args.national_code,phone=args.phone,email=args.email,
                   avg=args.avg)
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
if args.command == "ha" :
    manage = Student_manager(path_file=args.p)
    print(manage.highest_gpa())