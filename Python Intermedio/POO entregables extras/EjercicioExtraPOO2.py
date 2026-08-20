class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def speak(self):
        return "Hace sonido"

class Dog(Animal):
    def speak(self):
        return "Guau"

class Cat(Animal):
    def speak(self):
        return "MIAU"


dog = Dog("Firulais")
cat = Cat("Firulais")


print(f"El perro se llama {dog.nombre} y hace: {dog.speak()}")
print(f"El gato se llama {cat.nombre} y hace: {cat.speak()}")