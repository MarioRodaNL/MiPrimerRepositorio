def iva(precio, iva=21):        #hace que si el usuario no pasa ese parámetro, se use 21 automáticamente.
    preciofinal = precio * (1 + iva / 100)
    return preciofinal

print(f"Factura 1: ${iva(1000, 10):.2f}")   # con IVA del 10%
print(f"Factura 2: ${iva(2000):.2f}")      # sin especificar → aplica 21%