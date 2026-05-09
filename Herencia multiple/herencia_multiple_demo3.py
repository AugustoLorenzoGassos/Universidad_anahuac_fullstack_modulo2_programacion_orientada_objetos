import datetime

class CuentaBancaria:
    """Cuenta bancaria con saldo protegido"""
    
    def __init__(self, titular, saldo_inicial):
        self.titular = titular  # Público
        self._numero_cuenta = self._generar_numero()  # Protegido
        self.__saldo = saldo_inicial  # Privado (name mangling)
        self.__historial = []  # Privado
            
    def _generar_numero(self):
        """Método protegido: uso interno"""
        import random
        return f"{random.randint(1000, 9999)}-{random.randint(1000, 9999)}"
    
    def depositar(self, cantidad):
        """Método público para depositar"""
        if cantidad > 0:
            self.__saldo += cantidad
            self.__registrar_transaccion(f"Depósito: +${cantidad}")
            return True
        return False
    
    def retirar(self, cantidad):
        """Método público para retirar"""
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            self.__registrar_transaccion(f"Retiro: -${cantidad}")
            return True
        return False
    
    def __registrar_transaccion(self, descripcion):
        """Método privado: solo uso interno"""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.__historial.append(f"[{timestamp}] {descripcion}")
    
    def get_saldo(self):
        """Getter para el saldo"""
        return self.__saldo
    
    def get_historial(self):
        """Getter para el historial"""
        return self.__historial.copy()  # Copia para evitar modificación externa


# --- Ejecución del código ---
mi_cuenta = CuentaBancaria("René Ruiz", 5000)

print(f"Titular: {mi_cuenta.titular}") # Acceso público: OK
print(f"Cuenta: {mi_cuenta._numero_cuenta}") # Acceso protegido: Funciona, pero es mala práctica

# Intentos de transacciones
mi_cuenta.depositar(1500)
mi_cuenta.retirar(2000)

print(f"Saldo actual: ${mi_cuenta.get_saldo()}")

# --- PRUEBA DE SEGURIDAD ---
try:
    print(mi_cuenta.__saldo) # Esto fallará
except AttributeError:
    print("\n❌ Error de seguridad: No puedes acceder al saldo directamente (es privado)")

# Ver el historial
print("\n=== HISTORIAL DE TRANSACCIONES ===")
for movimiento in mi_cuenta.get_historial():
    print(movimiento)
