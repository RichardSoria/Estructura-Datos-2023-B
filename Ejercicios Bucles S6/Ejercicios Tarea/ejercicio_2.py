# Dado un número, cuente el número total de dígitos de un número. Por ejemplo, el número es 75869, por lo que la salida debería ser 5.
numero = int(input("Ingrese el número del cual desea conocer la cantidad de dígitos que este posea: "))
numero_final = numero
contador = 0
while (numero>=1 or numero<=-1):
    numero= numero/10
    contador = contador+1
if(contador>1 or contador<0 ):
    print("El número", numero_final, "tiene una cantidad total de:", contador, "dígitos.")
else:
    print("El número", numero_final, "tiene una cantidad total de:", contador, "dígito.")

print("Richard Soria")
