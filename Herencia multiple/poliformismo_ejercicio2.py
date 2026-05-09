"""
Ejercicio 2: Interfaces Implícitas con ABC
Objetivo: Garantizar contratos con ABC.
Descripción: Crea Vehiculo(ABC) con arrancar() y frenar() abstractos. 
Implementa Coche y Bicicleta. 
Intenta instanciar Vehiculo directamente y observa el error.
"""

from abc import ABC, abstractmethod

class Vehiculo(ABC):
    @abstractmethod
    def arrancar(self):
        pass
    @abstractmethod
    def frenar():
        pass

class Coche(Vehiculo):
    def arrancar(self):
        return "El  coche arranca"
    
    def frenar(self):
        return "el ccoche frena"
    
class Bicicleta(Vehiculo):
    def frenar(self):
        return "la bicicleta frena"

def probar_vehiculo(tipo_vehiculo):
    """Función polimórfica"""
    print(f"Probando: {type(tipo_vehiculo).__name__}")
    print(tipo_vehiculo.arrancar())
    print(tipo_vehiculo.frenar())
    print("=" * 30)

coche = Coche()

"""Prueba con la clase Coche() que esta completa"""
probar_vehiculo(coche)

"""Prueba con la clase Bicicleta() que esta incompleta"""
try:
    bicicleta = Bicicleta()
except TypeError as err:
    print(f"error en la costrucción de la clase Bicicleta(). Error: {err}")
