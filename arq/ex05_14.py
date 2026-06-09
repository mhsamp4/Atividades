
soma = 0
contador = 0

while True:
    num = int(input("Digite um número (0 para sair): "))
    if num == 0:
        break
    soma += num
    contador += 1

if contador > 0:
    media = soma / contador
else:
    media = 0

print("Quantidade:", contador)
print("Soma:", soma)
print("Média:", media)
