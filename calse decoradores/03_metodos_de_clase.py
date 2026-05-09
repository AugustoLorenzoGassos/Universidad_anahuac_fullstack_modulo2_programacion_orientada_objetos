"""
Constructor Alternativo. Básicamente, le estás dando a tu clase Persona dos formas diferentes de "nacer".
La Lógica del Método: desde_ano_nacimiento
Este método actúa como una fábrica. No necesita que la persona ya exista para funcionar:

Recibe los datos: El nombre y el año en que nació.

Calcula la edad: Importa datetime y resta el año actual (¡estamos en 2026!) menos el año de nacimiento.

Crea la persona: Una vez que tiene la edad calculada, llama a cls (la clase Persona) para fabricar el objeto y devolverlo.

Casos de uso comunes:
- Constructores alternativos
- Factory methods
- Modificar configuración de la clase
"""
class Persona:
    def __init__(self, nombre, apellido_paterno, apellido_materno, edad):
        #Constructor estandar __init__
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.edad = edad
    
    #Este decorador le dice a Python: "Oye, este método no le pertenece a un objeto individual, le pertenece a la Clase entera"
    @classmethod
    #A diferencia de self, que representa al objeto (la persona), cls representa a la Clase
    def desde_ano_nacimiento(cls, nombre, apellido_paterno, apellido_materno, ano_nacimiento):
        """Constructor alternativo
            Lo usamos para poder llamar al constructor original desde adentro del método.
            Al final, cuando ves return cls(nombre, edad), es exactamente lo mismo que escribir return Persona(nombre, edad).
        """
        import datetime
        edad = datetime.date.today().year - ano_nacimiento
        return cls(nombre, apellido_paterno, apellido_materno, edad) # cls es la clase Persona

# Uso normal
persona1 = Persona("Ana","Lorenzo","Gassos", 25)
# Uso del método de clase
persona2 = Persona.desde_ano_nacimiento("Carlos","Lorenzo","Gassos", 1998)

print(f"{persona1.nombre} {persona1.apellido_paterno} {persona1.apellido_materno} tiene {persona1.edad} años.")
print(f"{persona2.nombre} {persona2.apellido_paterno} {persona2.apellido_materno} tiene {persona2.edad} años.")