from random import *

"""Práctica sobre Interacción entre Funciones 1
Crea una función (lanzar_dados) que arroje dos dados al azar y devuelva sus resultados:

La función debe retornar dos valores resultado, que se encuentren entre 1 y 6).

Dicha función no debe requerir argumentos para funcionar, sino que debe generar internamente los valores aleatorios.

Proporciona el resultado de estos dos dados a una función que se llame evaluar_jugada (es decir, esta segunda función debe recibir dos argumentos) y que retorne -sin imprimirlo- un mensaje según la suma de estos valores:

Si la suma es menor o igual a 6:

"La suma de tus dados es {suma_dados}. Lamentable"

Si la suma es mayor a 6 y menor a 10:

"La suma de tus dados es {suma_dados}. Tienes buenas chances"

Si la suma es mayor o igual a 10:

"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"

Pistas: utiliza el método choice o randint de la biblioteca random para elegir un valor al azar entre 1 y 6."""

def lanzar_dados():

    d1 = randint(1,6)

    d2 = randint(1,6)

    return d1,d2

def evaluar_jugada(d1,d2):

    suma_dados = 0

    suma_dados = d1 + d2

    if suma_dados <= 6:

        return {f"La suma de tus dados es {suma_dados}. Lamentable"}

    elif suma_dados > 6 and suma_dados < 10:

        return {f"La suma de tus dados es {suma_dados}. Tienes buenas chances"}

    else:

        return {f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"}

d1,d2 = lanzar_dados()

resultado = evaluar_jugada(d1, d2)

print(resultado)