class Student:
    def __init__(self,StudentID,age,marks):
        self.StudentID = StudentID
        self.age = age
        self.marks = marks
    def validate_marks(self):
        if self.marks>0 and self.marks<101:
            return True
        else:
            return False
    def validate_age(self):
        if self.age>20:
            return True
        else:
            return False
    def check_qualification(self):
        if self.marks>64 and self.age>20:
                return True
        else:
            return False

def main():
    StudID=input("Enter Student ID: ")
    age=input("Enter the age: ")
    marks=input("Enter the marks: ")
    S1 = Student(StudID,age,marks)
    mkv=S1.validate_marks()
    if mkv == False:
        print("Entered marks are invalid")
    va=S1.validate_age()
    if va==True and mkv==True:
        quali=S1.check_qualification()
        if quali == True:
            print("Congrats, you're eligible")
        else:
            print("Oh no, you're not eligible")
    if mkv==False:
        print("Entered marks is invalid")
    if va==False:
        print("Entered age is invalid")

main()
var=input("Do you want to check for another sudent? 1 for yes, 0 for no: ")
if var==1:
    main()
