# #CREANDO CLASES 

# class Car:
#     pass

# my_car=Car()
# print(my_car)


# # Con una sola clase puedo crear cuantas instancias yo quiera.

# class Car:
#     pass

# my_car= Car()

# my_car_2 = Car()

# print(my_car_2)
# print(my_car)



#----------------LOS ATRIBUTOS----------------
# class Car:
#     wheel_number = 4 #---> Atributo <---
#     #Decimos que todos los objetos "Car" van a tener un atributo de wheel_number = 4    

# #Podemis accesarlo, como? R/ my_car.wheel_number
# #Porque ".wheel_number"? Porque es un atributo no una variable cualquiera, lo que quiere decir que necesito un objeto para accesarla
# my_car = Car()
# print(my_car.wheel_number)


# #Tambien puedo cambiarles el valor como a las variables=

# class Car:
#     wheel_number = 4 #Valor ya definido

# my_car = Car()
# my_car.wheel_number = 6 #Agregando un nuevo valor
# print(my_car.wheel_number)

# #Esto significa que distintos objetos de la misma clase pueden tener distintos valores en sus atributos.
# class Car:
# 	wheel_number = 4 #salidos de la fabrica todos


# my_car = Car() # My_car tiene 4

# my_truck = Car()#A este punto my_truck tiene 4
# my_truck.wheel_number = 6 # Ya ahora tiene 6 pero my_car sigue en 4

# my_bigger_truck = Car()#A este punto my_bigger_truck tiene 4
# my_bigger_truck.wheel_number = 8 # Ya ahora tiene 8 pero my_car sigue en 4 y my_truck en 6


# print(my_car.wheel_number) # Resultado= 4
# print(my_truck.wheel_number)# Resultado= 6
# print(my_bigger_truck.wheel_number)# Resultado= 8 


#----------------LOS METODOS----------------

# #Son como funciones dentro de un objeto, ejemplo = .append()
# #Se declaran dentro de las clases y se declaran casi igual a una fiuncion normal:
# #                          def my_first_method():
# #PERO!!!! el primero paramentro siempre siempre sera "self"
# #                          def my_first_method(self):

# class Car:
# 	wheel_number = 4

# 	def my_first_method(self):
# 		print("Hola mundo")


# # Ahora podemos llamarlo justo como si fuera el append de una lista. 
# # Necesitamos una instancia de Car seguido de .my_first_method().

# class Car:
# 	wheel_number = 4

# 	def my_first_method(self):
# 		print("Hola OOP mundo")

# my_car = Car()
# my_car.my_first_method()


#---------------- PARA QUE ES EL SELF?----------------
#REPASAR HASTA LLEGAR A LO CONSTRUCTORES 

#El self hace referencia al objeto que llame a esa funcion en el futuro


# class Car:
# 	wheel_number = 4

# 	def my_first_method(self):
# 		print("Hola OOP mundo")

# 	def show_history(self, miles, crashes): #self va a tener como valor my_car que es el objeto que esta llamando show_history
# 		print(f'This cas has: {miles} miles and {crashes} crashed')

# my_car = Car()
# my_car.show_history(45000, 2) # este metodo puede ser llamado solo por class Car y no por fuera




# class Car:
# 	wheel_number = 4
# 	door_number = 4
# 	window_number = 6
	
# 	# def my_first_method(self):
# 	# 	print("Hello OOP World!")

# 	def show_history(self, miles, crashes ):
# 		print(f"This car has {miles} miles, {crashes} crashes, has {self.wheel_number} wheels, has {self.door_number} doors and has {self.window_number} windows")
		
		
# my_car = Car()
# my_car.show_history(45000, 2)

#pregunta: Cual es la diferencia entre:

# def show_history(self, miles, crashes, doors, windows ):
# 		print(f"This car has {miles} miles, {crashes} crashes, has {self.wheel_number} wheels, has {doors} doors and has {windows} windows")
		
		
# my_car = Car()
# my_car.show_history(45000, 2, 4, 6)


# y :


# class Car:
# 	wheel_number = 4
# 	door_number = 4
# 	window_number = 6
	
# 	# def my_first_method(self):
# 	# 	print("Hello OOP World!")

# 	def show_history(self, miles, crashes ):
# 		print(f"This car has {miles} miles, {crashes} crashes, has {self.wheel_number} wheels, has {self.door_number} doors and has {self.window_number} windows")
		
		
# my_car = Car()
# my_car.show_history(45000, 2)



# class Car: #clase
# 	wheel_number = 4 # atributo
	
# 	def my_first_method(self): # metodos
# 		print("Hello OOP World!")

# 	def show_history(self, miles, crashes):# otro metodo con parametros
# 		print(f"This car has {miles} miles, {crashes} crashes and {self.wheel_number} wheels")
		
		
# my_car = Car()

# my_truck = Car()
# my_truck.wheel_number = 6

# my_bigger_truck = Car()
# my_bigger_truck.wheel_number = 8


# my_car.show_history(45000, 2)
# my_truck.show_history(45000, 2)
# my_bigger_truck.show_history(45000, 2)



# #---------------- LOS CONSTRUCTORES ----------------

# #Es el metodo que se ejecuta por defecto cada vez que instanciamos una clase.

# class Person:
# 	pass

# person_1 = Person() #---> Esto tiene una funcion a nivel interno que se ejecuta al realizar esto
# 					# Lo que se ejecuta es el constructor															

# #Npodemos sobre-escribir ese constructor vacío añadiendo un método 
# #llamado __init__ a nuestras clases. Unica y exclusivamente __init__ funciona para esto



# class Person:
# 	def __init__(self): # es un metodo, con su self
# 		print("Ha nacido una persona")

# person_1 = Person()

# podemos darle parametros a los constructores 

# class Person():
# 	def __init__(self, name):
# 		print(f"Ha nacido una persona llamada {name}!")
# 		self.age = 0 #agregando atributos al contructor 

# person_1 = Person("John")
# print(person_1.age)# accediendo ese atributo


#como agregamos el "name" en def __init__(self, name):, tengo que pasarle el 
#nombre del parametro a person()


class Person():
	def __init__(self,name):
		print(f'Ha nacido una persona llamado: {name}')

		self.age = 0
		self.name = name

person_1= Person("Jose")
print(person_1.age)
print(person_1.name)
