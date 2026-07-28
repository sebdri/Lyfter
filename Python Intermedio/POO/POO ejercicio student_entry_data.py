#    ------------<CAMBIOS SOLICITADOS>------------


# FOR-> student_top_three

# Fixed the attribute name in the print statement.
# Changed student.student to student.name because the Student class
# stores the student's name in the 'name' attribute.

#-----------------------------------------------------------------------------

#FOR-> obtain_all_average

# Fixed the variable name used to calculate the overall average.
# Replaced all_students with all_students_averages to match the
# variable declared at the beginning of the function.


class Student:
    def __init__(self, name, section, spanish, english, social_studies, science):
        self.name = name
        self.section = section
        self.spanish = spanish
        self.english = english
        self.social_studies = social_studies
        self.science = science


        self.average = (spanish+english+social_studies+science)/4


def add_student():
    name = input("Add the student's name: ")
    section = input("Add student's section: ")

    while True:
        try:
            spanish = int(input("Please add the Spanish score: "))
            if 0 <= spanish <= 100:
                break
            print("The score needs to be between 0 & 100.")
        except ValueError:
            print("Invalid data. ⚠️")

    while True:
        try:
            english = int(input("Please add the English score: "))
            if 0 <= english <= 100:
                break
            print("The score needs to be between 0 & 100.")
        except ValueError:
            print("Invalid data. ⚠️")

    while True:
        try:
            social_studies = int(input("Please add the Social Studies score: "))
            if 0 <= social_studies <= 100:
                break
            print("The score needs to be between 0 & 100.")
        except ValueError:
            print("Invalid data. ⚠️")

    while True:
        try:
            science = int(input("Please add the Science score: "))
            if 0 <= science <= 100:
                break
            print("The score needs to be between 0 & 100.")
        except ValueError:
            print("Invalid data. ⚠️")

    return Student(
        name,
        section,
        spanish,
        english,
        social_studies,
        science
    )



def show_students_data(students):
    if len(students) == 0:
        print("No students added yet.")
        return

    for student in students:
        print("\n----------------------------")
        print(f'student: {student.name}')
        print(f'section: {student.section}')
        print(f'spanish: {student.spanish}')
        print(f'english: {student.english}')
        print(f'social_studies: {student.social_studies}')
        print(f'science: {student.science}')
        print(f'average: {student.average}')

    


def student_top_three(students):
    if len(students) == 0:
        print("No students registered.")
        return

    top_three = sorted(
        students,
        key=lambda student:student.average,
        reverse=True
    )

    print("\nTop 3 students")

    for student in top_three[:3]:
        print(f'{student.name} - Average: {student.average}')


def obtain_all_average(students):


    if len(students)==0:
        print ("You'll have to add data before been able to use this functionality 😞")
        return
    
    all_students_averages = 0

    for student in students:
        all_students_averages += (student.average)
    
    general_avarage = all_students_averages / len(students)

    print(f'The general avarage is:{general_avarage}')