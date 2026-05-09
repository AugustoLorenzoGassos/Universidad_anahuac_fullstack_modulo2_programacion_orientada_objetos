class Producto:
    """
    Representa un produ cto online
    """
    pass #Esta palabra reservada indica que no esta haciendo nada

#Creamos objetos o instancias
producto1 = Producto()
producto2 = Producto()
producto3 = Producto()

#Verificar identidad y tipo de nuestro objeto
print(f"Tipo del producto 1: {type(producto1)}")
print(f"ID del producto 1: {id(producto1)}")
print(f"Tipo del producto 2: {type(producto2)}")
print(f"ID del producto 2: {id(producto2)}")
print(f"Tipo del producto 3: {type(producto3)}")
print(f"ID del producto 3: {id(producto3)}")
print(f"¿Son el mismo objeto? {producto1 is producto2} ")
print(f"¿Son el mismo objeto? {producto1 is producto3} ")

#Agregar atributos a la instancia de forma dinámica
producto1.nombre = "Laptop DELL"
producto1.precio = 25000
producto1.stock = 10

producto2.nombre = "switch cisco 350"
producto2.precio = 7000
producto2.stock = 18

producto3.nombre = "Impresora"
producto3.precio = 45000
producto3.stock = 27

producto3 = producto1
print(f"¿Son el mismo objeto? {producto1 is producto3} ")

#Acceder a los atributos
print(f"\nProducto 1: {producto1.nombre} - ${producto1.precio}")
print(f"\nProducto 2: {producto2.nombre} - ${producto2.precio}")
print(f"\nProducto 2: {producto3.nombre} - ${producto3.precio}")
