# Experimente con el concepto de scope:
# Intente acceder a una variable definida dentro de una función desde afuera.
# Intente acceder a una variable global desde una función y cambiar su valor.


def test ():
    x  = 1
test(x)
print (x)


number = 5

def test():
    global number
    number = number + 1  


test()
print(number)

