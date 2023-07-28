""" Escribe un programa para leer 10 números del teclado y encontrar
su suma y promedio. """

con = 1
n = []
for i in range(1, 11):
    # append es pa agregar numero al array
    n.append(float(input(f"ingresa un numero {con} ")))
    con += 1

prom = sum(n)/10
print(f"EL promedio del total es numeros ingresados es: {prom}")
