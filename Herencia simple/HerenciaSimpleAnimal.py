class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hacer_sonido(self):
        return "Algún sonido"

class Perro(Animal):
    def __init__(self, nombre, raza):
        # Llamar al constructor del padre
        super().__init__(nombre)
        # Añadir atributo específico del hijo
        self.raza = raza
    
    def hacer_sonido(self):
        # Sobrescribir método del padre
        return "¡Guau!"

class Gato(Animal):
    def __init__(self, nombre, raza, color):
        super().__init__(nombre)
        self.raza = raza
        self.color = color
    
    def hacer_sonido(self):
        return "¡Miau!"

print("Información de un perro")
datos_perro = Perro("jack","Golden Retriver")
print(datos_perro.nombre)
print(datos_perro.raza)
print(datos_perro.hacer_sonido())

print("\n")
print("Información de un gato")
datos_gato = Gato("Piccina","Persa","Blanco")
print(datos_gato.nombre)
print(datos_gato.raza)
print(datos_gato.color)
print(datos_gato.hacer_sonido())

print("\nInstancias")
print(isinstance(datos_perro, Perro))
print(isinstance(datos_perro, Animal))
print(isinstance(datos_perro, Gato))
print(isinstance(datos_gato, Gato))
print(isinstance(datos_gato, Animal))
print(isinstance(datos_gato, Perro))

print("\nsubclass")
print(issubclass(Perro, Animal))

#Mi_labrador = Perro()
print("Prueba con type")
print(type(datos_perro) is Perro)
print(type(datos_perro) is Animal)

print("Validadndo si es instancia")
print(isinstance(datos_perro,Perro))
print(isinstance(datos_perro,Animal))
