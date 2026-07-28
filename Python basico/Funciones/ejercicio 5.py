#Cree una función que imprima el número de mayúsculas y el número de minúsculas en un string.

word_number1 = 'Hola Mundo' #Palabra 


def i(word_number1): # Funcion
    Caps = 0 #Variables vacias para el print 
    lows = 0 #Variables vacias para el print

    for letters in word_number1: #Recorre la palabra 
        if letters.isupper(): #Nuestra condicional
            Caps = Caps + 1 #suma al contador Caps 
        elif letters.islower():#Nuestra condicionalb contraria
            lows = lows + 1 #suma al contador lows 
    return Caps,lows # return para obtener los daos de vuelta  
Caps, lows = i(word_number1) # contador del def

print ('Usted tiene una cantidad de mayusculas de: ', Caps)
print ('Usted tiene una cantidad de minusculas de: ', lows)



