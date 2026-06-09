
a = int(input("Número 1: "))
b = int(input("Número 2: "))
c = int(input("Número 3: "))

maior = a
menor = a

if b > maior:
    maior = b
if c > maior:
    maior = c

if b < menor:
    menor = b
if c < menor:
    menor = c

print("Maior:", maior)
print("Menor:", menor)
