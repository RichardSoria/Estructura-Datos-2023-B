# Calcule la media de varias notas ingresadas por teclado. El usuario ingresará tantas notas hasta que ingrese el “0”.
suma = 0
n = 1
print("Calculadora de promedio de notas")
while (True):
    print("Ingrese la nota",n,"(Ingrese 0 para ver el informe obtenido):", end=" ")
    notas = float(input())
    if(notas==0):
        break
    elif(notas<0):
        print("Ingrese notas mayores y diferentes a 0")
    elif(notas>20):
        print("Recuerde que el sitema admite notas menores o iguales a 20")
    else:
        suma+=notas
        n+=1
if(notas>=0):
    print("Ha ingresado",n-1,"notas")
    print("El promedio de las nota es:",round(suma/(n-1),2),)  
else:
    print("No se puede calcular ningun promedio con el valor ingresado")  
print("Richard Soria")