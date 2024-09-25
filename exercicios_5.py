""" Exercicio 1 """
import math
import cmath
# Entrada
numero_1 = float(input('Escreva um número'))
numero_2 = float(input('Escreva um número'))

# Processamento e Saída
if numero_1 > numero_2:
    print(f'{numero_1} é o maior número')
elif numero_2 > numero_1:
    print(f'{numero_2} é o maior número')
else:
    print('Não há maior número, ambos são iguais')

""" Exercicio 2 """

# Entrada
numero_3 = float((input('Escreva um número')))

# Processamento e Saída
if numero_3 >= 0:
    raiz_3 = math.sqrt(numero_3)
    print(f'{raiz_3} é a raiz quadrada desse número')
else:
    print('Esse número é invalido')

""" Exercicio 3 """

# Entrada
numero_4 = float(input('Escreva um número'))

# Processamento e Saída
if numero_4 >= 0:
    raiz_4 = math.sqrt(numero_4)
    print(f'{raiz_4} é a raiz quadrada desse número')
else:
    quadrado_1 = numero_4 ** 2
    print(f'{quadrado_1} é o quadrado desse número')

""" Exercicio 4 """

# Entrada
numero_5 = float(input('Escreva um número'))

# Processamento e Saída
if numero_5 >= 0:
    quadrado_2 = numero_5 ** 2
    raiz_5 = math.sqrt(numero_5)
    print(f'{quadrado_2} é o quadrado desse número '
          f'{raiz_5} é a raiz quadrada desse número')

""" Exercicio 5 """

# Entrada
numero_6 = int(input('Escreva um número inteiro'))

# Processamento e Saída
if numero_6 % 2 == 0:
    print('Esse número é par')
else:
    print('Esse número é impar')

""" Exercicio 6 """

# Entrada
numero_7 = int(input('Escreva o valor de um número inteiro'))
numero_8 = int(input('Escreva o valor de um número inteiro'))

# Processamento e Saída
if numero_8 > numero_7:
    diferenca_1 = numero_8 - numero_7
    print(f'{numero_8} é o maior número, com a diferença de {diferenca_1} unidades')
else:
    diferenca_1 = numero_7 - numero_8
    print(f'{numero_7} é o maior número, com a diferença de {diferenca_1} unidades')

""" Exercicio 7 """

# Entrada
numero_9 = float(input('Escreva um número'))
numero_10 = float(input('Escreva um número'))

# Processamento e Saída
if numero_9 > numero_10:
    print(f'{numero_9} é o maior número')
elif numero_10 > numero_9:
    print(f'{numero_9} é o maior número')
else:
    print('Números iguais')

""" Exercicio 8 """

# Entrada
nota_1 = float(input('Escreva uma nota'))
nota_2 = float(input('Escreva um nota'))

# Processamento e Saída
if nota_1 > 10 or nota_2 > 10:
    print('Nota invalida')
elif nota_1 < 0 or nota_2 < 0:
    print('Nota invalida')
else:
    media = (nota_1 + nota_2) / 2
    print(f'{media} é a sua média')

""" Exercicio 9 """

# Entrada
salario = int(input('Escreva o seu salário'))
prestacao = int(input('Escreva o valor da prestação'))

# Processamento e Saída
if prestacao > salario * 0.2:
    print('Emprestimo não concedido')
else:
    print('Emprestimo concedido')

""" Exercicio 10 """

# Entrada
altura = float(input('Escreva sua altura em metros'))
sexo = input('Escreva seu sexo')

# Processamento e Saída
if sexo == 'Homem':
    peso_ideal = (72.7 * altura) - 58
    print(f'{peso_ideal} é o seu peso ideal')
elif sexo == 'Mulher':
    peso_ideal = (62.1 * altura) - 44.7
    print(f'{peso_ideal} é o seu peso ideal')
else:
    print('Escreva Homem ou Mulher')

""" Exercicio 11 """

# Entrada
numero_11 = int(input('Escreva um número inteiro de três digitos'))

