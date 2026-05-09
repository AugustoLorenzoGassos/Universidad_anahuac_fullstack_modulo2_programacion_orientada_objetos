class Empleado:
    def calcular_salario(self, bruto):
        # El padre aplica un 10% de impuesto general
        return bruto * 0.9

class Vendedor(Empleado):
    def calcular_salario(self, bruto):
        # TODO: Usar super() para obtener el salario con impuesto 
        # y sumar $2000 de comisión.
        pass

class Director(Empleado):
    def calcular_salario(self, bruto):
        # TODO: Calcular el salario restando el 20% (bruto * 0.8)
        # y sumar $5000 de bono.
        pass

