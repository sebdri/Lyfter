'''ALGORITMOS DE ORDENAMIENTO
    Big O notation'''

def my_bubble_sort(list_to_order): # o(n)
    for out_index in range(len(list_to_order) - 1): # o(n)
        for index in range(len(list_to_order) - 1 - out_index):# o(n²)
            current = list_to_order[index]# o(1)
            next_value = list_to_order[index + 1]# o(1)

            if current > next_value:# o(n)
                list_to_order[index] = next_value# o(1)
                list_to_order[index + 1] =  current# o(1)


test = [1,3,80,4,5,6,70,8,10,9]# o(n)
my_bubble_sort(test)# o(n²)


print(test)# o(n)

