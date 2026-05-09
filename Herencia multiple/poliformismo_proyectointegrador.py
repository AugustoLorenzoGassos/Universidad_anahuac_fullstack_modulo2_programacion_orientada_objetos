"""
Proyecto Integrador - Fase 1: Modelo de Publicaciones
Fase 1: Diseño y Clases Base
Implementa Publicacion con Mixins y ABC. 
Crea Libro, Revista y Tesis con atributos específicos y métodos abstractos implementados.
"""

from abc import ABC, abstractmethod
import datetime

class PublicacionMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fecha_creacion = datetime.datetime.today()

class Pubicacion(PublicacionMixin, ABC):
    def __init__(self, titulo, autor, edicion, año, isbn, disponible):
        super().__init__()
        self.titulo = titulo
        self.autor  = autor
        self.edicion = edicion
        self.año = año
        self.isbn = isbn
        self._disponible = disponible

    def prestar(self):
        self._disponible = False
        return self._disponible

    def poner_disponible(self):
        self._disponible = True
        return self._disponible
        
    @property
    def disponible(self): return self._disponible

    @abstractmethod
    def tiempo_prestamo(self): return 10

"""Fase 2"""
class Socio:
    limite_prestamos = 2
    def __init__(self, nombre, curp, correo):
        self.nombre = nombre
        self.curp = curp
        self._correo = correo
        self.__historial_prestamos = []

    @property
    def correo(self): return self._correo

    def registrar_prestamo(self,titulo):
        self.__historial_prestamos.append(titulo)
        return(self.__historial_prestamos)

    def prestamo_autorizado(self):
        return len(self.__historial_prestamos) < self.limite_prestamos

    def reporte_prestamos(self):
        return self.__historial_prestamos
    
class Prestamo(PublicacionMixin):
    MULTA_POR_DIA = 10
    def __init__(self, socio, publicacion):
        super().__init__()
        self.socio = socio
        self.publicacion = publicacion
        self.fecha_prestamo = datetime.date.today()
        dias = publicacion.tiempo_prestamo()
        self.fecha_devolucion_esperada = self.fecha_prestamo + datetime.timedelta(days=dias)
        self._devuelto = False

    def dias_retraso(self):
        hoy = datetime.date.today()
        if hoy > self.fecha_devolucion_esperada:
            return (hoy - self.fecha_devolucion_esperada).days
        return 0    

    def calcular_multa(self): 
        return self.dias_retraso() * self.MULTA_POR_DIA

    def devolver(self):
        self._devuelto = True

    def __str__(self):
        #return f"Prestamo: Título: {self.publicacion}\nfecha de prestamo {self.fecha_prestamo} con fecha de devolucion esperada: {self.fecha_devolucion_esperada}"
        return f"Préstamo: '{self.publicacion.titulo}'\n"f"Socio: {self.socio.nombre}\n"f"Fecha del préstamo: {self.fecha_prestamo.strftime("%d/%m/%Y")}\n"f"Fecha de devolición: {self.fecha_devolucion_esperada.strftime("%d/%m/%Y")}"

"""Fase 3"""
class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.__publicaciones = []
        self.__socios = []
        self.__prestamos = []

    def agregar_publicacion(self, pub):
        if isinstance(pub, Pubicacion):
            self.__publicaciones.append(pub)

    def agregar_socio(self, soc):
        if isinstance(soc, Socio):
            self.__socios.append(soc)

    def reporte_socios(self):
        return self.__socios
    
    def reporte_publicaciones(self):
        return self.__publicaciones
    
    def realizar_prestamo(self, socio_id, pub_id):
        socio = self.buscar_socio_por_id(socio_id)
        pub = self.buscar_publicacion_por_id(pub_id)
        # and socio.prestamo_autorizado()
        if socio and pub and pub.disponible:
            prestamo = Prestamo(socio, pub)
            socio.registrar_prestamo(prestamo)
            self.__prestamos.append(prestamo)
            pub.prestar()
            return prestamo
        raise ValueError("No se puede realizar el préstamo")    
    
    def buscar_socio_por_id(self,socio_id):
        for item_socio in self.__socios:
            if item_socio.curp == socio_id:
                return item_socio
        return False
    
    def buscar_publicacion_por_id(self, pub_id):
        for item_pub in self.__publicaciones:
            if item_pub.isbn == pub_id:
                return item_pub
        return False

    def reporte_prestamos(self):
        return self.__prestamos
    
    def devolver_prestamo(self,prestamo):
        """
        for item_devuelto in self.__prestamos:
            if prestamo.publicacion.isbn == item_devuelto.publicacion.isbn:
                self.__prestamos.remove(item_devuelto)
        """
        prestamo.devolver()
        publicacion_actual = self.buscar_publicacion_por_id(prestamo.publicacion.isbn)
        publicacion_actual.poner_disponible()

"""
Crea Libro, Revista y Tesis con atributos específicos y métodos abstractos implementados.
"""

class Libro(Pubicacion):
    def __init__(self, titulo, autor, edicion, año, isbn, disponible, genero, idioma):
        super().__init__(titulo, autor, edicion, año, isbn, disponible)
        self.genero = genero
        self.idioma = idioma
    def tiempo_prestamo(self): 
        return 10
    def __str__(self): 
        return f"📚 {self.titulo} ({self.año}) ({self.edicion} ({self.genero}))"

