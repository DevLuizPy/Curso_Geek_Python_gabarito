""" Exercicio 1 """

matriz_4x4 = []
for i in range(4):
    linha = []
    for j in range(4):
        valor = int(input(f"Digite o valor para a posição ({i}, {j}): "))
        linha.append(valor)
    matriz_4x4.append(linha)

contador = 0
for linha in matriz_4x4:
    for valor in linha:
        if valor > 10:
            contador += 1

print(matriz_4x4)
print(contador)

""" Exercicio 2 """

matriz_5x5 = []
for i in range(5):
    linha_1 = []
    for j in range(5):
        if j == i:
            valor = 1
            linha_1.append(valor)
        else:
            valor = 0
            linha_1.append(valor)
    matriz_5x5.append(linha_1)

for linha_1 in matriz_5x5:
    print(' '.join(map(str, linha_1)))

""" Exercicio 4 """

matriz_4x4_1 = []
for i in range(4):
    linha_2 = []
    for j in range(4):
        valor = int(input(f"Digite o valor para a posição ({i}, {j}): "))
        linha_2.append(valor)
    matriz_4x4_1.append(linha_2)

maior_valor = matriz_4x4_1[0][0]
for linha_2 in matriz_4x4_1:
    for valor in linha_2:
        if valor > maior_valor:
            maior_valor = valor
print(maior_valor)

