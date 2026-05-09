"""
Ejercicio 1: Tu Primer Polimorfismo
Objetivo: Implementar una función polimórfica.
Descripción: Crea clases ReproductorMP3, ReproductorWAV y ReproductorFLAC. 
Cada una debe tener un método reproducir() que imprima un mensaje específico. 
Crea una función reproducir_playlist(lista) que itere y reproduzca cada uno.
"""

class ReproducgtorMP3:
    def reproducir(slef):
        return "Reproducir MP3"

class ReproductorWAV:
    def reproducir(slef):
        return "Reproducir WAV"
    
class ReproductorFLAC:
    def reproducir(slef):
        return "Reproducir FLAC"
    
def reproducir_playlist(reproductor):
    print(reproductor.reproducir())

def reproducir_playlist_lista(lista):
    for item_reproductor in lista:
        reproducir_playlist(item_reproductor)

print("Aplicación del poliformismo individual")
reproducir_playlist(ReproducgtorMP3())
reproducir_playlist(ReproductorWAV())
reproducir_playlist(ReproductorFLAC())
print("\n")

print("Aplicación del poliformismo a través de una lista\n")
lista_reporoductor = [ReproducgtorMP3(),ReproductorWAV(),ReproductorFLAC()]
reproducir_playlist_lista(lista_reporoductor)
