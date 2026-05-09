"""
Es las dos caras del objeto __str__ vs __repr__
"""

class producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        #Para los usuarios
        return f"{self.nombre} - {self.precio}"
    
    def __repr__(self):
        #Para desarrolladores
        return f"Producto({self.nombre},${self.precio})"
    
p = producto("laptop", 27000)
print(p)
print(repr(p))