# Processamento e Saída
if numero_11 >= 0:
    algarismo = str(numero_11)[0]
    algarismo_2 = str(numero_11)[1]
    algarismo_3 = str(numero_11)[2]
    soma = int(algarismo) + int(algarismo_2) + int(algarismo_3)
    print(f'{soma} é a soma dos algarismo do seu número')
else:
    print('Número inválido')

""" Exercicio 12 """

# Entrada
numero_12 = int(input('Escreva um número inteiro'))

# Processamento e Saída
if numero_12 >= 0:
    logaritmo = math.log10(numero_12)
    print(f'{logaritmo} é o logaritmo do número escolhido')
else:
    print('Número inválido')

""" Exercicio 13 """

# Entrada
nota_3 = int(input('Escreva sua primeira nota de peso 1'))
nota_4 = int(input('Escreva sua segunda nota de peso 1'))
nota_5 = int(input('Escreva sua terceira nota de peso 3'))

# Processamento e Saída
media_ponderada_1 = (nota_3 + nota_4 + (nota_5 * 2)) / 4
if media_ponderada_1 >= 60:
    print(f'{media_ponderada_1} é a sua média nessa matéria, Parabéns Sujeito, voce foi Aprovado')
else:
    print(f'{media_ponderada_1} é a sua média dessa disciplina, infelizmente você tá Reprovado Aquino, '
          f'pela felicidade de nosso amigo Dornelos')

""" Exercicio 14 """

# Entrada
trabalho_laboratorio = int(input('Escreva a nota do trabalho do laboratorio'))
avaliacao_semestral = int(input('Escreva a nota da sua avaliação semestral'))
exame_final = int(input('Escreva a nota do exame final'))

# Processamento e Saída
media_ponderada_2 = ((trabalho_laboratorio * 2) + (avaliacao_semestral * 3) + (exame_final * 5)) / 10
if media_ponderada_2 >= 5:
    print('Voce ta Aprovado Aquino')
elif media_ponderada_2 >= 3:
    print('Voce está de Recuperação Aquino')
else:
    print('Você está Reprovado Aquino')

""" Exercicio 15 """
# Entrada
dia_da_semana = int(input('Escreva um número de 1 a 7'))

# Processamento e Saída
if dia_da_semana == 1:
    print('Domingo')
elif dia_da_semana == 2:
    print('Segunda-feira')
elif dia_da_semana == 3:
    print('Terça-feira')
elif dia_da_semana == 4:
    print('Quarta-feira')
elif dia_da_semana == 5:
    print('Quinta-feira')
elif dia_da_semana == 6:
    print('Sexta-feira')
elif dia_da_semana == 7:
    print('Sabado')

""" Exercicio 16 """

# Entrada
mes_do_ano = int(input('Escreva um número de 1 a 12'))

# Processamento e Saída
if mes_do_ano == 1:
    print('Janeiro')
elif mes_do_ano == 2:
    print('Fevereiro')
elif mes_do_ano == 3:
    print('Março')
elif mes_do_ano == 4:
    print('Abril')
elif mes_do_ano == 5:
    print('Maio')
elif mes_do_ano == 6:
    print('Junho')
elif mes_do_ano == 7:
    print('Julho')
elif mes_do_ano == 8:
    print('Agosto')
elif mes_do_ano == 9:
    print('Setembro')
elif mes_do_ano == 10:
    print('Outubro')
elif mes_do_ano == 11:
    print('Novembro')
elif mes_do_ano == 12:
    print('Dezembro')

""" Exercicio 17 """

# Entrada
base_maior = float(input('Escreva a base maior de um trapézio'))
base_menor = float(input('Escreva a base menor de um trapézio'))
altura = float(input('Escreva a altura de um trapézio'))

# Processamento e Saída
if base_maior > 0 and base_menor > 0:
    area_do_trapezio = ((base_maior + base_menor) * altura) / 2
    print(f'{area_do_trapezio} é a área do trapézio')

""" Exercicio 18 """

