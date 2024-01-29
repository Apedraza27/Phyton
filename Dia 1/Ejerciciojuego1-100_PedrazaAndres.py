# Importar el módulo random
import random

# Definir la función que simula el juego
def guess_the_number():
    # Seleccionar aleatoriamente un número secreto entre 1 y 100
    secret_number = random.randint(1, 100)
    # Inicializar el número de intentos en cero
    num_guesses = 0
    # Dar la bienvenida y explicar las instrucciones
    print("¡Bienvenido al juego de adivinanza de números!")
    print("El objetivo es adivinar el número secreto en la menor cantidad de intentos posible.")
    print("Tienes un total de 10 intentos para adivinar el número secreto.")
    # Iterar hasta que el usuario adivine correctamente o agote los 10 intentos
    while num_guesses < 10:
        # Solicitar al usuario ingresar un número
        guess = input("Ingresa un número entre 1 y 100: ")
        # Manejar eventos como entrada no válida (por ejemplo, si el usuario ingresa algo que no es un número)
        try:
            guess = int(guess)
            if guess < 1 or guess > 100:
                print("El número debe estar entre 1 y 100.")
                continue
        except ValueError:
            print("Debes ingresar un número.")
            continue
        # Incrementar el número de intentos
        num_guesses += 1
        # Dar pistas indicando si el número secreto es mayor o menor que la suposición del usuario
        if guess < secret_number:
            print("El número secreto es mayor que tu suposición.")
        elif guess > secret_number:
            print("El número secreto es menor que tu suposición.")
        else:
            # Si el usuario adivina correctamente, mostrar en cuántos intentos lo logró
            print(f"¡Felicidades! Adivinaste el número secreto en {num_guesses} intentos.")
            break
    else:
        # Si el usuario agota los 10 intentos, mostrar el número secreto y un mensaje de consolación
        print(f"Lo siento, no adivinaste el número secreto. El número era {secret_number}.")
        
    print("¡Gracias por jugar al juego de adivinanza de números!")
    print("Recuerda que puedes volver a jugar en cualquier momento.")
