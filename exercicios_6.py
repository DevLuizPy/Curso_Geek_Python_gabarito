""" Exercicio 1 """
import math
import random
import statistics


for num in range(1, 16):
    if num % 3 == 0:
        print(f'{num}')


""" Exercicio 2 """

for _ in range(3):
    for num_1 in range(1, 101):
        print(num_1)

num_2 = 1
while num_2 <= 100:
    print(num_2)
    num_2 = num_2 + 1

""" Exercicio 3 """

num_3 = 10

while num_3 >= 0:
    print(num_3)
    num_3 = num_3 - 1
print('FIM!')

""" Exercicio 4 """

num_4 = 0

while num_4 <= 100_000:
    print(num_4)
    num_4 = num_4 + 1000

""" Exercicio 5 """

soma_1 = 0
for num_5 in range(1, 11):
    valor_1 = float(input('Digite um valor'))
    soma_1 = soma_1 + valor_1

print(f'{soma_1} é o valor da soma desses números')

""" Exercicio 6 """

media_1 = 0
for _ in range(1, 11):
    valor_2 = int(input('Digite um valor'))
    media_1 = media_1 + (valor_2 / 10)

print(f'{media_1} é a media dos 10 numeros')

""" Exercicio 7 """

media_2 = 0
for _ in range(1, 11):
    valor_3 = int(input('Digite um valor positivo'))
    media_2 = media_2 + (abs(valor_3) / 10)

print(f'{media_2} é a media dos 10 numeros')

""" Exercicio 8 """
lista = []
maior_valor = ''
menor_valor = ''
for _ in range(1, 11):
    valor_4 = input('Digite um valor positivo')
    lista.append(valor_4)
    maior_valor = max(lista)
    menor_valor = min(lista)


print(f'{maior_valor} é o maior valor desses numeros, enquanto o '
      f'{menor_valor} é o menor valor desses numeros.')

""" Exercicio 9 """

# Entrada
numero_n = int(input('Escreve um numero inteiro N'))

# Processamento e Saída
count_1 = 0

num_6 = 1
while count_1 < numero_n:
    print(num_6)
    count_1 = count_1 + 1
    num_6 = num_6 + 2

""" Exercicio 10 """

count_2 = 0
num_7 = 0
while count_2 <= 50:
    print(num_7)
    num_7 += 2
    count_2 += 1

""" Exercicio 11 """

# Entrada
numero_n_2 = int(input('Escreva uma numero inteiro positivo'))

# Processamento e Saída
count_3 = 0
num_8 = 0
while count_3 <= numero_n_2:
    print(num_8)
    num_8 += 1
    count_3 += 1

""" Exercicio 12 """

# Entrada
numero_n_3 = int(input('Escreva uma numero inteiro positivo'))

# Processamento e Saída
for num_9 in range(numero_n_3, 0, -1):
    print(num_9)

""" Exercicio 13 """

# Entrada
numero_n_4 = int(input('Escreva uma numero inteiro positivo'))

# Processamento e Saída
count_4 = 0
num_9 = 0
while count_4 < numero_n_4:
    print(num_9)
    num_9 += 2
    count_4 += 1

""" Exercicio 14 """

# Entrada
numero_n_5 = int(input('Escreva uma numero inteiro positivo'))

# Processamento e Saída
count_5 = (numero_n_5 + 1)
num_10 = numero_n_5 * 2
while count_5 > 0:
    print(num_10)
    num_10 -= 2
    count_5 -= 1

""" Exercicio 15 """

# Entrada
numero_n_6 = int(input('Escreva uma numero inteiro positivo'))

# Processamento e Saída
count_6 = 0
num_11 = 1
while count_6 < numero_n_6:
    print(num_11)
    num_11 += 2
    count_6 += 1

""" Exercicio 16 """

# Entrada
numero_n_7 = int(input('Escreva uma numero inteiro positivo'))

# Processamento e Saída
count_7 = (numero_n_7 + 1)
num_12 = (numero_n_7 * 2) - 1
while count_7 > 1:
    print(num_12)
    num_12 -= 2
    count_7 -= 1

""" Exercicio 17 """

