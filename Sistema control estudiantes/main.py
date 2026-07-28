from New_menu import show_menu
from Students_entry_data import add_student, show_students_data, student_top_three, obtain_all_average
from export_data import export_data
from  Import import import_data

def main():
    students = []

    while True:
        option = show_menu()

        if option == 1:
            student = add_student()
            students.append(student)
            
            print("\nEstudiante agregado correctamente.\n")

        elif option == 2:
            show_students_data(students)
            

        elif option == 3:
            # show_students_data(students) Esto no es valido porque mi funcion no hara nada 
            student_top_three(students) #esto es lo correcto
         

        elif option == 4:
            obtain_all_average(students)

        elif option == 5:
            export_data("Exportar.csv",students)

        elif option == 6:
            students = import_data("Exportar.csv", students)
            show_students_data(students)

        elif option == 7:
            print("Gracias por utilizar el sistema.")
            break


if __name__ == "__main__":
    main()

