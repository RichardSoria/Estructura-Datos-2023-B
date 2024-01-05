#Mateo Torres y Richard Soria
#Ejercicio de identificar un número entre 1 - 100
print("Identificador de un número entre el 10 al 100:")
print("1.- Verificar un número. ""\n2.- Salir.")
opcion = int(input("Ingrese el número con la opción requerida: "))
while opcion!=2:
    if opcion==1:
        numero = float(input("Ingrese un número: "))
        while numero < 0:
            print("El número debe ser positivo, intente de nuevo.")
            numero = float(input("Ingrese un número: "))
        if numero >= 0 and numero<10:
            print("El número no pertenece.")
        elif numero>=10 and numero<=100:
            print("El número pertenece.")
        elif numero>100:
            print("El número no pertenece.")            
    else:
        print("Opción no valida, intente de nuevo.")

    print()
    print("1.- Verificar un número. ""\n2.- Salir.")
    opcion = int(input("Ingrese el número con la opción requerida: "))
print("Saliendo del menú")
print("Richard Soria")
print("Mateo Torres")