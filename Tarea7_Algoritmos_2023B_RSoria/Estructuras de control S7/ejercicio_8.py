#Mateo Torres y Richard Soria
# Se requiere un programa para la panadería “LA UNIÓN” en el cual les permita obtener la suma total del precio de N guaguas de pan que el programa debe solicitar. Además, se requiere obtener la suma de las guaguas que son de mora. Para la solución al problema el bucle de repetición (while).

import os
unidad = 0
total_venta = 0
print("Bienvenido a la panadería 'LA UNIÓN' ")
print("Este programa le permitira realizar la suma total de los precios de las guaguas de pna vendidas o adquiridas")
while(True):
    cantidad_guaguas = int(input("Ingrese la cantidad de guaguas de pan adquiridas o vendidas: "))
    if(cantidad_guaguas>0):
        while(unidad<cantidad_guaguas):
            while(True):
                precio = float(input("Ingrese el precio de la guagua de pan: $"))
                if(precio>0):
                    unidad+=1
                    total_venta+=precio
                    break
                else:
                    os.system("cls")
                    print("Ingrese una cantida mayor a $0")
        break
    else:
        os.system("cls")
        print("Ingrese una cantidad superior a 0")
print("El total a pagar por un total de", unidad, "de guaguas de pan es de: $",total_venta)
print("Richard Soria")
print("Mateo Torres")