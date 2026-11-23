"""
Escribe un programa que pida al usuario tres notas (pueden tener decimales)
 y muestre la media redondeada a 2 decimales y su calificación:
"""
notas = input("escriba sus 3 notas: ")
nota = notas.split(" ")
nota1 = float(nota[0])
nota2 = float(nota[1])
nota3 = float(nota[2])
print(f"Nota 1 {nota1:4.2f}")
print(f"Nota 2 {nota2:4.2f}")
print(f"Nota 3 {nota3:4.2f}")

if nota1 > 10 or nota1 < 0 or nota2 > 10 or nota2 < 0 or nota3 > 10 or nota3 < 0:
    print("No valido")
else:
    media = (nota1 + nota2 + nota3) / 3
    print("Media:", media)
    if media < 5:
        print("Suspenso")
    elif media < 7:
        print("Aprobado")
    elif media < 9:
        print("Notable")
    else:
        print("Sobresaliente")

