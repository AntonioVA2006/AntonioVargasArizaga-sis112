def suma(num1, num2):
    result = num1+num2
    print (result)
    seguir(result)
def resta(num1, num2):
    result = num1-num2
    print (result)
    seguir(result)
def multiplicacion(num1, num2):
    result = num1*num2
    print (result)
    seguir(result)
def division(num1,num2):
    result1 = num1/num2
    result = round(result1,2)
    print (result)
    seguir(result)
def seguir(result):
    print("Desea seguir");
    print("1. SI")
    print("2. NO")
    seguir = int(input())
    if seguir == 1:
        num1 = result
        num2 = int(input("Ingrese otro numero "))
        elec(num1, num2)
    else:
        print ("Gracias por su atencion")

def elec(num1, num2):
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    eleccion = int(input())
    if eleccion == 1:
        suma(num1, num2)
    elif eleccion == 2:
        resta(num1, num2)
    elif eleccion == 3:
        multiplicacion(num1, num2)
    elif eleccion == 4:
        division(num1, num2)
print("CALCULADORA")
num1 = int(input("Inserte un numero "))
num2 = int(input("Inserte otro numero "))
elec(num1, num2)
