""" Exercicio 1 """
import statistics
import math

vetor_a = [1, 0, 5, -2, -5, 7]

soma_simples = vetor_a[0] + vetor_a[1] + vetor_a[5]
print(soma_simples)

vetor_a[4] = 100

for numero in vetor_a:
    print(numero)

""" Exercicio 2 """

lista_1 = []
for _ in range(6):
    numero_inteiro = int(input('Escreva um numero inteiro'))
    if numero_inteiro > 1:
        lista_1.append(numero_inteiro)
    else:
        print('Dados invalidos')

print(lista_1)

""" Exercicio 3 """

lista_2 = []
lista_3 = []
for _ in range(10):
    numero_real = float(input('Escreva um numero real'))
    lista_2.append(numero_real)

soma_quadrado = 0
for numero_real in lista_2:
    quadrado = (numero_real ** 2)
    lista_3.append(soma_quadrado)

print("Conjunto original:", lista_2)
print("Conjunto dos quadrados:", lista_3)

""" Exercicio 4 """

vetor_1 = []
for _ in range(8):
    valores = float(input('Escreva um numero real: '))
    vetor_1.append(valores)

indice_x = int(input('Escreva um número entre 0 a 7: '))
indice_y = int(input('Escreva um número entre 0 a 7: '))

if 0 <= indice_x <= 7 and 0 <= indice_y <= 7:
    soma_1 = vetor_1[indice_x] + vetor_1[indice_y]
    print(f'A soma dos valores nas posições {indice_x} e {indice_y} é: {soma_1}')
else:
    print('Os valores de X e Y devem estar entre 0 e 7.')

""" Exercicio 5 """

vetor_2 = []

for _ in range(10):
    valores_1 = int(input('Escreva um numero: '))
    vetor_2.append(valores_1)

contagem_pares_1 = 0
pares = []

for valores_1 in vetor_2:
    if valores_1 % 2 == 0:
        contagem_pares = + 1
        pares.append(valores_1)


print(f'A quantidade de números pares nesse vetor foi de {contagem_pares_1} e eles são respectivamente{pares}')

""" Exercicio 6 """

vetor_3 = []
for _ in range(10):
    valores_2 = int(input('Escreva um numero: '))
    vetor_3.append(valores_2)

maior_valor = max(vetor_3)
menor_valor = min(vetor_3)

print(f'O maior valor desse vetor é {maior_valor}, enquanto o menor valor é {menor_valor}')

""" Exercicio 7 """

vetor_4 = []
for _ in range(10):
    valores_3 = int(input('Escreva um numero inteiro: '))
    if valores_3 >= 1:
        vetor_4.append(valores_3)

maior_valor_1 = max(vetor_4)
indice_maior = vetor_4.index(maior_valor_1)
print(f'O maior valor desse vetor é {maior_valor_1}, enquanto o indice desse maior valor é {indice_maior}, e o vetor '
      f'em si é {vetor_4}')

""" Exercicio 8 """

vetor_5 = []
for _ in range(10):
    valores_4 = int(input('Escreva um numero inteiro: '))
    if valores_4 >= 1:
        vetor_4.append(valores_4)

vetor_4.reverse()
print(f'Valores na ordem inversa: {vetor_4}')

""" Exercicio 9 """

vetor_6 = []
while vetor_6.__len__() < 6:
    valores_5 = int(input('Escreva um numero inteiro par: '))
    if valores_5 % 2 == 0:
        vetor_6.append(valores_5)
    else:
        print('Dado invalido')

vetor_6.reverse()
print(f'Valores na ordem inversa: {vetor_6}')

""" Exercicio 10 """

vetor_6 = []
for _ in range(15):
    valores_5 = int(input('Escreva a nota da sua prova: '))
    if valores_5 >= 1:
        vetor_6.append(valores_5)

media_1 = statistics.mean(vetor_6)
print(f'A média da turma é {media_1}')

""" Exercicio 11 """

