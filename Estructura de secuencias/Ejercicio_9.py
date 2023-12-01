
# Ejercicio 9 #

print("Program que pide los dos nombres y los dos apellidos al usuario, mostrando solo sus iniciales\n")

n1 = str(input("Ingrese su primer nombre:\n"))
n2 = str(input("Ingrese su segundo nombre:\n"))
a1 = str(input("Ingrese su primer apellido:\n"))
a2 = str(input("Ingrese su segundo apellido:\n"))

n1_extraccion = n1.upper()[0]
n2_extraccion = n2.upper()[0]
a1_extraccion = a1.upper()[0]
a2_extraccion = a2.upper()[0]


print("La inial de su primer nombre es:\n",n1_extraccion)
print("La inial de su segundo nombre es:\n",n2_extraccion)
print("La inial de su primer apellido es:\n",a1_extraccion)
print("La inial de su segundo apellido es:\n",a2_extraccion)

print("\nRichard Soria")