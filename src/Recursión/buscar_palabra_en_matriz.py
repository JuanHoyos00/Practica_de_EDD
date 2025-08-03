import random as rd
import string
n: int = 5
mi_matriz: list[list[str]] = []
for _ in range(n):
    fila = [rd.choice(string.ascii_uppercase)for _ in range(n)]
    mi_matriz.append(fila)


#mi_matriz: list[list[str]] = [['I', 'G', 'B', 'U', 'D'], ['W', 'U', 'B', 'B', 'Z'], ['M', 'R', 'M', 'Q', 'O'], ['I', 'D', 'N', 'G', 'Q'], ['C', 'M', 'F', 'F', 'E']]
for filas in mi_matriz:
    print(filas)


def buscar_palabra_en_matriz(mi_matriz: list[list[str]], palabra: str, fila: int = n-1, columna:int = 0, indice: int = 0, N: int = n) -> bool:
    if len(palabra) == 0:
        return False
    if fila < 0:
        return False
    if columna < N:
        if mi_matriz[fila][columna] != palabra[indice]:
            return buscar_palabra_en_matriz(mi_matriz, palabra, fila, columna+1, indice=0,)

        if mi_matriz[fila][columna] == palabra[indice]:
            if len(palabra) == indice+1:
                return True
            else:
                return buscar_palabra_en_matriz(mi_matriz,palabra,fila,columna+1,indice+1)


    return buscar_palabra_en_matriz(mi_matriz,palabra,fila-1,columna=0,indice=0)

print(buscar_palabra_en_matriz(mi_matriz,"ABC"))




