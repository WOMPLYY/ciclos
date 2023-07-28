"""  """

n = []
facto = 1

numfacto = int(
    input("ingrese el numero al que quiere sacar el NumeroFactorial:  "))

for i in range(numfacto, 1, -1):
    n.append(i)

    cadena = '*'.join(map(str, n))

    facto *= i

print(f"El factorial de {numfacto} es {cadena} = {facto}")
