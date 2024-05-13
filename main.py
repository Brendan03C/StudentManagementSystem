#‘ ‘ ‘
#CS 131: Python Programming 1
#Project: Student Record Management System
#Brendan Cantril
#J Pickering
#‘ ‘ ‘

students=[]
students_num=len(students)

#Prints the menu system text, and then asks for the user's choice.
#It will run the function that corresponds to that numbers chioce.
#If the user doesn't input a number between 1-5, then it prints an error message and displays the menu again.
def main():
    print("Student Record Management System","\n1. Add a student.","\n2. Delete a student.","\n3. Search for a student.","\n4. Display all students.","\n5. Exit","\n")
    method=int(input("Please enter your choice (1-5): "))
    if method==1:
        addStudent()
        main()
    if method==2:
        deleteStudent()
        main()
    if method==3:
        searchStudent()
        main()
    if method==4:
        displayAllStudents()
        main()
    if method==5:
        print("Now exiting the system. Goodbye!")
    else:
        print("Invalid input!","\n")
        main()

#Checks if number of students is greater than or equal to 100.
#If greater than or equal to 100, prints an error message.
#If less than 100, asks for the name, adds it to the list, and prints a success message.
def addStudent():
    if (len(students))>=100:
        print("Error: Maximum number of students reached.","\n")
    else:
        student=input("Student's Name: ")
        students.append(student)
        print("Successfully added",student,"to the system.","\n")

#Asks for the name, and then calls the findStudent() function.
#If the function returns a value of -1, the student isn't in the system and it prints an error message.
#If the function doesn't return a value of -1, the student is in the system.
#It then removes the student from the list and prints a success message.
def deleteStudent():
    student=input("Student's Name: ")
    if findStudent(student)==-1:
        print("Error: Student record not found.","\n")
    else:
        students.pop(students.index(student))
        print("Successfully removed",student,"from the system.","\n")

#Asks for the name, and then calls the findStudent() function.
#If the function returns a value of -1, the student isn't in the system and it prints an error message.
#If the function doesn't return a value of -1, the student is in the system and it prints a success message.
def searchStudent():
    student=input("Student's Name: ")
    if findStudent(student)==-1:
        print("Error: Student record not found.","\n")
    else:
        print(student,"has been found in the system.","\n")

#Checks if number of students is equal to 0.
#If equal to 0, it prints an error message.
#If it isn't equal to 0, it prints all the students names by using a loop that ends when it reaches the number of students.
def displayAllStudents():
    if len(students)==0:
        print("Error: No student records found.","\n")
    else:
        for i in range(0,len(students)):
            print(students[i])
        print("")

#Checks if student is in the list. If they are, then the index value becomes the student's index in the list.
#If the student isn't in the list, the index value becomes -1.
#It returns the value of index.
def findStudent(student):
    if student in students:
        index=students.index(student)
    else:
        index=-1
    return index

main()
