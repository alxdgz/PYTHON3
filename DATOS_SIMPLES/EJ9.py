cantidad = float(input("¿Cantidad a invertir?: "))
interes = float(input("¿Interés anual (en porcentaje)?: "))
anios = int(input("¿Número de años?: "))
capital = cantidad * (1 + interes / 100) ** anios
print("El capital obtenido en la inversión es: " + str(round(capital, 2)))