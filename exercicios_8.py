""" Exercicio 1 """
from fractions import Fraction
import math
from math import gcd
import random
import statistics

def dobro(numero):
    return numero * 2


""" Exercicio 2 """


def data(dia, mes, ano):
    return f'{dia} de {mes} de {ano}'


""" Exercicio 3 """


def positivo(numero):
    if numero > 0:
        return 1
    elif numero == 0:
        return 0
    return -1


""" Exercicio 4 """


def quadrado_perfeito(numero):
    if math.sqrt(numero) is int:
        return 'Esse número é um quadrado perfeito'


""" Exercicio 5 """


def volume_esfera(raio):
    return 4/3 * 3.1415 * (raio ** 3)


""" Exercicio 6 """


def horas(segundo, minuto, horas):
    segundos = segundo + minuto * 60 + horas * 3600
    return f'Esse é o seu valor em {segundos}'


""" Exercicio 7 """


def temperatura(Celsius):
    return Celsius * 9/5 + 32


""" Exercicio 8 """


def hipotenusa(cateto_a, cateto_b):
    return math.sqrt((cateto_a ** 2) + (cateto_b ** 2))


""" Exercicio 9 """


def volume_cilindro(altura, raio):
    return 3.14 * (raio ** 2) * altura


""" Exercicio 10 """


def maior_numero(num_1, num_2):
    return max(num_1,num_2)


""" Exercicio 11 """


def notas(nota_1, nota_2, nota_3, letra):
    if letra == 'A':
        return (nota_1 + nota_2 + nota_3) / 3
    elif letra == 'P':
        return (nota_1 * 5 + nota_2 * 3 + nota_3 * 2) / 10


""" Exercicio 12 """


def soma_algarismos(numero_inteiro):
    numero = str(numero_inteiro)
    algarismo_1 = int(numero[0])
    algarismo_2 = int(numero[1])
    algarismo_3 = int(numero[2])
    return algarismo_1 + algarismo_2 + algarismo_3

print(soma_algarismos(251))


""" Exercicio 13 """


def calculadora(num_1, num_2, simbolo):
    if simbolo == '+':
        return num_1 + num_1
    elif simbolo == '-':
        return num_1 - num_2
    elif simbolo == '/':
        return num_1 / num_2
    elif simbolo == '*':
        return num_1 * num_2


print(calculadora(10, 20, '+'))


""" Exercicio 14 """

def consumo_combustivel(distancia, litros):
    if distancia / litros < 8:
        return 'Venda o carro'
    elif 8 < distancia / litros < 12:
        return 'Econômico'
    elif distancia / litros > 12:
        return 'Super econômico'


""" Exercicio 15 """


def lado_triangulo(l_1, l_2, l_3):
    if (l_1 or l_2 or l_3) < 0:
        return 'Dados invalidos'
    elif l_1 < l_2 + l_3 and l_2 < l_3 + l_1 and l_3 < l_2 + l_1:
        return 'Esses lados formam um triangulo'
    return 'Não forma um triangulo'


print(lado_triangulo(3, 4, 5))


def nome_triangulo(l_1, l_2, l_3):
    if lado_triangulo(l_1, l_2, l_3) == 'Esses lados formam um triangulo':
        if l_1 == l_2 == l_3:
            return 'Triangulo equilatero'
        elif l_1 == l_2 or l_3 == l_2 or l_1 == l_3:
            return 'Triangulo isosceles'
        return 'Triangulo escaleno'
    return 'Não é triangulo, forte abraço'


""" Exercicio 16 """


def desenha_linha(numero):
    return '=' * numero


print(desenha_linha(10))


""" Exercicio 17 """

def soma_entre_numeros(numero_1, numero_2):
    if numero_1 <= 0 or numero_2 <= 0:
        return 'Dados invalidos, escreva um número inteiro'
    elif numero_1 > numero_2:
        return 'Escreva o numero 1 como menor, e o numero 2 como maior'
    else:
        soma = 0
        for numero in range(numero_1 + 1, numero_2):
            soma = soma + numero
        return soma


print(soma_entre_numeros(2, 10))

""" Exercicio 18 """


def exponencial(x, z):
    return x ** z


""" Exercicio 19 """

def maior_fator_primo(numero):
    if numero <= 1:
        return None  # Não há fator primo para números menores ou iguais a 1
    # Inicialmente, o maior fator primo é 2
    maior_fator = None
    # Verifica a divisibilidade por 2
    while numero % 2 == 0:
        maior_fator = 2
        numero //= 2
    # Verifica a divisibilidade por números ímpares a partir de 3
    fator = 3
    while fator * fator <= numero:
        while numero % fator == 0:
            maior_fator = fator
            numero //= fator
        fator += 2
    # Se numero ainda é maior que 2, então ele mesmo é um fator primo
    if numero > 2:
        maior_fator = numero
    return maior_fator


