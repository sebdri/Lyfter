"""
Cree un decorador que haga print de los parámetros y retorno de la función que decore.

"""


def print_parameters(func):
    def wrapper(*args, **kwargs):
        print(f'Args parameters: {args}')
        print(f'Kwargs parameters: {kwargs}')

        result = func(*args, **kwargs)
        print(result )
        return result 

    return wrapper



@print_parameters
def function(a,b,c):
    return a+b+c

function(9,13,c=2000)
print (function)