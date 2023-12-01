
# Ejercicio 3 #

import math

print("Programa que recibe minutos mostrando su equivalente en horas y minutos\n")

minutos = float(input("Ingrese la cantida de minutos:\n"))

horas = math.trunc(minutos/60)

minutos_hora = int(minutos%60)

print("La cantidad de",minutos,"minutos corresponde a:\n",horas,"horas y",minutos_hora,"minutos")

print("\nRichard Soria")