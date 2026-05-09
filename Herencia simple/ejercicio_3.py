import turtle

class Figura:
    def __init__(self,nombre_figura):
        self.nombre_figura=nombre_figura

class Cuadrado(Figura):
    def __init__(self,nombre_figura,lado):
        super().__init__(nombre_figura)
        self.lado=lado

    def area(self):
        t = turtle.Turtle()
        for _ in range(4):
            t.forward(100)
            t.right(90)
        return f"\n{self.nombre_figura}. Area: {self.lado*self.lado}"
    
class Rectangulo(Figura):
    def __init__(self, nombre_figura,base,altura):
        super().__init__(nombre_figura)
        self.base=base
        self.altura=altura

    def area(self):
        t = turtle.Turtle()
        t.forward(self.base)
        t.right(90)
        t.forward(self.altura)
        t.left(90)
        t.backward(self.base)
        t.left(90)
        t.forward(self.altura)
        return f"\n{self.nombre_figura}. Area: {self.base*self.altura}"

class circulo(Figura):
    def __init__(self, nombre_figura, radio):
        super().__init__(nombre_figura)
        self.radio = radio

    def area(self):
        t = turtle.Turtle()
        t.circle(50)
        return f"\n{self.nombre_figura}. Area: {3.1416*(self.radio**2)}"
    
dibujar_cuadrado = Cuadrado("Cuadrado",20)
print(dibujar_cuadrado.area())

dibujar_rectangulo = Rectangulo("Rectangulo",100,50)
print(dibujar_rectangulo.area())

dibujar_circulo = circulo("Círculo", 20)
print(dibujar_circulo.area())

turtle.done()
