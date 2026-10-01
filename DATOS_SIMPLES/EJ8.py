n = int(input("Introduce el primer número (dividendo): "))
m = int(input("Introduce el segundo número (divisor): "))
c = n // m
r = n % m
print(str(n) + " entre " + str(m) + " da un cociente " + str(c) + " y un resto " + str(r))