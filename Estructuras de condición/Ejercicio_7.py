
# Ejercicio 7 #

print("Algoritmo para determinar el cobro por la entrega de un paquete o, en su caso, el rechazo de la entrega\n")

print("Recuerde que el peso máximo de envío es de 5 kgn")

print("Zonas disponibles para el srvicio de envío de paquetes\n")
print("Zona 1: América del Norte, $24 el gramo")
print("Zona 2: América Central, $20 el gramo")
print("Zona 3: América del Sur, $21 el gramo")
print("Zona 4: Europa, $10 el gramo")
print("Zona 5: Asia, $18 el gramo")

zona = int(input("Ingese de las 5 opciones para enviar su paquete (Elija una opción del 1 al 5):\n"))
peso = float(input("Ingrese el peso de su paquete en Kg:\n"))

peso = peso*1000
if peso>5 and zona==1:
    print("El costo de envío sera de:\n$",peso*24)
elif peso>5 and zona==2:
    print("El costo de envío sera de:\n$",peso*20)
elif peso>5 and zona==3:
    print("El costo de envío sera de:\n$",peso*21)
elif peso>5 and zona==4:
    print("El costo de envío sera de:\n$",peso*10)
elif peso>5 and zona==5:
    print("El costo de envío sera de:\n$",peso*18)
else:
    print("El paquete supera la cantida máxima de envío")

print("\nRichard Soria")