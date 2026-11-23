"""
Escribe un programa que pida una palabra y la muestre en forma de escalera,
 añadiendo una letra en cada línea:

Introduce una palabra: python
p
py
pyt
pyth
pytho
python
"""

palabra = str(input("Introduce una palabra: "))

for i in range(len(palabra) + 1):
    print(palabra[0:i])
    


    
    