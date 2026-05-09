"""
# Así se ve la respuesta de una API típica
datos_api = {
    "info_personal": {
        "primer_nombre": "Lucía",
        "apellido": "García"
    },
    "nacimiento": {
        "anio": 1992,
        "pais": "México"
    }
}

Abstracción de la complejidad: El programa principal no tiene que saber que la API tiene una llave llamada info_personal. Solo llama a desde_api y recibe un objeto limpio.

Mantenimiento: Si el día de mañana la API cambia la llave primer_nombre por name, solo tienes que cambiar una línea dentro del método de clase, y el resto de tu programa seguirá funcionando igual.

Encapsulamiento: La lógica de "cómo se calcula la edad" o "cómo se une el nombre y apellido" vive dentro de la clase, donde pertenece.
"""
import datetime

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @classmethod
    def desde_api(cls, diccionario):
        """
        Constructor alternativo que 'mapea' las llaves de un diccionario
        hacia los atributos de nuestra clase.
        """
        # 1. Extraemos el nombre combinando campos anidados
        nombre_completo = f"{diccionario['info_personal']['primer_nombre']} {diccionario['info_personal']['apellido']}"
        
        # 2. Calculamos la edad (Estamos en 2026)
        anio_actual = datetime.date.today().year
        edad_calculada = anio_actual - diccionario['nacimiento']['anio']
        
        # 3. Retornamos la instancia de Persona ya limpia
        return cls(nombre_completo, edad_calculada)

    def __repr__(self):
        return f"Persona(nombre='{self.nombre}', edad={self.edad})"

# --- USO PRÁCTICO ---

# 1. Los datos crudos de la "API"
datos_sucios = [
    {
        "info_personal": {"primer_nombre": "Lucía", "apellido": "García"},
        "nacimiento": {"anio": 1992, "pais": "México"}
    },
    {
        "info_personal": {"primer_nombre": "Augusto", "apellido": "Lorenzo"},
        "nacimiento": {"anio": 1966, "pais": "México"}
    }
]

"""
# 2. Creamos el objeto usando el constructor alternativo
persona_api = Persona.desde_api(datos_sucios)

print(f"Objeto creado: {persona_api}")
print(f"Nombre procesado: {persona_api.nombre}")
print(f"Edad calculada (en 2026): {persona_api.edad}")
"""