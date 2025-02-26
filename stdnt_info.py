# Aman Gautam
students = []
while True:
    print("\n1. Add Student")
    print("2. View Single Student")
    print("3. View All Students")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        students.append((roll, name))
        print("Student Added!")
    elif choice == '2':
        roll = input("Enter Roll Number: ")
        for student in students:
            if student[0] == roll:
                print("Name:", student[1])
                break
        else:
            print("Student Not Found!")
    elif choice == '3':
        for student in students:
            print("Roll Number:", student[0], "Name:", student[1])
    elif choice == '4':
        roll = input("Enter Roll Number to Delete: ")
        for student in students:
            if student[0] == roll:
                students.remove(student)
                print("Student Deleted!")
                break
        else:
            print("Student Not Found!")

    elif choice == '5':
        break
    