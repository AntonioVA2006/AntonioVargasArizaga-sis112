if __name__ == '__main__':
    n = int(input())
    i = 1
    resultado = ""

    while n >= i:
        resultado += str(i)
        i = i+1

    print(resultado)
