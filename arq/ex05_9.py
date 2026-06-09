
a = int(input("Dividendo: "))
b = int(input("Divisor: "))

quociente = 0
resto = a

while resto >= b:
    resto -= b
    quociente += 1

print("Quociente:", quociente)
print("Resto:", resto)
