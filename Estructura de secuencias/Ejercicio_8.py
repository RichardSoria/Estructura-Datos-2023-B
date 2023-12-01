
# Ejercicio 8 #

print("Programa que imprime el tiempo que tardar en alcanzar el vehiculo más rápido al que esta adelante")

v1 = float(input("Ingrese la velocidad del primer auto (Km/h):\n"))
v2 = float(input("Ingrese la velocidad del segundo auto (Km/h):\n"))
d = float(input("Ingrese la distancia que existe entre los dos autos:\n"))

t = 60*d/(v1-v2)

print("El tiempo en minutos en que el primer auto alcanzará al segundo auto es de:\n",t,"minutos")

print("\nRichard Soria")