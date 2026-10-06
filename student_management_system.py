print("===== STUDENT MANAGEMENT SYSTEM =====")

students = []


def add_student():
    print("\n===== ADD STUDENT =====")

    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    department = input("Enter department: ")
    semester = input("Enter semester: ")

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "department": department,
        "semester": semester
    }

    students.append(student)

    print("Student added successfully!")


def view_students():
    print("\n===== ALL STUDENTS =====")

    if len(students) == 0:
        print("No student records found.")
        return

    for student in students:
        print("----------------------------")
        print("Student ID:", student["id"])
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Department:", student["department"])
        print("Semester:", student["semester"])


def search_student():
    print("\n===== SEARCH STUDENT =====")

    student_id = input("Enter student ID: ")

    for student in students:
        if student["id"] == student_id:
            print("\nStudent Found!")
            print("Student ID:", student["id"])
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Department:", student["department"])
            print("Semester:", student["semester"])
            return

    print("Student not found.")


def update_student():
    print("\n===== UPDATE STUDENT =====")

    student_id = input("Enter student ID: ")

    for student in students:
        if student["id"] == student_id:

            print("Leave a field empty if you don't want to change it.")

            name = input("Enter new name: ")
            age = input("Enter new age: ")
            department = input("Enter new department: ")
            semester = input("Enter new semester: ")

            if name:
                student["name"] = name

            if age:
                student["age"] = age

            if department:
                student["department"] = department

            if semester:
                student["semester"] = semester

            print("Student record updated successfully!")
            return

    print("Student not found.")


def delete_student():
    print("\n===== DELETE STUDENT =====")

    student_id = input("Enter student ID: ")

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found.")


while True:
    print("\n===== MAIN MENU =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice. Please try again.")