class Tesis(Pubicacion):
    def __init__(self, titulo, autor, edicion, año, isbn, disponible, grado, universidad):
        super().__init__(titulo, autor, edicion, año, isbn, disponible)
        self.grado = grado
        self.universidad = universidad
    def tiempo_prestamo(self):
        return 60
    def __str__(self):
        return f"La tesis elaborada por {self.autor} en el año {self.año} en su {self.edicion} edición con el tema {self.titulo}\nPara la obtención del grado {self.grado} en la institución {self.universidad} fue aprobada"

class Revista(Pubicacion):
    def __init__(self, titulo, autor, edicion, año, isbn, disponible, nombre_revista, editorial):
        super().__init__(titulo, autor, edicion, año, isbn, disponible)
        self.nombre_revista = nombre_revista
        self.editorial = editorial
    def tiempo_prestamo(self):
        return 1
    def __str__(self):
        return f"El artículo {self.titulo} elaborado por {self.autor} en el año {self.año}.\nFue publicado en la revista {self.nombre_revista} de la editoral {self.editorial}"

print("Clase: Libro")
Libro1=Libro("It","Stephen King","Tercera edición",2020,"1",True,"Terror","Español")
print(Libro1)
print("\n")

print("-"*50)
print("Clase: Tesis")
Tesis1 = Tesis("Programación de objetos","Augusto Lorenzo Gassós","Primera edición",2026,"2",True,"Diplomado","Univerdidad Anahuac")
print(Tesis1)
print("\n")

print("-"*50)
print("Clase: Revista")
Revista1 = Revista("Los pilares del poliformismo en python","René","Única edición",2026,"3",True,"Ciencia y tecnología","Porrua")
print(Revista1)
print("\n")

print("-"*50)
print("Clase: Socio y préstamo")
Socio1 = Socio("Augusto","LOGA661005HVZRSG02","augsuto@gmail.com")
Socio2 = Socio("Juan Manuel","LOGJ680914HVZ","augsuto@gmail.com")
Prestamo1 = Prestamo(Socio1,Revista1)
print(Prestamo1)
print("\n")

print("-"*50)
print("Clase: Socio y préstamo (Status de la devolución)")
print(Prestamo1._devuelto)
Prestamo1.devolver()
print(Prestamo1)
print(Prestamo1._devuelto)
print("\n")

print("-"*50)
print("Clase: Bibloteca (agregar socios y reporte de socios)")
datos_biblioteca  = Biblioteca("La rueca de gandhi")
datos_biblioteca.agregar_socio(Socio1)
datos_biblioteca.agregar_socio(Socio2)
for item_socio in datos_biblioteca.reporte_socios():
    print(f"Nombre del socio: {item_socio.nombre} en la biblioteca {datos_biblioteca.nombre}")
print("\n")

print("-"*50)
print("Clase: Bibloteca (agregar publicaciones y reporte de publicaciones)")
datos_biblioteca.agregar_publicacion(Libro1)
datos_biblioteca.agregar_publicacion(Tesis1)
datos_biblioteca.agregar_publicacion(Revista1)
print(f"Biblioteca: {datos_biblioteca.nombre}")
for item_pub in datos_biblioteca.reporte_publicaciones():
    print(f"Título: {item_pub.titulo} - Autor: {item_pub.autor}")
print("\n")

print("-"*50)
print("Funciones mejoradas")
datos_biblioteca.realizar_prestamo("LOGA661005HVZRSG02","1")
datos_biblioteca.realizar_prestamo("LOGJ680914HVZ","2")
datos_biblioteca.realizar_prestamo("LOGA661005HVZRSG02","3")
print("-"*50)

print("-"*50)
print("Clase: Socio (histórico de préstamos)")
print(f"Socio: {Socio1.nombre}")
for item_prestamo_socio in Socio1.reporte_prestamos():
    print(item_prestamo_socio)
    print("\n")
print(f"Socio: {Socio2.nombre}")
for item_prestamo_socio in Socio2.reporte_prestamos():
    print(item_prestamo_socio)
    print("\n")

print("-"*50)
print("Clase: Biblioteca (histórico de préstamos)")
print("Biblioteca: {datos_biblioteca.nombre}")
for item_prestamo_biblioteca in datos_biblioteca.reporte_prestamos():
    print(item_prestamo_biblioteca)
    print("\n")


print("-"*50)
print("Clase: Publicación (antes de devolver un título)")
print(f"Biblioteca: {datos_biblioteca.nombre}")
for item_pub in datos_biblioteca.reporte_publicaciones():
    print(f"Título: {item_pub.titulo} - Autor: {item_pub.autor} - Disponible: {item_pub._disponible}")
print("\n")

datos_biblioteca.devolver_prestamo(datos_biblioteca.reporte_prestamos()[2])
print("-"*50)
print("Clase: Préstamo (histórico de préstamos después de devolver un título)")
for item_prestamo_socio in datos_biblioteca.reporte_prestamos():
    print(f"Préstamo devuelto: {item_prestamo_socio._devuelto}")
print("\n")

print("-"*50)
print("Clase: Publicación (después de devolver un título)")
print(f"Biblioteca: {datos_biblioteca.nombre}")
for item_pub in datos_biblioteca.reporte_publicaciones():
    print(f"Título: {item_pub.titulo} - Autor: {item_pub.autor} - Disponible: {item_pub._disponible}")
print("\n")


"""
datos_biblioteca.devolver_prestamo(datos_biblioteca.reporte_prestamos()[2])
prestamo_actualizado = datos_biblioteca.reporte_prestamos()[2]
print(prestamo_actualizado._devuelto)
"""