# Entrada
menu = input('Escolha entre quatro operações, Adição, Subtração, Multiplicação e Divisão')
numero_13 = float(input('Escreva um número'))
numero_14 = float(input('Escreva um número'))

# Processamento e Saída
if menu == 'Adição':
    soma_2 = numero_13 + numero_14
    print(f'{soma_2} é o resultado da soma desses dois números')
elif menu == 'Subtração':
    subtracao = numero_13 - numero_14
    print(f'{subtracao} é o resultado da subtração desses dois números')
elif menu == 'Multiplicação':
    multiplicacao = numero_13 * numero_14
    print(f'{multiplicacao} é o resultado da multiplicação desses dois números')
elif menu == 'Divisão':
    divisao = numero_13 / numero_14
    print(f'{divisao} é o resultado da divisão desses dois números')
else:
    print('Opção invalida, escolha entre Adição, Subtração, Multiplicação e Divisão')

""" Exercicio 19 """

# Entrada
numero_15 = int(input('Escreva um número'))

# Processamento e Saída
if numero_15 % 3 == 0 and not numero_15 % 5 == 0:
    print('Esse número é divisivel por 3')
elif not numero_15 % 3 == 0 and numero_15 % 5 == 0:
    print('É divisivel simultaneo por 5')
else:
    print('Esse número é divisivel ambos por 3 e 5')

""" Exercicio 20 """

# Entrada
l_1 = int(input('Escreva o lado de um triangulo'))
l_2 = int(input('Escreva o lado de um triangulo'))
l_3 = int(input('Escreva o lado de um triangulo'))

# Processamento e Saída
if l_1 < l_2 + l_3 and l_2 < l_1 + l_3\
 and l_3 < l_1 + l_2:
    if l_2 == l_3 == l_1:
        print('Esses lados são valídas como um triangulo do tipo equilátero')
    elif l_2 == l_3 != l_1:
        print('Esses lados são valídas como um triangulo do tipo isosceles')
    elif l_2 != l_1 != l_3:
        print('Esses lados são valídas como um triangulo do tipo escaleno')
else:
    print('Esses lados não são validos')

""" Exercicio 21 """

# Entrada
menu_2 = int(input('Escolha uma opção entre essas 4 números: 1 - Soma de 2 números ; 2 - Diferença entre 2 números'
                   '; 3 - Produto entre 2 números ; 4 - Divisão entre 2 números'))
numero_16 = int(input('Escreva um número'))
numero_17 = int(input('Escreva um número'))

# Processamento e Saída
if menu_2 == 1:
    soma_3 = numero_16 + numero_17
    print(f'{soma_3} é a soma dos 2 números acima')
elif menu_2 == 2:
    if numero_16 < numero_17:
        diferenca_2 = numero_17 - numero_16
        print(f'{diferenca_2} é a subtração desses 2 números')
    elif numero_16 > numero_17:
        diferenca_2 = numero_16 - numero_17
        print(f'{diferenca_2} é a subtração desses 2 números')
elif menu_2 == 3:
    multiplicacao_2 = numero_17 * numero_16
    print(f'{multiplicacao_2} é o resultado da multiplicação desses números')
elif menu_2 == 4:
    if numero_17 != 0:
        divisao_2 = numero_16 / numero_17
    else:
        print('Erro')
else:
    print('Erro')

""" Exercicio 22 """

# Entrada
idade_1 = int(input('Escreva a sua idade'))
tempo_1 = int(input('Escreva o seu tempo de contribuição'))

# Processamento e Saída
if idade_1 >= 65:
    print('Voce pode se aposentar')
elif tempo_1 >= 30:
    print('Voce pode se aposentar')
elif tempo_1 >= 25 and idade_1 >= 60:
    print('Voce pode se aposentar')
else:
    print('Voce não pode se aposentar')


""" Exercicio 23 """

# Entrada
ano_1 = int(input('Escreva um ano'))

if ano_1 % 400 == 0:
    print('Esse ano é bissexto')
elif ano_1 % 4 == 0 and not ano_1 % 100 == 0:
    print('Esse ano é bissexto')
