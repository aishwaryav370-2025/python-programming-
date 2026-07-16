import os

FILE_NAME = "students.txt"


def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    age = input("Enter Age: ")
    marks = input("Enter Marks: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{roll},{name},{age},{marks}\n")

    print("\nStudent added successfully!\n")


def view_students():
    if not os.path.exists(FILE_NAME):
        print("\nNo student records found.\n")
        return

    print("\n---------------- Student Records ----------------")

    with open(FILE_NAME, "r") as file:
        for line in file:
            roll, name, age, marks = line.strip().split(",")
            print(f"Roll No : {roll}")
            print(f"Name    : {name}")
            print(f"Age     : {age}")
            print(f"Marks   : {marks}")
            print("----------------------------------------------")


def search_student():
    roll_no = input("Enter Roll Number to Search: ")

    if not os.path.exists(FILE_NAME):
        print("\nNo records found.\n")
        return

    found = False

    with open(FILE_NAME, "r") as file:
        for line in file:
            roll, name, age, marks = line.strip().split(",")

            if roll == roll_no:
                print("\nStudent Found")
                print("--------------------------")
                print(f"Roll No : {roll}")
                print(f"Name    : {name}")
                print(f"Age     : {age}")
                print(f"Marks   : {marks}")
                print("--------------------------")
                found = True
                break

    if not found:
        print("\nStudent not found.\n")


def update_student():
    roll_no = input("Enter Roll Number to Update: ")

    if not os.path.exists(FILE_NAME):
        print("\nNo records found.\n")
        return

    updated = False
    records = []

    with open(FILE_NAME, "r") as file:
        for line in file:
            roll, name, age, marks = line.strip().split(",")

            if roll == roll_no:
                print("\nEnter New Details")
                name = input("New Name: ")
                age = input("New Age: ")
                marks = input("New Marks: ")
                updated = True

            records.append(f"{roll},{name},{age},{marks}\n")

    with open(FILE_NAME, "w") as file:
        file.writelines(records)

    if updated:
        print("\nStudent record updated successfully!\n")
    else:
        print("\nStudent not found.\n")


def delete_student():
    roll_no = input("Enter Roll Number to Delete: ")

    if not os.path.exists(FILE_NAME):
        print("\nNo records found.\n")
        return

    deleted = False
    records = []

    with open(FILE_NAME, "r") as file:
        for line in file:
            roll, name, age, marks = line.strip().split(",")

            if roll != roll_no:
                records.append(line)
            else:
                deleted = True

    with open(FILE_NAME, "w") as file:
        file.writelines(records)

    if deleted:
        print("\nStudent deleted successfully!\n")
    else:
        print("\nStudent not found.\n")


def main():
    while True:
        print("========== Student Management System ==========")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

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
            print("\nThank you for using Student Management System!")
            break

        else:
            print("\nInvalid choice! Please try again.\n")


if __name__ == "__main__":
    main()