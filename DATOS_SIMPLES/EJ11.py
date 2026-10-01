inversion = float(input("Introduce la cantidad de dinero depositada: "))
interes = 0.04

balance_ano1 = inversion * (1 + interes)
print("Ahorros tras el primer año: " + str(round(balance_ano1, 2)))

balance_ano2 = balance_ano1 * (1 + interes)
print("Ahorros tras el segundo año: " + str(round(balance_ano2, 2)))

balance_ano3 = balance_ano2 * (1 + interes)
print("Ahorros tras el tercer año: " + str(round(balance_ano3, 2)))