vetor_7 = []
contagem_negativo = 0
soma_1 = 0
for _ in range(10):
    valores_6 = float(input('Escreva um numero real: '))
    vetor_7.append(valores_6)
    if valores_6 < 0:
        contagem_negativo = contagem_negativo + 1
    elif valores_6 > 0:
        soma_1 = valores_6 + soma_1

print(f'A quantidade de numeros negativos é {contagem_negativo} números, enquanto a soma dos positivos é'
      f' {soma_1}')

""" Exercicio 12 """

vetor_8 = []
for _ in range(5):
    valores_7 = float(input('Escreva um valor: '))
    vetor_8.append(valores_7)

media_2 = statistics.mean(vetor_8)
maior_valor_2 = max(vetor_8)
menor_valor_2 = min(vetor_8)
print(f'A média dos valores é {media_2}, enquanto o maior valor é {maior_valor_2}, e o menor valor é {menor_valor_2}')

""" Exercicio 13 """

vetor_9 = []
for _ in range(5):
    valores_8 = float(input('Escreva um valor: '))
    vetor_8.append(valores_8)

maior_valor_3 = max(vetor_9)
menor_valor_3 = min(vetor_9)
indice_maior_1 = vetor_9.index(maior_valor_3)
indice_menor_1 = vetor_9.index(menor_valor_3)
print(f'O indice do maior valor é {indice_maior_1}, e o indice do menor valor é {indice_menor_1}')

""" Exercicio 14 """

vetor_10 = []
for _ in range(10):
    valores_9 = float(input('Escreva um valor: '))
    vetor_10.append(valores_9)

valores_iguais = set()
valores_vistos = set()

for valor in vetor_10:
    if valor in valores_vistos:
        valores_iguais.add(valor)
    else:
        valores_vistos.add(valor)

print(f'Valores iguais encontrados: {valores_iguais}')

""" Exercicio 15 """

vetor_11 = []
for _ in range(20):
    valores_10 = float(input('Escreva um valor: '))
    vetor_11.append(valores_10)

vetor_sem_repeticao = set(vetor_11)

print(vetor_sem_repeticao)

""" Exercicio 16 """

vetor_12 = []
for _ in range(5):
    valores_11 = float(input('Escreve um número real: '))
    vetor_12.append(valores_11)

codigo_1 = int(input('Escreva um codigo: 1 para ordem direta, 2 para ordem inversa'))

if codigo_1 == 1:
    print(vetor_12)
elif codigo_1 == 2:
    print(vetor_12.reverse())
else:
    print('Codigo inválido')

""" Exercicio 17 """

vetor_13 = []
for _ in range(10):
    valores_12 = float(input('Escreva um valor: '))
    if valores_12 > 0:
        vetor_13.append(valores_12)
    else:
        vetor_13.append(0)

""" Exercicio 18 """

vetor_14 = []
vetor_15 = []
for _ in range(10):
    valores_13 = float(input('Escreve um valor: '))
    vetor_14.append(valores_13)

codigo_2 = int(input('Escreva um número qualquer: '))

for valor in vetor_14:
    if valor % codigo_2 == 0:
        vetor_15.append(valor)
    else:
        ''
print(f'A quantidade de multiplos de de {codigo_2} contidos no vetor é {len(vetor_15)} e eles são respectivamente {vetor_15}')

""" Exercicio 19 """

vetor_16 = []
for valor in range(50):
    valores_12 = (valor + 5 * valor) % (valor + 1)
    vetor_16.append(valores_12)

print(vetor_16)

""" Exercicio 20 """

vetor_17 = []
vetor_18 = []
num_1 = 0
while num_1 <= 10:
    valores_14 = int(input('Escreva um valor entre 0 a 50: '))
    if 0 <= valores_14 <= 50:
        vetor_17.append(valores_14)
        num_1 += 1
    else:
        print('Valor invalido')

for valor in vetor_17:
    if valor % 2 != 0:
        vetor_18.append(valor)

