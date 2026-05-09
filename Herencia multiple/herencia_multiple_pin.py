

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial, pin):
        self.titular = titular
        self.__saldo = saldo_inicial
        self.__pin = pin  # Atributo privado
        self.__historial = []

    def __verificar_pin(self, pin_ingresado):
        return self.__pin == pin_ingresado

    def retirar(self, cantidad, pin_ingresado):
        # TODO: Solo permitir el retiro si el PIN es válido Y hay saldo
        if not self.__verificar_pin(pin_ingresado):
            print("PIN incorrecto")
            return False
        if cantidad > self.__saldo:
            print("Sin saldo suficiente")
            return False
        self.__saldo -=cantidad
        return True

    def get_saldo(self):
        return self.__saldo

cuenta = CuentaBancaria("Leonardo Ruiz", 1000, "2026")
print(cuenta.retirar(100, "0000")) # Debería ser False
print(cuenta.retirar(100, "2026")) # Debería ser True
print(cuenta.get_saldo())