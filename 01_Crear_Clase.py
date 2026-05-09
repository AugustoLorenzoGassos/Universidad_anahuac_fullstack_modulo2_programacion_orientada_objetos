class Libro:
    """Representa un libro"""
    #Contador de todos los libros
    total_libros = 0
    #pass #Esta palabra reservada indica que no esta haciendo nada

Libro1 = Libro()
Libro1.titulo = "La reina roja"
Libro1.autor = "Juan Gómez-Jurado"
Libro1.ISBN = "ISBN - 000001"
Libro1.disponible = True
Libro.total_libros += 1

Libro2 = Libro()
Libro2.titulo = "El resplandor"
Libro2.autor = "Stephen King"
Libro2.ISBN = "ISBN - 000002"
Libro2.disponible = True
Libro.total_libros += 1

Libro3 = Libro() 
Libro3.titulo = "Los tres mundos"
Libro3.autor = "Santiago Posteguillo"
Libro3.ISBN = "ISBN - 000003"
Libro3.disponible = True
Libro.total_libros += 1

print(f"Datos del libro {Libro1.titulo}")
print("Autor: ", Libro1.autor)
print("ISBN :", Libro1.ISBN)
print("Disponible: ", Libro1.disponible)

print("\n")
print(f"Datos del libro {Libro2.titulo}")
print("Autor: ", Libro2.autor)
print("ISBN :", Libro2.ISBN)
print("Disponible: ", Libro2.disponible)

print("\n")
print(f"Datos del libro {Libro3.titulo}")
print("Autor: ", Libro3.autor)
print("ISBN :", Libro3.ISBN)
print("Disponible: ", Libro3.disponible)

print("\n")
print(f"El total de libros es {Libro.total_libros}")