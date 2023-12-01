
# Ejercicio 4 #

import math

print("Programa que determina que tipo de triángulo es dado por sus lados\n")

a = float(input("Ingrese el lado A del triángulo:\n"))
b = float(input("Ingrese el lado B del triángulo:\n"))
c = float(input("Ingrese el lado C del triángulo:\n"))

if pow(a,2)+pow(b,2)==pow(c,2) or pow(a,2)+pow(c,2)==pow(b,2) or pow(b,2)+pow(c,2)==pow(a,2):
    print("Es un triángulo rectángulo")
elif a==b and a!=c or a==c and a!=b:
    print("Es un triángulo isóceles")
elif a==b==c:
    print("Es un triángulo equilátero")
else:
    print("Es un triángulo escaleno")

print("\nRichard Soria")