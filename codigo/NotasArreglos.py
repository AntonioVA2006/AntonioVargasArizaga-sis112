estudiantes = []
n = int(input("numeros de notas: ")) #Ingrese la cantidad de listas
while n>0:
    estudiantes.append(int(input(f"ingrese notas {n} = "))) #Ahí se ingrese las notas
    n -= 1 #El bucle termina cuando n sea 0 termina el bucle
print(estudiantes) #Después de que termine el bucle muestra la lista