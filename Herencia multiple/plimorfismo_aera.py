import math

# Interfaz implícita (clase base)
class Forma:
    def area(self):
        raise NotImplementedError
    
    def perimetro(self):
        raise NotImplementedError
    
    def describir(self):
        return f"{self.__class__.__name__}: Área={self.area():.2f}, Perímetro={self.perimetro():.2f}"

# Implementaciones específicas
class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio
    def area(self):
        return math.pi * self.radio ** 2
    def perimetro(self):
        return 2 * math.pi * self.radio

class Rectangulo(Forma):
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
    def area(self):
        return self.largo * self.ancho
    def perimetro(self):
        return 2 * (self.largo + self.ancho)

class Triangulo(Forma):
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
    def area(self):
        return (self.base*self.altura)/2

# Función polimórfica
def calcular_area_total(formas):
    return sum(forma.area() for forma in formas)

# Crear y usar
formas = [Circulo(5), Rectangulo(10, 6), Circulo(3), Triangulo(3,4)]
for i, f in enumerate(formas, 1):
    print(f"{i}. {f.describir()}")

print(f"ÁREA TOTAL: {calcular_area_total(formas):.2f}")

#Triangulo_1 = Triangulo.area(4,4)