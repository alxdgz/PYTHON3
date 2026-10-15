nombre = input("Introduzca su nombre: ")
primeraletra = nombre[0].upper()
sexo = input("Introduzca si es hombre (H) o mujer (M): ").upper()

if sexo == "M":
    if primeraletra < "M":
        print("Estás en el grupo A")
    else:
        print("Estás en el grupo B")
else:
    if primeraletra > "N":
        print("Estás en el grupo A")
    else:
        print("Estás en el grupo B")