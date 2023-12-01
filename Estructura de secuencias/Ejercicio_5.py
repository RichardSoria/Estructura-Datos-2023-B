
# Ejercicio 5 #

print("Programa que permite conocer la nota final en la materia de Algoritmos\n")

print("La ponderación de las notas es:\n")
print("Promdio de sus tres calificaciones parciales (55%)")
print("Calificación Exámen Final (30%)")
print("Calificación Trabajo Final (15%)\n")
print("Recordar las notas deben ser valores positivos y hasta el 10\n")

nota_1 = float(input("Ingrese su nota del primer parcial:\n"))
nota_2 = float(input("Ingrese su nota del segundo parcial:\n"))
nota_3 = float(input("Ingrese su nota del tercer parcial:\n"))
examen = float(input("Ingrese la nota de su exámen final:\n"))
trabajo = float(input("Ingrese la nota de su trabajo final:\n"))

promedio = round(((nota_1+nota_2+nota_3)/3)*0.55,2)
examen = round(examen*0.3,2)
trabajo = round(trabajo*0.15,2)

total_nota = promedio+examen+trabajo

print("Su promedio de las 3 notas parciales (55%) es:\n",promedio)
print("Su nota del exámen final (30%) es:\n",examen)
print("Su nota del trabajo final (15%) es:\n",trabajo)
print("Su nota final (100%) es:\n",total_nota)

print("\nRichard Soria")