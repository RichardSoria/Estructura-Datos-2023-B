
# Ejercicio Prueba Switch #

print("********** Bienvenido a las hamburguesas CARBONERO **********")
print("Contamos con diferentes hamburguesas y métodos de pago")
print("Ofrecemos los siguientes tipos de hamburguesas:")
print("1) Sencilla $1.50")
print("2) Doble $2.50")
print("3) Triple $3.25")
tipo_hamburguesa = int(input("Ingrese el tipo de hamburguesa que desea, digitando el número que le corresponde:\n"))

match tipo_hamburguesa:
    case 1:
            cantidad_hamburguesa = int(input("Ingrese la cantidad de hamburguesas que desea comprar:\n"))
            pago_efectivo_simple = 1.50*cantidad_hamburguesa
            pago_credito_simple = 1.50*cantidad_hamburguesa+pago_efectivo_simple*0.05
            print("Usted ha selecionado Hamburguesas Simples con una cantidad de", cantidad_hamburguesa, ",selecione el método de pago:")
            print("1) Efectivo")
            print("2) Tarjeta de crédito (5% recargo)")
            tipo_pago = int(input("Ingrese el método de pago, digitando el número que le corresponde:\n"))

            match tipo_pago:
                 case 1:
                        print("Usted ha selecionado como método de pago efectivo:")
                        print("Su total a cancelar es de:\n$",round(pago_efectivo_simple,2), "por una cantidad de", cantidad_hamburguesa, "Hamburguesas Simples")
                        print("Porfavor digite los datos para su factura")
                        nombre = str(input("Ingrese su nombre:\n"))
                        cedula = str(input("Ingrese su cédula:\n"))
                        correo = str(input("Ingrese su correro electrónico:\n"))
                        print("Muchas gracias por su compra", nombre, "la factura será enviada a su correo", correo,".")
                        print("Vuelva pronto, lo estaremos esperando.")
                 case 2:
                        print("Usted ha selecionado como método de pago trajeta de crédito:")
                        print("Su total a cancelar es de:\n$",round(pago_credito_simple,2), "por una cantidad de", cantidad_hamburguesa, "Hamburguesas Simples con un recargo de 5%")
                        print("Porfavor digite los datos para su factura")
                        nombre = str(input("Ingrese su nombre:\n"))
                        cedula = str(input("Ingrese su cédula:\n"))
                        correo = str(input("Ingrese su correro electrónico:\n"))
                        print("Muchas gracias por su compra", nombre, "la factura será enviada a su correo", correo,".")
                        print("Vuelva pronto, lo estaremos esperando.")
                 case other: print("No es un método de pago válido.")
    case 2:
            cantidad_hamburguesa = int(input("Ingrese la cantidad de hamburguesas que desea comprar:\n"))
            pago_efectivo_doble = 2.50*cantidad_hamburguesa
            pago_credito_doble = 2.50*cantidad_hamburguesa+pago_efectivo_doble*0.05
            print("Usted ha selecionado Hamburguesas Dobles con una cantidad de", cantidad_hamburguesa, ",selecione el método de pago:")
            print("1) Efectivo")
            print("2) Tarjeta de crédito (5% recargo)")
            tipo_pago = int(input("Ingrese el método de pago, digitando el número que le corresponde:\n"))

            match tipo_pago:
                 case 1:
                        print("Usted ha selecionado como método de pago efectivo:")
                        print("Su total a cancelar es de:\n$",round(pago_efectivo_doble,2), "por una cantidad de", cantidad_hamburguesa, "Hamburguesas Dobles")
                        print("Porfavor digite los datos para su factura")
                        nombre = str(input("Ingrese su nombre:\n"))
                        cedula = str(input("Ingrese su cédula:\n"))
                        correo = str(input("Ingrese su correro electrónico:\n"))
                        print("Muchas gracias por su compra", nombre, "la factura será enviada a su correo", correo,".")
                        print("Vuelva pronto, lo estaremos esperando.")
                 case 2:
                        print("Usted ha selecionado como método de pago trajeta de crédito:")
                        print("Su total a cancelar es de:\n$",round(pago_credito_doble,2), "por una cantidad de", cantidad_hamburguesa, "Hamburguesas Dobles con un recargo de 5%")
                        print("Porfavor digite los datos para su factura")
                        nombre = str(input("Ingrese su nombre:\n"))
                        cedula = str(input("Ingrese su cédula:\n"))
                        correo = str(input("Ingrese su correro electrónico:\n"))
                        print("Muchas gracias por su compra", nombre, "la factura será enviada a su correo", correo,".")
                        print("Vuelva pronto, lo estaremos esperando.")
                 case other: print("No es un método de pago válido.")
    case 3:
            cantidad_hamburguesa = int(input("Ingrese la cantidad de hamburguesas que desea comprar:\n"))
            pago_efectivo_triple = 3.25*cantidad_hamburguesa
            pago_credito_triple = 3.25*cantidad_hamburguesa+pago_efectivo_triple*0.05
            print("Usted ha selecionado Hamburguesas Simples con una cantidad de", cantidad_hamburguesa, ",selecione el método de pago:")
            print("1) Efectivo")
            print("2) Tarjeta de crédito (5% recargo)")
            tipo_pago = int(input("Ingrese el método de pago, digitando el número que le corresponde:\n"))

            match tipo_pago:
                 case 1:
                        print("Usted ha selecionado como método de pago efectivo:")
                        print("Su total a cancelar es de:\n$",round(pago_efectivo_triple,2), "por una cantidad de", cantidad_hamburguesa, "Hamburguesas Triples")
                        print("Porfavor digite los datos para su factura")
                        nombre = str(input("Ingrese su nombre:\n"))
                        cedula = str(input("Ingrese su cédula:\n"))
                        correo = str(input("Ingrese su correro electrónico:\n"))
                        print("Muchas gracias por su compra", nombre, "la factura será enviada a su correo", correo,".")
                        print("Vuelva pronto, lo estaremos esperando.")
                 case 2:
                        print("Usted ha selecionado como método de pago trajeta de crédito:")
                        print("Su total a cancelar es de:\n$",round(pago_credito_triple,2), "por una cantidad de", cantidad_hamburguesa, "Hamburguesas Triples con un recargo de 5%")
                        print("Porfavor digite los datos para su factura")
                        nombre = str(input("Ingrese su nombre:\n"))
                        cedula = str(input("Ingrese su cédula:\n"))
                        correo = str(input("Ingrese su correro electrónico:\n"))
                        print("Muchas gracias por su compra", nombre, "la factura será enviada a su correo", correo,".")
                        print("Vuelva pronto, lo estaremos esperando.")
                 case other: print("No es un método de pago válido.")
    case other: print("Ese tipo de hamburguesa no se encuentra dentro del menú.")