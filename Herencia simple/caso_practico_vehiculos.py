# CLASE PADRE
class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.encendido = False
    
    def encender(self):
        if not self.encendido:
            self.encendido = True
            return f"{self.marca} {self.modelo} encendido"
        return "Ya estaba encendido"
    
    def descripcion(self):
        return f"{self.marca} {self.modelo} ({self.año})"

# CLASE HIJA
class Auto(Vehiculo):
    def __init__(self, marca, modelo, año, puertas):
        super().__init__(marca, modelo, año)
        self.puertas = puertas
    
    def abrir_cajuela(self):
        return "Cajuela abierta"

class motocicleta(Vehiculo):
    def __init__(self, marca, modelo, año, cilindraje):
        super().__init__(marca, modelo, año)
        self.cilindraje = cilindraje

    def descripcion(self):
        return f"{self.marca} {self.modelo} ({self.año}) {self.cilindraje}"

class camion(Vehiculo):
    def __init__(self, marca, modelo, año, capacidad_carga):
        super().__init__(marca, modelo, año)
        self.capacidad_carga = capacidad_carga

    def cargar(self, peso_cargado):
        if peso_cargado > self.capacidad_carga:
            return "Capacidad excedicda"
        else:
            return "Capacidad aceptada"

# CLASE HIJA 2
class Motocicleta(Vehiculo):
    """Motocicleta hereda de Vehiculo"""

    def __init__(self, marca, modelo, año, cilindrada):
        super().__init__(marca, modelo, año)
        self.cilindrada = cilindrada

    def hacer_caballito(self):
        """Método específico de Motocicleta"""
        if self.encendido:
            return "¡Haciendo caballito!"
        return "Primero enciende la moto"

# --- Uso del código ---

auto = Auto("Toyota", "Corolla", 2023, 4)
moto = Motocicleta("Yamaha", "R1", 2024, 1000)

print("=== AUTO ===")
print(auto.descripcion())    # Método heredado
print(auto.encender())       # Método heredado
print(auto.abrir_cajuela())  # Método propio
print(f"Puertas: {auto.puertas}\n")

print("=== MOTOCICLETA ===")
print(moto.descripcion())       # Método heredado
print(moto.hacer_caballito())   # No está encendida
print(moto.encender())          # Método heredado
print(moto.hacer_caballito())   # Ahora sí
print(f"Cilindrada: {moto.cilindrada}cc")

"""
#Uso de la sublase camión
camion1 = camion("Mercedez Benz","Camkión de carga",2024,3)
print(camion1.cargar(3))


# Uso
auto = Auto("Toyota", "Corolla", 2023, 4)
print(auto.descripcion())   # Método heredado
print(auto.abrir_cajuela()) # Método propio

#Uso de motocileta
moto = motocicleta("Honda","Indian",2000,"1.5 cc")
print(moto.descripcion())   # Método heredado

Atributos heredados:
    marca
    modelo
    año
    encendido
Atributos nuevos:
   puertas 

Auto agrega el método abrir_cajuela

Se agregó l clase motiocicleta con un atributo para el cilinfraje. Se sobreescribio el método "descrpcion" para que regresara el cilkinfraje

"""