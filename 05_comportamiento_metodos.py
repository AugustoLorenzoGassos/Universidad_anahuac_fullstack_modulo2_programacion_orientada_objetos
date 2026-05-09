#Comportamiento de metodos

class cuenta_bancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular=titular
        self.saldo_inicial=saldo_inicial
        self.movimientos=0

    def depositar(self, cantidad):
        #incrementar el saldo
        if cantidad > 0:
            self.saldo_inicial += cantidad
            self.movimientos +=1
            print(f"Depósito exitoso: ${cantidad}")
            return True
        else:
            print("Depósito no exitoso")
            return False

    def retirar(self, cantidad):
        #Retirar si hay fondos suficientes
        if cantidad<=0:
            print("Retiro  no se pudo realizar")
            return False
        if cantidad > self.saldo_inicial:
            print(f"Saldo insuficiente: ${self.saldo_inicial}")
            return False
        print(f"Returo exitopso por la cantidad de {cantidad}")
        self.saldo_inicial -= cantidad
        self.movimientos += 1
        return True
    
    def consultar_saldo(self):
        return self.saldo_inicial

    def resumen(self):
        print(f"Titular: {self.titular}")
        print(f"Cantidad de movimientos: {self.movimientos}")
        print(f"Saldo actual: {self.saldo_inicial}")

cuenta1 = cuenta_bancaria("Augusto Lorenzo", 15000)
print(f"Saldo inicial: ${cuenta1.consultar_saldo()}")
cuenta1.depositar(5000)
cuenta1.depositar(2000)
print(f"Saldo actual: ${cuenta1.consultar_saldo()}")
print("\n")
cuenta1.retirar(12000)
print(f"Saldo actual: ${cuenta1.consultar_saldo()}")
print("\n")
cuenta1.resumen()


