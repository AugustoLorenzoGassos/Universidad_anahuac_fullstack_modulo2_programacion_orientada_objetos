class Nadador:
    """Capacidad de nadar"""
    
    def nadar(self):
        return f"{self.nombre} está nadando"

class Volador:
    """Capacidad de volar"""
    
    def volar(self):
        return f"{self.nombre} está volando"

class Caminante:
    """Capacidad de caminar"""
    
    def caminar(self):
        return f"{self.nombre} está caminando"


# Animales con diferentes combinaciones
class Pato(Nadador, Volador, Caminante):
    """El pato puede hacer las tres cosas"""
    
    def __init__(self, nombre):
        self.nombre = nombre


class Pinguino(Nadador, Caminante):
    """El pingüino nada y camina, pero no vuela"""
    
    def __init__(self, nombre):
        self.nombre = nombre


class Aguila(Volador):
    """El águila solo vuela"""
    
    def __init__(self, nombre):
        self.nombre = nombre


# Pruebas
pato = Pato("Donald")
pinguino = Pinguino("Pingu")
aguila = Aguila("Águila Real")

print("=== PATO ===")
print(pato.nadar())
print(pato.volar())
print(pato.caminar())

print("\n=== PINGÜINO ===")
print(pinguino.nadar())
print(pinguino.caminar())

print("\n=== ÁGUILA ===")
print(aguila.volar())

# Verificar el MRO del pato
print("\n=== MRO DEL PATO ===")
for clase in Pato.__mro__:
    print(f"  → {clase.__name__}")
