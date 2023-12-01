
# Ejercicio 7 #

print("Programa que invierte un número ingresado\n")

numero = int(input("Ingrese el número a invertir:\n"))

n1 = numero%10
n2 = int((numero%100)/10)

numero_invertido = str(n1)+str(n2)

print("El número invertido es:\n",numero_invertido)

print("\nRichard Soria")