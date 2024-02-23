from random import *
print("*****************************")
print("JUEGO: ADIVINA EL NUMERO!!")
print("*****************************")
nombre= (input("Decime tu nombre: "))
print(f"Bueno, {nombre},he pensado un número entre 1 y 100, y tienes solo ocho intentos para adivinar.")
numeroRandom= randint(1,100)
intentos =0
while intentos < 8:
    numero = int(input(' Cuál crees que es el número?: '))
    intentos += 1
    if numero not in range(1,101):
        print("Lo siento. El numero ingresado NO es un numero valido. Debe ser entre 1 y 100")

    if numero < numeroRandom :
        print("El numero es MAYOR al elegido")

    elif numero > numeroRandom:
        print("El numero es MENOR al elegido")
    else:
        print(f"Felicitaciones {nombre} has acertado! has adivinado en {intentos} intentos")
        break
if numero != numeroRandom:
    print(f"Lo siento {nombre} se han acabado los intentos. El numero a adivinar era: {numeroRandom}")
