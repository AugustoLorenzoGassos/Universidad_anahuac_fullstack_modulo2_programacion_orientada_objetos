"""
Demo 2: Diferencia entre atributos e instancias

"""

class Producto:
    """
    Producto con atrinutp de clase
    """
    #Atributo de clase: Compartido para todos los producto
    Impuesto = 0.16

Laptop = Producto()
Mouse = Producto()

#1. CASO NORMAL: Ambos leen la clase
print(f"Impuesto laptop (clase): {Laptop.Impuesto}")
print(f"Impuesto mouse (clase): {Mouse.Impuesto}")

#2. EL EFECTO SOMBRA
Laptop.Impuesto = 0.30
print("\n Después de aplicar el efecto sombra")
print(f"Impuesto laptop (instancia): {Laptop.Impuesto:.2f}")
print(f"Impuesto mouse (clase): {Mouse.Impuesto:.2f}")
print(f"Impuesto general (clase): {Producto.Impuesto:.2f}")

#3. ¿Qué pasa si cambiamos el global?
Producto.Impuesto = 0.10
print("\n Cambio de impuesto global")
print(f"Nuevo impuesto mouse: {Mouse.Impuesto}")
print(f"Nuevo impuesto laptop: {Laptop.Impuesto}")