else:
    print('Esse ano não é bissexto')

""" Exercicio 24 """

# Entrada
estado_1 = input('Escreva a Sigla do estado para o onde o produto está sendo vendido')
valor_1 = float(input('Escreva o valor do produto vendido'))

# Processamento e Saída
if estado_1 == 'RJ':
    imposto_1 = 0.15 * valor_1
    print(f'{imposto_1} é o valor do imposto')
elif estado_1 == 'RJ':
    imposto_1 = 0.15 * valor_1
    print(f'{imposto_1} é o valor do imposto')
elif estado_1 == 'RJ':
    imposto_1 = 0.15 * valor_1
    print(f'{imposto_1} é o valor do imposto')
elif estado_1 == 'RJ':
    imposto_1 = 0.15 * valor_1
    print(f'{imposto_1} é o valor do imposto')
else:
    print('Erro')

""" Exercicio 25 """

# Entrada
a = float(input('Escreva o coeficiente a da equação do 2 grau'))
b = float(input('Escreva o coeficiente b da equação do 2 grau'))
c = float(input('Escreva o coeficiente c da equação do 2 grau'))

# Processamento e Saída
delta = (b ** 2) - 4 * a * c
x_1 = (- b + cmath.sqrt(delta)) / 2 * a
x_2 = (- b - cmath.sqrt(delta)) / 2 * a

if a == 0:
    print('Não é equação do segundo grau')
elif a != 0:
    if delta < 0:
        print('Não existe raiz')
    elif delta == 0:
        print(f'{x_1} é a unica raiz dessa equação')
    elif delta > 0:
        print(f'{x_1} e {x_2} são as raizes dessa equação')

""" Exercicio 26 """

# Entrada
distancia = int(input('Escreva a distancia '))
litros_gasolina = int(input('Escreva a quantidade de litros consumidos'))

# Processamento e Saída
consumo_1 = distancia / litros_gasolina
if consumo_1 <= 8:
    print('VENDA O CARRO')
elif 8 < consumo_1 < 14:
    print('Economico')
elif consumo_1 > 14:
    print('Super economico')


""" Exercicio 27 """

# Entrada
idade_2 = int(input('Escreva sua idade nadador'))

# Processamento e Saída
if 5 <= idade_2 <= 7:
    print(f'Categoria Infantil A')
elif 8 <= idade_2 <= 10:
    print(f'Categoria Infantil B')
elif 11 <= idade_2 <= 13:
    print(f'Categoria Juvenil A')
elif 14 <= idade_2 <= 17:
    print(f'Categoria Juvenil B')
elif idade_2 >= 18:
    print(f'Categoria Sênior')

""" Exercicio 28 """

# Entrada
numero_21 = int(input('Escreva o número para opção espefica: 1 - Geométrica ; 2 - Ponderada ; 3 - Harmônica ; '
                      '4 - Aritmética'))
numero_18 = int(input('Escreva um número inteiro positivo'))
numero_19 = int(input('Escreva um número inteiro positivo'))
numero_20 = int(input('Escreva um número inteiro positivo'))

# Processamento e Saída
if numero_21 == 1:
    media_1 = (numero_20 * numero_18 * numero_19) * 1/3
elif numero_21 == 2:
    media_1 = (numero_18 + (numero_20 * 3) + (numero_19 * 2)) / 6
elif numero_21 == 3:
    media_1 = 1 / ((1 / numero_20) + (1 / numero_19) + (1 / numero_18))
elif numero_21 == 4:
    media_1 = (numero_20 + numero_18 + numero_19) / 3

""" Exercicio 29
 Muito avançado, voltar depois"""


""" Exercicio 30 """

# Entrada
numero_22 = float(input('Escreva um número'))
numero_23 = float(input('Escreva um número'))
numero_24 = float(input('Escreva um número'))

# Processamento e Saída
if numero_24 > numero_23 > numero_22:
    print(f'{numero_24}, {numero_23}, {numero_22}')
elif numero_23 > numero_22 > numero_24:
    print(f'{numero_23}, {numero_22}, {numero_24}')
