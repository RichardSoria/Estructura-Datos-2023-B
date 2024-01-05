# En los almacenes “ETAFASHION” se van aplicar unos descuentos para el siguiente feriado en el que se rebaja el 10% del precio total de la compra si se adquieren más de 20 unidades y 5% si adquieren hasta 20 unidades, pero más de 10. Por otra parte, no hay descuento para cantidades menores o iguales a 9 unidades. Con el precio total de la compra y la cantidad adquirida de prendas realice un programa, para mostrar el nuevo valor pagar y la cantidad de prendas de vestir adquiridas.
import os

print("Biemvemido a ETAFASHION")
while(True):
    dinero_compra = float(input("Ingrese la cantidad total de su compra: $"))
    if (dinero_compra>0):
        while(True):
            print("Contamos con varios descuentos por este feriado:")
            print("Si usted adquire más de 20 unidades se le hará un descuento del 10% en su compra")
            print("Si usted adquire 10 o más (hasta un máximo de 20) unidades se le hará un descuento del 5% en su compra")
            unidades = int(input("Ingrese la cantidad de unidades que adquirio: "))
            if (unidades>20):
                os.system("cls")
                print("El descueto que se le hara a su compra es del 10%")
                descuento_10 = dinero_compra-(dinero_compra*0.10)
                print("El valor a pagar por su compra es de: $",dinero_compra,"sin descuento.")
                print("El valor a pagar por su compra es de: $",descuento_10,"con el descuento del 10%")
                break
            elif(unidades>=10 and unidades<=20):
                os.system("cls")
                print("El descueto que se le hara a su compra es del 5%")
                descuento_5 = dinero_compra-(dinero_compra*0.05)
                print("El valor a pagar por su compra es de: $",dinero_compra,"sin descuento.")
                print("El valor a pagar por su compra es de: $",descuento_5,"con el descuento del 5%")
                break
            elif(unidades>0 and unidades<10):
                os.system("cls")
                print("No se le aplicará ninguna clase de descuento")
                print("El valor a pagar por su compra es de: $",dinero_compra,".")
                break
            else:
                os.system("cls")
                print("Ingrese una cantidad mayor a 0")
        break
    else:
        os.system("cls")
        print("Ingrese una monto superior a $0")
print("Richard Soria")