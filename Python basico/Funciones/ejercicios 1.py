# Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.'


def my_first_print(): 
    print("Hola") 
    my_second_print() 
    
def my_second_print(): 
    print("Mundo") 
    
def main(): 
    my_first_print()
    
main()


