""" Exercicio 1 """
import math

# Entrada
numero_inteiro = int(input('Escreva um numero inteiro'))

# Saida
print(f'O seu número é esse {numero_inteiro}')

""" Exercicio 2 """

# Entrada
numero_real = float(input('Escreva um numero real'))

# Saida
print(f'O seu número é esse {numero_real}')

""" Exercicio 3 """

# Entrada
valor_inteiro_1 = int(input('Escreva um numero inteiro '))
valor_inteiro_2 = int(input('Escreva outro numero inteiro'))
valor_inteiro_3 = int(input('Escreva mais um numero inteiro'))

# Processamento
soma_inteiros = valor_inteiro_1 + valor_inteiro_2 + valor_inteiro_3

# Saida
print(f'A soma dos três nuúmeros inteiros é {soma_inteiros}')

""" Exercicio 4 """

# Entrada
numero_real_1 = float(input('Escreva um numero real'))

# Processamento
potencia_real = numero_real_1**2

# Saída
print(f'Esse é o reusltado da potencia desse número {potencia_real}')

""" Exercicio 5 """

# Entrada
numero_real_2 = float(input('Escreva um numero real'))

# Processamento
quinta_parte = numero_real_2 / 5

# Saida
print(f'{quinta_parte} é a quinta parte desse numero real ')

""" Exercicio 6 """

# Entrada
temperatura_celsius_1 = float(input('Escreva uma temperatura em graus Celsius'))

# Processamento
temperatura_fahrenheit_1 = temperatura_celsius_1 * (9/5) + 32

# Saída
print(f'{temperatura_fahrenheit_1} é a temperatura escrita na escala de graus fahrenheit')

""" Exercicio 7 """

# Entrada
temperatura_fahrenheit_2 = float(input('Escreva uma temperatura em graus Fahreinheit'))

# Processamento
temperatura_celsius_2 = 5 * (temperatura_fahrenheit_2 - 32)/9

# Saida
print(f'{temperatura_celsius_2} é a temperatura escrita na escala de graus celsius')

""" Exercicio 8 """

# Entrada
temperatura_kelvin_1 = float(input('Esreva uma temperatura em graus Kelvin'))

# Processamento
temperatura_celsius_3 = temperatura_kelvin_1 - 273.15

# Saída
print(f'{temperatura_celsius_3} é a temperatura escrita na escala de graus celsius')

""" Exercicio 9 """

# Entrada
temperatura_celsius_4 = float(input('Escreva uma temperatura na escala de graus celsius'))

# Processamento
temperatura_kelvin_2 = temperatura_celsius_4 + 273.15

# Saída
print(f'{temperatura_kelvin_2} é a temperatura escrita na escala de graus kelvin')

""" Exercicio 10 """

# Entrada
velocidade_km_h_1 = float(input('Escreva uma velocidade em km/h'))

# Processamento
velocidade_m_s_1 = velocidade_km_h_1/3.6

# Saida
print(f'{velocidade_m_s_1} é velocidade na escala de metros por segundo')

""" Exercicio 11 """

# Entrada
velocidade_m_s_2 = float(input('Escreva uma velocidade em m/s'))

# Processamento
velocidade_km_h_2 = velocidade_m_s_2 * 3.6

# Saida
print(f'{velocidade_km_h_2} é a sua velocidade na escala de kilometros por hora')

""" Exercicio 12 """

# Entrada
milhas_1 = float(input('Escreva uma distancia em milhas'))

# Processamento
kilometros_1 = milhas_1 * 1.61

# Saída
print(f'{kilometros_1} é a distancia em kilometros ')

""" Exercicio 13 """

# Entrada
kilometros_2 = float(input('Escreva uma distancia em kilometros'))

# Processamento
milhas_2 = kilometros_2 / 1.61

# Saída
print(f'{milhas_2} é a distancia em milhas')

""" Exercicio 14 """

# Entrada
graus_1 = float(input('Escreva um angulo em graus'))

# Processamento
radianos_1 = graus_1 * 3.14/180

# Saída
print(f'{radianos_1} é o angulo em radianos')

""" Exercicio 15 """

# Entrada
radianos_2 = float(input('Escreva um angulo em radianos'))

# Processamento
graus_2 = radianos_2 * 180 / 3.14

# Saída
print(f'{graus_2} é o angulo em graus')

""" Exercicio 16 """

# Entrada
polegadas_1 = float(input('Escreva um comprimento em polegadas'))

# Processamento
centimetros_1 = polegadas_1 * 2.54

# Saída
print(f'{centimetros_1} é o comprimento em centimetros')

""" Exercicio 17 """

# Entrada
centimetros_2 = float(input('Escreva um comprimemto em centimetros'))

# Processamento
polegadas_2 = centimetros_2 / 2.54

