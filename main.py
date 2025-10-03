from idlelib.run import manage_socket

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

list_data = sub_parser.add_parser("l",help="list all student in csv file")
list_data.add_argument("--p",required=True,help="file address for list students",type=str)


args = parser.parse_args()


if args.command == "a" :
    data = Student(name=args.name,lastname=args.lastname,gender=args.gender,national_code=args.national_code,phone=args.phone,email=args.email)
    manage = Student_manager(args.p)
    manage.add_student(data)
if args.command == "l" :
    manage = Student_manager(path_file=args.p)
    print(manage.list_student())
