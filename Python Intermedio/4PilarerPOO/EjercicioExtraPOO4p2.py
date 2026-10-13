from abc import ABC,abstractmethod


class User(ABC):
    def __init__(self, name):
        self.name = name
        

    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod 
    def has_permission(self, permission):
        pass





#{clases que heredan}





class AdminUser(User): #siempre tiene permisos 

    def get_role(self):
        return "Admin"

    def has_permission(self, permission):
        return "User has permission"




class RegularUser(User):
    def get_role(self):
        return 'Regular user'

    def has_permission(self, permission):
        if permission == 'read':
            return "User do not has this permission"
        else:
            return False

# {Parte interactiva}

name = input("Enter the user's name: ")
role = input("Enter the users role: ")

if role.lower() == "admin":
    user1 = AdminUser(name)
    print(f'User {user1.name} is as: {user1.get_role()} ')

    permission = input("Enter the permission you want to check: ")
    print(user1.has_permission(permission))

elif role.lower() == "regular user":
    user2 = RegularUser(name)
    print(f'User {user2.name} is as: {user2.get_role()} ')

    permission = input("Enter the permission you want to check: ")
    print(user2.has_permission(permission))











