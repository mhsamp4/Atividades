
n = int(input("Digite um número: "))

if n <= 1:
    print("Não é primo")
else:
    primo = True
    i = 2
    while i < n:
        if n % i == 0:
            primo = False
            break
        i += 1

    if primo:
        print("É primo")
    else:
        print("Não é primo")
