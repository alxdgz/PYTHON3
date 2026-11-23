"""
Ejercicio 5: Múltiplos
Escribe un programa que pida un número entero positivo n y
muestre todos los números del 1 al n que sean múltiplos de 3 o de 5,
separados por espacios. Al final, muestra cuántos hay y cuánto suman.
"""

n = int(input("Introduzca un número entero positivo: "))

if n <= 0:
    print("No valido")
else:
    sumanum = 0
    sumamul = 0
    for i in range(1, n+1, 1):
        if i % 3 == 0 or i % 5 == 0:
            print(i, end=" ")
            sumanum = sumanum + i
            sumamul = sumamul + 1
    print()
    print("Hay", sumamul ,"multiplos")
    print("Suman: ", sumanum)