# En la “Escuela Politécnica Nacional” el área de Talento Humano requiere de un programa el cual, mediante la utilización de un bucle de repetición, imprima los sueldos de todos los empleados, el número de horas trabajadas y el número de aquellos que son profesores de una cantidad de N empleados que el programa debe solicitar.

print("Bienvenido al programa para registrar a los empleados de la EPN")

suedlo_empleados = 0
sueldo_total = 0

cantidad_horas = 0
horas_total = 0

docentes_total = 0

cantidad_empleados = int(input("Ingrese la cantidad de empleados de la EPN: "))

for i in range(1,cantidad_empleados+1):
    suedlo_empleados = float(input(f'Ingrese el sueldo del empleado N°{i}: $'))
    sueldo_total+=suedlo_empleados
    cantidad_horas = float(input(f'Ingrese las horas del empleado N°{i}: '))
    horas_total+=cantidad_horas
    docentes = str(input("¿El empleado es docente\n"))
    if (docentes=="Si" or docentes=="si"):
        docentes_total+=1

print("La cantidad de empleados que hay en la EPN es:", cantidad_empleados)
print("El sueldo de todos los empleados de la EPN es de: $", sueldo_total)
print("La cantidad de horas de todos los empleados es:", horas_total)
print("La cantidad de profesores que trabajan en la EPN son:", docentes_total)
print("Richard Soria")