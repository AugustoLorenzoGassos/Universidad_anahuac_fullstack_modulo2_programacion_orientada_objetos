class CuentaBancaria:
    def __init__(self, numero_cuenta,saldo):
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo

    def informacion_cuenta(self):
        return f"Número de cuenta: {self.numero_cuenta}. Saldo actual: $ {self.saldo}"

class CuentaAhorro(CuentaBancaria):
    def __init__(self, numero_cuenta, saldo, porcentaje_interes):
        super().__init__(numero_cuenta, saldo)
        self.porcentaje_interes = porcentaje_interes

    def informacion_cuenta(self):
        return f"Número de cuenta: {self.numero_cuenta}. Saldo actual: $ {self.saldo}. Porcentaje de intereses: {self.porcentaje_interes}\nSaldo actual: ${self.saldo + (self.saldo*self.porcentaje_interes)}"

class CuentaCorriente(CuentaBancaria):
    def __init__(self, numero_cuenta, saldo, saldo_usado):
        super().__init__(numero_cuenta, saldo)
        self.saldo_usado = saldo_usado

    def informacion_cuenta(self):
        if self.saldo_usado < self.saldo:
            return f"EL saldo disponible es de $ {self.saldo-self.saldo_usado}"
        else:
            return f"Su cuenta presenta un sobre giro de $ {self.saldo_usado-self.saldo}"
    
print("Cuenta base")
datos_cuenta = CuentaBancaria("45000120111112222233",150000)
print(datos_cuenta.informacion_cuenta())

print("\nCuenta de ahorros")
datos_cuenta_ahorro = CuentaAhorro("45000120111112222233",87000,.10)
print(datos_cuenta_ahorro.informacion_cuenta())

print("\nCuenta de corriente con sobregiro")
datos_cuenta_corriente = CuentaCorriente("45000120111112222233",87000,95000)
print(datos_cuenta_corriente.informacion_cuenta())
