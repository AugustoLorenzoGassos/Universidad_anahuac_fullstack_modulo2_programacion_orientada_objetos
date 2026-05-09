class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def presentarse(self):
        return f"Hola, soy {self.nombre}"

class Estudiante(Persona):
    def __init__(self, nombre, edad, matricula):
        super().__init__(nombre, edad)
        self.matricula = matricula
    
    def presentarse(self):
        return f"Hola, soy {self.nombre}, estudiante matrícula {self.matricula} y tengo {self.edad} años de edad"
    
datos_estudiante = Estudiante("Augusto Lorenzo", 59, "12345678")
print(datos_estudiante.presentarse())
