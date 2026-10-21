'''ALGORITMOS DE ORDENAMIENTO'''

def my_bubble_sort(list_to_order): 
    l = len(list_to_order)

    for out_index in range(l -1): 
        for index in range(l-1,out_index,-1):
            current = list_to_order[index]
            next_value = list_to_order[index - 1]

            if current < next_value:
                list_to_order[index] = next_value
                list_to_order[index - 1] =  current


test = [1,3,80,4,5,6,70,8,10,9]
my_bubble_sort(test)


print(test)




