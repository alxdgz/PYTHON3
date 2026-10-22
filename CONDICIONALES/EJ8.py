rendim = float(input("Introduzca su puntuacion de rendimiento: "))

if rendim == 0.0:
    nivel = "inaceptable"
elif rendim == 0.4:
    nivel = "aceptable"
elif rendim >= 0.6:
    nivel = "meritorio"
else:
    nivel = "no válido"

sueldo = 2400 * rendim

if nivel != "no válido":
    print(f"Su nivel de rendimiento es: {nivel}")
    print(f"Su sueldo es: {sueldo}€")
else:
    print("La puntuación introducida no corresponde a ningún nivel válido.")