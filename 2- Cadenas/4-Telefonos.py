telefono = input("Introduce el número de teléfono: ")

if telefono.startswith("54") and len(telefono) >= 13:
    sin_prefijo = telefono[2:]      #toma la cadena desde la posición 2 en adelante
    numero = sin_prefijo[:-4]       #toma la cadena quitando los últimos 4 caracteres
    print("Número sin prefijo ni extensión:", numero)
else:
    print("Formato inválido. Debe comenzar con 54 y tener 13 o más dígitos.")
    numero = None
