import random #Se importa libreria
def genList(lista, rango, Vmin, Vmax):
    n = 0
    while n<rango:
        num = random.randint(Vmin,Vmax)
        lista.append(num)
        n += 1
    return lista
lista = []
rango = int(input("Ingrese el rango: "))#Se determina la cantidad de elements
Vmin = int(input("Ingrese el valor minimo: "))
Vmax = int(input("Ingrese valor maximo: "))
genList(lista,rango, Vmin, Vmax)
print(lista)
print(type(lista))
print(len(lista))