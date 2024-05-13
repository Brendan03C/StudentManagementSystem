students=[]
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

def addStudent():
    if (len(students))>=100:
        print("Error: Maximum number of students reached.","\n")
    else:
        student=input("Student's Name: ")
        students.append(student)
        print("Successfully added",student,"to the system.","\n")

def deleteStudent():
    student=input("Student's Name: ")
    if findStudent(student)==-1:
        print("Error: Student record not found.","\n")
    else:
        students.pop(students.index(student))
        print("Successfully removed",student,"from the system.","\n")

def searchStudent():
    student=input("Student's Name: ")
    if findStudent(student)==-1:
        print("Error: Student record not found.","\n")
    else:
        print(student,"has been found in the system.","\n")

def displayAllStudents():
    if len(students)==0:
        print("Error: No student records found.","\n")
    else:
        for i in range(0,len(students)):
            print(students[i])
        print("")

def findStudent(student):
    if student in students:
        index=students.index(student)
    else:
        index=-1
    return index

main()