# Entrada
numero_n_8 = int(input('Escreva uma numero inteiro positivo'))

# Processamento e Saída
soma_2 = 0
for num_13 in range(0, numero_n_8):
    soma_2 += num_13

print(f'{soma_2} é o valor do somatório dos números')

""" Exercicio 18 """

# Entrada
numeros_lidos = int(input('Escreva a quantidade de numeros a ser lido'))

# Processamento e Saída
lista_1 = []
for num_14 in range(0, numeros_lidos):
    valor_5 = int(input('Escreva um valor'))
    lista_1.append(valor_5)

maior_valor_2 = max(lista_1)
quantidade_1 = lista_1.count(maior_valor_2)

print(f'{maior_valor_2} é o valor mais alto da lista e a quantidade que se repete é {quantidade_1}')

""" Exercicio 19 """

# Entrada
numero_int = int(input('Escreva um número inteiro entre 100 e 999'))

# Processamento e Saída
if 100 <= numero_int <= 999:
    numero_str = str(numero_int)
    print(f'{numero_str[0]} é o primeiro algarismo, {numero_str[1]} é o segundo algarismo, {numero_str[2]} é o terceiro algarismo  ')
else:
    print('Erro')

""" Exercicio 20 """

lista_2 = []
lista_par = []
while True:
    numero_inteiro = int(input('Escreva um número inteiro'))
    if numero_inteiro % 2 == 0:
        lista_2.append(numero_inteiro)
        lista_par.append(numero_inteiro)
        print(f'{numero_inteiro} é par')
    elif numero_inteiro % 2 != 0:
        lista_2.append(numero_inteiro)
    elif numero_inteiro == 1000:
        break

numeros_pares = lista_par.__len__()
numeros_total = lista_2.__len__()

print(f'{numeros_total} é a quantidade de numeros lidos, enquanto {numeros_pares} é a quantidade de números pares')


""" Exercicio 21 """

# Entrada
numero_1 = int(input('Escreva um número '))
numero_2 = int(input('Escreva um número '))

# Processamento e Saída
soma = 0
multiplicacao = 1
for num_15 in range(numero_1, numero_2):
    if num_15 % 2 == 0:
        soma += num_15
    else:
        multiplicacao *= num_15


print(f'{multiplicacao} é o valor da multiplicação')
print(f'{soma} é o valor da soma')

""" Exercicio 22 """

lista_3 = []
while True:
    nota_1 = int(input('Escreva sua nota'))
    if 10 < nota_1 < 20:
        lista_3.append(nota_1)
    else:
        break

media = statistics.mean(lista_3)
print(media)

""" Exercicio 23 """

# Entrada
numero_inteiro_1 = int(input('Escreve um numéro inteiro positivo'))

# Processamento e Saída
for num_16 in range(1, numero_inteiro_1+1):
    if numero_inteiro_1 % num_16 == 0:
        print(num_16)

""" Exercicio 24 """

# Entrada
numero_inteiro_3 = int(input('Escreve um numéro inteiro positivo'))

# Processamento e Saída
soma = 0
for num_17 in range(1, numero_inteiro_3):
    if numero_inteiro_3 % num_17 == 0:
        soma += num_17

print(soma)

""" Exercicio 25 """

soma_3 = 0
for num_18 in range(1, 1001):
    if num_18 % 3 == 0 or num_18 % 3 == 0:
        soma_3 += num_18

print(soma_3)

""" Exercicio 26 """

# Entrada
numero_inteiro_4 = int(input('Escreve um numéro inteiro positivo'))

# Processamento e Saída

while True:
    if numero_inteiro_4 % 11 == 0 or numero_inteiro_4 % 13 == 0 or numero_inteiro_4 % 17 == 0:
        print(numero_inteiro_4)
        break
    else:
        numero_inteiro_4 += 1

""" Exercicio 27 """

# Entrada
n_1 = int(input('Escreve um numéro inteiro positivo'))
soma_4 = 0
if n_1 <= 0:
    print("Por favor, digite um número positivo inteiro.")
else:
    for num_19 in range(1, n_1 + 1):
        soma_4 = soma_4 + 1/num_19

print(soma_4)

""" Exercicio 28 """

