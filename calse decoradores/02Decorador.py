"""
Auditar el rendimiento de las funciones por el tie po que tardan en ejecutarse
Se va a ocupar la libreróia time
Decoradosr: de la librerúa func tools
"""

import time
from functools import wraps

def medir_tiempo(func):
    @wraps(func)
    def envoltura(*arg, **kwargs):
        inicio = time.time()
        #ejecurar una función
        resultado = func(*arg, **kwargs)
        #tomar el timepo final
        fin = time.time()
        duracion = fin - inicio
        print(f"La funcion '{func.__name__}' tardó {duracion:.4f} segundos en ejecutarsde")
        return resultado
    return envoltura

@medir_tiempo
def simular_proceso_pesado(n):
    #Simular proceso
    total = sum(range(n))
    time.sleep(1)
    return total

#ejemplo de uso
resultado_final = simular_proceso_pesado(1000000)
print(f"Resultado del cálculo: {resultado_final}")

