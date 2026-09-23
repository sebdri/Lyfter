import datetime

def log_call(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        print(f'func:{func.__name__} - args: {", ".join(str(x) for x in args)} - [{datetime.datetime.now()}]- Resultado: {result}')
        return result
    return wrapper

def validate_numbers(func):
    def wrapper (*args,**kwargs):
        for data in args:
            if not isinstance (data,(int,float)):
                raise ValueError(f"The {data} is not a number")
        return func(*args,**kwargs)
    return wrapper

@log_call
@validate_numbers
def multiply(a , b):
    return a*b



valor = multiply(3, 0)
print(valor)