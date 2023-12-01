
# Ejercicio 6 #

import math

print("Programa que calcula la distancia entre dos puntos en el plano cartesiano\n")

x1 = float(input("Ingrese la abscisa (x) del punto 1:\n"))
y1 = float(input("Ingrese la abscisa (y) del punto 1:\n"))
x2 = float(input("Ingrese la ordenada (x) del punto 2:\n"))
y2 = float(input("Ingrese la ordenada (y) del punto 2:\n"))

distancia_puntos = round(abs(math.sqrt(pow(x2-x1,2)+pow(y2-y1,2))),2)

print("La distancia que existe entre el punto (",x1,",",y1,") y el punto (",x2,",",y2,") es de:\n", distancia_puntos)

print("\nRichard Soria")