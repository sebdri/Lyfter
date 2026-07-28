numbers = [] #alamacen sde los numeros ingresados por el usuario

for i in range(10):
    user_number = int(input("ingrese un numeros: "))
    numbers.append(user_number)
print(numbers)

largest = numbers[0]

for j in numbers:
    if j > largest:
        largest = j
print("El mayor es:", largest)