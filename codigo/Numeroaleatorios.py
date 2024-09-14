import random
intento = 1
opcion = 0
numeroal=random.randint(1,100)

print("Adivine el número")

while True:
    opcion = int(input("Introduce el numero: "))
    if opcion<numeroal:
        print("Demasiado bajo. Intenta de nuevo")
        intento=intento+1
    elif opcion>numeroal:
        print("Demasiado Alto. Intenta de nuevo")
        intento=intento+1
    elif opcion==numeroal:
        print("Felicidades has logrado logrado adivinar el numero")
        print("Lo has logrado en", intento, "intentos")
        break
