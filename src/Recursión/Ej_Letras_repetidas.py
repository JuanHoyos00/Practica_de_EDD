


def letras_repetidas(palabra: str, i: int = 0, lista: set[str] = None, repetidas: list[str]  = None):
    if lista == None:
        lista = set()
    if repetidas == None:
        repetidas = []
    if i == len(palabra):
        if repetidas:
            return f"EL ÚLTIMO CARACTER EN REPETIRSE FUE: {repetidas[-1]}"
        else:
            return "NO HAY LETRAS QUE SE REPITEN."

    letra = palabra[i]
    if letra in lista:
        if letra not in repetidas:
            repetidas.append(letra)
    else:
        lista.add(letra)

    return letras_repetidas(palabra, i+1, lista, repetidas )

print(letras_repetidas("¿¿ HOLA, COMO ESTAS??"))




