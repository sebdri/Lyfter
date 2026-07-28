
import random
from random import randint

secret_number = randint(1, 10)
guessed  = False

while not guessed:
    guess = int(input("Adivina el número (1 al 10): "))

    if guess == secret_number:
        print("Correcto! Adivinaste el número.")
        guessed  = True
    else:
        print("Incorrecto. Intenta de nuevo.")
