print("CALCULADORA ¿Que opción desea usted?")
print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")
eleccion = int(input())
if eleccion == 1:
    num1 = int(input("Ingrese un numero "))
    num2 = int(input("Ingrese otro numero "))
    result = num1+num2
    print(num1, "+", num2, "=", result)
elif eleccion == 2:
    num1 = int(input("Ingrese un numero "))
    num2 = int(input("Ingrese otro numero "))
    result = num1 - num2
    print(num1, "-", num2, "=", result)
elif eleccion == 3:
    num1 = int(input("Ingrese un numero "))
    num2 = int(input("Ingrese otro numero "))
    result = num1 * num2
    print(num1, "x", num2, "=", result)
elif eleccion == 4:
    num1 = int(input("Ingrese un numero "))
    num2 = int(input("Ingrese otro numero "))
    result1 = num1 / num2
    result = round(result1, 2)
    print(num1, "/", num2, "=", result)