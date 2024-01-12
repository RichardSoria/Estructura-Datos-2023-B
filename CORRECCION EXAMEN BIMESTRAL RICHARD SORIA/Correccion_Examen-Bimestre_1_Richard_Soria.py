# Correccion Examen-Bimestre 1
#Richard Soria
correo = "tosh@gmail.com"
contraseña = "Secret*"
descuento_articulo = 0.10
precio_final = 0
articulos = 0
articulos_descuento = 0
while(True):
    print("----------LOGIN-AMAZON----------")
    correo_verificar= str(input("Ingrese su correo electrónico: "))
    contraseña_verificar = str(input("Ingrese su contraseña: "))
    if(correo==correo_verificar and contraseña==contraseña_verificar):
        print("----------------------------")
        print("Bienvenido de nuevo, es un gusto tenerlo de nuevo.")
        break
    else:
        print("----------------------------")
        print("Crendenciales incorrectas. Intentelo de nuevo.")
while(True):
    print("------BIENVVENIDO A AMAZON------")
    print("Menú de opciones")
    print("1.-Ingresar productos en el carrito")
    print("2.- Facturar")
    print("3.- Salir")
    opcion = int(input("Ingrese la opción que desea realizar: "))
    if(opcion==1):
        print("----------------------------")
        while(True):
            #Richard Soria
            productos = int(input("Ingrese el número de productos a comprar: "))
            if(productos>0):
                break
            else:
                print("Ingrese una cantidad válida")
        contador_productos = 0
        while(contador_productos<productos):
            print(" ")
            print("¿El producto tiene cupón de descuento?")
            descuento = str(input("Ingrese si o no: "))
            if(descuento == "si" or descuento == "Si"):
                while(True):
                    palabra = str(input("Ingrese el código del producto: "))
                    if(palabra == "enero"):
                        while(True):
                            precio = float(input("Ingrese el precio del producto: $"))
                            if(precio>0):
                                precio_descuento = precio-(precio*descuento_articulo)
                                precio_final+=precio_descuento
                                articulos_descuento+=1
                                break
                            else:
                                print("Ingrese una cantidad superior a $0")
                            print(" ")
                        break
                    else:
                        print("Ingrese un cupón válido")
            elif(descuento == "no" or descuento == "No"):
                while(True):
                    #Richard Soria
                    precio = float(input("Ingrese el precio del producto: $"))
                    if(precio>0):
                        precio_descuento = precio-(precio*descuento_articulo)
                        precio_final+=precio
                        articulos+=1
                        break
                    else:
                        print("Ingrese una cantidad superior a $0")
            contador_productos+=1
        print(" ")
    elif(opcion==2):
        print("------FACTURA ELECTRÓNICA------")
        print("*Detalle del cupón de descuento")
        print("*Nombre del cupo de descuento es enero")
        print("El número de artículos con descuento es: ",articulos_descuento)
        print("El precio final de la compra es: $",precio_final)
        print("La factura electrónoica sera enviada a su correo.")
    elif(opcion==3):
        print("----------------------------")
        print("Muchas Gracias por utilizar nuestro sitema.")
        break
    else:
        print("Ingrese una opción válida")
# Richard Soria