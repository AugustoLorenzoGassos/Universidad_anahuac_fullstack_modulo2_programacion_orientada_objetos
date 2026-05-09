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

def realizar_reporte(conector,consulta):
    print(conector.conectar())
    print(conector.ejecutar_consulta(consulta))

db_sql = SQLServerConnector()
db_mysql = MySQLConnector()
db_mongo = MongoDBConnector()

realizar_reporte(db_mysql,"Select * from ventas")