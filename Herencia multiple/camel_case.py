#Método: elMetodoCamelCase -> el_metodo_camel_case

texto = input("Ingresa una cadena camel case: ")
for caracter in texto:
    if caracter.upper():
        print(caracter)
