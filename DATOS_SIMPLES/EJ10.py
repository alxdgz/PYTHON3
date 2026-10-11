peso_payaso = 112
peso_muneca = 75
payasos_vendidos = int(input("Número de payasos vendidos: "))
munecas_vendidas = int(input("Número de muñecas vendidas: "))
peso_total = (peso_payaso * payasos_vendidos) + (peso_muneca * munecas_vendidas)
print("El peso total del paquete que será enviado es:", peso_total, "g")