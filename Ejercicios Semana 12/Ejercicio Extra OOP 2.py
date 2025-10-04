#Ejercicio Extra OOP 2

from abc import ABC, abstractmethod

class User(ABC): #Abstract Class

    @abstractmethod
    def get_role(self): #All users must include get_role
        pass

    @abstractmethod
    def has_permission(self, permission): #All users must include has_permissions
        pass


class AdminUser(User): #Inherits from User
    def __init__(self, name):
        self.name = name #Stores name

    def get_role(self):
        return "AdminUser: Tiene todos los accesos"
    
    def has_permission(self, permission):
        return True #All permissions = True


class RegularUser(User):
    def __init__(self, name):
        self.name = name #Stores name
        self.allowed_permissions = ["read"] #List of permissions for this user

    def get_role(self):
        return "RegularUser: Tiene permisos limitados"
    
    def has_permission(self, permissions):
        return permissions in self.allowed_permissions


user1 = AdminUser("Axel")
print(user1.get_role())
print(user1.has_permission("delete"))

user2 = RegularUser("Test")
print(user2.get_role())
print(user2.has_permission("delete"))
print(user2.allowed_permissions)