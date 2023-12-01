
# Ejercicio 2 #

print("Program que pide al usuario una nota, edad y sexo, cumpliendo ciertas condiciones\n")
nota = int(input("Ingrese su nota:\n"))
edad = int(input("Ingrese se edad:\n"))
sexo = str(input("Ingrese su sexo (M o F):\n"))

if nota >= 5 and edad >= 18 and sexo=='f'or sexo=='F':
    print("ACEPTADA")
elif nota >= 5 and edad >= 18 and sexo=='m'or sexo=='M':
    print("POSIBLE")
else:
    print("NO ACEPTADA")

print("\nRichard Soria")