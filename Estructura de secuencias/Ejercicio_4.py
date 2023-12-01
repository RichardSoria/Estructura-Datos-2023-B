
# Ejercicio 4 #

print("Program que calcula el extra por comisiones de un empleado\n")

sueldo = float(input("Ingrese el sueldo base del empleado:\n"))
comisiones = int(input("Ingrese el número de comisiones del empleado en el mes:\n"))

comisiones_valor = round(sueldo*(comisiones*0.10),2)

total_pagar = sueldo + comisiones_valor

print("El total a pagar por",comisiones,"comisiones es de:\n$",comisiones_valor)
print("El del sueldo con comisiones es:\n$",total_pagar)

print("\nRichard Soria")