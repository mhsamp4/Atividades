
vel = float(input("Velocidade: "))
if vel > 80:
    multa = (vel - 80) * 5
    print("Multado! Valor:", multa)
else:
    print("Dentro do limite")