elif numero_24 > numero_22 > numero_23:
    print(f'{numero_24}, {numero_22}, {numero_23}')
elif numero_23 > numero_24 > numero_22:
    print(f'{numero_23}, {numero_24}, {numero_22}')
elif numero_22 > numero_24 > numero_23:
    print(f'{numero_22}, {numero_24}, {numero_23}')
elif numero_22 > numero_23 > numero_24:
    print(f'{numero_22}, {numero_23}, {numero_24}')


""" Exercicio 31 """

# Entrada
altura_1 = float(input('Escreva sua altura'))
peso_1 = float(input('Escreva o seu Peso'))

# Processamento e Saída
if altura_1 < 1.20:
    if peso_1 < 60:
        print('Classificação A')
    elif 60 <= peso_1 <= 90:
        print('Classificação D')
    elif peso_1 > 90:
        print('Classificação G')
elif 1.2 <= altura_1 <= 1.70:
    if peso_1 < 60:
        print('Classificação B')
    elif 60 <= peso_1 <= 90:
        print('Classificação E')
    elif peso_1 > 90:
        print('Classificação H')
elif altura_1 > 1.70:
    if peso_1 < 60:
        print('Classificação C')
    elif 60 <= peso_1 <= 90:
        print('Classificação F')
    elif peso_1 > 90:
        print('Classificação I')

""" Exercicio 32 """

# Entrada
codigo = int(input('Escreva o codigo do produto entre 100 a 106'))
quantidade_1 = int(input('Escreva a quantidade do pedido'))

# Processamento e Saída
if codigo == 100:
    valor_2 = quantidade_1 * 1.2
    print(f'{valor_2} é o valor do pedido')
elif codigo == 101:
    valor_2 = quantidade_1 * 1.3
    print(f'{valor_2} é o valor do pedido')
elif codigo == 102:
    valor_2 = quantidade_1 * 1.5
    print(f'{valor_2} é o valor do pedido')
elif codigo == 103:
    valor_2 = quantidade_1 * 1.2
    print(f'{valor_2} é o valor do pedido')
elif codigo == 104:
    valor_2 = quantidade_1 * 1.7
    print(f'{valor_2} é o valor do pedido')
elif codigo == 105:
    valor_2 = quantidade_1 * 2.2
    print(f'{valor_2} é o valor do pedido')
elif codigo == 106:
    valor_2 = quantidade_1 * 1
    print(f'{valor_2} é o valor do pedido')

""" Exercicio 33 """

# Entrada
valor_antigo = int(input('Escreva o valor antigo do produto'))

# Processamento e Saída
if valor_antigo < 50:
    preco_novo = valor_antigo * 1.05
    print(f'{preco_novo} é o preço novo, considerado Barato')
elif 50 <= valor_antigo <= 100:
    preco_novo = valor_antigo * 1.10
    if preco_novo < 80:
        print(f'{preco_novo} é o preço novo, considerado Barato')
    elif preco_novo >= 80:
        print(f'{preco_novo} é o preço novo, considerado Normal')
elif valor_antigo >= 100:
    preco_novo = valor_antigo * 1.15
    if 80 <= preco_novo <= 120:
        print(f'{preco_novo} é o preço novo, considerado Normal')
    elif 120 <= preco_novo <= 200:
        print(f'{preco_novo} é o preço novo, considerado Caro')
    elif preco_novo > 120:
        print(f'{preco_novo} é o preço novo, considerado Muito Caro')

""" Exercicio 34 """

# Entrada
nota_6 = float(input('Escreva sua nota'))
faltas_1 = int(input('Escreva a sua quantidade'))

# Processamento e Saída
if 9 <= nota_6 <= 10:
    if faltas_1 <= 20:
        print('Conceito A')
    elif faltas_1 > 20:
        print('Conceito B')
elif 7.5 <= nota_6 <= 8.9:
    if faltas_1 <= 20:
        print('Conceito B')
    elif faltas_1 > 20:
        print('Conceito C')
