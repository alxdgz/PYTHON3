"""
Escribe un programa que pida números enteros al usuario uno a uno, hasta que escriba 0. Cuando termine, muestra:

cuántos números ha introducido (sin contar el 0),
cuántos eran pares y cuántos impares,
la suma de todos,
el mayor de todos.
"""

num = int(input("Introduce un numero (0 si quieres terminar): "))

contadornum = 0
contadorpar = 0
contadorimpar = 0
sumanum = 0
maxnum = num

while num != 0:
    contadornum = contadornum + 1
    if num % 2 == 0:
        contadorpar = contadorpar + 1
    else:
        contadorimpar = contadorimpar + 1
    sumanum = sumanum + num
    if num > maxnum:
        maxnum = num

    num = int(input("Introduce un numero (0 si quieres terminar): "))


if contadornum == 0:
    print ("No has introducido ningun numero")
else:
    print ("Has introducido", contadornum , "numeros")
    print ("Pares:", contadorpar)
    print ("Impares:", contadorimpar)
    print ("Suma:", sumanum)
    print ("El mayor numero es:", maxnum)
    