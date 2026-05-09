class Empleado:
    def calcular_salario(self):
        return 30000  # Salario base

class Gerente(Empleado):
    def calcular_salario(self):
        # Sobrescribimos completamente
        salario_base = super().calcular_salario()

        bono = 10000
        importeImpuesto = .15

        return (salario_base + bono) - salario_base*importeImpuesto

class AnalistaDatos(Empleado):
    def calcular_salario(self):

        salario_base = 27000
        importeImpuesto = .10

        return salario_base - (salario_base*importeImpuesto)

datos_gerente = Gerente()
print(datos_gerente.calcular_salario())

datos_analista = AnalistaDatos()
print(datos_analista.calcular_salario())
