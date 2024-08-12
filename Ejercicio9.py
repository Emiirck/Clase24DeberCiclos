
n = int(input("Ingrese el número de términos de la serie de Fibonacci que desea ver: "))

a, b = 0, 1
contador = 0

while contador < n:
    print(a)
    a, b = b, a + b
    contador += 1
