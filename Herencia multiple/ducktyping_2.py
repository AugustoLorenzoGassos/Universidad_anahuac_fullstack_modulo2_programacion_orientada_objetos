class Pato:
    def vuela(self): return "El pato vuela"

class Avion:
    def vuela(self): return "El avión vuela"

class Murcielago:
    def vuela(self): return "El murciélago vuela"

class Persona:
    def se_mueve(self): return "Las personas se mueven"

class Vehiculo_terrestre:
    def se_mueve(self): return "Los vehícilos terrestres se mueven"

class Insecto:
    def se_mueve(self): return "Los insectos se mueven"

def despegar(objeto_volador):
    print(objeto_volador.vuela())

def movimiento(objeto_mueve):
    print(objeto_mueve.se_mueve())

movimiento(Persona())
movimiento(Vehiculo_terrestre())
movimiento(Insecto())

despegar(Pato())
despegar(Avion())
despegar(Murcielago())

