class coche:
    def __init__(self, marca, modelo, year):
        #Se ejecuta automáticamente al crear el objeto
        self.marca = marca
        self.modelo = modelo
        self.year = year
        self.kilometraje = 0 #Valor por defecto

#crear un objeto 
Mi_coche = coche("Toyoya","Corolla",2025)

#Phyton internamente hace algo como:
#coche.__init__,"Toyota","Corolla",

print(f"Tipo del objeto mi coche: {type(Mi_coche)}")
print(f"Id mi coche: {id(Mi_coche)}\n")
