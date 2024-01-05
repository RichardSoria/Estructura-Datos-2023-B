# Mostrar un menú con tres opciones:
import os

while(True):
    print("Bienvenido al menú de multiples usos")
    print("Opción 1: Comenzar Programa")
    print("Opción 2: Imprimir listado")
    print("Opción 3: Finalizar Programa")
    opcion = int(input("\nIngrese la opción que desea ejecutar: "))
    if (opcion==1):
        os.system ("cls") 
        print("\nPROGRAMA INICIALIZADO\n")
        while(True):
            print("Bienvenido al menú de multiples usos")   
            print("Opción 1: Comenzar Programa")
            print("Opción 2: Imprimir listado")
            print("Opción 3: Finalizar Programa")
            opcion = int(input("\nIngrese la opción que desea ejecutar: "))
            if (opcion==1):
                os.system ("cls") 
                print("\nPROGRAMA YA INICIALIZADO\n")
            elif(opcion==2):
                os.system ("cls") 
                print("\nLISTADO MOSTRADO EN PANTALLA\n")
            elif(opcion==3):
                os.system ("cls") 
                print("\nPROGRAMA FINALIZADO\n")
                break
            else:
                os.system ("cls") 
                print("\nEsa opción no se encuentra en el menú\n")
        break
    elif(opcion==2):
        os.system ("cls") 
        print("\nLISTADO MOSTRADO EN PANTALLA\n")
    elif(opcion==3):
        os.system ("cls") 
        print("\nPROGRAMA FINALIZADO\n")
        break
    else:
        os.system ("cls") 
        print("\nEsa opción no se encuentra en el menú\n")
    
print("Richard Soria")
print("Mateo Torres")