"""
class usuario:
    def __init__(self, username, email, activo=True):
        #valor por defecto
        self.username = username
        self.email = email
        self.activo = activo 
class ejemplo:
    def __init__(self, a, b, c=True):
        pass
class ejemplo_incorrecto:
    def __init__(self, a, c, b=True):
        pass
class Ejemplo:
    def __init__bre(self, nombre, edad=18, pais="Méxcico", activo=True):
        self.nombre = nombre
        self.edad=edad
        self.pais=pais
        self.activo=activo
        pass
"""
#Pasar lista en parámetros por default es una muy malña práctica de programación
class ejemplo_bueno:
    def __init__(self,a,b=None):
        self.a = a
        self.b = b if not None else []

ejemplo1=ejemplo_bueno(1)
ejemplo2=ejemplo_bueno(1,[1,2,3,4])

print(ejemplo1.a, ejemplo1.b)
print(ejemplo2.a, ejemplo2.b)

"""
user1 = usuario("alorenzo","augusto.lorenzo.acero@gmail")
user2 = usuario("mlorenzo","monica@gmail.com",False)

print("\n")
print(f"El usuario {user1.username} esta con el status {user1.activo}")
print(f"El usuario {user2.username} esta con el status {user2.activo}")
print("\n")
"""
