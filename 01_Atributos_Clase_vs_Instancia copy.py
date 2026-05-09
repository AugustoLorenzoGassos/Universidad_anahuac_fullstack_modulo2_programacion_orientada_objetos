"""
Demo 2: Diferencia entre atributos e instancias

"""

class Producto:
    """
    Producto con atrinutp de clase
    """
    #Atributo de clase: Compartido para todos los producto
    Impuesto = 0.16

#Crear los productos
Laptop = Producto()
Laptop.nombre = "Laptos Dell"
Laptop.precio_base = 15000

mouse = Producto()
mouse.nombre = "mouse"
mouse.precio_base = 500

#Accedemos a los productos de la clase
print(f"Impuestos para {Laptop.nombre}: {Producto.Impuesto * Laptop.precio_base}")
print(f"Impuestos para {mouse.nombre}: {Producto.Impuesto * mouse.precio_base}")

#Calcular el precio final
print(f"Precio final para {Laptop.nombre} es {Laptop.precio_base + (Laptop.precio_base * Producto.Impuesto):.2f}")
print(f"Precio final para {mouse.nombre} es {mouse.precio_base + (mouse.precio_base * Producto.Impuesto):.2f}")
print("\n")

#Si modificamos el atributo de clase afecta a TODAs las instancias
Producto.Impuesto = 0.08
print(f"Nuevo inpuesto laptop: {Laptop.Impuesto}")
print(f"Nuevo inpuesto mouse {mouse.Impuesto}")

#Calcular el precio final
print(f"Precio final para {Laptop.nombre} es {Laptop.precio_base + (Laptop.precio_base * Producto.Impuesto):.2f}")
print(f"Precio final para {mouse.nombre} es {mouse.precio_base + (mouse.precio_base * Producto.Impuesto):.2f}")
print("\n")
