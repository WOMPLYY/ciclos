""" Escriba un programa para mostrar el patrón como un triángulo rectángulo con un número.
El patrón como:
1
12
123
1234
12345 """

numeros = ""
contador = 1
for i in range(1, 6):

    numeros = numeros + str(contador)

    print(numeros)
    contador += 1
