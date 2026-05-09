class Fuerza_sobre_humana:
    def usar_fuerza(self):
        return f"{self.alias} ha levantado un edificio de 20 pisos"

class Poder_vuelo:
    def volar(self):
        return f"{self.alias} ha volado por encima de los 300 metros"

class Poder_invisibilidad:
    def invisible(self):
        return f"{self.alias} ha logrado no ser vista"

class poder_programacion_objetos:
    def master_pfrogramacion(self):
        return f"{self.alias} ha logrado dominae la programacion de objetos"

class Superman(heroe, Fuerza_sobre_humana, Poder_vuelo):
    def __init__(self, nombre, alias):
        super().__init__(nombre, alias)

class Mujerinvisible(heroe, Poder_invisibilidad):
    def __init__(self, nombre, alias):
        super().__init__(nombre, alias)

class heroe_personal(heroe, poder_programacion_objetos):
    def __init__(self, nombre, alias):
        super().__init__(nombre, alias)

#Definir heroes

heroe_1 = Superman("Clark Kent","Superman")

#heroe_2 = Mujerinvisible("Invisible","Mujer Invisible",Poder_invisibilidad)
#heroe_3 = heroe_personal("Augusto", "SuperProgramador", poder_programacion_objetos)

"""
print(f"El supergeror {heroe_1.alias} tiene los siguientes superpoderes :")
for i in range(1,len(heroe_1.__mro__)):
    print(heroe_1.__mro__[i])
"""
