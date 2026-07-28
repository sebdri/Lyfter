#¿Cómo va a saber export_data() qué estudiantes guardar si solo recibe la ruta del archivo?
import csv

            


def export_data(file_path, students):
    if len(students)==0:
        print('Error, No hay data')
        return
    
    with open(file_path , "w", encoding='utf-8', newline='') as file:
        headers = students[0].keys()
        
        writer = csv.DictWriter(file, fieldnames= headers)

        writer.writeheader()

        writer.writerows(students)

        print("Datos exportados correctamente.")