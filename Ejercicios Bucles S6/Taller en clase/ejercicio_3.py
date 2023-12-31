# Crear un bucle que cuente los números pares e impares del 1 al 100, los números deberán ser ingresados por teclado, hasta que el usuario digite “0”. Al finalizar, informar la cantidad de números pares y de impares leídos en total

print("Números pares e impares")
numero_par=0
numero_impar=0
while(True):
    numero = int(input("Ingrese el número (Ingrese 0 para ver el informe obtenido): "))
    if(numero==0):
        break
    elif(numero<0):
        print("Ingrese un número mayor a 0")
    elif((numero%2)==0):
        numero_par+=1
    else:
        numero_impar+=1
print("La cantidad de números pares ingresados son:",numero_par)
print("La cantidad de números impares ingresados son:",numero_impar)
print("Richard Soria")