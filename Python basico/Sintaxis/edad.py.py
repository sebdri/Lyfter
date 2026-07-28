user_name = input("Ingrese su nombre: ")
user_last_name = input("Ingrese su apellido ")
user_age = int(input("Ingrese su edad: "))

if user_age < 5:
    print (f"Usted: {user_name} {user_last_name} es un bebé")

elif user_age < 6:
    print (f"Usted: {user_name} {user_last_name} es un niño")

elif user_age < 12:
    print (f"Usted: {user_name} {user_last_name} es un preadolescente")

elif user_age < 19:
    print (f"Usted: {user_name} {user_last_name} es un adolescente")

elif user_age < 23:
    print (f"Usted: {user_name} {user_last_name} es un adulto joven")

elif user_age < 60:
    print (f"Usted: {user_name} {user_last_name} es un adulto")

elif user_age < 100:
    print(f"Usted: {user_name} {user_last_name} es un adulto mayor")
