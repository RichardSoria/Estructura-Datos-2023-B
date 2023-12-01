
# Ejercicio 6 #

print("Program que calcula lla cantida que se debe cobrar a cada estudainte por el viaje escolar\n")

alumnos = int(input("Ingrese la cantidad de estudiantes que iran al viaje escolar:\n"))
print("Recuerde el costo del autobús es $4000 sin importar el número de estudiantes\n")

if alumnos>=100:
    print("El costo para el viaje para cada estudiante sera de $65\n")
    print("El valor total a pagar es de:\n$",alumnos*65)
elif alumnos>=50:
    print("El costo para el viaje para cada estudiante sera de $70\n")
    print("El valor total a pagar es de:\n$",alumnos*70)
else:
    print("El costo para el viaje para cada estudiante sera de $95\n")
    print("El valor total a pagar es de:\n$",alumnos*95)

print("\nCada estudiante debe pagar $",4000/alumnos,"por el uso del autobus")

print("\nRichard Soria")