for i in range(0, len(vetor_17), 2):
    if i+1 < len(vetor_17):
        print(vetor_17[i], vetor_17[i+1])
    else:
        print(vetor_17[i])

for i in range(0, len(vetor_18), 2):
    if i+1 < len(vetor_18):
        print(vetor_18[i], vetor_18[i+1])
    else:
        print(vetor_18[i])

""" Exercicio 21 """

vetor_19 = []
for _ in range(10):
    valores_15 = float(input('Escreve um valor para o primeiro vetor: '))
    vetor_19.append(valores_15)

vetor_20 = []
for _ in range(10):
    valores_16 = float(input('Escreve um valor para o segundo vetor: '))
    vetor_20.append(valores_16)

vetor_21 = []
for i in range(10):
    valor_1 = vetor_19[i] - vetor_20[i]
    vetor_21.append(valor_1)

print(vetor_21)

""" Exercicio 22 """

vetor_21 = []
for _ in range(10):
    valores_17 = float(input('Escreve um valor para o primeiro vetor: '))
    vetor_21.append(valores_17)

vetor_22 = []
for _ in range(10):
    valores_18 = float(input('Escreve um valor para o segundo vetor: '))
    vetor_22.append(valores_18)

vetor_23 = []
for i in range(10):
    if i % 2 == 0:
        vetor_23.append(vetor_21[i])
    else:
        vetor_23.append(vetor_22[i])

print(vetor_23)

""" Exercicio 23 """

vetor_23 = []
produto_escalar = 0
for _ in range(5):
    valores_19 = float(input('Escreve um valor para o primeiro vetor: '))
    vetor_23.append(valores_19)

vetor_24 = []
for _ in range(5):
    valores_20 = float(input('Escreve um valor para o segundo vetor: '))
    vetor_24.append(valores_20)

for i in range(5):
    produto_escalar = produto_escalar + (vetor_23[i] * vetor_24[i])

print(vetor_23)
print(vetor_24)
print(produto_escalar)

""" Exercicio 24 """

dicionario = dict()
for _ in range(10):
    chave = input("Digite a chave para o dicionário: ")
    altura_aluno = input(f"Digite o valor para a chave '{chave}': ")
    dicionario[chave] = altura_aluno

alturas = list(dicionario.values())
maior_altura = max(alturas)
menor_altura = min(alturas)

for chave, valor in dicionario.items():
    if valor >= maior_altura:
        maior_altura = valor
        maior_chave = chave
    elif valor <= menor_valor:
        menor_valor = valor
        menor_chave = chave
print(maior_chave)
print(maior_altura)
print(menor_chave)
print(maior_altura)

""" Exercicio 25 """

vetor_25 = []

valor = 0
while len(vetor_25) < 100:
    if valor % 7 != 0 and valor % 10 != 0:
        vetor_25.append(valor)
    valor = valor + 1

print(vetor_25)
print(len(vetor_25))


""" Exercicio 26 """

vetor_26 = []
for _ in range(10):
    valores_21 = float(input('Escreva um valor para o vetor: '))
    vetor_26.append(valores_21)

media_3 = statistics.mean(vetor_26)

desvio = 0
for valor in vetor_26:
    desvio = desvio + (valor - media_3) ** 2

desvio_padrao = math.sqrt((1/len(vetor_26)+1) * desvio)

print("Vetor:", vetor_26)
print("Média:", media_3)
print("Desvio padrão:", desvio_padrao)

""" Exercicio 27 """

vetor_27 = []
for _ in range(10):
    valores_22 = int(input('Escreva um valor para o vetor: '))
    vetor_27.append(valores_22)

