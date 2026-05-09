class Playlist:
    def __init__(self, nombre, canciones):
        self.nombre = nombre
        self.canciones = canciones  # Esperamos una lista de strings

    # 1. __len__: Define qué pasa cuando haces len(objeto)
    def __len__(self):
        """Devuelve la cantidad de canciones en la playlist."""
        return len(self.canciones)

    # 2. __eq__: Define el comportamiento del operador '==' (Equality)
    def __eq__(self, otro):
        """Dos playlists son iguales si tienen las mismas canciones."""
        if not isinstance(otro, Playlist):
            return False
        return self.canciones == otro.canciones

    # 3. __lt__: Define el comportamiento del operador '<' (Less Than)
    def __lt__(self, otro):
        """Permite comparar si una playlist es 'menor' que otra según su tamaño."""
        return len(self) < len(otro)

    # 4. __add__: Define qué pasa cuando usas el símbolo '+'
    def __add__(self, otro):
        """Combina dos playlists en una nueva."""
        nuevo_nombre = f"{self.nombre} & {otro.nombre}"
        nuevas_canciones = self.canciones + otro.otro_atributo_canciones(otro)
        return Playlist(nuevo_nombre, nuevas_canciones)

    # Método auxiliar para el ejemplo de __add__
    def otro_atributo_canciones(self, objeto):
        return objeto.canciones

    # 5. __getitem__: Permite usar corchetes [índice] como si fuera una lista
    def __getitem__(self, indice):
        """Permite acceder a una canción específica: playlist[0]"""
        return self.canciones[indice]

    def __repr__(self):
        return f"Playlist('{self.nombre}', {self.canciones})"

# --- PRUEBAS DEL PROGRAMA ---

rock = Playlist("Rock 80s", ["Back in Black", "Jump"])
pop = Playlist("Pop 90s", ["Toxic", "Believe", "Vogue", "Persiana americana","Tire tu pañuelo al río","Don corazón"])

# Uso de __len__
"""
print(f"Canciones en pop: {len(pop)}") # Salida: 1
print(f"Canciones en Rock: {len(rock)}") # Salida: 2

# Uso de __getitem__
print(f"La primera canción de Pop es: {pop[0]}") # Salida: Toxic

# Uso de __lt__ (Comparación)
if rock < pop:
    print(f"La playlist '{pop.nombre}' es más larga.")

# Uso de __add__
mega_mix = rock + pop
print(f"Nueva playlist: {mega_mix.nombre}") 
print(f"Total canciones: {len(mega_mix)}") # Salida: 5

# Uso de __eq__
playlist_copia = Playlist("Rock 80s", ["Back in Black", "Jump"])
print(f"¿Son iguales? {rock == playlist_copia}") # Salida: True
"""
#a = [1,1,2,3,5,8,13]
#print(a[1:5:2])

print(f"Canciones en pop: {len(pop)}") # Salida: 1
print(f"El tercer elemen to de la lista pop es {pop[2]}")
print(f"El último elemento de la lista pop es {pop[-1]}")
print(f"Elementos de la lista pop tomados entre el elemento 2 al 5 con salto en 1: {pop[2:5:1]}")

nueva_musica=[]
nueva_musica = pop + rock
print(nueva_musica)
print(nueva_musica[::-1])
