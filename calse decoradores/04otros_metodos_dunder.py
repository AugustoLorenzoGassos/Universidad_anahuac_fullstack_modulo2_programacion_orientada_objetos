class play_list:
    def __init__(self, nombre, canciones):
        self.nombre = nombre
        self.canciones = canciones
    
    #len - longitud de un objeto
    def __len__(self):
        return len(self.canciones)
    
    def __getitem__(self, indice):
        return self.canciones[indice]
    
    def __delitem__(self, indice):
        #eliminar una canción de la lista usando la sintaxis del objeto
        #del objecto[indice]

        print(f" Borrando canción de la lista: {self.canciones[indice]}")

        del self.canciones[indice]

    def __repr__(self):
        return f"{play_list}"