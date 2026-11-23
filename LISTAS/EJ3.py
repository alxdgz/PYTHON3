asignaturas = ['Mates', 'Fisica', 'Quimica', 'Historia', 'Lengua']
notas = []

for asignatura in asignaturas:
    nota = float(input('¿Qué nota has sacado en ' + asignatura + '? '))
    notas.append(nota)

for i in range(len(asignaturas)):
    print('En', asignaturas[i], 'has sacado', notas[i])
    