elif 5 <= nota_6 <= 7.4:
    if faltas_1 <= 20:
        print('Conceito C')
    elif faltas_1 > 20:
        print('Conceito D')
elif 4 <= nota_6 <= 4.9:
    if faltas_1 <= 20:
        print('Conceito D')
    elif faltas_1 > 20:
        print('Conceito E')
elif 0 <= nota_6 <= 3.9:
    if faltas_1 <= 20:
        print('Conceito E')
    elif faltas_1 > 20:
        print('Conceito E')

""" Exercicio 35 """

# Entrada
dia_1 = int(input('Escreva um dia de uma data'))
mes_1 = int(input('Escreva um mes de uma data'))
ano_2 = int(input('Escreva um ano'))

# Processamento
if ano_2 % 400 == 0 or (ano_2 % 4 == 0 and not ano_2 % 100 == 0):
    if mes_1 == 2:
        if 0 <= dia_1 <= 29:
            print('É uma data valida')
        else:
            print('Essa data não é valida')
    elif mes_1 == 1 or mes_1 == 3 or mes_1 == 5 or mes_1 == 7 or mes_1 == 8 or mes_1 == 9 or mes_1 == 12:
        if 0 <= dia_1 <= 31:
            print('É uma data válida')
        else:
            print('Essa data não é valida')
    elif mes_1 == 4 or mes_1 == 6 or mes_1 == 9 or mes_1 == 22:
        if 0 <= dia_1 <= 30:
            print('É uma data válida')
        else:
            print('Essa data não é valida')
    else:
        print('Essa data não é valida')
else:
    if mes_1 == 2:
        if 0 <= dia_1 <= 28:
            print('É uma data valida')
        else:
            print('Essa data não é valida')
    elif mes_1 == 1 or mes_1 == 3 or mes_1 == 5 or mes_1 == 7 or mes_1 == 8 or mes_1 == 9 or mes_1 == 12:
        if 0 <= dia_1 <= 31:
            print('É uma data válida')
        else:
            print('Essa data não é valida')
    elif mes_1 == 4 or mes_1 == 6 or mes_1 == 9 or mes_1 == 22:
        if 0 <= dia_1 <= 30:
            print('É uma data válida')
        else:
            print('Essa data não é valida')
    else:
        print('Essa data não é valida')

""" Exercicio 36 """

# Entrada
valor_venda = int(input('Escreva o valor da venda'))

# Processamento
if valor_venda >= 100_000:
    comissao_1 = 700 + 0.16 * valor_venda
elif 80_000 <= valor_venda < 100_000:
    comissao_1 = 650 + 0.14 * valor_venda
elif 60_000 <= valor_venda < 80_000:
    comissao_1 = 600 + 0.14 * valor_venda
elif 40_000 <= valor_venda < 60_000:
    comissao_1 = 550 + 0.14 * valor_venda
elif 20_000 <= valor_venda < 40_000:
    comissao_1 = 500 + 0.14 * valor_venda
elif valor_venda < 20_000:
    comissao_1 = 400 + 0.14 * valor_venda

""" Exercicio 38 """

# Entrada
hora_entrada = int(input('Escreva a hora de entrada'))
minutos_entrada = int(input('Escreva os minutos de entrada'))
hora_saida = int(input('Escreva a hora de saida'))
minutos_saida = int(input('Escreva os minutos de saida'))

# Processamento e Saída
entrada = (hora_entrada * 60) + minutos_entrada
saida = (hora_saida * 60) + minutos_saida
tempo_2 = saida - entrada

if 0 < tempo_2 <= 60:
    valor_3 = 1
    print(f'{valor_3} é o preço cobrado pelo estacionamento')
elif 60 < tempo_2 <= 120:
    valor_3 = 2
    print(f'{valor_3} é o preço cobrado pelo estacionamento')
elif 120 < tempo_2 <= 180:
    valor_3 = 3.4
    print(f'{valor_3} é o preço cobrado pelo estacionamento')
