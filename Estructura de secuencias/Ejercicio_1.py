
# Ejercicio 1 #

import math

print("Programa que calcula el perímetro y el área de un rectángulo\n")
print("Programa que calcula el perímetro y el área de un círculo\n")

altura_rectangulo = float(input("Ingrese su altura del rectángulo:\n"))
base_rectangulo = float(input("Ingrese la altura del rectángulo:\n"))
perimetro_rectangulo = (altura_rectangulo*2)+(base_rectangulo*2)
area_rectangulo = (altura_rectangulo*base_rectangulo)

radio_circulo = float(input("Ingrese el radio del circulo:\n"))


print("El perímetro del rectángulo:\n",perimetro_rectangulo)
print("El aréa del rectángulo:\n",area_rectangulo)

perimetro_circulo = (2*math.pi*radio_circulo)
area_circulo = math.pi*pow(radio_circulo,2)

print("El perímetro del círculo:\n",perimetro_circulo)
print("El área del círculo:\n",area_circulo)

print("\nRichard Soria")