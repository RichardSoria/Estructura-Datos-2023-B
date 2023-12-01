
# Ejercicio 3 #

print("Algoritmo que pida tres números y los muestre ordenados (de mayor a menor\n")

num1 = int(input("Ingrese el número 1:\n"))
num2 = int(input("Ingrese el número 2:\n"))
num3 = int(input("Ingrese el número 3:\n"))

if (num1>num2) and (num2>num3):
    print("El orden de los números de mayor a menor es:\n",num1,num2,num3)
elif (num2>num1) and (num1>num3):
    print("El orden de los números de mayor a menor es:\n",num2,num1,num3)
elif (num3>num2) and (num2>num1):
    print("El orden de los números de mayor a menor es:\n",num3,num2,num1)
elif (num1>num3) and (num3>num2):
    print("El orden de los números de mayor a menor es:\n",num1,num3,num2)
elif (num2>num3) and (num3>num1):
    print("El orden de los números de mayor a menor es:\n",num2,num3,num1)
else:
    print("El orden de los números de mayor a menor es:\n",num3,num1,num2)

print("\nRichard Soria")