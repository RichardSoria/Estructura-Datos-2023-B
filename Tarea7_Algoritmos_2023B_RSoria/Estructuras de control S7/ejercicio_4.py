#Mateo Torres y Richard Soria
#Ejercicio promedio de notas de estudiantes
print("Promedio de notas de la escuela Fe y Alegria.")
print("Menú de opciones:""\n1.Ingresar notas de un estudiante.""\n2.Salir.")
opcion = int(input("Ingrese el número con la opcion requerida: "))
while(opcion!=2):
    if(opcion==1):
        nota1 = float(input("Ingrese la primera nota: "))
        while(nota1<0 or nota1>20):
            if(nota1<0):
                print("La nota ingresada debe ser mayor a 0, vuelva a intentarlo.")
            elif(nota1>20):
                print("La nota no puede ser mayor a 20, intente de nuevo.")
            nota1 = float(input("Ingrese la primera nota: "))
        nota2 = float(input("Ingrese la segunda nota: "))
        while(nota2<0 or nota2>20):
            if(nota2<0):
                print("La nota ingresada debe ser mayor a 0, vuelva a intentarlo.")
            elif(nota2>20):
                print("La nota no puede ser mayor a 20, intente de nuevo.")
            nota2 = float(input("Ingrese la segunda nota: "))
        nota3 = float(input("Ingrese la tercera nota: "))
        while(nota3<0 or nota3>20):
            if(nota3<0):
                print("La nota ingresada debe ser mayor a 0, vuelva a intentarlo.")
            elif(nota3>20):
                print("La nota no puede ser mayor a 20, intente de nuevo.")
            nota3 = float(input("Ingrese la tercera nota: "))
        nota4 = float(input("Ingrese la cuarta nota: "))
        while(nota4<0 or nota4>20):
            if(nota4<0):
                print("La nota ingresada debe ser mayor a 0, vuelva a intentarlo.")
            elif(nota4>20):
                print("La nota no puede ser mayor a 20, intente de nuevo.")
            nota4 = float(input("Ingrese la cuarta nota: "))
    promedio = (nota1 + nota2 + nota3 + nota4)/4
    print(f"El promedio del estudiante es {promedio}")
    if (promedio>=14):
        print("Felicitaciones, ha aprobado el curso.")
        break
    elif(promedio>=9):
        print("Usted tiene que dar un examen supletorio.")
        break
    else:
        print("Usted a sido rechazado.")
        break
print("Saliendo del sistema...")
print("Richard Soria")
print("Mateo Torres")