elif 180 < tempo_2 <= 240:
    valor_3 = 4.8
    print(f'{valor_3} é o preço cobrado pelo estacionamento')
elif 240 < tempo_2 <= 300:
    valor_3 = 6.8
    print(f'{valor_3} é o preço cobrado pelo estacionamento')
elif tempo_2 > 300:
    valor_3 = math.ceil((tempo_2 - 300) / 60) * 2 + 6.8
    print(f'{valor_3} é o preço cobrado pelo estacionamento')
elif tempo_2 < 0:
    valor_3 = math.ceil(((tempo_2 + 1440) - 300) / 60) * 2 + 6.8
    print(f'{valor_3} é o preço cobrado pelo estacionamento')

""" Exercicio 38 """

# Entrada
dia_2 = int(input('Escreva o dia da data de nascimento'))
mes_2 = int(input('Escreva o mês de uma data de nascimento'))
ano_3 = int(input('Escreva o ano de uma data de nascimento'))

# Processamento
if ano_3 % 400 == 0 or (ano_3 % 4 == 0 and not ano_3 % 100 == 0) and ano_3 <= 2008:
    if mes_2 == 2:
        if 0 <= dia_2 <= 29:
            print('É uma data valida')
        else:
            print('Essa data não é valida')
    elif mes_2 == 1 or mes_2 == 3 or mes_2 == 5 or mes_2 == 7 or mes_2 == 8 or mes_2 == 9 or mes_2 == 12:
        if 0 <= dia_2 <= 31:
            print('É uma data válida')
        else:
            print('Essa data não é valida')
    elif mes_2 == 4 or mes_2 == 6 or mes_2 == 9 or mes_2 == 22:
        if 0 <= dia_2 <= 30:
            print('É uma data válida')
        else:
            print('Essa data não é valida')
    else:
        print('Essa data não é valida')
elif ano_3 <= 2008:
    if mes_2 == 2:
        if 0 <= dia_2 <= 28:
            print('É uma data valida')
        else:
            print('Essa data não é valida')
    elif mes_2 == 1 or mes_2 == 3 or mes_2 == 5 or mes_2 == 7 or mes_2 == 8 or mes_2 == 9 or mes_2 == 12:
        if 0 <= dia_2 <= 31:
            print('É uma data válida')
        else:
            print('Essa data não é valida')
    elif mes_2 == 4 or mes_2 == 6 or mes_2 == 9 or mes_2 == 22:
        if 0 <= dia_2 <= 30:
            print('É uma data válida')
        else:
            print('Essa data não é valida')
    else:
        print('Essa data não é valida')
else:
    print('Essa data não é valida')

""" Exercicio 39 """

# Entrada
salario_atual = float(input('Escreva o seu salário atual'))
tempo_de_servico = int(input(' Escreva quantos anos voce tem de trabalho na empresa'))

# Processamento e Saída
if salario_atual < 500:
    if tempo_de_servico < 1:
        salario_reajustado = salario_atual * 1.25
        print(f'{salario_reajustado} é o valor do seu novo salário')
    elif 1 <= tempo_de_servico <= 3:
        salario_reajustado = salario_atual * 1.25 + 100
        print(f'{salario_reajustado} é o valor do seu novo salário')
    elif 4 <= tempo_de_servico <= 6:
        salario_reajustado = salario_atual * 1.25 + 200
        print(f'{salario_reajustado} é o valor do seu novo salário')
    elif 7 <= tempo_de_servico <= 10:
        salario_reajustado = salario_atual * 1.25 + 300
        print(f'{salario_reajustado} é o valor do seu novo salário')
    elif tempo_de_servico > 10:
        salario_reajustado = salario_atual * 1.25 + 500
        print(f'{salario_reajustado} é o valor do seu novo salário')
