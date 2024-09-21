# lib/cli.py

from lib.helpers import (
   Create_students, 
   Add_student,
   Update_student,
   Delete_student,
   Find_student_by_name,
   List_students,
   Create_course,
   Add_course,
   Delete_course,
   Update_course,
   Find_course_by_title,
   List_course,
   Create_enrollment,
   Add_enrollment,
   Delete_enrollment,
   Update_enrollment,
   Find_enrollment_by_id
)

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            student_menu()
            student_input = input(":")
            if student_input == "1":
                 Create_students()
            elif student_input == "2":
                 Add_student()
            elif student_input == "3":
                Update_student()
            elif student_input == "4":
                Delete_student()
            elif student_input == "5":
                Find_student_by_name()
            elif student_input == "6":
                List_students()
            elif student_input == "7":
                menu()
            elif student_input == "8":
                break
            else:
                print("Enter a valid option!")
                student_menu()
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Student profile")
    print("1. Course details")
    print("2. Manage Enrolment")
def student_menu():
    print("1.Create Student")
    print("2. Add student")
    print("3. Update student")
    print("4. Delete student")
    print("5. Find student by name")
    print("6. View students and their courses")
    print("7. Back")
    print("8. Exit")
def course_menu():
     print("1. Create Course")
     print("2. Add Course")
     print("3. Update Course")
     print("4. Delete Course")
     print("5. Find Course by title")
     print("6. List all Courses")
     print("7. Back")
     print("8. Exit")
def enrolment_menu():
     print("1. Create Enrolment")
     print("2. Add Enrolment")
     print("3. Update Enrollment")
     print("4. Delete Enrollment")
     print("5. Find Enrollment by Id")
     print("6. List Enrollments")
     print("7. Back")
     print("8. Exit")


if __name__ == "main":
    main()