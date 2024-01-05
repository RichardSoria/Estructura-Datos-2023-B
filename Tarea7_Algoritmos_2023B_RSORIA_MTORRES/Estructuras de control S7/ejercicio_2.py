#Mateo Torres y Richard Soria
#Ejercicio del detector de fugas de de gas de tres talleres Chevrolet  
print("Sensor de fugas de gas de Chevrolet:")
print("Menú de opciones:""\n1. Ingresar datos sobre fugas de gas.""\n2. Salir")
opcion = int(input("Ingresar el número con la opción requerida: "))
print()
num_cocen = 0
fugas = 0
talleres = 3 
while opcion != 2:
    if opcion == 1:
        while num_cocen < talleres:
            num_cocen += 1
            print(f"Taller # {num_cocen}.")
            estado = input("¿El taller tuvo fugas de gas?""\nIngrese si o no: ")
            print()
            while estado != "si" and estado != "no":
                print("Ingrese solo si o no, intente de nuevo.")
                estado = input("¿El taller tuvo fugas de gas?""\nIngrese si o no: ")

            if estado == "si":
                fugas += 1

        if fugas >= 1:
            print(f"Se enviará un correo notificando las {fugas} fugas presentes en los talleres.")
            print()
        else:
            print("No hay nada que notificar sobre fugas de gas.")
            print()

    elif opcion != 1 and opcion != 2:
        print("Opción inválida, intente de nuevo.")

    opcion = int(input("Menú de opciones:""\n1. Ingresar datos sobre fugas de gas.""\n2. Salir""\nIngresar el número con la opción requerida: "))

if opcion == 2:
    print("Saliendo del menú...")
print("Richard Soria")
print("Mateo Torres")