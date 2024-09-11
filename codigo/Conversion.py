import funciones_conversion as fc #Importamos y el as es para acortar
def menu():
    print ("Que desea convertir?")
    print("1. Metros a Kilometros")
    print("2. Kilometros a Metros")
    print("3. Gramos a Kilogramos")
    print("4. Kilogramos a gramos")
    print("5. Grados Celsius a Fahrenheit")
    print("6. Grados Fahrenheit a Celsius")
    print("7. Salir") #Hemos imprimido un menu para el usuario
while True:
    menu() #Eso lleva al menu
    opcion = int(input("Que opcion usted elige: "))
    if opcion == 7:
        break #Si el usuario elige 7, se cierra el programa
    #Si no se elige 7, el programa continua
    else:
        num1 = float(input("Ingrese la cantidad: "))
        if opcion == 1:
            print(f"Resultado: {fc.longitud1(num1)}") #Así convocamos a una funcion del otro documento
        elif opcion == 2:
            print(f"Resultado: {fc.longitud2(num1)}") #Se acorto la escritura gracias al as y la abreviatura
        elif opcion == 3:
            print(f"Resultado: {fc.masa1(num1)}")
        elif opcion == 4:
            print(f"Resultado: {fc.masa2(num1)}")
        elif opcion == 5:
            print(f"Resultado: {fc.temperatura1(num1)}")
        elif opcion == 6:
            print(f"Resultado: {fc.temperatura2(num1)}")
        else:
            print("opcion no valida")
