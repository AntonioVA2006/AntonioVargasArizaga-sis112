import random

def adivinar():
    # Lista de palabras creadas para este juego
    palabras = ["perro", "gato", "escuela", "calle", "auto"]
    
    # Con random.choice se escoge las palabra
    palabra = random.choice(palabras)
    
    #Se crea otra lista para reemplazar la palabra por _
    adivinanza = ["_"] * len(palabra) #len indica la cantidad de palabras
    intentos = 6
    oportunidad = set() #Aquí se almacena las palabras
    
    print("¡Bienvenido al juego del Ahorcado!")
    
    # El bucle termina cuando intentos sea 0 
    while intentos > 0 and "_" in adivinanza:
        print(f"\nPalabra: {' '.join(adivinanza)}")
        print(f"Intentos restantes: {intentos}")
        print(f"Letras intentadas: {', '.join(sorted(oportunidad)) if oportunidad else 'Ninguna'}")
        
        # Solicitar una letra pero se usa lower en el caso de que sea mayuscula
        letra = input("Introduce una letra: ").lower()
        
        # Si se repite la misma letra el programa mandara este mensaje
        if letra in oportunidad:
            print(f"Ya has intentado la letra '{letra}'. Intenta otra.")
            continue
        
        oportunidad.add(letra) #Y lo toma como intento
        
        # Verificar si la letra está en la palabra secreta
        indice = 0
        encontrada = False
        while indice < len(palabra):
            if palabra[indice] == letra:
                adivinanza[indice] = letra
                encontrada = True
            indice += 1
        
        if encontrada:
            print(f"¡Bien hecho! La letra '{letra}' está en la palabra.")
        else:
            intentos -= 1
            print(f"La letra '{letra}' no está en la palabra. Pierdes un intento.")
        
    # Aquí se verifica si el jugador ganó o perdió
    if "_" not in adivinanza:
        print(f"\n¡Felicidades! Adivinaste la palabra: {palabra}")
    else:
        print(f"\nLo siento, te has quedado sin intentos. La palabra era: {palabra}")

# Aquí se ejecuta la función
adivinar()