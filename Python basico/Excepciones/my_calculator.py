#Mostrar menu
def show_menu(actual_number):
    print("-- Hola bienvenido a la calculadora--")
    print("                                     ")
    print(f'El numero actual es: {actual_number}')
    print("                                     ")
    print("Las opciones son las siguientes:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Borrar resultado")
    print("6. Salir de la calculadora")
    print("                                     ")
    print("                                     ")

#obtener datos 
def obtain_data():
    while True:
        try:
            number = float(input("Ingrese el numero que desees: "))
            return number
        except ValueError:
            print("❌Error el numero ingresado es invalido")


def main():
    actual_number = 0 
    while True:
        
        show_menu(actual_number)

        option = input("Ingrese la opcion que desea realizar:")

        if option == "6":
            print("Saliendo de la calculadora, adios")
            break

        elif option == "5":
            actual_number = 0
            print(f"✅ Resultado borrado. \nEl numero actual es: {actual_number}")
        
        elif option in ["1","2","3","4"]:
            number = obtain_data()

            if option == "1":
                actual_number += number

            elif option == "2":
                actual_number -= number
            elif option =="3":
                actual_number*=number
            elif option == "4":
                if number == 0:
                    print("❌Error, 0 no es un numero divisible ")       
                else:
                    actual_number /= number
        
        else:
            print("❌Error el numero ingresado es invalido")

if __name__== "__main__":
    main()