# File: student_manager.py

def add_student():
    file = open("students.txt", "a")
    
    name = input("Enter student name: ")
    age = input("Enter age: ")
    course = input("Enter course: ")
    
    file.write(name + "\n")
    file.write(age + "\n")
    file.write(course + "\n")
    file.write("---\n")
    
    file.close()
    print("Student added successfully!\n")


def view_students():
    file = open("students.txt", "r")
    lines = file.readlines()
    file.close()

    if len(lines) == 0:
        print("No records found.\n")
        return

    print("\nStudent Records:")

    i = 0
    while i < len(lines):
        name = lines[i]
        age = lines[i+1]
        course = lines[i+2]

        print("Name:", name, "| Age:", age, "| Course:", course)
        i += 4

    print()


def search_student():
    name_to_search = input("Enter name to search: ")
    
    file = open("students.txt", "r")
    lines = file.readlines()
    file.close()

    i = 0
    while i < len(lines):
        name = lines[i]

        if name.lower().startswith(name_to_search.lower()):
            age = lines[i+1]
            course = lines[i+2]

            print("Record Found:")
            print("Name:", name, "| Age:", age, "| Course:", course)
            return   # exit immediately

        i += 4

    print("Student not found.\n")


def delete_student():
    name_to_delete = input("Enter name to delete: ")

    file = open("students.txt", "r")
    lines = file.readlines()
    file.close()

    new_lines = []

    i = 0
    while i < len(lines):
        name = lines[i]

        if name.lower().startswith(name_to_delete.lower()):
            i += 4   # skip record
        else:
            new_lines.append(lines[i])
            new_lines.append(lines[i+1])
            new_lines.append(lines[i+2])
            new_lines.append(lines[i+3])
            i += 4

    file = open("students.txt", "w")
    file.writelines(new_lines)
    file.close()

    if len(lines) == len(new_lines):
        print("Student not found.\n")
    else:
        print("Student deleted successfully!\n")


def menu():
    while True:
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice\n")


menu()