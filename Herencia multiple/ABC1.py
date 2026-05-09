from abc import ABC, abstractmethod

"""1. Definir la clase abstracta o contrato"""
class Basededatos(ABC):
    @abstractmethod
    def conectar(self):
        #Esto obliga una conexíon - Obligatorio para la lógica de la conexión
        pass
    @abstractmethod
    def ejecutar_consulta(self,query):
        #Obligatorio para la lógica de la consulta
        pass

"""2. Cumplimiento de los contratos"""
class SQLServerConnector(Basededatos):
    def conectar(self):
        return "Conectando a SQL Server... (Usando Trusted_Connection=yes)"
    
    def ejecutar_consulta(self, query):
        return f"Resultado de SQL Server para: '{query}'"

class MySQLConnector(Basededatos):
    def conectar(self):
        return "Conectando a MySQL... (Usando host:localhost, port:3306)"
    