
n1 = float(input("Número 1: "))
n2 = float(input("Número 2: "))

op = input("Operação (+, -, *, /): ")

if op == "+":
    print(n1 + n2)
elif op == "-":
    print(n1 - n2)
elif op == "*":
    print(n1 * n2)
elif op == "/":
    print(n1 / n2)
else:
    print("Operação inválida")
