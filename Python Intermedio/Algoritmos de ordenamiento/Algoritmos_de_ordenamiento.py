'''ALGORITMOS DE ORDENAMIENTO
    Big O notation'''

# def my_bubble_sort(list_to_order): # O(n²)
#     for out_index in range(len(list_to_order) - 1): # o(n) Reptie la vuelta para seguir comparando
#         for index in range(len(list_to_order) - 1 - out_index):# o(n²) solo compara a los vecinos por vuelta
#             current = list_to_order[index]# o(1)
#             next_value = list_to_order[index + 1]# o(1)

#             if current > next_value:# o(1)
# #                 list_to_order[index] = next_value# o(1)
# #                 list_to_order[index + 1] =  current# o(1)


# # test = [1,3,80,4,5,6,70,8,10,9]# o(n)
# # my_bubble_sort(test)# o(n²)


# # print(test)# o(n)




# def my_bubble_sort(list_to_order):
#     for out_of_index in range(0,len(list_to_order)-1):
#         for index in range(0, len(list_to_order) - 1 - out_of_index):
#             current = list_to_order[index]
#             next_current = list_to_order[index + 1]

#         if current < next_current:
#             list_to_order[index] = next_current
#             list_to_order[index+1]= current



# list = [1,2,5,89,100]
# my_bubble_sort(list)

# print(list)





def bubble_sort_count(lista):
    counter = 0
    for index_out in range(0, len(lista) - 1):
        for index in range(0,len(lista) - 1 - index_out):
            
            current = lista[index]
            new_current = lista [index + 1]

            print(f'Cantidad de intercambios:{counter}. Elemento actual: {current}, Elemento a la izquierda: {new_current}')


            if current > new_current:
                counter = counter + 1
                lista[index] = new_current 
                lista[index+1]= current
    
    return counter



datos = [4, 2, 5, 1, 3,70]
resultado = bubble_sort_count(datos)
print(datos)        # [1, 2, 3, 4, 5]
print(resultado)    # 6

# datos = [1, 2, 3, 4, 5]
# print(bubble_sort_count(datos))   # 0  (ya estaba ordenada)

# datos = [5, 4, 3, 2, 1]
# print(bubble_sort_count(datos))   # 10 (el peor caso)

# datos = [7]
# print(bubble_sort_count(datos))   # 0

# datos = []
# print(bubble_sort_count(datos))   # 0