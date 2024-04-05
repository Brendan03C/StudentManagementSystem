'''
CS 131: Python Programming I
Project: Student Record Management System
Brendan 
J Pickering
'''

studentRecords = []
userInput = ''
welcomeText = 'welcome.txt'

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
    pass

def deleteStudent():
    pass

def searchStudent():
    pass

def displayAllStudents():
    pass

def findStudent():
    pass

main()