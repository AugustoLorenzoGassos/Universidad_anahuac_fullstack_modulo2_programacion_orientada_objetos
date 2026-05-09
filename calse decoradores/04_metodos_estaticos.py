"""
Los métodos estáticos son funciones que pertenecen lógicamente a la clase pero no necesitan
acceso ni a la instancia ( self ) ni a la clase ( cls ).

¿Qué es un @staticmethod?
Es un método que vive dentro de una clase por orden y organización, pero que no necesita saber nada de la clase (cls) ni de la instancia (self).

Es como una función normal y corriente, pero que guardas dentro de una clase porque tiene sentido temático que esté ahí.

Casos de uso:
- Funciones de utilidad relacionadas con la clase
- Validaciones que no dependen del estado del objeto
- Organizar código lógicamente
"""

class Utilidades:
    @staticmethod
    def es_email_valido(email):
        """Valida formato de email - no necesita self ni cls
            Lógica: Comprueba si existe un @ y si, después de ese @, hay al menos un punto . (para asegurar que hay un dominio como .com).

            Independencia: Para validar un correo, no necesitas saber el nombre de una persona ni cuántas personas hay creadas. Solo necesitas el texto del correo. Por eso es estático.  
        """
        return "@" in email and "." in email.split("@")[1]
    
    @staticmethod
    def formatear_precio(precio):
        """Formatea un precio - función de utilidad
            Lógica: Toma un número y lo convierte en un string bonito.
            :,: Añade comas para los miles (ej. 15,000).
            .2f: Asegura que siempre haya exactamente 2 decimales.
            Utilidad: Es una función de diseño. No depende de ningún "estado" de la aplicación.
        """
        return f"${precio:,.2f}"
    
# Uso sin crear instancia
print(Utilidades.es_email_valido("usuario@example.com")) # True
print(Utilidades.formatear_precio(15000.5)) # $15,000.50

""""
¿Por qué usar clases para esto? (El concepto de Namespace)
Podrías tener estas funciones sueltas en tu archivo, pero al ponerlas dentro de class Utilidades:

Evitas colisiones de nombres: Puedes tener otra función llamada formatear_precio en otra parte de tu código sin que choquen.

Legibilidad: Cuando alguien lee Utilidades.es_email_valido(), sabe exactamente que esa función es una herramienta de apoyo.

Sin instancias: Como ves en los print, no hace falta escribir u = Utilidades(). Se llaman directamente desde la clase.
"""