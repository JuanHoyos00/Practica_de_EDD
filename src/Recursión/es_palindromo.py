def es_palindromo(palabra: str, i: int = 0, j:int = -1) -> bool:
    if len(palabra)== 0:
        return False
    if len(palabra) == 1:
        return True
    if palabra[i] != palabra[j]:
        return False
    if len(palabra)//2 == i+1:
        return True



    return es_palindromo(palabra, i+1, j-1)
print(es_palindromo(""))