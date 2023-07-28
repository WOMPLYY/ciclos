''' Escriba un programa para hacer un patrón como una pirámide
con números aumentados en 1.
   1
  2 3
 4 5 6
7 8 9 10

'''

num_filas = 4
numero = 1

for i in range(1, num_filas + 1):
    for j in range(num_filas - i):
        print(" ", end="")
    for numeros in range(1, i + 1):
        print(numero, end=" ")
        numero += 1
    print()
