"""
1. Crie um programa que.
a) Crie/abra um arquivo texto de nome “arq.txt”
b) Permita que o usuário grave diversos caracteres nesse arquivo, até que o usuário entre com o caractere “0”.
c) Feche o arquivo
d) Abra, leia o arquivo e escreva na tela todos os caracteres armazenados.
"""

with open('arq.txt', 'w') as arquivo:
    while True:
        caractere: str = (input('Escreva o caractere do arquivo usuário'))
        if caractere != 'O':
            arquivo.write(f'{caractere}\n')
        else:
            break


with open('arq.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

for linha in linhas:
    print(linha)

"""
2. Faça um programa que receba do usuário o nome de um arquivo texto e mostre
na tela quantas letras são vogais e quantas são consoantes.

"""

vogais: int = 0
consoantes: int = 0
arquivo: str = input('Informe o nome do arquivo para abrir')

with open(arquivo, 'r') as arquivo_2:
    linhas_2 = arquivo_2.readlines()

for linha in linhas_2:
    if linha.replace('\n', '').lower() in ['a', 'e', 'i', 'o', 'u']:
        vogais = vogais + 1
    else:
        consoantes = consoantes + 1


if vogais > 0:
    print(f'Existe(m) {vogais} vogais no arquivo.')
else:
    print('Não existem vogais no arquivo')

if consoantes > 0:
    print(f'Existe(m) {consoantes} consoantes no arquivo.')
else:
    print('Não existem consoantes no arquivo')

"""
3. Faça um programa que receba do usuário o nome de um arquivo texto e mostre na tela
quantas linhas este arquivo possui.
"""

arquivo: str = input('Informe o nome do arquivo para abrir')

with open(arquivo, 'r') as arquivo_2:
    linhas_2 = arquivo_2.readlines()

print(f'Existe(m) {len(linhas)} linhas no arquivo')
