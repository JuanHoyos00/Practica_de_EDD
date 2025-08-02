def sumatoria(lista, i=0, contador=0):
    if len(lista) == i:
        return contador

    contador += 1
    return sumatoria(lista, i+1, contador)

print(sumatoria([1,2,3,4]))