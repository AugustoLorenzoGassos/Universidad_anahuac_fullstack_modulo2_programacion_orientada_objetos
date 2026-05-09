class Clase_A:
    pass

class Clase_B:
    pass

class Clase_C:
    pass

class Hija_1(Clase_A, Clase_B):
    pass

class Hija_2(Clase_A, Clase_B, Clase_C):
    pass

class Hija_3(Clase_A, Clase_C):
    pass

print("Hija 1 tiene las siguinetes clases:")
for clase in Hija_1.__mro__:
    print(f"{clase.__name__}")
print("-"*30)
print("Hija 2 tiene las siguinetes clases:")
for clase in Hija_2.__mro__:
    print(f"{clase.__name__}")
print("-"*30)
longitud= len(Hija_3.__mro__)
print(longitud)
print("Hija 3 tiene las siguinetes clases:")
for i in range(1,longitud-1):
    print(Hija_3.__mro__[i])
    

