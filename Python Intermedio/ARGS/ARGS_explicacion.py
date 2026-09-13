''' 
                    {ARGS}

- Ya sabemos que las funciones pueden tener n cantidad de parámetros.
-Sin embargo, también hemos visto funciones que aceptan una cantidad aparentemente infinita de estos.

Por ejemplo, podemos pasarle "n" cantidad de datos al print divididos por coma, y este los imprimirá todos:

Esto lo podemos lograr agregando un asterisco * a la izquierda de uno de los parámetros de nuestra función.
:def my_function_with_infinite_params(*args):

'''







# def my_function_with_infinite_params(*args):
#     for index, arg in enumerate(args):
#         print(f"Arg {index}: {arg}")


# my_function_with_infinite_params(
#     2, 5, 6, 3, 6, 5, 6
# )



# print(my_function_with_infinite_params)





'''
Podemis tener combinaciones con funciones que tengan parametros normales def pedo(pedo, *args) y ponerme un 
paramtro infinio 

'''


# def my_function_with_infinite_params(my_other_param, *args):
#     for i, arg in enumerate(args):
#         print(f'Arg {i}: {arg}')

#     print (f'My other param: {my_other_param}')



# my_function_with_infinite_params (10,2,5,3,6,5,6)



"""
-Tambien puedo cambiar de posicion el parametro extra pero python no sabra donde esta la diferencia
por lo que en ese caso si debemos de especificarlo:

"""

# def my_function_with_infinite_params( *args,my_other_param):
#     for i, arg in enumerate(args):
#         print(f'Arg {i}: {arg}')

#     print (f'My other param: {my_other_param}')



# my_function_with_infinite_params (2,5,3,6,5,6, my_other_param = 10)



"""
{Kwargs}

Son parametro infinitos pero con nombre
Son igual que los args pero siempren necesitan un key, como un diccionario 
Se cran usando (**) a la izq de uno de los parametros 
Su estandar de nombramiento es Kwargs  
    -Vienen en formato de diccionario  
Importante! =  Estos siempre tienen que ir de ultimos

Ejemplo -->

"""

# def my_function_with_infinite_named_params(parameter1 , **kwargs):
#     print(f'Parameter 1: {parameter1}')
#     print(f'kwargs: {kwargs}')


# my_function_with_infinite_named_params("Hello",my_other_parameter="World",whatever=6)


# print(my_function_with_infinite_named_params)








"""
Tambien es posible combinar todo 
puedo tener parametro, junto a (*args), junto a (**kwargs)

"""


def my_function(firts_parameter, *args,**kwargs):
    print(f"First parameter: {firts_parameter}")
    for i, arg in enumerate(args):
        print(f'Arg: {i}: {arg}')

    print(f'kwargs: {kwargs}')


my_function("First value",1,2,3,4,my_other_parameter="World",whatever=6)