elif 500 < salario_atual < 1000:
    if tempo_de_servico < 1:
        salario_reajustado = salario_atual * 1.20
        print(f'{salario_reajustado} é o valor do seu novo salário')
    elif 1 <= tempo_de_servico <= 3:
        salario_reajustado = salario_atual * 1.20 + 100
        print(f'{salario_reajustado} é o valor do seu novo salário')
    elif 4 <= tempo_de_servico <= 6:
        salario_reajustado = salario_atual * 1.20 + 200
        print(f'{salario_reajustado} é o valor do seu novo salário')
    elif 7 <= tempo_de_servico <= 10:
        salario_reajustado = salario_atual * 1.20 + 300
        print(f'{salario_reajustado} é o valor do seu novo salário')
    elif tempo_de_servico > 10:
        salario_reajustado = salario_atual * 1.20 + 500
        print(f'{salario_reajustado} é o valor do seu novo salário')
elif 1000 < salario_atual < 1500:
    if tempo_de_servico < 1:
        salario_reajustado = salario_atual * 1.15
        print(f'{salario_reajustado} é o valor do seu novo salário')
    elif 1 <= tempo_de_servico <= 3:
        salario_reajustado = salario_atual * 1.15 + 100
        print(f'{salario_reajustado} é o valor do seu novo salário')
    elif 4 <= tempo_de_servico <= 6:
        salario_reajustado = salario_atual * 1.15 + 200
        print(f'{salario_reajustado} é o valor do seu novo salário')
    elif 7 <= tempo_de_servico <= 10:
        salario_reajustado = salario_atual * 1.15 + 300
        print(f'{salario_reajustado} é o valor do seu novo salário')
    elif tempo_de_servico > 10:
        salario_reajustado = salario_atual * 1.15 + 500
        print(f'{salario_reajustado} é o valor do seu novo salário')
elif 1500 < salario_atual < 2000:
    if tempo_de_servico < 1:
        salario_reajustado = salario_atual * 1.10
        print(f'{salario_reajustado} é o valor do seu novo salário')
    elif 1 <= tempo_de_servico <= 3:
        salario_reajustado = salario_atual * 1.10 + 100
        print(f'{salario_reajustado} é o valor do seu novo salário')
    elif 4 <= tempo_de_servico <= 6:
        salario_reajustado = salario_atual * 1.10 + 200
        print(f'{salario_reajustado} é o valor do seu novo salário')
    elif 7 <= tempo_de_servico <= 10:
        salario_reajustado = salario_atual * 1.10 + 300
        print(f'{salario_reajustado} é o valor do seu novo salário')
    elif tempo_de_servico > 10:
        salario_reajustado = salario_atual * 1.10 + 500
        print(f'{salario_reajustado} é o valor do seu novo salário')
else:
    print('Você não tem direito a reajuste')

""" Exercicio 40 """

# Entrada
custo_fabrica = int(input('Escreva o custo de fabrica do carro'))

# Processamento e Saída
if custo_fabrica < 12_000:
    custo_carro = custo_fabrica * 1.05
    print(f'{custo_carro} é o custo do carro para o consumidor final')
elif 12_000 <= custo_fabrica <= 25_000:
    custo_carro = custo_fabrica * 1.10 * 1.15
    print(f'{custo_carro} é o custo do carro para o consumidor final')
elif custo_fabrica > 25_000:
    custo_carro = custo_fabrica * 1.15 * 1.20
    print(f'{custo_carro} é o custo do carro para o consumidor final')

""" Exercicio 41 """

# Entrada
peso = float(input('Escreva o seu Peso'))
altura = float(input('Escreva a sua altura'))

# Processamento e Saída
imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'{imc} esse é o seu IMC, está abaixo do peso')
elif 18.6 <= imc <= 24.9:
    print(f'{imc} esse é o seu IMC, está Saudável')
elif 25 <= imc <= 29.9:
    print(f'{imc} esse é o seu IMC, está com o peso em excesso')
elif 30 <= imc <= 34.9:
    print(f'{imc} esse é o seu IMC, Obesidade Grau I')
elif 35 <= imc <= 39.9:
    print(f'{imc} esse é o seu IMC, Obesidade Grau II (severa)')
elif imc >= 40:
    print(f'{imc} esse é o seu IMC, Obesidade Grau III (Mórbida)')

