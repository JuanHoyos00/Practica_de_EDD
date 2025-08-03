def producto_numero_con_sumas(a: int, b: int, resultado: int = 0):
    if a < 0 or b < 0:
        return ValueError("Solo se permiten numeros enteros positivos")
    if a < b:
        a,b = b,a
    if b == 0:
        return resultado

    return producto_numero_con_sumas(a, b-1, resultado + a )

print(producto_numero_con_sumas(1,20))