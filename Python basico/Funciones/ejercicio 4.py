# Cree una función que le dé la vuelta a un string y lo retorne.

word = input("Ingrese la palabra que quiere poner al reves: ")

def word_inverse(word):
    result=''
    for letter in word:
        result = letter  + result
    return result
result = word_inverse(word)
print(result)
 

