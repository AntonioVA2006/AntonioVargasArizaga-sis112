estudiantes = []
suma=0
i=1
n = int(input("numeros de notas: ")) #Ingrese la cantidad de estudiantes
n1 = n
while n1>0:
    estudiantes.append(int(input(f"ingrese la nota del estudiante {n1} = "))) #Ahí se ingrese las notas
    n1 -= 1 #El bucle termina cuando n sea 0 termina el bucle
if n<3:
    suma = estudiantes[0]+estudiantes[1] #En el caso de solo sacar el promedio de solo dos alumnos
else:
    sumaparcial= estudiantes[0]+estudiantes[1] #Aquí se suma los primeros dos elementos
    m = 2 
    while m<n:
        suma = float(sumaparcial+estudiantes[m]) #De esa manera sumamos los primeros tres elementos
        sumaparcial = suma #Declaramos a la suma como sumaparcial para que siga con el bucle
        m += 1 #Y para esto también tenemos que suma a uno
float(suma)
promedio=suma/n
print("El promedio es: ", promedio)
print(estudiantes) #Después de que termine el bucle muestra la lista