""" Exercicio 20 """


def fatorial(numero):
    fatorial = 1
    for valor in range(1, numero):
        fatorial = valor * fatorial
    return fatorial


print(fatorial(10))


""" Exercicio 21 """


def primo(numero):
    primos = []
    for valor in range(2, numero):
        is_prime = True
        limite = int(math.sqrt(valor)) + 1
        for divisor in range(2, limite):
            if valor % divisor == 0:
                is_prime = False
                break
        if is_prime:
                primos.append(valor)
    return primos.__len__()


print(primo(100))

""" Exercicio 22 """


def gerar_exclamacoes(n):
    for i in range(1, n + 1):
        print('!' * i)


gerar_exclamacoes(10)

""" Exercicio 23 """


def triangulo_lateral(n):
    for i in range(1, n + 1):
        print('!' * i)

    for i in range(n - 1, 0, -1):
        print('!' * i)


triangulo_lateral(5)


""" Exercicio 24 """

def triangulo(n):
    for i in range(1, 2 * n, 2):
        print('*' * i)

triangulo(6)


""" Exercicio 25 """

def serie(n):
    soma = 0
    for i in range(1, n +1):
        soma += (i ** 2 + 1) / (i+3)
    return soma

print(serie(3))


""" Exercicio 26 """

def somatorio(n):
    soma = 0
    for i in range(1, n+1):
        soma += i
    return soma

print(somatorio(5))


""" Exercicio 27 """


def seno(x):
    soma = 0
    for n in range(0, 5):
        soma += ((-1) ** n / math.factorial(2*n+1)) * x ** (2 * n + 1)
    return soma


print(seno(1))  # Angulo de 57 graus


""" Exercicio 28 """


def cosseno(x):
    soma = 0
    for n in range(0, 5):
        soma += ((-1) ** n / math.factorial(2*n)) * x ** (2 * n)
    return soma


print(cosseno(1))  # Angulo de 57 graus


""" Exercicio 29 """


def sinh(x):
    soma = 0
    for n in range(0, 5):
        soma += (x ** (2 * n + 1)) / math.factorial(2*n + 1)
    return soma


print(sinh(1))  # Angulo de 57,2958 graus


""" Exercicio 30 """


def cosh(x):
    soma = 0
    for n in range(0, 5):
        soma += (x ** (2 * n)) / math.factorial(2*n)
    return soma


print(cosh(1))  # Angulo de 57,2958 graus


""" Exercicio 31 """


def e(termos):
    soma = 0
    for n in range(0, termos):
        soma += 1 / math.factorial(n)
    return soma


print(e(100))


""" Exercicio 32 """


def simplifica(numerador, denominador):
    maior_fator = None
    if numerador > denominador:
        for i in range(2, denominador + 1):
            if numerador % i == 0 and denominador % i == 0:
                maior_fator = i
        novo_numerador = numerador / maior_fator
        novo_denominador = denominador / maior_fator
        return f'O maior fator divisor é {maior_fator} e a nova fração é {novo_numerador}/{novo_denominador}'
    else:
        for i in range(2, numerador + 1):
            if numerador % i == 0 and denominador % i == 0:
                maior_fator = i
        novo_numerador = numerador / maior_fator
        novo_denominador = denominador / maior_fator
        return f'O maior fator divisor é {maior_fator} e a nova fração é {novo_numerador}/{novo_denominador}'


print(simplifica(2, 20))


""" Exercicio 33 """


def soma_algarismos(n):
    fatorial = math.factorial(n)
    numero = str(fatorial)
    soma = 0
    for algarismos in numero:
        algarismo_novo = int(algarismos)
        soma += algarismo_novo
    return soma


print(soma_algarismos(10))


""" Exercicio 34 """

def fatorial_duplo(n):
    fatorial_duplo = 1
    for i in range(1, n +1):
        if i % 2 != 0:
            fatorial_duplo *= i
    return fatorial_duplo


print(fatorial_duplo(5))


""" Exercicio 35 """


def fatorial_quadruplo(n):
    numerador = 1
    denominador = 1
    for i in range(1, 2 * n + 1):
        numerador *= i
    for i in range(1, n + 1):
        denominador *= i
    return numerador / denominador


print(fatorial_quadruplo(5))


""" Exercicio 36 """


def superfatorial(n):
    superfatorial = 1
    for i in range(1, n + 1):
        superfatorial *= math.factorial(i)
    return superfatorial


print(superfatorial(4))


""" Exercicio 37 """

