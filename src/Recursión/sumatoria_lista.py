def sumatoria(lista: list[int], i: int = 0, suma: int = 0 ) -> int:

    if not lista:
        return 0

    if len(lista) == i:
        return suma

    suma += lista[i]

    return sumatoria(lista, i+1, suma)

print(sumatoria([12,12]))
