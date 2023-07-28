""" Escriba un programa para mostrar la tabla de multiplicar de un entero dado. """

numero = int(
    input("Ingresa el numero que quieres ver su tabla de multiplicar: "))
contador = 1
while contador <= 10:
    resultado = numero * contador
    print(f"{numero} * {contador} = {resultado}")
    contador += 1
