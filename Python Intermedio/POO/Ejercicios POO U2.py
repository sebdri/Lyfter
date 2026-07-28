# #                -----<Practica>-----
#     # Vamos a crear una clase estudiante que tenga los atributos de 
#     # "Nombre", "Edad" y "Grado" crearemos un metodo estudiar() con un
#     # Print(f"El estudiante{} esta estudiando)

class estudiante:
    def __init__(self, Nombre, Edad, Grado):
        self.nombre = Nombre
        self.edad = Edad
        self.grado = Grado

    def estudiar(self):
        print(f"{self.nombre} Estudiando....")
        


nombre = input("Digame su nombre: ")
edad = int(input("Ingrese su edad: "))
grado = input("Ingrese su grado: ")

Estudiante = estudiante(nombre,edad,grado)


print(f"""DATOS DEL ESTUDIANTE: \n\n
    Nombre:{Estudiante.nombre}\n
    Edad: {Estudiante.edad}\n
    Grado: {Estudiante.grado}""")

estudiar = input()
if estudiar.lower() == "estudiar":
    Estudiante.estudiar()


# #   <Aqui le entregamos los parametros al __init__>

# # Estudiante = estudiante("Sebastian", 20, 11)

# # print(Estudiante.nombre)
# # Estudiante.estudiar()