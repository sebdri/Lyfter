def edad():
    while True:
        edad = int(input('Ingrese su edad:'))
        if edad >= 0:
            return edad 
        else:
            print('Su edad debe ser mayor que 0')



def salario():
    while True:
        salario = float(input('Ingrese su salario: '))        
        if salario >=0:   
            return salario
        else:
            print('Invalido')

def transporte(edad,salario):

    if edad < 0 and salario < 0 :
        return 'Datos invalidos'
    elif edad >= 60 and salario <= 500000:
        return "Tiene derecho al subsidio de transporte adulto mayor"
    elif edad <= 25 and salario <= 300000:
        return "Tiene derecho al subsidio de transporte estudiante"
    elif salario <= 200000:
        return "Tiene derecho al subsidio de transporte básico"
    else:
        return "No tiene derecho al subsidio de transporte"

def verificar_educacion(edad,salario):
    if edad >= 18 and edad <= 35 and salario <= 400000:
        return "Beca académica aprobada"
    elif edad >= 18 and edad <= 35 and salario <= 600000:
        return "Beca de apoyo socioeconómico aprobada"
    elif edad >= 18 and edad <= 35 and salario > 600000:
        return "No cumple requisitos de ingresos para beca"
    else:
        return "No cumple requisitos de edad para becas"


def verificar_beneficio(edad,salario):
    if edad >= 18 and salario <= 250000:
        return "Puede postular al subsidio de arriendo"
    elif edad >= 18 and salario <= 450000:
        return "Puede postular al subsidio de compra de vivienda"
    elif edad >= 18 and salario > 450000:
        return "Ingresos superan límites para subsidio de vivienda"
    else:
        return "Debe ser mayor de edad para postular a beneficios de vivienda"

def verificar_descuento(edad,salario):
    if edad >= 70 and salario <= 350000:
        return "Descuento del 50% en cuentas de agua, luz y gas"
    elif edad >= 60 and salario <= 350000:
        return "Descuento del 30% en cuentas de agua, luz y gas"
    elif salario <= 200000:
        return "Descuento del 20% en cuentas de servicios básicos"
    else:
        return "No tiene descuento en servicios básicos"


#{menu}


while True:
    print("*******************************************************")
    print("********* SISTEMA DE BENEFICIOS SOCIALES *********")
    print("*******************************************************")
    print()
    print("1. Verificar subsidio de transporte")
    print("2. Verificar beca de estudios")
    print("3. Verificar beneficio de vivienda")
    print("4. Verificar descuento en servicios básicos")
    print("5. Salir")
    print()
    print("*******************************************************")


    opcion = input('Ingrese la opcion deseada: ')

    match opcion:

        case "1":
            Uedad = edad()
            Usalario = salario()
            print(transporte(Uedad,Usalario))
        case "2":
            Uedad = edad()
            Usalario = salario()
            print(verificar_educacion(Uedad,Usalario))
        case "3":
            Uedad = edad()
            Usalario = salario()
            print(verificar_beneficio(Uedad,Usalario))
        case "4":
            Uedad = edad()
            Usalario = salario()
            print(verificar_descuento(Uedad, Usalario))
        case"5":
            print("=============================")
            print("Saliendo del programa👋")
            break
        case _:
            print("Opción inválida")

print()

