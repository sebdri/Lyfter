# tendrá toda la lógica relacionada al menú de opciones.


# def show_menu():
#     print("\n--- Bienvenido al menú ---")
#     print("1. Agregar estudiantes")
#     print("2. Ver estudiantes")
#     print("3. Top 3 promedios")
#     print("4. Promedio general")
#     print("5. Exportar CSV")
#     print("6. Importar CSV")
#     print("7. Salir")



# def get_option():
#     while True:
#         try:
#             option = int(input("Ingrese la opcion deseada:"))

#             if 1<= option <= 7:
#                 return option
#             else:
#                 print("Ingrese una opcion entre 1 y 7")
        
#         except ValueError:
#             print("Ingrese una valor aceptado")


def show_menu():
    while True:
        print("\n===== MENÚ =====")
        print("1. Agregar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Top 3 estudiantes")
        print("4. Promedio general")
        print("5. Exportar CSV")
        print("6. Importar CSV")
        print("7. Salir")

        try:
            option = int(input("Seleccione una opción: "))

            if 1 <= option <= 7:
                return option
            else:
                print("Debe ingresar una opción entre 1 y 7.")

        except ValueError:
            print("Debe ingresar un número.")