# Entrada
n_2 = int(input('Escreve um numéro inteiro positivo'))
fatorial = 0
if n_2 <= 0:
    print("Por favor, digite um número positivo inteiro.")
else:
    for num_20 in range(1, n_2 + 1):
        fatorial = fatorial + (1/math.factorial(num_20))

print(fatorial)

""" Exercicio 29 """

# Entrada
soma_5 = 0
for num_20 in range(0, 5):
    soma_5 = soma_5 + num_20/(math.factorial(num_20 + 1))

print(soma_5)

""" Exercicio 30 """

# Entrada
n_3 = int(input('Escreve um numéro inteiro positivo'))
n_4 = int(input('Escreve um numéro inteiro positivo'))
n_5 = int(input('Escreve um numéro inteiro positivo'))

# Processamento e Saída
soma_6 = 0
soma_7 = 0
soma_8 = 0
for num_21 in range(1, n_3 + 1):
    soma_6 += num_21

for num_22 in range(1, 2 * n_3):
    if num_22 % 2 != 0:
        soma_7 = soma_7 + num_22
    else:
        soma_7 = soma_7 - num_22

for num_23 in range(1, 2 * n_3):
    if num_23 % 2 != 0:
        soma_8 = soma_8 + num_23
    else:
        ''


""" Exercicio 31 """

numerador = 1
denominador = 1
soma_9 = 0
while True:
    soma_9 = soma_9 + numerador / denominador
    numerador += 2
    denominador += 1
    if numerador > 99:
        break

print(soma_9)

""" Exercicio 32 """


# Entrada
n_4 = int(input("Digite o número de lançamentos: "))

dado_1 = 0
dado_2 = 0
relacao = ''

for _ in range(0, n_4):
    dado_1 = random.randint(1, 6)
    dado_2 = random.randint(1, 6)
    if dado_1 < dado_2:
        relacao = '<'
        print(f"d1: {dado_1}, d2: {dado_2} -> d1 {relacao} d2")
    elif dado_1 > dado_2:
        relacao = '>'
        print(f"d1: {dado_1}, d2: {dado_2} -> d1 {relacao} d2")
    else:
        relacao = '='
        print(f"d1: {dado_1}, d2: {dado_2} -> d1 {relacao} d2")


""" Exercicio 33 """

# Entrada
n_5 = int(input("Digite o número n: "))
i = int(input('Escreve um numero inteiro positivo'))
j = int(input('Escreve um numero inteiro positivo'))

lista_4 = []
multiplo_2 = 0
multiplo_3 = 0
# Processamento e Saída
for _ in range(1, n_5 + 1):
    multiplo_2 += 2
    lista_4.append(multiplo_2)

for _ in range(1, n_5 + 1):
    multiplo_3 += 3
    lista_4.append(multiplo_3)

print(lista_4[0:6])

""" Exercicio 34 """
numero_5 = 0
while True:
    numero_5 += numero_5
    if numero_5 % 2 == 0 and numero_5 % 3 == 0 and numero_5 % 4 == 0 and numero_5 % 5 == 0 and numero_5 % 6 == 0 and numero_5 % 7 == 0:
        if numero_5 % 8 == 0 and numero_5 % 9 == 0 and numero_5 % 10 == 0 and numero_5 % 11 == 0 and numero_5 % 12 == 0 and numero_5 % 13 == 0:
            if numero_5 % 14 == 0 and numero_5 % 15 == 0 and numero_5 % 16 == 0 and numero_5 % 17 == 0 and numero_5 % 18 == 0 and numero_5 % 19 == 0 and numero_5 % 20 == 0:
                print(numero_5)
                break

""" Exericio 35 """

# Entrada
numero_6 = int(input('Escreve o número do inicio do intervalo: '))
numero_7 = int(input('Escreve o numéro do final do invervalo: '))

# Processamento e Saída
soma_10 = 0
if numero_6 > numero_7:
    print('Intervalo de dados inválido')
else:
    for num_24 in range(numero_6, numero_7):
        if num_24 % 2 != 0:
            soma_10 += num_24
print(f'Soma dos impares neste intervalo: {soma_10}')

""" Exercicio 36 """

