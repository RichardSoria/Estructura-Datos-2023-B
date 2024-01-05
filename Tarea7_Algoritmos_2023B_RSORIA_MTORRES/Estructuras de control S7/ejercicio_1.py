#Mateo Torres y Richard Soria
#Ejercicio de impresión de números pares hasta N
print("Sumatoria de números pares: ")
numero = int(input("Ingrese el número hasta el cual se hará la sumatoria (Ingrese cero para salir): "))
sumatoria = 0

while numero != 0:
    if numero > 0:
        for i in range(2, numero + 1, 2):
            print(i)
            sumatoria += i

        print(f"La sumatoria de los números pares hasta el {numero} es: {sumatoria}")
    elif numero < 0:
        print("El número ingresado tiene que ser positivo, intente de nuevo.")
    numero = int(input("Ingrese el número hasta el cual se hará la sumatoria (Ingrese cero para salir): "))
    
if numero == 0:
    print("Saliendo del menú.")
print("Richard Soria")
print("Mateo Torres")