# El empresario “Juan Alvear” desea saber cuánto ha venido ahorrando a lo largo de todo el año, si al final de cada mes él fue depositando cantidades X de dinero. Además, él requiere saber cuánto lleva ahorrando cada mes y el total ahorrado, para lo cual la entidad bancaria “PRODUBANCO” desea un programa para ayudar a Juanito y sus demás clientes a realizar lo siguiente: a. Permitir agregar cantidades X de dinero por cada mes. b. Determinar cuánto es el total ahorrado que tiene el cliente.

import os
total_ahorro = 0

print("Bienvenido a PRODUBANCO")
print("Este programa permite calcular las cantidades que ha ido depositando en su cuenta")
while(True):
    print("Este menú le ofrece las siguientes opciones")
    print("Opción 1: Depositar dinero")
    print("Opción 2: Consultar dinero")
    print("Opción 3: Salir")
    opcion = int(input("Ingrese la opción que desea: "))
    if(opcion==1):
        os.system("cls")
        while(True):
            print("Usted ha seleccionado DEPOSITAR")
            deposito = float(input("Ingrese la cantidad a depositar: "))
            if(deposito>0):
                total_ahorro +=deposito 
                break
            else:
                os.system("cls")
                print("Ingrese una cantidad de dinero válida")
    elif(opcion==2):
        os.system("cls")
        print("Usted ha seleccionado CONSULTAR DINERO")
        print("La cantidad de dinero ahorrado es de: $",total_ahorro)
    elif(opcion==3):
        os.system("cls")
        print("Usted ha seleccionado SALIR")
        print("Tenga un buen día")
        break
    else:
        os.system("cls")
        print("Ingrese una opción válida")
print("Richard Soria")