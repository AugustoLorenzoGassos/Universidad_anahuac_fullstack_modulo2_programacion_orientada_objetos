class ProcesadorPayPal:
    def procesar_pago(self, cantidad, cuenta):
        print(f"💳 Procesando ${cantidad:.2f} vía PayPal")
        return {'exito': True, 'metodo': 'PayPal'}

class ProcesadorStripe:
    def procesar_pago(self, cantidad, cuenta):
        print(f"💳 Procesando ${cantidad:.2f} vía Stripe")
        return {'exito': True, 'metodo': 'Stripe'}

class ProcesadorTransferencia:
    def procesar_pago(self, cantidad, cuenta):
        print(f"🏦 Procesando ${cantidad:.2f} vía Transferencia")
        return {'exito': True, 'metodo': 'Transferencia'}

class Pago_efectivo:
    def procesar_pago(self, cantidad,cuenta):
        print(f"🏦 Procesando ${cantidad:.2f} en efectivo")
        return {'exito': True, 'metodo': 'Pago_efectivo'}

# Función polimórfica - Duck Typing puro
def realizar_cobro(procesador, cantidad, cuenta):
    resultado = procesador.procesar_pago(cantidad, cuenta)
    if resultado['exito']:
        print(f"✅ Pago exitoso vía {resultado['metodo']}")
    return resultado

# La misma función funciona con todos
realizar_cobro(Pago_efectivo(),3100,'')
realizar_cobro(ProcesadorPayPal(), 1500.00, "ana@example.com")
realizar_cobro(ProcesadorStripe(), 2300.00, "tok_abc123")
realizar_cobro(ProcesadorTransferencia(), 5000.00, "CLABE123")