contador_1 = 0
soma_11 = 0
soma_12 = 0
while contador_1 <= 100:
    contador_1 += 1
    soma_11 += contador_1 ** 2
    soma_12 += contador_1

soma_13 = (soma_12 ** 2) - soma_11

print(f'A diferença entre a soma dos quadrados e o quadrado da soma é: {soma_13}')

""" Exercicio 37 """

contador_2 = 1000
lista_5 = []
while contador_2 <= 9999:
    contador_3 = str(contador_2)
    grupo_1 = int(contador_3[:2])
    grupo_2 = int(contador_3[2:])
    soma_14 = grupo_1 + grupo_2
    if soma_14 ** 2 == contador_2:
        lista_5.append(contador_2)
        contador_2 += 1
    else:
        contador_2 += 1

print(lista_5)

""" Exercicio 38 """


def encontrar_terno_pitagorico():
    for a_1 in range(1, 1000):
        for b_1 in range(a_1, 1000 - a_1):
            c_1 = 1000 - a_1 - b_1
            if a_1**2 + b_1**2 == c_1**2:
                return a_1, b_1, c_1
    return None

# Calcular o terno pitagórico


resultado = encontrar_terno_pitagorico()
if resultado:
    a_1, b_1, c_1 = resultado
    print(f"O terno pitagórico é: a = {a_1}, b = {b_1}, c = {c_1}")
    print(f"A soma é: a + b + c = {a_1 + b_1 + c_1}")
    print(f"Verificação: a^2 + b^2 = {a_1**2 + b_1**2}, c^2 = {c_1**2}")
else:
    print("Nenhum terno pitagórico encontrado.")


""" Exercicio 39 """

# Entrada
numero_9 = int(input('Escreva a base de um triangulo: '))
numero_10 = int(input('Escreva a altura de um triangulo: '))

# Processamento e Saída
if numero_9 or numero_10 <= 0:
    print('Dados inválidos')
else:
    area_1 = (numero_9 + numero_10) / 2
    print(area_1)

""" Exercicio 40 """

lista_6 = []
while True:
    numero_20 = int(input('Escreve um numero inteiro: '))
    if numero_20 >= 0:
        lista_6.append(numero_20)
    else:
        break

maior_valor_3 = max(lista_6)
menor_valor_3 = min(lista_6)

print(f'{maior_valor_3} é o maior valor desses numeros, enquanto o '
      f'{menor_valor_3} é o menor valor desses numeros.')


""" Exercicio 41 """

while True:
    resistor_1 = int(input('Escreva o valor de resistencia do primeiro resistor: '))
    resistor_2 = int(input('Escreva o valor de resistencia do segundo resistor: '))
    paralelo = (resistor_1 * resistor_2) / resistor_1 + resistor_2
    if resistor_1 and resistor_2 != 0:
        print(f'{paralelo} é o valor da resistencia em paralelo desses dois transformadores')
    else:
        break

""" Exercicio 42 """

while True:
    numero_21 = int(input('Escreva um valor: '))
    if numero_21 >= 0:
        cubo = numero_21 ** 3
        quadrado = numero_21 ** 2
        raiz_quadrada = math.sqrt(numero_21)
        print(f'{cubo} é o cubo desse número, enquanto {quadrado} é o quadrado desse número, enquanto {raiz_quadrada} '
              f'é a raiz quadrada desse número')
    else:
        break


""" Exercicio 43 """

lista_7 = []
while True:
    idade_1 = int(input('Escreva uma idade: '))
    if idade_1 != 0:
        lista_7.append(idade_1)
    else:
        break
media_3 = statistics.mean(lista_7)
print(media_3)

""" Exercicio 44 """

# Entrada
numero_22 = int(input('Escreva um numéro positivo: '))

# Processamento e Saída
a, b = 0, 1
soma = 0
lista_8 = []

while a <= numero_22:
    soma += a
    lista_8.append(a)
    a, b = b, a + b

print(lista_8)

""" Exercicio 45 """

