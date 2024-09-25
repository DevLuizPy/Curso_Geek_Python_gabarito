""" Exercicio 1 """

numero = 1
multiplo = []
while numero <= 15:
    if numero % 3 == 0:
        multiplo.append(numero)
    numero += 1

print(multiplo)

""" Exercicio 2 """

numero_1 = 10
while numero_1 >= 0:
    if numero_1 == 0:
        print(numero_1)
        print("Fim")
    else:
        print(numero_1)
    numero_1 -= 1

""" Exercicio 3 """

numero_2 = 0
while numero_2 <= 100_000:
    print(numero_2)
    numero_2 += 1000
