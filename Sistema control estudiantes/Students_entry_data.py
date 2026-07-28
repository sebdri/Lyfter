


def add_student():

    name = input("Ingrese el nombre del estudiante: ")
    section = input("Ingrese la sección del estudiante: ")

    while True:
        try:
            spanish = int(input("Ingrese la nota de Español: "))
            if 0 <= spanish <= 100:
                break
            else:
                print("La nota debe estar entre 0 y 100.")
        except ValueError:
            print("Dato inválido.")

    while True:
        try:
            english = int(input("Ingrese la nota de Inglés: "))
            if 0 <= english <= 100:
                break
            else:
                print("La nota debe estar entre 0 y 100.")
        except ValueError:
            print("Dato inválido.")

    while True:
        try:
            social = int(input("Ingrese la nota de Sociales: "))
            if 0 <= social <= 100:
                break
            else:
                print("La nota debe estar entre 0 y 100.")
        except ValueError:
            print("Dato inválido.")

    while True:
        try:
            science = int(input("Ingrese la nota de Ciencias: "))
            if 0 <= science <= 100:
                break
            else:
                print("La nota debe estar entre 0 y 100.")
        except ValueError:
            print("Dato inválido.")

    average = (spanish + english + social + science) / 4

    student = {
        "Estudiante": name,
        "Sección": section,
        "Español": spanish,
        "Ingles": english,
        "Sociales": social,
        "Ciencias": science,
        "Promedio": average
    }

    return student


def show_students_data(students):
    if len(students) == 0:
        print("No hay estudiantes agregados aún.")
        return

    for student in students:
        print("\n----------------------------")
        print(f'Nombre: {student["Estudiante"]}')
        print(f'Sección: {student["Sección"]}')
        print(f'Español: {student["Español"]}')
        print(f'Inglés: {student["Ingles"]}')
        print(f'Sociales: {student["Sociales"]}')
        print(f'Ciencias: {student["Ciencias"]}')
        print(f'Promedio: {student["Promedio"]}')

    


def student_top_three(students):
    if len(students) == 0:
        print("No hay estudiantes registrados.")
        return

    top_three = sorted(
        students,
        key=lambda student:student["Promedio"],
        reverse=True
    )

    print("\nTop 3 estudiantes")

    for student in top_three[:3]:
        print(f'{student["Estudiante"]} - Promedio: {student["Promedio"]}')


def obtain_all_average(students):
    average = 0

    if len(students)==0:
        print ("Tienes que pasar por la opcion 1 para agregar estudiantes antes de usar esta funcionalidad 😞")
        return
    
    all_students = 0

    for student in students:
        all_students+= (student["Promedio"])
    
    general_avarage = all_students / len(students)

    print(f'El promedio general es de:{general_avarage}')

    

