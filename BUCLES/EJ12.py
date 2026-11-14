frase = str(input("Escriba una frase: "))
letra = str(input("Escriba una letra: "))

vecesletra = 0
for i in frase:
    if letra == i:
        vecesletra = vecesletra + 1

print ("La letra", letra, "aparece" , vecesletra , "veces")