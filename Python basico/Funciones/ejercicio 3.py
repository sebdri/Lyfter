#Cree una función que retorne la suma de todos los números de una lista.

new_list = [1,1,2,3,4]


def plus(new_list):
    total=0
    for num in new_list:
        total = total + num

    return total

result = plus(new_list)
print(result)