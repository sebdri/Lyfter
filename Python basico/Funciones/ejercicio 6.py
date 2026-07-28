# Cree una función que acepte un string con palabras separadas por un guion y retorne un string igual pero ordenado alfabéticamente.

word = input('INGRESE SU PALABRA SEPARADA POR GUIONES:')

def order():
   entry = word.split("-")
   mid = sorted(entry) 
   final = "-".join(mid)
   return final

final_result  = order()
print(final_result)






