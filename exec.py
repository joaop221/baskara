import math

a = int(input("insira o valor de A: "))
b = int(input("insira o valor de B: "))
c = int(input("insira o valor de C: "))

delta = b*b - 4*a*c

print("delta igual a:", delta)

doisA = 2*a

if delta > 0:
    raiz = math.sqrt(delta)
    x1 = -b + raiz
    x2 = -b - raiz
    print("para delta positivo dois valores de x")
    print("valor de x1 igual a:", x1 / doisA)
    print("valor de x2 igual a:", x2 / doisA)

elif delta == 0:
    print("para delta igual a 0 somente um valor de x")
    print("valor de x1 e x2 igual a:", -b / doisA)

else:
    print("não existe valor de x para delta negativo.")
