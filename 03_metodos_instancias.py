class cuenta_bancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.saldo_inicial = saldo_inicial
    
    def depositar(self, cantidad):
        if cantidad>0:
            self.saldo += cantidad
            return True
        else:
            return False
    
    def consultar_saldo(self):
        #Devolver información
        return self.saldo_inicial

