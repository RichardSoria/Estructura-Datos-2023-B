#Mateo Torres y Richard Soria
#Ejercicio sumatoria entre dos números ingresados por el usuario
print("Sumatoria entre dos números.")
numero1 = int(input("Ingrese el número inicial: "))
while (numero1<0):
    print("El número ingresado no puede ser negativo, porfavor ingrese un número positivo.")
    numero1 = int(input("Ingrese el número inicial: "))
numero2 = int(input("Ingrese el número final: "))
while (numero2<0):
    print("El número ingresado no puede ser negativo, porfavor ingrese un número positivo.")
    numero2 = int(input("Ingrese el número final: "))
sumatoria = 0

while (numero1>=numero2):
    if (numero1>numero2):
        print("Número final tiene que ser mayor que el inicial, intente de nuevo.")
        numero2 = int(input("Ingrese el número final: "))

if (numero2>numero1):
    for i in range(numero1,numero2+1,1):
        print(i)
        sumatoria += i
    print(f"El resultado de la operación: {sumatoria}")
print("Richard Soria")
print("Mateo Torres")