while True:
    menu = int(input('Escolha uma opção, 1 - km/h para m/s, 2 - m/s para km/h, 3 - Finalizar: '))
    numero_23 = int(input('Escreva o numero a ser convertido: '))
    if menu == 1:
        convertido_1 = numero_23 / 3.6
        print(convertido_1)
    elif menu == 2:
        convertido_1 = numero_23 * 3.6
        print(convertido_1)
    elif menu == 3:
        break
    else:
        print('dados invalidos')

""" Exercicio 46 """

lista_9 = []
aleatorio = random.randint(1, 1000)
while True:
    numero_24 = int(input('Tente advinhar o numéro escolhido: '))
    lista_9.append(numero_24)
    if numero_24 > aleatorio:
        print('Chutou pra cima')
    elif numero_24 < aleatorio:
        print('Chutou pra baixo')
    else:
        break

print('Acertou')
tentativas = lista_9.__len__()
print(f'{tentativas} foi o número de tentativas')

""" Exercicio 47 """

while True:
    menu_2 = int(input('Escolha uma opção, 1 - Adição, 2 - Subtração, 3 - Multiplicação, 4 - Divisão, 5 - Saída: '))
    numero_23 = int(input('Escreva o numero: '))
    numero_24 = int(input('Escreva o numero: '))
    if menu_2 == 1:
        operacao_1 = numero_23 + numero_24
        print(operacao_1)
    elif menu_2 == 2:
        operacao_1 = numero_23 - numero_24
        print(operacao_1)
    elif menu_2 == 3:
        operacao_1 = numero_23 * numero_24
        print(operacao_1)
    elif menu_2 == 4:
        operacao_1 = numero_23 / numero_24
        print(operacao_1)
    elif menu_2 == 5:
        break
    else:
        print('dados invalidos')


""" Exercicio 48 """

a, b = 0, 1
soma_15 = 0

while a <= 4_000_000:
    a, b = b, a + b
    if a % 2 == 0:
        soma_15 += a

print(soma_15)

""" Exercicio 49 """

# Entrada
salario_carlos = int(input('Escreva o salário do carlos: '))

# Processamento e Saída
salario_joao = salario_carlos / 3
meses = 1

while True:
    meses += 1
    valor_futuro_joao = salario_joao * (1+0.05) * ((((1+0.05) ** meses) - 1) / 0.05)
    valor_futuro_carlos = salario_carlos * (1+0.02) * ((((1+0.02) ** meses) - 1) / 0.05)
    if valor_futuro_joao > valor_futuro_carlos:
        break

print(meses)


""" Exercicio 50 """

altura_chico = 1.50
altura_ze = 1.10
anos_1 = 0
while True:
    anos_1 += 1
    altura_final_chico = altura_chico + (0.02 * anos_1)
    altura_final_ze = altura_ze + (0.03 * anos_1)
    if altura_final_ze > altura_final_chico:
        break

print(anos_1)

""" Exercicio 51 """

salario_fun = 2000 * 1.015
anos_2 = 0.03
salario_atual = 0
for _ in range(1, 29):
    salario_atual = salario_fun * (1 + anos_2)
    anos_2 = anos_2 * 2

print(salario_atual)

""" Exercicio 52 """


def calcular_notas(saque):
    notas = [100, 50, 20, 10, 5, 2, 1]
    quantidade_notas = {}

    for nota in notas:
        if saque >= nota:
            quantidade_notas[nota] = saque // nota
            saque = saque % nota

    return quantidade_notas

# Solicitar ao usuário o valor do saque


valor_saque = int(input("Digite o valor do saque: "))
resultado = calcular_notas(valor_saque)

# Imprimir o resultado
print("Notas necessárias para o saque:")
for nota, quantidade in resultado.items():
    print(f"Nota de R${nota}: {quantidade} nota(s)")


""" Exercicio 53 """

# Entrada
n = int(input("Digite o número de linhas do Triângulo de Floyd: "))

# Processamento e Saída
num = 1
for i in range(1, n + 1):
    for _ in range(1, i + 1):
        print(num, end=' ')
        num += 1
    print()  # Nova linha após cada linha do triângulo

""" Exercicio 54 """

# Entrada
numero_30 = int(input('Escreva um número inteiro positivo: '))

