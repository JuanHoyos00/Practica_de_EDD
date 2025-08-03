def numero_primo(numero, i = 2):
    if numero < 2:
        return False
    if i * i > numero:
        return True
    if numero % i == 0:
        return False
    return numero_primo(numero, i+1)
print(numero_primo(23))
