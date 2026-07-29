class Student:
    def __init__(self,name, grade1 , grade2, grade3):
        if grade1 > 100 or grade2 > 100 or grade3>100:
            raise ValueError('The grade must be lower than 100')

        if grade1 < 0 or grade2< 0 or grade3<0:
    
            raise ValueError('The grade must be higher tha 0')

            
        self.name = name
        self.grade1 = grade1
        self.grade2 = grade2
        self.grade3 = grade3


    def average(self):
        return(self.grade1 + self.grade2 + self.grade3) /3

    
    def passed(self):
        if self.average() >= 70:
            return "You have approved👏👏"
        else:
            return "You have not approved😞"
        



# <NECESITO QUE SEA INTERACTIVO>

while True:
    try:
        name = input("Enter your name: ")
        grade1 = int(input("Add the your first grade: "))
        grade2 = int(input("Add the your second grade: "))
        grade3 = int(input("Add the your third grade: "))
        student = Student(name,grade1,grade2,grade3)

        break
    except ValueError as error:
        print(error)


#<Prints de los resultados>

print(f"Hi {student.name}!")
print(f"Your grades are: {student.grade1}, {student.grade2}, {student.grade3}")
print(f"Average: {student.average():.2f}")
print(student.passed())