for valor in vetor_27:
    if valor <= 1:
        print(f'{valor} não é primo')
    elif valor == 2:
        print(f'{valor} é primo')
        print(f'Índice de {valor} no vetor: {vetor_27.index(valor)}')
    elif valor % 2 == 0:
        print(f'{valor} não é primo')
    else:
        primo = True
        limite = int(math.sqrt(valor)) + 1
        for i in range(3, limite, 2):
            if valor % i == 0:
                primo = False
                break
        if primo:
            print(f'{valor} é primo')
            print(f'Índice de {valor} no vetor: {vetor_27.index(valor)}')


""" Exercicio 28 """

vetor_28 = []
for _ in range(10):
    valores_23 = int(input('Escreva um valor para o vetor: '))
    vetor_28.append(valores_23)

vetor_29 = []
for valor in vetor_28:
    if valor % 2 != 0:
        vetor_29.append(valor)  # Numero impar

vetor_30 = []
for valor in vetor_30:
    if valor % 2 == 0:
        vetor_30.append(valor)  # Numero par

print(vetor_29)
print(vetor_30)

""" Exercicio 29 """

vetor_31 = []
i = 0
soma_par = 0
soma_impar = 0
while i < 6:
    valores_24 = int(input('Escreva um número inteiro: '))
    if valores_24 > 0:
        vetor_31.append(valores_24)
        i = i + 1
    else:
        print('Dados invalidos')
for valor in vetor_31:
    if valor % 2 == 0:
        print(f'{valor} é par')
        soma_par += valor
    else:
        print(f'{valor} é impar')
        soma_impar += valor

print(soma_par)
print(soma_impar)

""" Exercicio 30 """

vetor_32 = []
for _ in range(10):
    valores_25 = float(input('Escreva um valor para o primeiro vetor: '))
    vetor_32.append(valores_25)

vetor_33 = []
for _ in range(10):
    valores_26 = float(input('Escreva um valor para o segundo vetor: '))
    vetor_33.append(valores_26)

conjunto_1 = set(vetor_32)
conjunto_2 = set(vetor_33)

print(conjunto_1.intersection(conjunto_2))

""" Exercicio 31 """

vetor_34 = []
for _ in range(10):
    valores_27 = float(input('Escreva um valor para o primeiro vetor: '))
    vetor_34.append(valores_27)

vetor_35 = []
for _ in range(10):
    valores_28 = float(input('Escreva um valor para o segundo vetor: '))
    vetor_35.append(valores_28)

conjunto_3 = set(vetor_34)
conjunto_4 = set(vetor_35)

print(conjunto_3.union(conjunto_4))

""" Exercicio 32 """

vetor_36 = []
for _ in range(5):
    valores_29 = float(input('Escreva um valor para o primeiro vetor: '))
    vetor_36.append(valores_29)

vetor_37 = []
for _ in range(5):
    valores_30 = float(input('Escreva um valor para o segundo vetor: '))
    vetor_37.append(valores_30)

vetor_38 = []
for i in range(0, 5):
    valores_31 = vetor_36[i] + vetor_37[i]
    vetor_38.append(valores_31)

print(vetor_38)

vetor_39 = []
for i in range(0, 5):
    valores_32 = vetor_36[i] * vetor_37[i]
    vetor_39.append(valores_32)

print(vetor_39)

vetor_40 = []
for i in range(0, 5):
    valores_33 = vetor_36[i] - vetor_37[i]
    vetor_40.append(valores_33)

print(vetor_40)

conjunto_5 = set(vetor_36)
conjunto_6 = set(vetor_37)

print(conjunto_5.intersection(conjunto_6))

print(conjunto_5.union(conjunto_6))

""" Exercicio 33 """

# Inicializando o vetor com 15 zeros
vetor = [0] * 15

# Recebendo valores do usuário para preencher o vetor
for i in range(15):
    vetor[i] = float(input(f'Escreva um valor para a posição {i+1} do vetor: '))

# Compactando o vetor
j = 0  # índice para percorrer o vetor original
i = 0  # índice para posicionar os elementos não zero compactados

while j < 15:
    if vetor[j] != 0:
        vetor[i] = vetor[j]
        i += 1
    j += 1

