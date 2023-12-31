#Escriba un programa que simule un banco. El programa solicitará primero una cantidad, que será la cantidad de dinero que queremos ahorrar. A continuación, el programa solicitará una y otra vez las cantidades que se irán ahorrando, hasta que el total ahorrado iguale o supere al objetivo ($ 1000). El programa deberá comprobar que las cantidades sean positivas, no se permitirán ingresar cantidades negativas.
while(True):
    cantidad_objetivo = float(input("Ingrese la cantidad de dinero objetivo a ahorrar: $"))
    if(cantidad_objetivo>0):
        cantitdad_ahorar = 0
        while(True):
            cantidades = float(input("Ingrese la cantidad de ahorros: $"))
            if(cantidades>0):
                cantitdad_ahorar+=cantidades
                print("Su cantidad de ahorro actual es de: $",cantitdad_ahorar)
                if(cantitdad_ahorar>=cantidad_objetivo):
                    break
            elif(cantidades<0):
                print("Ingrese una cantidad válida mayor y diferete de 0")

        break
    else:
        print("Ingrese una cantidad mayor a 0")
print("Richard Soria")