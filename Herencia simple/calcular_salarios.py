class Empleado:
    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.salario_base = salario_base
    
    def calcular_salario(self):
        return self.salario_base
    
    def presentarse(self):
        return f"Empleado: {self.nombre}"

class Gerente(Empleado):
    def __init__(self, nombre, salario_base, departamento):
        super().__init__(nombre, salario_base)
        self.departamento = departamento
        self.bono = 10000
    
    def calcular_salario(self):
        # Sobrescribe para añadir bono
        salario_empleado = super().calcular_salario()
        return salario_empleado + self.bono
    
    def presentarse(self):
        # Sobrescribe presentación
        presentacion_base = super().presentarse()
        return f"{presentacion_base}, Gerente de {self.departamento}"

class Desarrollador(Empleado):
    def __init__(self, nombre, salario_base, lenguaje):
        super().__init__(nombre, salario_base)
        self.lenguaje = lenguaje
        self.proyectos_completados = 0
    
    def calcular_salario(self):
        # Bono por proyectos
        salario_base = super().calcular_salario()
        bono_proyectos = self.proyectos_completados * 2000
        return salario_base + bono_proyectos
    
datos_gerente = Gerente("Augusto Lorenzo",45000,"Desarrollo de sistemas")
print(datos_gerente.presentarse())
print(datos_gerente.calcular_salario())

datos_desarrollador = Desarrollador("Juan Manuel Loenzo",37000,"Angular")
print(datos_desarrollador.presentarse())
print(datos_desarrollador.calcular_salario())
