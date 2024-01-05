#Mateo Torres y Richard Soria
# El día de la madre usted desea comprarle un regalo a su madre, usted visita almacenes Coral y decide comprarle varios objetos que le podrían gustar a su madre.
import os

print("Bienvenido al catálogo del almacenes Coral")
subtotal_permuferia=0
subtotal_joyeria = 0
subtotal_maquillaje = 0
subtotal_ropa= 0
while(True):
    print("DESEAMOS UN FELIZ DÍA A TODAS ESAS MADRES")
    print("Contamos con diversas categorías de artículos que puede regarle a su madre")
    print("Opción 1: Perfumería")
    print("Opción 2: Joyería")
    print("Opción 3: Maquillaje")
    print("Opción 4: Perfumería")
    print("Opcion 0: Conocer el total a cancelar")
    opcion = int(input("Ingrese la categoría que desea: "))
    match opcion:
        case 0 | " ":
            os.system ("cls") 
            break
        case 1:
            while(True):
                os.system ("cls") 
                print("Ha seleccionado la categoría")
                print("PERFUMERÍA")
                print("Artículos de esta categoría: ")
                print("Opción 1: Tentación $30")
                print("Opción 2: Primavera $28")
                print("Opción 3: Otoño $15")
                print("Opción 4: Seducción $35")
                print("Opción 0: salir al menú anterior y conocer subtotal de PERFUMERÍA")
                perfume = int(input("Ingrese el artículo que desea adquirir: "))
                match perfume:
                    case 1:
                        subtotal_permuferia+=30
                    case 2:
                        subtotal_permuferia+=28
                    case 3:
                        subtotal_permuferia+=15
                    case 4:
                        subtotal_permuferia+=35
                    case 0 | " ":
                        os.system ("cls") 
                        print("\nEl subtotal de la categoría Perfumería es: $", subtotal_permuferia,"\n")
                        break
        case 2:
            while(True):
                os.system ("cls") 
                print("Ha seleccionado la categoría")
                print("JOYERÍA")
                print("Artículos de esta categoría: ")
                print("Opción 1: Aretes $7")
                print("Opción 2: Collar $5")
                print("Opción 3: Cadena $20")
                print("Opción 4: Pulsera $15")
                print("Opción 0: salir al menú anterior y conocer subtotal de JOYERÍA")
                joyeria = int(input("Ingrese el artículo que desea adquirir: "))
                match joyeria:
                    case 1:
                        subtotal_joyeria+=7
                    case 2:
                        subtotal_joyeria+=5
                    case 3:
                        subtotal_joyeria+=20
                    case 4:
                        subtotal_joyeria+=15
                    case 0 | " ":
                        os.system ("cls") 
                        print("\nEl subtotal de la categoría Joyería es: $", subtotal_joyeria,"\n")
                        break
        case 3:
            while(True):
                os.system ("cls") 
                print("Ha seleccionado la categoría")
                print("MAQUILLAJE")
                print("Artículos de esta categoría: ")
                print("Opción 1: Sombras $8")
                print("Opción 2: Maquillaje $5")
                print("Opción 3: Labiales $4")
                print("Opción 4: Rimel $6")
                print("Opción 0: salir al menú anterior y conocer subtotal de MAQUILLAJE")
                maquillaje = int(input("Ingrese el artículo que desea adquirir: "))
                match maquillaje:
                    case 1:
                        subtotal_maquillaje+=8
                    case 2:
                        subtotal_maquillaje+=5
                    case 3:
                        subtotal_maquillaje+=4
                    case 4:
                        subtotal_maquillaje+=6
                    case 0 | " ":
                        os.system ("cls") 
                        print("\nEl subtotal de la categoría Maquillaje es: $", subtotal_maquillaje,"\n")
                        break
        case 4:
            while(True):
                os.system ("cls") 
                print("Ha seleccionado la categoría")
                print("ROPA")
                print("Artículos de esta categoría: ")
                print("Opción 1: Blusa $25")
                print("Opción 2: Chaqueta $60")
                print("Opción 3: Pantalón $18")
                print("Opción 4: Abrigo $90")
                print("Opción 0: salir al menú anterior y conocer subtotal de ROPA")
                ropa = int(input("Ingrese el artículo que desea adquirir: "))
                match ropa:
                    case 1:
                        subtotal_ropa+=25
                    case 2:
                        subtotal_ropa+=60
                    case 3:
                        subtotal_ropa+=18
                    case 4:
                        subtotal_ropa+=90
                    case 0 | " ":
                        os.system ("cls") 
                        print("\nEl subtotal de la categoría Ropa es: $", subtotal_ropa,"\n")
                        break
        case _:
            os.system ("cls") 
            print("Ingrese una opción válida")
print("El subtotal de la categoría Perfumería es: $", subtotal_permuferia)
print("El subtotal de la categoría Joyería es: $", subtotal_joyeria)
print("El subtotal de la categoría Maquillaje es: $", subtotal_maquillaje)
print("El subtotal de la categoría Ropa es: $", subtotal_ropa)
total = subtotal_permuferia+subtotal_joyeria+subtotal_maquillaje+subtotal_ropa
print("\nEL total a pagar por todo es: $",total)
print("Richard Soria")
print("Mateo Torres")