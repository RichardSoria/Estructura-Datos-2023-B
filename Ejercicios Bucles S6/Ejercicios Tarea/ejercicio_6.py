# Crear un programa que permita al usuario ingresar títulos de libros por teclado, finalizando el ingreso al leerse el string “*” (asterisco). Cada vez que el usuario ingrese un string de longitud 1 que contenga sólo una barra ("/") se considera que termina una línea. Por cada línea completa, informar cuántos dígitos numéricos (del 0 al 9) aparecieron en total (en todos los títulos de libros que componen en esa línea).

total_lineas = 0
digitos_linea = 0
titulo = input("Ingrese el titulo del libro: ")

while(titulo!="*"):
    if titulo== "/":
        total_lineas+=1
        print("Línea completa. Aparecen", digitos_linea, "dígitos.")
        digitos_linea = 0
    else:
        for i in titulo:
            if i in "0123456789":
                digitos_linea+=1
    titulo = input("Ingrese el titulo del libro: ")
print("Fin. Se leyeron", total_lineas, "líneas.")

