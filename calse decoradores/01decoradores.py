def mi_decorador(func):
    def envoltura():
        #función
        print("1.- entro antes a la función")
        #func()
        print("3.- despu´s de salir de la función")

    return envoltura

@mi_decorador
def saludar():
    print("entro al decorador. Saludos")

saludar()

