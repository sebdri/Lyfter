'''                       {Decorators}
Que son?
R/ Son plabras con la sintaxis: @palabra , son basicamente funciones que modifican y le dan funcionamiento extras a otras funciones 
(sean de una clase o no)

- Pueden usarsen para ejecutar instruccione antes o despues de las instrucciones de la función que decoran
- Tambien pueden usarsen para revisar o mo;dificar parametros de la funcion 

Su sintaxis:
def decorator_name(func):
    def wrapper(parameters):
        # Logica extra
        func(parameters) # Llamada a la funcion decorada
				# Logica extra

    return wrapper


Por ejemplo -->

'''


# class User:
#     role = str

#     def __init__(self,role):
#         self.role = role




# def create_product (user, product_name):
#     if user.role.lower() != "admin":
#         raise ValueError('You are not allowed to run this function. You are not an admin')

#     else: 
#         print(f'Product {product_name} created!')




# def create_product_category(user, product_category_name):
#     if user.role.lower() != 'admin':  
#         raise ValueError('You are not allowed to run this function. You are not an admin')

#     else: 
#         print(f'Product {product_category_name} created!')



# def modify_order(user, order_id):
#     if user.role.lower() !="admin":
#         raise ValueError('You are not allowed to run this function. You are not an admin')

#     else: 
#         print(f'Product {order_id} created!')




# my_user = User("ADmin")
# modify_order(my_user, 4)
# Output: Order 4 modified!




# my_user = User("Customer")
# modify_order(my_user, 4)
# Output = ValueError: You are not allowed to run this function. You are not an admin



'''
- Mas si embargo aqui estamos rompiendo con el principio DRY (Don't Repeat Yourself)
💡 Una posible solucion seria convertir esa lógica de verificación en una función -->

'''


# class User:

#     def __init__(self,role):
#         self.role = role


# def check_if_user_admin(user):
#     if user.role.lower() != 'admin':
#         raise ValueError('You are not allowed to run this function. You are not an admin')


# def create_product(user, product_name):
#     check_if_user_admin(user)

#     print(f"Product {product_name} created!")



# def create_product_category(user, product_category_name):
#     check_if_user_admin(user)


#     print(f"Product {product_category_name} created!")




# def modify_order(user, order_id):
#     check_if_user_admin(user)


#     print(f"Product {order_id} created!")






# sebas = User('admin')
# create_product(sebas, "iphone17")




'''
-Mas sin embargo la solucion mas recomendada y elegante es crear un decorator🚀 -->


'''


# class User: 

#     def __init__(self, role):
#         self.role = role


# def only_admin(func):
#     def wrapper(user,*args):
#         if user.role.lower()!= 'admin':
#             raise ValueError('You are not allowed to run this function. You are not an admin')
#         func(user, args)

#     return wrapper

# @only_admin
# def create_product(user, product_name):
#     print(f"Product {product_name} created!")



# @only_admin
# def create_product_category(user, product_category_name):
#     print(f"Product {product_category_name} created!")




# @only_admin
# def modify_order(user, order_id):
#     print(f"Product {order_id} created!")


# sebas = User('Admin')
# create_product(sebas,'iphone 17')    




'''
La forma que le vamos a decir al decorador que haga cosas antes o despues de una funcion depende de donde pongamos 
esa accion en la creacion del decorador

Ejemplo-->

def function(func):
    def wrapper():
        print("Pre-function")
        func()
        print("Goodbye")
    return wrapper

'''


def function(func):
    def wrapper():
        print("Pre-function")
        func()
        print("Goodbye")
    return wrapper


@function
def greeting():
    print("Hello world")





#Esto yo lo puedo hacer con cuantas funciones yo quiera
#Asi como revisar parametros



@function
def Too_many_greeting():
    print("Hello world")
    print("Hello world")
    print("Hello world")
    print("Hello world")
    print("Hello world")
    print("Hello world")
    print("Hello world")


Too_many_greeting()
