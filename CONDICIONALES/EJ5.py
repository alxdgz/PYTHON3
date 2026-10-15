edad = int(input("Introduzca su edad:"))
ingresos = int(input("Introduzca sus ingresos:"))

if edad > 16:
    if ingresos > 1000:
        print ("Usted puede tirbutar")
    else:
        print ("No puedes tributar")
else:
    print ("No puedes tributar")