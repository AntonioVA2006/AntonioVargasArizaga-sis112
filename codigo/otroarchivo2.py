import otroarchivo as fun
notas=[]
promedio = 0
while True:
    fun.menu()
    eleccion = int(input("Elija una opcion: "))
    if eleccion == 7:
        print("==SALIENDO DEL PROGRAMA==")
        break
    else:
        if eleccion == 1:
            fun.add_nota(notas)
        if eleccion == 2:
            fun.del_notas(notas)
        if eleccion == 3:
            fun.mod_nota(notas)
        if eleccion == 4:
            mostrar = fun.mos_nota(notas)
            print(mostrar)
        if eleccion == 5:
            promedio=fun.cal_nota(notas)
            print(promedio)
        if eleccion == 6:
            fun.max_min(notas)
        else:
            print("Opcion no valida")