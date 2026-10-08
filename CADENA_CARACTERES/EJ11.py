nombre = input("Introduce el nombre del producto: ")
precio = float(input("Introduce el precio del producto: "))
unidades = int(input("Introduce el número de unidades del producto: "))
total = precio * unidades
print(f"El producto {nombre} tiene un precio de {precio:9.2f}, un total de {unidades:3d} unidades y un total de {total:11.2f} €")