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

Tarea: corregir para que carge más de un dato y los muestre en pantalla

Primer dato: Cadena de  nombre contiene nombre y apellido separado por eun espacio en blanco
Segundo dato: Edad o año de nacimiento

Mostrar en pantalla en formato de columna: Nomnbre, apellido y edad

"""
import datetime

class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    @classmethod
    def desde_api(cls, diccionario):
        """
        Constructor alternativo que 'mapea' las llaves de un diccionario
        hacia los atributos de nuestra clase.
        """
        # 1. Separar el nombre_completo en nombre y apellido
        nombre_separado = diccionario['info_personal']['nombre_completo'].split(" ")
        nombre = nombre_separado[0]
        apellido = nombre_separado[1]
        # 2. Calculamos la edad (Estamos en 2026)
        anio_actual = datetime.date.today().year
        if diccionario['info_personal']['año_nacimiento']>=1800 and diccionario['info_personal']['año_nacimiento']<=anio_actual:
            edad_calculada = anio_actual - diccionario['info_personal']['año_nacimiento']
        elif diccionario['info_personal']['año_nacimiento']>100:
            edad_calculada = "fuera de rango"
        else:
            edad_calculada = diccionario['info_personal']['año_nacimiento']
        
        # 3. Retornamos la instancia de Persona ya limpia
        return cls(nombre, apellido, edad_calculada)

    def __repr__(self):
        return f"Persona(nombre='{self.nombre}', apellido = '{self.nombre}', edad={self.edad})"

# --- USO PRÁCTICO ---

# 1. Los datos crudos de la "API"
datos_sucios = [
    {
        "info_personal": {"nombre_completo": "Augusto Lorenzo", "año_nacimiento": 1966}
    },
    {
        "info_personal": {"nombre_completo": "Juan Lorenzo", "año_nacimiento": 1968}
    },
    {
        "info_personal": {"nombre_completo": "Mónica Lorenzo", "año_nacimiento": 1964}
    },
    {
        "info_personal": {"nombre_completo": "Daniela Lorenzo", "año_nacimiento": 1992}
    },
    {
        "info_personal": {"nombre_completo": "Judith Lorenzo", "año_nacimiento": 1990}
    },
    {
        "info_personal": {"nombre_completo": "Gloria Gassós", "año_nacimiento": 150}
    },
]

Personas = [Persona.desde_api(DatosPersona) for DatosPersona in datos_sucios]
for item_persona in Personas:
    print(f'Nombre: {item_persona.nombre}')
    print(f'Apellido: {item_persona.apellido}')
    print(f'Edad: {item_persona.edad}')
    print("\n")
    