# Saída
print(f'{polegadas_2} é o comprimento em polegadas')

""" Exercicio 18 """

# Entrada
volume_metros_cubicos_1 = float(input('Escreva um volume em metros cubicos'))

# Processamento
volume_litros_1 = volume_metros_cubicos_1 * 1000

# Saída
print(f'{volume_litros_1} é o volume em litros')

""" Exercicio 19 """

# Entrada
volume_litros_2 = float(input('Escreva um volume em litros'))

# Processamento
volume_metros_cubicos_2 = volume_litros_2 / 1000

# Saída
print(f'{volume_metros_cubicos_2} é o volume em metros cubicos')

""" Exercicio 20 """

# Entrada
kilogramas_1 = float(input('Escreva o valor de uma massa em kilos'))

# Processamento
libras_1 = kilogramas_1 / 0.45

# Saída
print(f'{libras_1} é o valor da massa em libras')

""" Exercicio 21 """

# Entrada
libras_2 = float(input('Escreva o valor de uma massa em libras'))

# Processamento
kilometros_2 = libras_2 * 0.45

# Saída
print(f'{kilometros_2} é o valor da massa em kilos ')

""" Exercicio 22 """

# Entrada
jardas_1 = float(input('Escreva um comprimento em jardas'))

# Processamento
metros_1 = jardas_1 * 0.91

# Saída
print(f'{metros_1} é o valor do comprimento em metros')

""" Exercicio 23 """

# Entrada
metros_2 = float(input('Escreva um comprimento em metros'))

# Processamento
jardas_2 = metros_2 / 0.91

# Saída
print(f'{jardas_2} é o valor do comprimento em jardas')

""" Exercicio 24 """

# Entrada
metros_quadrados_1 = float(input('Escreva uma área em metros quadrados'))

# Processamento
acres_1 = metros_quadrados_1 * 0.000247

# Saída
print(f'{acres_1} é o valor da área em acres')

""" Exercicio 25 """

# Entrada
acres_2 = float(input('Escreva uma área em acres'))

# Processamento
metros_quadrados_2 = acres_2 / 4048.58

# Saída
print(f'{metros_quadrados_2} é o valor da área em metros quadrados')

""" Exercicio 26 """

# Entrada
metros_quadrados_3 = float(input('Escreva uma área em metros quadrados'))

# Processamento
hectares_1 = metros_quadrados_3 * 0.0001

# Saída
print(f'{hectares_1} é o valor da área em hectares')

""" Exercicio 27 """

# Entrada
hectares_2 = float(input('Escreva uma área em hectares'))

# Processamento
metros_quadrados_4 = hectares_2 * 10000

# Saída
print(f'{metros_quadrados_4} é o valor da área em metros quadrados')

""" Exercicio 28 """

# Entrada
valor_1 = float(input('Escreva um valor qualquer'))
valor_2 = float(input('Escreva um valor qualquer'))
valor_3 = float(input('Escreva um valor qualquer'))

# Processamento
valor_final_1 = ((valor_1 ** 2) + (valor_2 ** 2) + (valor_3 ** 2))

# Saída
print(f'{valor_final_1} é a soma dos quadrados dos três valores')

""" Exercicio 29 """

# Entrada
nota_1 = float(input('Escreva uma nota'))
nota_2 = float(input('Escreva uma nota'))
nota_3 = float(input('Escreva uma nota'))
nota_4 = float(input('Escreva uma nota'))

# Processamento
media_1 = (nota_1 + nota_2 + nota_3 + nota_4) / 4

# Saída
print(f'{media_1} é a média das 4 notas lidas')

""" Exercicio 30 """

# Entrada
real = float(input('Escreva um valor em reais'))
cotacao_dolar = float(input('Escreva a cotação do dólar'))

# Processamento
dolar = real / cotacao_dolar

# Saída
print(f'{dolar} é o valor em dolares dessa quantidade de reais')

""" Exercicio 31 """

# Entrada
numero_inteiro_2 = int(input('Escreva um número inteiro'))

# Processamento
antecessor = numero_inteiro_2 - 1
sucessor = numero_inteiro_2 + 1

# Saída
print(f'{antecessor} é o antecessor desse numero inteiro lido, enquanto {sucessor} é o seu sucessor')

""" Exercicio 32 """

# Entrada
numero_inteiro_3 = int(input('Escreva um número inteiro'))

# Processamento
resultado = ((numero_inteiro_3 * 3) + 1) + ((numero_inteiro_3 * 2) - 1)

# Saída
print(f'{resultado} é o resultado da soma do sucessor de seu triplo com o antecessor de seu dobro')

""" Exercicio 33 """

# Entrada
lado_do_quadrado = float(input('Escreva o lado de um quadrado'))

# Processamento
area_do_quadrado = lado_do_quadrado ** 2

