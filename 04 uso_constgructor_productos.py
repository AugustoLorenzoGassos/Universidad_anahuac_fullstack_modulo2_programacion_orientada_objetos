class producto:
    impuesto = .16
    def __init__(self, nombre, precio, stock):
        self.nombre=nombre
        self.precio = precio
        self.stock = stock
        self.venta = 0.0

Producto1 = producto("Laptop Dell",17000,1500)
Producto2 = producto("Mouse",500,350)

lista_productos = [Producto1, Producto2]
for item in lista_productos:
    print(f"Producto 1: Nombre - {item.nombre}, Precio - {item.precio}, Cantidad: {item.stock}")
