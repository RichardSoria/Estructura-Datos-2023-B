# Dado un número entero positivo, mostrar su factorial. El factorial de un número se obtiene multiplicando todos los números enteros positivos que hay entre el 1 y ese número.
import sys
print("Calculadora para obtener el factorial de un número")
while(True):
    numero = int(input("Ingrese el número del número que desea conocer su factorial: "))
    factorial = 1
    if(numero>1):
        for i in range(1,numero+1):
            if(i<numero):
                print(i,"x",end=" ")
            elif(i==numero):
                print(i, end=" = ")
        factorial*=i
        break
    elif(numero<0):
        print("Ingrese un número mayor y diferente de 0")
    elif(numero==1):
        print("1! = 1")
        sys.exit()
    else:
        print("0! = 1")
        sys.exit()
        
print(factorial)
print(numero,"! =",factorial)
print("Richard Soria")