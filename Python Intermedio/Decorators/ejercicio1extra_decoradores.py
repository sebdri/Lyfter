def repeat_line_twice(func):
    def wrapper(*args, **kwargs):
        func (*args,**kwargs)
        func (*args,**kwargs)
    return wrapper


@repeat_line_twice
def say_hi_to(name):
    
    print(f'Hello, {name}')



say_hi_to("Sebas")