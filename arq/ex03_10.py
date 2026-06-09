
salario = float(input("Salário: "))
percentual = float(input("Aumento (%): "))

aumento = salario * percentual / 100
novo = salario + aumento

print("Aumento:", aumento)
print("Novo salário:", novo)
