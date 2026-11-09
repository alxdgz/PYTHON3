num = int(input("Introducza un número: "))

es_primo = True

for i in range(2, num, 1):
    if num % i == 0:
        es_primo = False  
        break             

if es_primo:
    print("El número es primo")
else:
    print("No es primo")