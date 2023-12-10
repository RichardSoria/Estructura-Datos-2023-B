
# Ejercicio Calculadora #

print("Calculadora de operaciones básicas")
num_1 = float(input("Ingrese el primer número:\n"))
num_2 = float(input("Ingrese el segundo número:\n"))

suma = num_1 + num_2
resta = num_1 - num_2
producto = num_1 * num_2
potencia = num_1 ** num_2

print("Opción 1: Suma")
print("Opción 2: Resta")
print("Opción 3: Multiplicación")
print("Opción 4: División")
print("Opción 5: Potencia")
print("Opción 6: Módulo")
opcion = int(input("Ingrese la operación que desea realizar:\n"))

if opcion == 4 and num_2 ==0:
    print("No se puede dividir para cero")
elif opcion == 6 and num_2 ==0:
    print("No se puede obtener el módulo para cero")
else:
    match opcion:
        case 1:
            print("La suma de los números",num_1,",",num_2,"es:\n",suma)
        case 2:
            print("La resta de los números",num_1,",",num_2,"es:\n",resta)
        case 3:
            print("La multiplicación de los números",num_1,",",num_2,"es:\n",producto)
        case 4:
            division = num_1 / num_2
            print("La división de los números",num_1,",",num_2,"es:\n",division)
        case 5:
            print("El producto de los números",num_1,",",num_2,"es:\n",potencia)
        case 6:
            modulo = num_1 % num_2
            print("La suma de los números",num_1,",",num_2,"es:\n",modulo)
        case other: print("No es una operación válida")