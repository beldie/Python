from random import choice

print("*********************")
print(f'Juego: "El ahorcado"')

palabras = ['panadero', 'otorrinonaringologo', 'mesada', 'costumbres', 'desafios', 'aprendiendo', "humanidad",
            'hermana', 'criatura']
letras_correctas = []
letras_incorrectas = []
intentos = 6
aciertos = 0
juego_terminado = False


def elegir_palabra(lista_palabras):
    palabra_elegida = choice(lista_palabras)
    letras_unicas = len(set(palabra_elegida))

    return palabra_elegida, letras_unicas


def pedir_letra():
    letra_elegida = ''
    es_valida = False
    abecedario = 'abcdefghijklmnopqrstuvwxyz'
    while not es_valida:
        letra_elegida = input("Elige una letra:").lower()
        if letra_elegida in abecedario and len(letra_elegida) == 1:
            es_valida = True
        else:
            print("Letra incorrecta! ")
    return letra_elegida


def mostrar_nuevo_tablero(palabra_elegida):
    lista_oculta = []
    for l in palabra_elegida:
        if l in letras_correctas:
            lista_oculta.append(l)
        else:
            lista_oculta.append('-')
    print(f"La palabra a adivinar es: " + ' '.join(lista_oculta))


def chequear_letra(letra_elegida, palabra_oculta, vidas, coincidencias):
    fin = False
    if letra_elegida in palabra_oculta and letra_elegida not in letras_correctas:
        letras_correctas.append(letra_elegida)
        coincidencias += 1
    elif letra_elegida in palabra_oculta and letra_elegida in letras_correctas:
        print("Ya has encontrado esa letra")
    elif letra_elegida not in letras_incorrectas:
        letras_incorrectas.append(letra_elegida)
        vidas -= 1
        print("Esta letra no esta en la palabra. Intenta con otra diferente")
    else:
       # letras_incorrectas.append(letra_elegida)
        #vidas -= 1
       print("Ya has intentado esa letra y es incorrecta, elige otra diferente.")
    if vidas == 0:
        fin = perder()
    elif coincidencias == letras_unicas:
        fin = ganar(palabra_oculta)
    return vidas, fin, coincidencias
