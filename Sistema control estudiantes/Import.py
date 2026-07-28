import csv

def import_data(file_path, students):
    try:
        with open(file_path, "r", encoding="utf-8", newline="") as file:

            reader = csv.DictReader(file)

            # Si quieres reemplazar los estudiantes actuales
            students.clear()

            for student in reader:
                student["Español"] = int(student["Español"])
                student["Ingles"] = int(student["Ingles"])
                student["Sociales"] = int(student["Sociales"])
                student["Ciencias"] = int(student["Ciencias"])
                student["Promedio"] = float(student["Promedio"])

                students.append(student)

        print("Datos importados correctamente.")
        return students

    except FileNotFoundError:
        print("No hay un archivo previamente exportado.")
        return students