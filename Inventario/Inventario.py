class articulo:
    almacen_principal = "Bodega central"

articulo1 = articulo()
articulo1.codigo = "0001"
articulo1.descripcion = "Tornillos 3/4"
articulo1.cantidad = 500
articulo1.precio_unitario = 2.50

articulo2 = articulo()
articulo2.codigo = "0002"
articulo2.descripcion = "Clavos 1 piulgada"
articulo2.cantidad = 700
articulo2.precio_unitario = 1.50

articulo3 = articulo()
articulo3.codigo = "0003"
articulo3.descripcion = "Pinzas persión"
articulo3.cantidad = 120
articulo3.precio_unitario = 125

articulo4 = articulo()
articulo4.codigo = "0004"
articulo4.descripcion = "Desarmador de cruz"
articulo4.cantidad = 1500
articulo4.precio_unitario = 37.00

articulo5 = articulo()
articulo5.codigo = "0005"
articulo5.descripcion = "Desarmador de punta plana"
articulo5.cantidad = 1800
articulo5.precio_unitario = 35.00

#Valor total del inventario
#Costo total por artículo

costo_total_inventario = 0.0
costo_total_articulo = 0.0

lista_articulos = [articulo1, articulo2, articulo3, articulo4, articulo5]

print(f"Ivnetnario de {articulo.almacen_principal}\n")

for i in lista_articulos:
    print(f"Cosoto del artículo ({i.codigo} - {i.descripcion}): {i.cantidad * i.precio_unitario:.2f}")
    costo_total_inventario += i.cantidad * i.precio_unitario

print("\n")
print(f"El valor total del inventario es: {costo_total_inventario:.2f}\n")