# Saída
print(f'{area_do_quadrado} é a área do quadrado de lado fornecido')

""" Exercicio 34 """

# Entrada
raio_do_circulo = float(input('Escreva o raio de um circulo'))

# Processamento
area_do_circulo = (raio_do_circulo ** 2) * 3.141592

# Saída
print(f'{area_do_circulo} é o valor da area do circulo dado o raio fornecido')

""" Exercicio 35 """

# Entrada
cateto_a = float(input('Forneça o cateto de um triangulo'))
cateto_b = float(input('Forneça o outro cateto de um triangulo'))

# Processamento
hipotenusa = math.sqrt(cateto_a + cateto_b)

# Saída
print(f'{hipotenusa} é o valor da hipotenusa de acordo coms o catetos a e b fornecidos')

""" Exercicio 36 """

# Entrada
altura_do_cilindro = float(input('Escreva a altura do cilindo'))
raio_do_cilindro = float(input('Escreva o raio do cilindro'))

# Processamento
volume_cilindro = altura_do_cilindro * (raio_do_cilindro ** 2) * 3.141592

# Saída
print(f'{volume_cilindro} é o volume do cilindro dado a altura e o raio fornecidos')

""" Exercicio 37 """

# Entrada
valor_do_produto = float(input('Escreva o valor de um produto'))

# Processamento
valor_com_desconto = valor_do_produto * 0.88

# Saída
print(f'R$ {valor_com_desconto} é o valor fornecido descontado de 12%')

""" Exercicio 38 """

# Entrada
salario_do_funcionario = float(input('Escreva o sálario do funcionário'))

# Processamento
salario_com_reajuste = salario_do_funcionario * 1.25

# Saída
print(f'R$ {salario_com_reajuste} é o valor do salario com reajuste de 25%')

""" Exercicio 39 """

# Processamento
primeiro_ganhador = 780_000 * 0.46
segundo_ganhador = 780_000 * 0.32
terceiro_ganhador = 780_000 - primeiro_ganhador - segundo_ganhador

# Saída
print(f'R$ {primeiro_ganhador} é o valor recebido pelo primeiro ganhador, R$ {segundo_ganhador} é o '
      f'valor recebido pelo segundo ganhador, R$ {terceiro_ganhador} é o valor recebibdo pelo terceiro ganhador')

""" Exercicio 40 """

# Entrada
dias_trabalhados = int(input('Quantos dias foram trabalhados?'))
salario_do_trabalhador = 30

# Processamento
salario_liquido = (salario_do_trabalhador * dias_trabalhados) * 0.92

# Saída
print(f'R$ {salario_liquido} é o seu salário liquido nesse mês')

""" Exercicio 41 """

# Entrada
valor_hora_trabalhada = float(input('Foneça o valor da sua hora de trabalho'))
horas_trabalhadas = float(input('Forneça a quantidade de horas trabalhas no mês'))

# Processamento
salario_final = (valor_hora_trabalhada * horas_trabalhadas) * 1.10

# Saída
print(f'R$ {salario_final} é o valor do seu sálario a ser pago')

""" Exercicicio 42 """

# Entrada
salario_base = float(input('Forneça o seu salário base'))

# Processamento
salario_a_receber = (salario_base * 1.05) * 0.93

# Saída
print(f'R$ {salario_a_receber} esse é o seu sálario a receber')

""" Exercicio 43 """

# Entrada
valor_lido = float(input('Forneça o valor do produto'))

# Processamento
total_a_pagar = valor_lido * 0.9
parcela = valor_lido / 3
comissao_a_vista = total_a_pagar * 0.05
comissao_parcelada = valor_lido * 0.05

# Saída
print(f'R$ {total_a_pagar} é o valor a ser pago com desconto a vista, R${parcela} é o valor da parcela'
      f'em três vezes sem juros, R$ {comissao_a_vista} é o valor da comissão do vendendor em '
      f'caso de pagamento a vista, R$ {comissao_parcelada} é o valor da comissão do vendedor em'
      f'caso de pagamento parcelado')

""" Exercicio 44 """

# Entrada
altura_do_degrau = float(input('Forneça a altura do degrau'))
altura_do_andar = float(input('Forneça a altura do andar que deseja'))

# Processamento
numero_de_degraus = altura_do_andar / altura_do_degrau

# Saída
print(f'{numero_de_degraus} é o numero de degraus que você deverá subir')

""" Exercicio 45 """

# Entrada
letra_maiuscula = int(input('Escreva o valor da tabela ASCII da letra maiscula'))

# Processamento
letra_minuscula = letra_maiuscula + 32

# Saída
print(f'{letra_minuscula} é o codigo da tabela ASCII da letra em versão minuscula')

""" Exercicio 46 """

