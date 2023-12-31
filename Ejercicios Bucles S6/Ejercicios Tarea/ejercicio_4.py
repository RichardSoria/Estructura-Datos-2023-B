#Crear un programa que permita al usuario ingresar los montos de las compras de un cliente (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario ingrese el monto 0 .
import os
print("Bienvenido al program que le permite calcular el valor de sus compras")
compras_total = 0
while(True):
    compras = float(input("Ingrese el valor de artículo seleccionado(digite 0 para finalizar): $"))
    if(compras==0):
        os.system ("cls") 
        break
    elif(compras>0):
        compras_total+=compras
        os.system ("cls") 
        print("El valor actual de sus compras es: $",compras_total)
    else:
        os.system ("cls") 
        print("Por favor ingrese una cantidad válida(mayor y diferente de 0)")
if(compras_total>1000):
    os.system ("cls") 
    print("Felicidades es acredor de un 10% en sus compras.")
    descuento = compras_total-(compras_total*0.10)
    print("Total a pagar si descuento: $",compras_total)
    print("Total a pagar por sus compras es: $",descuento)
else:
    os.system ("cls") 
    print("Total a pagar por sus compras es: $",compras_total)

print("Richard Soria")