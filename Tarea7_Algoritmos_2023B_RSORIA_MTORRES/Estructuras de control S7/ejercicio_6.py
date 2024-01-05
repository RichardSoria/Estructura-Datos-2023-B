#Mateo Torres y Richard Soria
#Ejercicio Banco Pichincha
print("Bienvenid@ a Banco Pichincha:")
print("Menú de tarjetas:")
print("Tipo 1""\nTipo 2""\nTipo 3""\nTipo 4""\n5.- Salir del menú")
tipo = int(input("Ingrese el número del tipo de tarjeta que tiene o 5 para salir: "))
while tipo != 5:
    if 1 <= tipo <= 4:
        creditoActual = float(input("Ingrese su crédito actual: "))
        while creditoActual <= 0:
            print("Valor inválido, inténtelo de nuevo.")
            creditoActual = float(input("Ingrese su crédito actual: "))
        
        if creditoActual > 0:
            match tipo:
                case 1:
                    creditoNuevo = (creditoActual * 0.25) + creditoActual
                case 2:
                    creditoNuevo = (creditoActual * 0.35) + creditoActual
                case 3:
                    creditoNuevo = (creditoActual * 0.40) + creditoActual
                case 4:
                    creditoNuevo = (creditoActual * 0.50) + creditoActual

            print()
            #print(f"Señor {nombre} con C.I: {cedula} y correo: {correo}")
            print(f"Su tarjeta tipo {tipo} con un crédito anterior de: ${creditoActual}. Ahora tiene un crédito de ${creditoNuevo}")
    else:
        print("Ingrese una opción válida.")
    print()
    print("Menú de tarjetas:")
    print("Tipo 1""\nTipo 2""\nTipo 3""\nTipo 4""\n5.- Salir del menú")
    tipo = int(input("Ingrese el número del tipo de tarjeta que tiene o 5 para salir: "))
    
print("Saliendo del sistema...")