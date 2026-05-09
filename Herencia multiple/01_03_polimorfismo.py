import time

class SQLServerConnector:
    def conectar(self):
        return "Conectando a SQL Server... (Usando Trusted_Connection=yes)"
    
    def ejecutar_consulta(self, query):
        return f"Resultado de SQL Server para: '{query}'"

class MySQLConnector:
    def conectar(self):
        return "Conectando a MySQL... (Usando host:localhost, port:3306)"
    
    def ejecutar_consulta(self, query):
        return f"Resultado de MySQL para: '{query}'"

class MongoDBConnector:
    def conectar(self):
        return "Conectando a MongoDB... (Usando protocolo mongodb+srv://)"
    
    def ejecutar_consulta(self, query):
        return f"Resultado de NoSQL (MongoDB) para: '{query}'"

class Mockconnector:
    def conectar(self):
        return "Conectando a base de datos bo definida... (Usando protocolo mock://)"
    
    def ejecutar_consulta(self, query):
        print(f"Clave del artículo")
        for i in range(1,100):
            print(f"Laptop_{i}")
            time.sleep(.5)
        return f"Resultado de Mpck para: '{query}'\nSe regresaron {i} artículos"


# --- LA FUNCIÓN POLIMÓRFICA ---
def realizar_reporte(conector, consulta):
    """
    A esta función no le importa qué base de datos sea, 
    mientras tenga los métodos 'conectar' y 'ejecutar_consulta'.
    """
    print(conector.conectar())
    datos = conector.ejecutar_consulta(consulta)
    print(f"PROCESANDO: {datos}")
    print("Reporte generado con éxito.\n")

# --- PRUEBAS EN CLASE ---

# El alumno puede elegir cualquier conector
db_sql = SQLServerConnector()
db_mysql = MySQLConnector()
db_mongo = MongoDBConnector()
db_mock = Mockconnector()

print("=== REPORTE DE VENTAS (SQL) ===")
realizar_reporte(db_sql, "SELECT * FROM Ventas")

print("=== REPORTE DE USUARIOS (MySQL) ===")
realizar_reporte(db_mysql, "SELECT * FROM Usuarios")

print("=== REPORTE DE LOGS (MongoDB) ===")
realizar_reporte(db_mongo, "db.logs.find()")

print("=== REPORTE DE LOGS (Mock) ===")
realizar_reporte(db_mock, "Select * from articulos")
