def media(lista):
    if len(lista) == 0:  # evitar división por cero
        return None
    return sum(lista) / len(lista)

numeros = [4, 8, 15, 16, 23, 42]
print(f"La media es: {media(numeros):.2f}")