def hiperfatorial(n):
    hiperfatorial = 1
    for x in range(1, n + 1):
        hiperfatorial *= (x ** x)
    return hiperfatorial


print(hiperfatorial(4))


""" Exercicio 38 """

def fatorial_exponencial(n):
    resultado = 1
    for i in range(1, n+1):
        resultado = i ** resultado
    return resultado


""" Exercicio 39 """


def troque(a, b):
    a, b = b, a
    return a, b


print(troque(1, 2))


""" Exercicio 40 """

vetor_inteiros = list(random.randint(1, 999,) for _ in range(10))
print(vetor_inteiros)


def numeros_pares(lista):
    pares = []
    for elemento in lista:
        if elemento % 2 == 0:
            pares.append(elemento)
    return len(pares)


print(numeros_pares(vetor_inteiros))


""" Exercicio 41 """

vetor_inteiros = list(random.randint(1, 999,) for _ in range(10))
print(vetor_inteiros)

def maior_valor(lista):
    return max(lista)


print(maior_valor(vetor_inteiros))


""" Exercicio 42 """

vetor_reais = [random.uniform(1, 999) for _ in range(100)]
print(vetor_reais)


def media(lista):
    return statistics.mean(lista)


print(media(vetor_reais))


""" Exercicio 43 """


def gera_vetor_aleatorio(lista):
    numeros_disponiveis = list(range(1, 999))
    vetor_aleatorio = list(random.sample(numeros_disponiveis,30))
    return vetor_aleatorio + lista


print(gera_vetor_aleatorio(vetor_inteiros))


""" Exercicio 44 """


vetor_inteiros = list(random.randint(1, 999,) for _ in range(30))
print(vetor_inteiros)


def pares_e_impares(lista):
    pares = []
    impares = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    return pares, impares


print(pares_e_impares(vetor_inteiros))


""" Exercicio 45 """


def desvio_padrao(lista):
    media = statistics.mean(lista)
    desvio = 0
    for numero in lista:
        desvio = desvio + (numero - media) ** 2
    return math.sqrt(1 / (len(lista) - 1) * desvio)


print(desvio_padrao(vetor_inteiros))
print(vetor_inteiros)

""" Exercicio 46 """

vetor_reais = [random.uniform(1, 999) for _ in range(20)]


def vetor(vetor_real):
    print(vetor_real)
    vetor_real.reverse()
    print(vetor_real)
    print(statistics.mean(vetor_real))


print(vetor_reais)
vetor(vetor_reais)


""" Exercicio 47 """

def ler_matriz():
    matriz_4x4 = []
    for i in range(4):
        linha = []
        for j in range(4):
            valor = int(input(f"Digite o valor para a posição ({i}, {j}): "))
            linha.append(valor)
        matriz_4x4.append(linha)
    return matriz_4x4


def contar_maiores_que_10(matriz):
    contador = 0
    for linha in matriz:
        for valor in linha:
            if valor > 10:
                contador += 1
    return contador

matriz = ler_matriz()

quantidade_maiores_que_10 = contar_maiores_que_10(matriz)

print(matriz)
print(quantidade_maiores_que_10)


""" Exercicio 48 """

def diagonal_principal_abaixo(matriz):
    soma = 0
    for i in range(1, len(matriz)):
        for j in range(i):
            soma += matriz[i][j]
    return soma


""" Exercicio 49 """

def soma_diagonal_principal(matriz):
    soma = 0
    for i in range(len(matriz)):
        soma += matriz[i][i]
    return soma

# Muitos exercicios de matriz


""" Exercicio 59 """

def uniao(vetor_1,vetor_2):
    conjunto_1 = set(vetor_1)
    conjunto_2 = set(vetor_1)
    return conjunto_1.union(conjunto_2)


""" Exercicio 60 """


def primeiro_termo_string(string):
    primeiro_termo = string[0]
    if primeiro_termo is None:
        return -1
    return primeiro_termo


""" Exercicio 61 """


def anagrama(string_1, string_2):
    if string_1[:: -1] == string_2:
        return True
    return False


""" Exercicio 62 """


def tamanho_string(string):
    return len(string)


""" Exercicio 63 """


def igualdade_strings(string_1, string_2):
    if string_1 == string_2:
        return 'São strings iguais'
    return 'São strings diferentes'


""" Exercicio 64 """


def concatenar_strings(string_1,string_2):
    return string_1 + string_2


""" Exercicio 65 """


def concatenar_strings_n(string_1,string_2, n):
    nova_string = ''
    for letra in string_1[0:n]:
        nova_string = nova_string + letra
    return nova_string + string_2


print(concatenar_strings_n('Marcelo', 'Games', 4))


