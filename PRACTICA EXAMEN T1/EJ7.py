"""
Escribe un programa que pida un número entero n y dibuje este triángulo:

Introduce un número: 4
4 3 2 1
3 2 1
2 1
1
"""

n = int(input("introduce un numero: "))

for i in range(n, 0 , -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()