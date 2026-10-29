capital = float(input("Introduzca la cantidad a invertir: "))
interes = float(input("Introduzca el interés anual (en tanto por uno, ej: 0.05): "))
anos = int(input("Introduzca el número de años que quiere que dure: "))

for i in range(1, anos + 1):
    capital = capital + (capital * interes)
    
    print(f"Año {i}: {capital:.2f} €")

print("Año", i, ":", capital)