# Entrada
numero_inteiro_tres_digitos = input('Forneça um numero inteiro positivio entre 100 a 999')

# Processamento
numero_invertido = numero_inteiro_tres_digitos[::-1]

# Saída
print(numero_invertido)

""" Exercicio 47 """

# Entrada
numero_inteiro_quatro_digitos = input('Escreva um numero de 4 digitos')

# Processamento
primeiro_digito = numero_inteiro_quatro_digitos[0]
segundo_digito = numero_inteiro_quatro_digitos[1]
terceiro_digito = numero_inteiro_quatro_digitos[2]
quarto_digito = numero_inteiro_quatro_digitos[3]

# Saída
print(f'{primeiro_digito} é o primeiro digito do seu numero, '
      f'{segundo_digito} é o segundo digito do seu numero, '
      f'{terceiro_digito} é o terceiro digito do seu numero, '
      f'{quarto_digito} é o quarto digito do seu numero')

""" Exercicio 48 """

# Entrada
segundos = int(input('Escreva uma quantidade de segundos'))

# Processamento
if segundos >= 3600:
    horas = segundos // 3600
    minutos = (segundos - (horas * 3600)) // 60
    segundos_final = (segundos - 3600) % 60
elif segundos >= 60:
    horas = 0
    minutos = segundos // 60
    segundos_final = segundos % 60
else:
    horas = 0
    minutos = 0
    segundos_final = segundos

# Sáida
print(f'{horas}: {minutos}: {segundos_final}')

""" Exercicio 49 """

# Entrada
horas_2 = int(input('Escreva uma quantidade de horas iniciais'))
minutos_2 = int(input('Escreva uma quantidade de minutos iniciais'))
segundos_2 = int(input('Escreva uma quantidade segundos iniciais'))
segundos_adicionados = int(input('Escreva quantos segundos você deseja adicionar'))

# Processamento
segundos_3 = horas_2 * 3600
segundos_4 = minutos_2 * 60
segundos_intermediario = segundos_3 + segundos_4 + segundos_adicionados

if segundos_intermediario >= 3600:
    horas_finais = segundos_intermediario // 3600
    minutos_finais = (segundos_intermediario - (horas_finais * 3600)) // 60
    segundos_finais = (segundos_intermediario - 3600) % 60
elif segundos_intermediario >= 60:
    horas_finais = 0
    minutos_finais = segundos_intermediario // 60
    segundos_finais = segundos_intermediario % 60
else:
    horas_finais = 0
    minutos_finais = 0
    segundos_finais = segundos_intermediario

print(f'{horas_finais}: {minutos_finais}: {segundos_finais}')


# Saída
print(f'O horario final é {horas_finais}: {minutos_finais}: {segundos_finais}')

""" Exercicio 50 """

# Entrada
idade = int(input('Escreva sua idade'))
ano_atual = int(input('Escreva o ano atual'))

# Processamento
ano_de_nascimento = ano_atual - idade

# Saída
print(f'{ano_de_nascimento} é o seu ano de nascimento')

""" Exercicio 51 """

# Entrada
coordenada_x = float(input('Escreva a coordeanda x do R2'))
coordenada_y = float(input('Escreva a coordenada y do R2'))

# Processamento
distancia_origem = math.sqrt((coordenada_x ** 2) + (coordenada_y ** 2))

# Saída
print(f'{distancia_origem} é a distancia desse ponto até a origem')

""" Exercicio 52 """

# Entrada
aposta_1 = int(input('Escreva o valor da aposta do primeiro amigo'))
aposta_2 = int(input('Escreva o valor da aposta do segundo amigo'))
aposta_3 = int(input('Escreva o valor da aposta do terceiro amigo'))
valor_do_premio = int(input('Escreva o valor do premio da loteria'))

# Processamento
premio_1 = aposta_1 * valor_do_premio / (aposta_1 + aposta_2 + aposta_3)
premio_2 = aposta_2 * valor_do_premio / (aposta_1 + aposta_2 + aposta_3)
premio_3 = aposta_3 * valor_do_premio / (aposta_1 + aposta_2 + aposta_3)

# Saída
print(f'R$ {premio_1} é o valor recebido pelo primeiro apostador, '
      f'R$ {premio_2} é o valor recebido pelo segundo apostador, '
      f'R$ {premio_3} é o valor recebido pelo terceiro apostador')

""" Exercicio 53 """

# Entrada
comprimento = float(input('Escreva o comprimento do seu terreno'))
largura = float(input('Escreva a largura do seu terreno'))
preco_metro_tela = float(input('Escreva o preço da cerca'))

# Processamento
custo_tela = (comprimento * 2 + largura * 2) * preco_metro_tela

# Saída
print(f'R$ {custo_tela} é o custo para cercar todo o seu terreno')
