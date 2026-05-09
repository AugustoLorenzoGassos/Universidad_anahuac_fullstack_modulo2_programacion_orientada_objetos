class Perro:
    def hablar(self):
        return "¡Guau!"

class Gato:
    def hablar(self):
        return "¡Miau!"

class vaca:
    def hablar(self):
        return("Muuuu")
    
def hacer_hablar(animal):
    print(animal.hablar())

hacer_hablar(Perro())  # ¡Guau!
hacer_hablar(Gato())   # ¡Miau!
hacer_hablar(vaca())