
# Ejercicio 5 #

print("Programa para fijar de un kilo de uvas")
print("Recuerde el precio inicial del kilo de uva es de $3.00\n")

tipo = str(input("Ingrese el tipo de uva (A o B):\n"))
tamaño = int(input("Ingrese el tamaño de uva (1 o 2):\n"))
uva = 3
if tamaño==1 and tipo=='a' or tipo=='A':
    print("El precio para el kilo de uvas tipo",tipo,"y tamaño",tamaño,"es de:\n$",(uva+0.20))
elif tamaño==2 and tipo=='a' or tipo=='A':
    print("El precio para el kilo de uvas tipo",tipo,"y tamaño",tamaño,"es de:\n$",(uva+0.30))
elif tamaño==1 and tipo=='b' or tipo=='B':
    print("El precio para el kilo de uvas tipo",tipo,"y tamaño",tamaño,"es de:\n$",(uva-0.30))
else:
    print("El precio para el kilo de uvas tipo",tipo,"y tamaño",tamaño,"es de:\n$",(uva-0.50))

print("\nRichard Soria")