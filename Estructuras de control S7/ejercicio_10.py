# Se requiere programar un sensor infrarrojo de arduino para realizar un control remoto para una Smart TV, el programa requiere hacer lo siguiente: a. Implementar un menú de opciones para 9 tipo de actividades en el que el usuario ingresa el número de actividad y luego el programa muestra la actividad a realizar o en este caso sintoniza en el Smart TV la actividad a proyectar. Recuerda que son únicamente 9 actividades las que el usuario puede elegir para lo cual se debe hacer su respectiva validación.

import os

while (True):
    print("Control remoto para TV")
    print("opción 1: Control por voz")
    print("opción 2: Botones de acceso directo")
    print("opción 3: Teclas de navegación inteligente")
    print("opción 4: Botones de configuración rápida")
    print("opción 5: Teclado integrado")
    print("opción 7: Control de dispositivos externos")
    print("opción 8: Botón de apagado rápido")
    print("opción 9: Botón de información")
    print("opción 0: SALIR")
    opcion = int(input("Ingrese la opción que desea que realice el control remoto: "))
    if(opcion==1):
        os.system("cls")
        print("Usted ha seleccionado seleccionado Control por Voz")
    elif(opcion==2):
        os.system("cls")
        print("Usted ha seleccionado Botones de acceso directo")
    elif(opcion==3):
        os.system("cls")
        print("Usted ha seleccionado Teclas de navegación inteligente")
    elif(opcion==4):
        os.system("cls")
        print("Usted ha seleccionado Botones de configuración rápida")
    elif(opcion==5):
        os.system("cls")
        print("Usted ha seleccionado Teclado integrado")
    elif(opcion==6):
        os.system("cls")
        print("Usted ha seleccionado Control de dispositivos externos")
    elif(opcion==7):
        os.system("cls")
        print("Usted ha seleccionado Botón de apagado rápido")
    elif(opcion==8):
        os.system("cls")
        print("Usted ha seleccionado Botón de información")
    elif(opcion==9):
        os.system("cls")
        print("Usted ha seleccionado Botón de captura de pantalla ")
    elif(opcion==0):
        os.system("cls")
        print("Usted ha seleccionado SALIR")
        break
    else:
        os.system("cls")
        print("No es una opción disponible o válida")
print("Richard Soria")