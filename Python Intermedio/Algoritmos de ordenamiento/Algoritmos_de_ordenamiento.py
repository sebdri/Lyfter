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

# print(list)





def bubble_sort_count(lista): #O(1)
    counter = 0 #O(1)
    for index_out in range(0, len(lista) - 1): #O(n)
        for index in range(0,len(lista) - 1 - index_out): #o(n²)
            
            current = lista[index] #O(1)
            new_current = lista [index + 1]#O(1)

            print(f'Cantidad de intercambios:{counter}. Elemento actual: {current}, Elemento a la izquierda: {new_current}') #O(1)


            if current > new_current: #O(1)
                counter = counter + 1 #o(n)
                lista[index] = new_current #O(1)
                lista[index+1]= current#O(1)
    
    return counter#O(1)



datos = [4, 2, 5, 1, 3,70]#O(1)
resultado = bubble_sort_count(datos)#O(1)
print(datos)        # [1, 2, 3, 4, 5]
print(resultado)    # 6