""" Exercicio 66 """


def title(string):
    return title(string)


""" Exercicio 67 """

# Exercicio de C


""" Exercicio 68 """


def intercalar_strings(str1, str2):
    intercalada = []
    len1, len2 = len(str1), len(str2)
    for i in range(max(len1, len2)):
        if i < len1:
            intercalada.append(str1[i])
        if i < len2:
            intercalada.append(str2[i])
    return ''.join(intercalada)


""" Exercicio 69 """


from fractions import Fraction


def ler_fracao():
    numerador = int(input("Digite o numerador: "))
    denominador = int(input("Digite o denominador: "))
    return Fraction(numerador, denominador)


def somar_fracoes(fracao1, fracao2):
    return fracao1 + fracao2


def subtrair_fracoes(fracao1, fracao2):
    return fracao1 - fracao2


def multiplicar_fracoes(fracao1, fracao2):
    return fracao1 * fracao2


def dividir_fracoes(fracao1, fracao2):
    return fracao1 / fracao2


def calcular_mdc(a, b):
    if b == 0:
        return a
    else:
        return calcular_mdc(b, a % b)


def main():
    print("Digite a primeira fração:")
    fracao1 = ler_fracao()

    print("Digite a segunda fração:")
    fracao2 = ler_fracao()

    soma = somar_fracoes(fracao1, fracao2)
    subtracao = subtrair_fracoes(fracao1, fracao2)
    produto = multiplicar_fracoes(fracao1, fracao2)
    quociente = dividir_fracoes(fracao1, fracao2)

    mdc_soma = calcular_mdc(soma.numerator, soma.denominator)
    mdc_subtracao = calcular_mdc(subtracao.numerator, subtracao.denominator)
    mdc_produto = calcular_mdc(produto.numerator, produto.denominator)
    mdc_quociente = calcular_mdc(quociente.numerator, quociente.denominator)

    print(f"A soma das frações é: {soma} ou {float(soma)} como número decimal.")
    print(f"O máximo divisor comum (MDC) da soma é: {mdc_soma}")

    print(f"A subtração das frações é: {subtracao} ou {float(subtracao)} como número decimal.")
    print(f"O máximo divisor comum (MDC) da subtracao é: {mdc_subtracao}")

    print(f"O produto das frações é: {produto} ou {float(produto)} como número decimal.")
    print(f"O máximo divisor comum (MDC) do produto é: {mdc_produto}")

    print(f"O quociente das frações é: {quociente} ou {float(quociente)} como número decimal.")
    print(f"O máximo divisor comum (MDC) do quociente é: {mdc_quociente}")


if __name__ == "__main__":
    main()


"""
 Exercicio 70, é de C, fora que é repetitivo
 Exercicio 71 é de C, não sei nem começar em python
 Exercicio 72 é de C, não sei nem começar em python
"""

""" Exercicio 73 """


def ler_dados():
    habitantes = []
    for i in range(5):
        print(f"Dados do habitante {i+1}:")
        sexo = input("Sexo (M/F): ")
        cor_olhos = input("Cor dos olhos (A - Azuis, C - Castanhos): ")
        cor_cabelos = input("Cor dos cabelos (L - Louros, P - Pretos, C - Castanhos): ")
        idade = int(input("Idade: "))
        habitantes.append({"sexo": sexo, "cor_olhos": cor_olhos, "cor_cabelos": cor_cabelos, "idade": idade})
    return habitantes


def media_idade_castanhos_pretos(habitantes):
    total_idade = 0
    count = 0
    for habitante in habitantes:
        if habitante["cor_olhos"] == "C" and habitante["cor_cabelos"] == "P":
            total_idade += habitante["idade"]
            count += 1
    return total_idade / count if count > 0 else 0


def maior_idade(habitantes):
    return max(habitante["idade"] for habitante in habitantes)


def quantidade_feminino_azuis_louros(habitantes):
    count = 0
    for habitante in habitantes:
        if (habitante["sexo"] == "F" and
            habitante["cor_olhos"] == "A" and
            habitante["cor_cabelos"] == "L" and
            18 <= habitante["idade"] <= 35):
            count += 1
    return count


def main():
    habitantes = ler_dados()
    print(f"Média de idade das pessoas com olhos castanhos e cabelos pretos: {media_idade_castanhos_pretos(habitantes)}")
    print(f"A maior idade entre os habitantes: {maior_idade(habitantes)}")
    print(f"Quantidade de indivíduos do sexo feminino, com idade entre 18 e 35 anos, olhos azuis e cabelos louros: {quantidade_feminino_azuis_louros(habitantes)}")


if __name__ == "__main__":
    main()

