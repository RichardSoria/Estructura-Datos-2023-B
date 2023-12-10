
# Corrección Ejercicio Prueba If-Else #

print("********** Bienvenido a las hamburguesas CARBONERO **********");
print("Contamos con diferentes hamburguesas y métodos de pago");
print("Ofrecemos los siguientes tipos de hamburguesas:");
print("1) Sencilla $1.50");
print("2) Doble $2.50");
print("3) Triple $3.25");
tipo_hamburguesa = int(input("Ingrese el tipo de hamburguesa que desea, digitando el número que le corresponde:\n"));
cantidad_hamburguesa = int(input("Ingrese la cantidad de hamburguesas que desea comprar:\n"));

if tipo_hamburguesa == 1:
    print("Uste ha selecionado Hamburguesas Simples con una cantidad de", cantidad_hamburguesa, ",selecione el método de pago:")
    print("1) Efectivo")
    print("2) Tarjeta de crédito (5% recargo)")
    tipo_pago = int(input("Ingrese el método de pago, digitando el número que le corresponde:\n"))

