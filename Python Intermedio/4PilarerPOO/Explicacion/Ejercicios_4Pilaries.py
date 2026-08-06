#                                   ==={Herencia}===


# class Vehicule:
#     is_on = False
#     wheel_number = 0


#     def turn_on(self):
#         self.is_on = True
#         print(f'Vehicle with {self.wheel_number} wheels is on')

#     def turn_off(self):
#         self.is_on = False
#         print(f'Vehicle with {self.wheel_number} wheels is off')


# class Car(Vehicule):
#     wheel_number = 4


# class Bike(Vehicule):
#     wheel_number = 2


# my_car = Car()
# my_car.turn_on()
# my_car.turn_off()
# my_bike = Car()
# my_bike.turn_on()
# my_bike.turn_off()





#                                   ==={Herencia Multiple}===


# class WalkMixin:
#     def walk(self):
#         print("I'm walking")

# class RunMixin:
#     def run(self):
#         print("I'm running")

# class FlyMixin:
#     def fly(self):
#         print("I'm flying")



# class superhuman(WalkMixin,RunMixin,FlyMixin): #Herencia multiple - se le agregan como atributos
#     pass




# human = superhuman()
# human.run()
# human.fly()
# human.walk()


#                                   ==={Clases abstractas}===

""" -Muchas veces se crean clases pero no queremos que esas se puedan instanciar . Como que un molde no se pueda
usar para crear pan si no para crear otros moldes 
- ES UNA CLASE CON LA QUE YO NO PUEDO CREAR OBJETOS! PUEDO CREAR ATRIBUTOS, METODOS LO QUE SEA, PERO NO LAS PUEDO INSTANCIAR
SI NO QUE SOLO SE USAN PARA QUE OTRAS CLASES HEREDEN DE ELLA

Podemos poner de ejemplo una computadora que todas tienen:
1. Memoria 
2. Disco
3. Procesador 
4. RAM

Pero yo no quiero que se creen computadoras como tal, si no que quiero que se creen:
-Celulares 
-Desktops
-Laptops

Pero mi clase computadora tienen todas esas caracteristicas compartidas 

========[METODOS ABSTRACTOS]========

- SON METODOS DE LAS CLASES ABSTRACTAS QUE AL HEREDARLOS NECESITAN SER SOBRESCRITOS


Ejemplo:
"""
# from abc import ABC, abstractmethod   #ESTO SIEMPRE DEBE DE IR YA QUE LAS CLASES ABSTRACTAS TIENEN QUE HEREDAR DE ABC
# # TIENEN QUE TENER ABC COMO PARAMETRO

# class Animal (ABC): #Clase animal
#     def breath(self): #Todos los animales deben respirar
#         pass 

#     def born(self):
#         pass

#     @abstractmethod # CON ESTO LE DECIMOS, SI USTED HEREDA DE CLASS ANIMAL USTED NECESITA CREAR SU PROPIA VERSION DE
#     # metodo def reproduce
#     def reproduce(self):
#         #Todos los animales deben reporducirse para sobrevivir, pero pueden hacerlo de dif maneras
#         pass



# class AsexualAnimal(Animal): #Heredan de animal
#     def reproduce(self): #Tienen el metodo reproducirse 
#         print("Reproducing in an asexual manner")

# class SexualAnimal(Animal):
#     def reproduce(self):
#         print(f"Reproducing in a sexual manner")

# class OtherAnimal(Animal): #Hereda si, pero no tiene su metodo creado por lo que a la hora de crar el objeto dara error
#     pass



# asexual_animal =AsexualAnimal()
# asexual_animal.reproduce()# -> Reproducing in an asexual manner 

# sexual_animal_a =SexualAnimal()
# sexual_animal_b =SexualAnimal()
# sexual_animal.reproduce(sexual_animal_b)# -> Reproducing in a sexual manner with sexual_animal_b

# # animal =Animal()# va a fallar porque Animal es una clase abstracta

# # other_animal =OtherAnimal()# va a fallar porque no se sobre-escribió el método reproduce



from abc import ABC, abstractmethod


class Animal(ABC):
	def breath(self):
		pass

	def born(self):
		pass

	@abstractmethod
	def reproduce(self):
		# Todas las especies de animales deben reproducirse para sobrevivir
		# Pero lo pueden hacer de distintas maneras
		pass

class AsexualAnimal(Animal):
	def reproduce(self):
		print("Reproducing in an asexual manner")

class SexualAnimal(Animal):
	def reproduce(self, mate):
		print(f"Reproducing in a sexual manner with {mate}")

class OtherAnimal(Animal):
	pass


asexual_animal = AsexualAnimal()
asexual_animal.reproduce() # -> Reproducing in an asexual manner 

sexual_animal_a = SexualAnimal()
sexual_animal_b = SexualAnimal()
sexual_animal.reproduce(sexual_animal_b) # -> Reproducing in a sexual manner with sexual_animal_b

# animal = Animal() # va a fallar porque Animal es una clase abstracta
# other_animal = OtherAnimal() # va a fallar porque no se sobre-escribió el método reproduce