# Processamento e Saída
if numero_30 > 1:
    for num_30 in range(2, numero_30):
        if numero_30 % num_30 == 0:
            print('Esse número não é primo')
            break
        else:
            print('Esse numero é primo')
            break
else:
    print('numero invalido')

""" Exercicio 55 """


def eh_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True


def soma_n_primos(n):
    soma = 0
    contador = 0
    numero = 2

    while contador < n:
        if eh_primo(numero):
            soma += numero
            contador += 1
        numero += 1

    return soma

# Solicitar ao usuário o valor de n


n = int(input("Digite o valor de n: "))
resultado = soma_n_primos(n)
print(f"A soma dos {n} primeiros números primos é {resultado}.")


""" Exercicio 56 """


def soma_primos_abaixo_de(limite):
    # Cria uma lista de booleanos representando se cada número até o limite é primo
    eh_primo = [True] * limite
    eh_primo[0] = eh_primo[1] = False  # 0 e 1 não são primos

    # Implementa o Crivo de Eratóstenes
    for num in range(2, int(limite**0.5) + 1):
        if eh_primo[num]:
            for multiplo in range(num * num, limite, num):
                eh_primo[multiplo] = False

    # Soma todos os números primos
    soma = sum(num for num, primo in enumerate(eh_primo) if primo)
    return soma


# Definir o limite
limite = 2000000

# Calcular a soma de todos os números primos abaixo do limite
resultado = soma_primos_abaixo_de(limite)
print(f"A soma de todos os números primos abaixo de {limite} é {resultado}.")


""" Exercicio 57 """


def crivo_de_eratostenes(limite):
    eh_primo = [True] * (limite + 1)
    eh_primo[0] = eh_primo[1] = False  # 0 e 1 não são primos

    for num in range(2, int(limite**0.5) + 1):
        if eh_primo[num]:
            for multiplo in range(num * num, limite + 1, num):
                eh_primo[multiplo] = False

    return eh_primo


def contar_primos_entre(a, b):
    if a > b:
        a, b = b, a  # Trocar para garantir que a seja menor que b

    eh_primo = crivo_de_eratostenes(b)
    contador_primos = sum(eh_primo[a:b+1])

    return contador_primos

# Solicitar ao usuário os valores de a e b


a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))

# Calcular a quantidade de números primos entre a e b
resultado = contar_primos_entre(a, b)
print(f"Existem {resultado} números primos entre {a} e {b}.")


""" Exercicio 58 """


def crivo_de_eratostenes_2(limite):
    eh_primo = [True] * (limite + 1)
    eh_primo[0] = eh_primo[1] = False  # 0 e 1 não são primos

    for num in range(2, int(limite**0.5) + 1):
        if eh_primo[num]:
            for multiplo in range(num * num, limite + 1, num):
                eh_primo[multiplo] = False

    return eh_primo


def somar_primos_entre(a, b):
    if a > b:
        a, b = b, a  # Trocar para garantir que a seja menor que b

    eh_primo = crivo_de_eratostenes_2(b)
    soma_primos = sum(num for num in range(a, b + 1) if eh_primo[num])

    return soma_primos

# Solicitar ao usuário os valores de a e b


a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))

# Calcular a soma dos números primos entre a e b
resultado = somar_primos_entre(a, b)
print(f"A soma dos números primos entre {a} e {b} é {resultado}.")


""" Exercicio 59 """

numero_habitantes = int(input("Digite o valor do número de habitantes: "))
preco_kwh = float(input("Digite o valor do preço do kwh: "))
lista_10 = []
total_residencial = 0
total_comercial = 0
total_industrial = 0
while True:
    consumo_habitante = int(input("Digite o valor do consumo em kwh: "))
    codigo_consumidor = int(input("Digite 1 - Residencial, 2 - Comercial, 3 - Industrial 4 - Terminar :"))
    par_ordenado = (consumo_habitante, codigo_consumidor)
    if codigo_consumidor == 4:
        break
    else:
        lista_10.append(par_ordenado)
        if codigo_consumidor == 1:
            total_residencial += consumo_habitante
        elif codigo_consumidor == 2:
            total_comercial += consumo_habitante
        elif codigo_consumidor == 3:
            total_industrial += consumo_habitante

