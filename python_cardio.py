import math
import random
print("""Hola este el unicio del reto de Datacademy

Comenzaremos con la semana 1 con el curso básico e intermedio de python Reto: \nPython Cardio""")

def run():

    def triangulo():
        print("""Primer Ejercicio es el área de un triangulo
        Recordemos que para calcular el area es necesario conocer tanto la base b como la altura h""")
        base = float(input("Ingrese el valor de la base"))
        height = float(input("Ingrese el valor de la altura"))

        area = float(( base * height ) / 2)
        print("El area de tu triangulo es ", area)

        if round(math.tan(math.pi/3),4) == round(((2 * height) / base), 4):
            print("Tu triangulo es equilatero")
        else:
            y = 0
            n = 0
            iso_esca = str(input("Tu triangulo tiene todos los lados diferentes (Si/No) \n"))
            if iso_esca == "y":
                print("Tu tiangulo es Escaleno")
            elif iso_esca == "n":
                print("Tu triangulo es isoceles")
            else:
                print("No has ingresado ningun valor ")
                triangulo()
        menu = int(input("Desea volver al menu o cálcular otro triangulo \n1.Menu \n2.Otra triangulo"))
        if menu == 1:
            run()
        else:
            triangulo()

    def ppt():
        select_usu = 0
        contadorUsuario = 0
        contadorPC = 0
        select_pc = 0
        game = {
            1: "Tijeras",
            2: "Piedra",
            3: "Papel"
        }
        while True:
            print("""Seleciona una de las categorias ya sea de la siguiente forma:
            1. Tijeras
            2. Piedra
            3. Papel
            Y la consola elegira uno al asar, gana el que  gane 2 rondas de tres """)
            select_usu = game[int(input())]
            print("Has seleccionado ", select_usu)

            select_pc = game[random.randrange(1,4)]
            print("La PC ha seleccionado ", select_pc)

            if select_usu == select_pc:
                print("Empate")

            elif select_pc == "Piedra" and select_usu == "Papel":
                contadorUsuario = contadorUsuario + 1
                print("Ganaste, papel envulve piedra")

            elif select_pc == "Papel" and select_usu == "Tijeras":
                print("Ganaste, Tijeras cortan Papel")
                contadorUsuario = contadorUsuario + 1

            elif select_pc =="Tijeras" and select_usu == "Piedra":
                print("Ganaste, Piedra daña tijeras")
                contadorUsuario = contadorUsuario + 1

            elif select_usu == "Piedra" and select_pc == "Papel":
                print("Perdiste, papel envuelve piedra")
                contadorPC = contadorPC + 1

            elif select_usu == "Papel" and select_pc == "Tijeras":
                print("Perdiste, Tijeras cortan papel")
                contadorPC = contadorPC + 1

            elif select_usu =="Tijeras" and select_pc == "Piedra":
                print("Perdiste, Piedra daña tijeras")
                contadorPC = contadorPC + 1

            print("PC: " , contadorPC)
            print("Usuario: " , contadorUsuario)

            if contadorUsuario == 2 or contadorPC == 2:
                break


        if contadorPC == 2:
            print("El ganador es PC")
        elif contadorUsuario == 2:
            print("El ganador es Usuario")


        menu = int(input("Desea volver al menu o hacer otro juego \n1.Menu \n2.Otro juego"))
        if menu == 1:
            run()
        else:
            ppt()

    def km_millas():

        def kmAmillas():
            km = float(input("Ingrese el valor en kilometros"))
            x = round(float(0.621371 * km),2)
            print("El valor de ", km, "en millas es ", x)

        def millAKm():
            milla = float(input("Ingrese el valor en millas"))
            x = round(float(1.609344 * milla),2)
            print("El valor de ", milla, "en kilometros es ", x)

        print("Bienvenido al conversor de Millas a kilometros por favor seleccione que desea hacer \n1.Kilometros a millas \n2. Millas a Kilometros")
        select3 = int(input())
        if select3 == 1:
            kmAmillas()

        elif select3 == 2:
            millAKm()

        else:
            print("NO seleccionó un valor correcto \nDesea seguir con el programa o desea ir al menu principal \n1. Seguir\n2.Menú Principal")
            menu = int(input())
            if menu == 1:
                km_millas()
            elif menu == 2:
                run()
            km_millas()

        menu = int(input("Desea volver al menu o hacer otra conversión \n1.Menu \n2.Otra converision"))
        if menu == 1:
            run()
        else:
            km_millas()

    def vol():
        shape = int(input("""Bienvenido a la calucladora de volumenes regulares:\nPor favor seleciona que figura quieres conocer su volumen:
        \n1. Prisma rectangular \n2. Prisma triangular \n3. Prisma hexagonal\n4. Piramide triangular \n5. Cilindro\n6. Cono\n7. Esfera \n8. menu\nTu respuesta es: """))

        if shape == 1:
            a = float(input("Ingrese el valor de uno de los lado a: "))
            b = float(input("Ingrese el valor de uno de los lado b: "))
            c = float(input("Ingrese el valor de uno de los lado c: "))

            vol_1 = (a * b * c)

            if a == b == c:
                print("Esto es un cubo y su volumen es ", round(float(vol_1),2) )
            else:
                print("El Prisma rectangular tiene un volumen de :", float(vol_1))
                vol()

        elif shape == 2:
            a = float(input("Ingrese el valor de la base 1 "))
            b = float(input("Ingrese el valor de la base 2: "))
            c = float(input("Ingrese el valor de la altura del triangulo: "))

            vol_2 = (a * b * c)/2
            print("El Prisma triangular tiene un volumen de :", round(float(vol_2),2))
            vol()

        elif shape == 3:
            a = float(input("Ingrese el valor de uno de los lados del hexagono "))
            b = float(input("Ingrese el valor de la apotema (distancia entre el centro de la figura respecto al centro de uno de los lados ): "))
            c = float(input("Ingrese el valor de la altura de la figura: "))

            vol_3 = 3 * a * b * c
            print("El Prisma hexagonal tiene un volumen de :", round(float(vol_3),2))
            vol()

        elif shape == 4:
            a = float(input("Ingrese el valor de uno de los lados de la base: "))
            b = float(input("Ingrese el valor de la altura correspondiente a la distancia en el centro de una cara a la punta opuesta "))

            vol_4 = ( math.sqrt(3) / 12 ) * a**2 * b
            print("la piramide triangular tiene un volumen de :", round(float(vol_4),2))
            vol()

        elif shape == 5:
            a = float(input("Ingrese el valor del radio del circulo: "))
            b = float(input("Ingrese el valor de la altura: "))

            vol_5 = math.pi * a**2 * b
            print("El cilindro tiene un volumen de :", round(float(vol_5),2))
            vol()

        elif shape == 6:
            a = float(input("Ingrese el valor del radio del circulo: "))
            b = float(input("Ingrese el valor de la altura: "))

            vol_6 = math.pi * a**2 * b / 3
            print("El cono tiene un volumen de :", round(float(vol_6),2))
            vol()

        elif shape == 7:
            a = float(input("Ingrese el valor del radio de la esfera: "))

            vol_7 = math.pi * a**2  * 4 / 3
            print("El cono tiene un volumen de :", round(float(vol_7),2))
            vol()
        elif shape == 8:
            run()

        else:
            print("No selcionó ningun valor dentro del rango")
            vol()

    def ran():
        print("Rangos Cambiantes. Elige 3 números y te dire si el ultimo numero desta en entro los dos primeros ")
        a = float(input("Ingrese el primer valor: "))
        b = float(input("Ingrese el Segundo valor: "))
        c = float(input("Ingrese el tercer valor: "))

        if a < b:
            if a < c and c < b:
                print("el valor de ", c ,"Si esta entre ",a," y ", b)
            else:
                print("El valor no esta entre los valores iniciales")

        elif b < a:
            print("colocaste los número en distinto orden")
        exit = int(input("desear intentarlo otra vez?, coloca 1 de lo contrario ira al menu principal"))
        if exit == 1:
            ran()
        else:
            run()



    select = int(input("Seleciona el reto que quieres probar: \n1. Triangulo \n2. Piedra Papel O Tijera \n3. Conversor de Millas a kilometros \n4. Calculadora de Volúmenes\n5. Rangos cambiantes \nTu respuesta es: "))

    if select == 1:
        triangulo()

    elif select == 2:
        ppt()

    elif select == 3:
        km_millas()

    elif select == 4:
        vol()

    elif select ==5:
        ran()

if __name__ == "__main__":
    run()