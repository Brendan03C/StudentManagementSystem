'''
CS 131: Python Programming I
Project: Student Record Management System
Brendan 
J Pickering
'''

studentRecords = []
MAX_RECORDS = 3
userInput = ''
welcomeText = 'welcome.txt'
userIndex = -1

def main():
    

    while True:
        try:
            with open(welcomeText, 'r') as txt:
                print(txt.read())
            userInput = int(input("Enter your choice (1-5): "))
            if userInput == 1:
                addStudent()
            elif userInput == 2:
                deleteStudent()
            elif userInput == 3:
                searchStudent()
            elif userInput == 4:
                displayAllStudents()
            elif userInput == 5:
                print("Thank you for using the Student Record Management System!")
                break

        except FileNotFoundError as e:
            print("Oops! File Not Found!")
            break
        except Exception as e:
            print("Oops! Something went wrong!")
            print(type(e))
            print(str(e))


def addStudent():
    while len(studentRecords) <= MAX_RECORDS-1:
        userInput = input("Please enter the name you would like to add (Q to quit): ")
        if not userInput.upper() == 'Q':
            studentRecords.append(userInput)
            print(f'successfully added user: {userInput}')
        else:
            break
    if len(studentRecords) == MAX_RECORDS: print("Database is full. Please delete a name first. ")
    userInput = input("Press anything to continue!")

def deleteStudent():
    userInput = '-1'
    while not userInput.upper() == 'Q':
        userInput = input("Please enter the name you would like to remove (Q to quit): ")
        userIndex = findStudent(userInput)
        if not userIndex == -1:
            studentRecords.pop(userIndex)
        elif not userInput.upper() == 'Q':
            print('Student not found. ')
    userInput = input("Press anything to continue!")


def searchStudent():
    userInput = '-1'
    while not userInput.upper() == 'Q':
        userInput = input("Please enter the name you would like to locate (Q to quit): ")
        userIndex = findStudent(userInput)
        if not userIndex == -1:
            print(f'Student {studentRecords[userIndex]} has been found in file. ')
        elif not userInput.upper() == 'Q':
            print('Student not found.')
    userInput = input("Press anything to continue!")

def displayAllStudents():
    while True:
        for i in range(len(studentRecords)): 
            if i == len(studentRecords)-1: print(studentRecords[i])
            else: print(studentRecords[i], end=', ')
        userInput = input("Press anything to continue:")
        break

def findStudent(student:str) -> int:
    try:
        x = studentRecords.index(student)
    except ValueError as e:
        x = -1
    #print(x)                                #for debugging only
    return x

main()