n = int(input("Introduzca la longitd del lado del cuadrado: "))

if n >= 2:
    for i in range (1, n + 1, 1):
        for j in range (n):
            if i == 1 or j == 1 or i == n or j == n:
                print ("*", end=" ")
            else:
                print (" ", end=" ") 
        print ()
else:
    print ("Introduzca un numero mayor o igual que 2")          