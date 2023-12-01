
# Ejercicio 10 #

print("Programa que muestra al esduiante un mensaje por sus notas en Inglés")

nombre = str(input("Ingrese su nombre:\n"))
nota = float(input("Ingrese sus notas de la asignatura de inglés:\n"))

if 10==nota>=9:
    print("Felicitaciones",nombre,"su nota es",nota,"equivalente a excelente")
elif 9>nota>=7:
    print("Siga adelante",nombre,"su nota es",nota,"equivalente a muy buena")
elif 7>nota>=5:
    print("Debe esforzarse más",nombre,"su nota es",nota,"equivalente a buena")
elif 0==nota>=4:
    print("Usted",nombre,"puede reprobar ya quesu nota es",nota,"equivalente a regulare")
else:
    print("No corresponte a ningun tipo de nota dentro del sistema del 0 al 10")

print("\nRichard Soria")