consumo = [par[0] for par in lista_10]
media_consumo = statistics.mean(consumo)

print(f"A média do consumo de energia é {media_consumo:.2f} kwh")
maior_valor_3 = max(consumo)
menor_valor_3 = min(consumo)
print(f'O maior valor consumido foi {maior_valor_3} kwh ')
print(f'O menor valor consumido foi {menor_valor_3} kwh ')
print(f'O consumo total na categoria Residencial foi {total_residencial} kwh')
print(f'O consumo total na categoria Comercial foi {total_comercial} kwh')
print(f'O consumo total na categoria Industrial foi {total_industrial} kwh')

""" Exercicio 60 """

lista_11 = []
while True:
    numero_25 = int(input("Digite um número: "))
    if numero_25 == 0:
        break
    else:
        lista_11.append(numero_25)

soma_16 = sum(lista_11)
print(f'O valor da soma entre esses dois números é {soma_16} ')
media_4 = statistics.mean(lista_11)
print(f"A média dos números digitados é {media_4} ")
quantidade_2 = lista_11.__len__()
print(f'A quantidade dos números digitados é {quantidade_2}')
maior_valor_4 = max(lista_11)
menor_valor_4 = min(lista_11)
print(f'O maior valor digitado foi {maior_valor_4} ')
print(f'O menor valor digitado foi {menor_valor_4} ')
numeros_pares = list(filter(lambda par: par % 2 == 0, lista_11))

""" Exercicio 61 """


def eh_palindromo(num):
    # Converter o número para string e verificar se é igual ao seu reverso
    return str(num) == str(num)[::-1]


def maior_palindromo():
    maior_palindromo = 0
    # Iterar sobre todos os pares de números de três dígitos
    for i in range(100, 1000):
        for j in range(i, 1000):
            produto = i * j
            if eh_palindromo(produto) and produto > maior_palindromo:
                maior_palindromo = produto
    return maior_palindromo

# Calcular e imprimir o maior número palíndromo


resultado = maior_palindromo()
print(f"O maior número palíndromo feito a partir do produto de dois números de 3 dígitos é {resultado}")

""" Exercicio 62 """

# Dicionário para mapear números por extenso para seus equivalentes numéricos
numeros_extenso = {
    "um": 1, "dois": 2, "três": 3, "quatro": 4, "cinco": 5,
    "seis": 6, "sete": 7, "oito": 8, "nove": 9, "dez": 10,
    "onze": 11, "doze": 12, "treze": 13, "catorze": 14, "quinze": 15,
    "dezesseis": 16, "dezessete": 17, "dezoito": 18, "dezenove": 19, "vinte": 20,
    "trinta": 30, "quarenta": 40, "cinquenta": 50, "sessenta": 60, "setenta": 70,
    "oitenta": 80, "noventa": 90, "cem": 100, "cento": 100, "duzentos": 200,
    "trezentos": 300, "quatrocentos": 400, "quinhentos": 500, "seiscentos": 600,
    "setecentos": 700, "oitocentos": 800, "novecentos": 900, "mil": 1000
}


def contar_letras(numero_por_extenso):
    # Remover hífens e espaços e dividir a string em palavras
    palavras = numero_por_extenso.replace('-', ' ').split()
    # Somar o número de letras de cada palavra
    return sum(len(palavra) for palavra in palavras)


def converter_para_numero(numero_por_extenso):
    # Dividir a string em palavras
    palavras = numero_por_extenso.split()
    total = 0
    temp = 0
    for palavra in palavras:
        # Adicionar o valor numérico da palavra ao total
        temp += numeros_extenso[palavra]
        # Se a palavra for "mil", multiplicar o total por mil e somar ao resultado final
        if palavra == 'mil':
            total += temp * 1000
            temp = 0
        # Se a palavra for maior que "mil", reiniciar o temporizador
        elif temp >= 100:
            total += temp
            temp = 0
    return total

# Somar o número de letras de todos os números de 1 a 1000 escritos por extenso


total_letras = sum(contar_letras(str(converter_para_numero(str(numero)))) for numero in range(1, 1001))

print("Total de letras de 1 a 1000 escritos por extenso:", total_letras)
