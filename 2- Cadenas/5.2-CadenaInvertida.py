frase = input("Ingrese una frase: ")
palabra = frase.split(" ")
s = ""

for palabra in reversed(palabra):
    s += palabra
    s += " "

print(s)