# Preenchendo o restante do vetor com zeros, se houver
while i < 15:
    vetor[i] = 0
    i += 1

print("Vetor compactado:", vetor)

""" Exercicio 34 """

i = 0
vetor_41 = []
while i < 10:
    valor_2 = float(input('Escreva um valor para o vetor: '))
    if valor_2 in vetor_41:
        print('dados invalidos')
    else:
        vetor_41.append(valor_2)
        i = i + 1

print(vetor_41)

""" Exercicio 35 """


def num_para_vetor(num):
    """Converte um número num vetor de algarismos, do menos para o mais significativo."""
    vetor = []
    while num > 0:
        vetor.append(num % 10)
        num //= 10
    return vetor


def soma_vetores(vetor_a, vetor_b):
    """Soma dois vetores de algarismos, simulando a soma de números inteiros."""
    resultado = []
    carry = 0
    max_len = max(len(vetor_a), len(vetor_b))

    for i in range(max_len):
        digito_a = vetor_a[i] if i < len(vetor_a) else 0
        digito_b = vetor_b[i] if i < len(vetor_b) else 0
        soma = digito_a + digito_b + carry
        resultado.append(soma % 10)
        carry = soma // 10

    if carry > 0:
        resultado.append(carry)

    return resultado

# Leitura dos números


a = int(input("Digite o primeiro número (positivo e menor que 10000): "))
b = int(input("Digite o segundo número (positivo e menor que 10000): "))

# Verificação dos limites dos números
if not (0 <= a < 10000 and 0 <= b < 10000):
    print("Os números devem ser positivos e menores que 10000.")
else:
    # Conversão dos números em vetores de algarismos
    vetor_a = num_para_vetor(a)
    vetor_b = num_para_vetor(b)

    # Soma dos vetores
    vetor_soma = soma_vetores(vetor_a, vetor_b)

    # Impressão dos resultados
    print(f"Vetor do número {a}: {vetor_a}")
    print(f"Vetor do número {b}: {vetor_b}")
    print(f"Vetor da soma: {vetor_soma}")


""" Exercicio 36 """

vetor_42 = []
for _ in range(10):
    valores_34 = float(input('Escreva um valor para o primeiro vetor: '))
    vetor_42.append(valores_34)

vetor_42.sort()
print(vetor_42)

""" Exercicio 37 """

vetor_43 = [1, 2, 5, 7, 8, 10, 15, 90, 36, 99, 101]
vetor_43.sort()
lista_4 = vetor_43[0:5]
lista_5 = vetor_43[5:]
lista_5.sort(reverse=True)
maior_elemento = max(lista_5)
lista_5.remove(maior_elemento)
vetor_43_ordenado = lista_4 + [maior_elemento] + lista_5
print(vetor_43_ordenado)

""" Exercicio 38 """

vetor_44 = []
for _ in range(10):
    valores_35 = float(input('Escreva um valor para o primeiro vetor: '))
    vetor_44.append(valores_35)
    vetor_44.sort()

print(vetor_44)

""" Exercicio 39 """


def generate_pascals_triangle(n):
    """Gera o triângulo de Pascal até a linha n."""
    triangle = []

    for i in range(n):
        # Inicia cada linha com um 1
        row = [1] * (i + 1)

        # Calcula os valores internos da linha
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]

        # Adiciona a linha ao triângulo
        triangle.append(row)

    return triangle


def print_pascals_triangle(triangle):
    """Imprime o triângulo de Pascal formatado."""
    max_width = len(' '.join(map(str, triangle[-1])))  # Largura da última linha
    for row in triangle:
        print(' '.join(map(str, row)).center(max_width))

# Leitura do número positivo n


n = int(input("Digite um número positivo n: "))

if n <= 0:
    print("Por favor, insira um número positivo.")
else:
    # Gera e imprime o triângulo de Pascal
    pascals_triangle = generate_pascals_triangle(n)
    print_pascals_triangle(pascals_triangle)
