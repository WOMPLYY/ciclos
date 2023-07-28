""" Escriba un programa para hacer un patrón como una pirámide con números aumentados en 1. """

x = 7

while x <= 7:
    print(x * "*")
    x += 1

xx = 4

while xx >= 0:
    print(xx * " ", "*")
    xx -= 1

xxx = 7

while xxx <= 7:
    print(xxx * "*")
    xxx += 1

print("")
print("en for")
print("")

for i in range(7, 6, -1):
    print(i * "*")
    i += 1

for i in range(4, -1, -1):
    print(i * " ", "*")
    i -= 1

for i in range(7, 6, -1):
    print(i * "*")
    i += 1

print("")
print("en for")
print("")

# a= 1
# for j in range(0, 7, -1):

#    print(" " * j + "*".join(a - i) for i in range(7, 0, -6))


#     j += 1

# for i in range(4, -1, -1):
#     print(i * " ", "*")
#     i -= 1

# for i in range(7, 6, -1):
#     print(i * "*")
#     i += 1
print("modokamikaze")
for i in range(7, 6, -1):
    print(i * "*")
    for x in range(4, -1, -1):
        print(x * " ", "*")
    print(i * "*")
