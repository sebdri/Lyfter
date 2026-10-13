def only_number(func):
    def wrapper(*args, **kwargs):
        for valor in args:
            if not isinstance(valor,(int , float)) or isinstance(valor, bool):
                raise TypeError(f"El valor {valor!r} no es un número")

        for clave , valor in kwargs.items():
            if not isinstance(valor, (int,float)) or isinstance(valor,bool):
                raise TypeError(f"El parámetro '{clave}' = {valor!r} no es un número")

        return func(*args, **kwargs)
    return wrapper


@only_number
def function(a, b):
    return a + b


print(function(12,3))
print(function(12,"ola"))