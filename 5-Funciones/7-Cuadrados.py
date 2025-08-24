def cuadrados(lista):
    nueva_lista = []
    for num in lista:
        nueva_lista.append(num ** 2)    #Se agrega a la lista vacia el cuadrado del número
    return nueva_lista

numeros = [1, 2, 3, 4, 5]
print(f"Lista original: {numeros}")
print(f"Lista de cuadrados: {cuadrados(numeros)}")