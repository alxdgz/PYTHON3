"""
Ejercicio 2: Análisis de palabras

Escribe un programa que pida al usuario una frase y muestre:

Cada palabra en una línea, con su número de letras al lado.
La palabra más larga de la frase. Si hay empate, la primera que aparezca.
Cuántas palabras tienen más de 4 letras.
La frase con cada palabra invertida, pero manteniendo el orden de las palabras.
"""

frase = input("Escriba una frase: ")
div = frase.split(" ")

maslarga = ""
invertida = ""
cuatroletras = 0
for i in div:
    sep = len(i)
    if sep > len(maslarga):
        maslarga = i
    if sep > 4:
        cuatroletras = cuatroletras + 1
    invertida = invertida + " " + i[::-1]
    print (i, "-", sep)

print ("La palabra mas larga es:", maslarga)
print ("Palabras con mas de 4 letras:", cuatroletras)
print ("Frase invertida:", invertida)