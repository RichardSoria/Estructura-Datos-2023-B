
# Ejercicio 9 #

print("Programa que depende la opción muestra el tipo de motor una de bomba para mover fluidos registrada")

tipo = int(input("Ingrese una ópcion del 1 a 4:\n"))

def dimeTipoMotor(a):

    if a==0:
        print("No hay establecido un valor definido para el tipo de bomba")
    elif a==1:
        print("La bomba es una bomba de agua")
    elif a==2:
        print("La bomba es una bomba de gasolina")
    elif a==3:
        print("La bomba es una bomba de hormigón")
    elif a==4:
        print("La bomba es una bomba de pasta alimenticia")
    else:
        print("No existe un valor válido para tipo de bomba")

    return ""

print(dimeTipoMotor(tipo))

print("\nRichard Soria")