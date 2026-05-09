class Empleado:
    def calcular_salario(self, bruto):
        # El padre aplica un 10% de impuesto general
        return bruto*.9

class Vendedor(Empleado):
    def calcular_salario(self, bruto):
        # TODO: Usar super() para obtener el salario con impuesto 
        # y sumar $2000 de comisión.
        salario_base = super().calcular_salario()

        return (salario_base*.90)+2000


        pass

class Director(Empleado):
    def calcular_salario(self, bruto):
        # TODO: Calcular el salario restando el 20% (bruto * 0.8)
        # y sumar $5000 de bono.
        pass


######Datos de prueba

monto_bruto = 10000

# Instancias
emp = Empleado()
ven = Vendedor()
dir = Director()

print(f"Empleado común neto: ${emp.calcular_salario(monto_bruto)}") # Debería dar 9000
# print(f"Vendedor neto: ${ven.calcular_salario(monto_bruto)}")      # Debería dar 11000
# print(f"Director neto: ${dir.calcular_salario(monto_bruto)}")      # Debería dar 13000

