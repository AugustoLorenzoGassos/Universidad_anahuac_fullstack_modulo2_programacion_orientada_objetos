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