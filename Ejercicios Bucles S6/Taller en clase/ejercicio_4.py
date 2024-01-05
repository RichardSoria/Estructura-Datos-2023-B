#Crear un programa que imprima la Sucesión de Fibonacci, desde el número 0 hasta el 1597, horizontalmente. (7 líneas de código)
a=0; b=1; c=0
print("La serie de Fibonacci desde el 0 hasta 1597 es:")
for i in range(0,18):
    print(a,end=" ")
    c = a + b
    a = b
    b = c
print("Richard Soria")
print("Mateo Torres")