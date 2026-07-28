number1 = int(input("Ingrese su primer numero: "))
number2 = int(input("Ingrese su segundo numero: "))
number3 = int(input("Ingrese su tercer numero: "))

if number1 > number2 and number1 > number3:
    print(number1)
elif number2 > number1 and number2 > number3:
    print(number2)
else:
    print(number3)
