import random

palabras = ["gallina", "gallo", "pollo", "cerdo", "vaca",
            "toro", "caballo", "oveja", "perro", "gato", "cuyo"]

palabra_secreta = random.choice(palabras)
letras_adivinadas = []
intentos = 3

print("Bienvenido al juego del ahorcado")
print("Adivina el animal de la granja")
print(f"Solo tienes {intentos} vidas\n")

while intentos > 0:
    # Crear la visualización actual
    display = [letra if letra in letras_adivinadas else "_" for letra in palabra_secreta]
    print(" ".join(display))

    if "_" not in display:
        print("\n¡Felicidades! Has adivinado la palabra:", palabra_secreta)
        break

    letra = input("Ingresa una letra: ").lower()

    if letra in palabra_secreta:
        if letra not in letras_adivinadas:
            letras_adivinadas.append(letra)
            print("¡Bien! Letra correcta.\n")
        else:
            print("Ya habías adivinado esa letra.\n")
    else:
        intentos -= 1
        print(f"Letra incorrecta. Te quedan {intentos} vidas.\n")
else:
    print("Te quedaste sin vidas. La palabra era:", palabra_secreta)