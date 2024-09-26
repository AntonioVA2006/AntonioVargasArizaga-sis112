def menu():
    print("""==== SISTEMA DE GESTIÓN DE NOTAS ====
    1. Agregar nota
    2. Eliminar nota
    3. Modificar nota
    4. Mostrar todas las notas
    5. Calcular promedio
    6. Obtener nota máxima y mínima
    7. Salir""")
def add_nota(notas):
    a=int(input("ingrese nota: "))
    notas.append(a)
    return notas
def del_notas(notas):
    ind=len(notas)
    a=int(input("Ingrese un indice: "))
    notas.pop(a)
    return notas
def mod_nota(notas):
    a=int(input("Ingrese indice a modificacion: "))
    b = float(input(f"Ingrese el numero a modificar de la lista {a}: "))
    notas[a]=b
    return notas
def mos_nota(notas):
    mostrar = notas
    return mostrar
def cal_nota(notas):
    ind = len(notas)
    sumaparcial = notas[0]+notas[1]
    if ind<2:
        promedio = sumaparcial/ind
    else:
        n = 2
        while n < ind:
            suma = sumaparcial + notas[n]
            sumaparcial = suma
            n += 1
    promedio = sumaparcial/ind
    return promedio
def max_min(notas):
    maximo = max(notas)
    minimo = min(notas)
    print("La maxima nota es: ", maximo)
    print("La minima nota es: ", minimo)