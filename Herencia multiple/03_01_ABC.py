"""
Al usar Clases Base Abstractas (ABC), dejas de 
confiar en la buena voluntad de los programadores 
y estableces un contrato legal. Si alguien intenta 
crear un conector y olvida implementar un método 
obligatorio, Python lanzará un error antes de que el 
programa siquiera empiece a correr.

Implementación con abc.ABC
Aquí tienes el código actualizado. Nota cómo 
importamos ABC y el decorador @abstractmethod.
"""

from abc import ABC, abstractmethod

# 1. Definimos la Clase Base Abstracta (El Contrato)
class BaseDatos(ABC):
    
    @abstractmethod
    def conectar(self):
        """Obligatorio: Lógica para abrir la conexión"""
        pass

    @abstractmethod
    def ejecutar_consulta(self, query):
        """Obligatorio: Lógica para procesar la consulta"""
        pass

# 2. Implementaciones reales (Cumpliendo el contrato)
class SQLServer(BaseDatos):
    def conectar(self):
        return "Conectado a SQL Server."

    def ejecutar_consulta(self, query):
        return f"Resultados SQL: {query}"

class MySQL(BaseDatos):
    def conectar(self):
        return "Conectado a MySQL."

    def ejecutar_consulta(self, query):
        return f"Resultados MySQL: {query}"

# 3. La "clase rebelde" (Esto causará error)
class ConectorIncompleto(BaseDatos):
    def conectar(self):
        return "Yo solo quiero conectar, no consultar."
    # Error: Olvidó implementar 'ejecutar_consulta'

# --- PRUEBAS DE FUNCIONAMIENTO ---

def probar_conexion(db_conector):
    """Función polimórfica que acepta cualquier subclase de BaseDatos"""
    print(f"Probando: {type(db_conector).__name__}")
    print(db_conector.conectar())
    print(db_conector.ejecutar_consulta("SELECT * FROM usuarios"))
    print("-" * 30)

# 1. PRUEBA DE ÉXITO: Instancias de clases que SÍ cumplen el contrato
sql_server = SQLServer()
mysql_db = MySQL()

print(">>> EJECUTANDO PRUEBAS DE ÉXITO <<<\n")
probar_conexion(sql_server)
probar_conexion(mysql_db)


# 2. PRUEBA DE FALLO 1: Intentar instanciar la clase abstracta directamente
print(">>> EJECUTANDO PRUEBAS DE FALLO <<<")
try:
    print("Intentando crear una instancia de 'BaseDatos'...")
    base = BaseDatos() # Esto lanzará un error
except TypeError as e:
    print(f"❌ ERROR LEGAL: {e}")


# 3. PRUEBA DE FALLO 2: Intentar instanciar una clase incompleta
try:
    print("\nIntentando crear una instancia de 'ConectorIncompleto'...")
    rebelde = ConectorIncompleto() # Esto también lanzará error
except TypeError as e:
    print(f"❌ ERROR DE CONTRATO: {e}")