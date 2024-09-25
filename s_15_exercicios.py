""" 1. Crie uma classe Pessoa, contendo nome, data de nascimento e email. Crie as propriedades getters e
setters para os atributos e um método para imprimir os dados de uma pessoa """

from datetime import date


class Pessoa:

    def __init__(self, nome: str, data_nascimento: date, email: str) -> None:
        self.__nome: str = nome
        self.__data_nascimento: date = data_nascimento
        self.__email: str = email

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str) -> None:
        self.__nome = nome

    @property
    def data_nascimento(self) -> date:
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento: date) -> None:
        self.__data_nascimento = data_nascimento

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str) -> None:
        self.__email = email

    def imprimir(self) -> None:
        print(f'Nome: {self.nome}')
        print(f'E-mail: {self.email}')
        print(f'Data de Nascimento: {self.data_nascimento}')


# pessoa_1 = Pessoa('Angelina Jolie', date(1975, 6, 4), 'angelinajolie@gmail.com')

# pessoa_1.impirmir()


"""
2. Crie uma classe Agenda que pode armazenar contatos e seja possível realizar as seguintes operações:
a) armazenar_contato(contato: Contato);
b) remover_contato(contato: Contato);
c) buscar_contato(nome: str); // Informa em que posição da agenda está o contato.
d) imprimir_agenda(); // Imprime os dados de todos os contatos da agenda.
e) imprimir_contato(indice: int); // Imprime os dados do contato informado pelo índice.
"""

from typing import List


class Agenda:

    def __init__(self):
        self.__contatos: List[Pessoa] = []

    @property
    def contatos(self) -> List[Pessoa]:
        return self.__contatos

    def armazenar_contato(self, contato: Pessoa) -> None:
        self.__contatos.append(contato)

    def remover_contatos(self, contato: Pessoa) -> None:
        self.__contatos.remove(contato)

    def buscar_contato(self, nome: str) -> None:
        for indice, contato in enumerate(self.contatos):
            if contato.nome == nome:
                print(f'O contato {nome} está na posição {indice}')

    def imprimir_agenda(self) -> None:
        for contato in self.contatos:
            contato.imprimir()

    def imprimir_contato(self, indice: int) -> None:
        self.contatos[indice].imprimir()


"""
3. Crie as classes Televisao com atributo status, volume, canal e ControleRemoto com o atributo televisao, de
forma que:
a) Devemos poder ligar, desligar e gerenciar som e canais tanto pela televisão quanto via controle remoto;
b) O controle de volume permite aumentar ou diminuir o volume de som em uma unidade de cada vez;
c) O controle de canal permite aumentar ou diminuir o canal em uma unidade de cada vez mas também
permitir que seja informado um número de canal para efetuar a troca;
"""

class Televisao:

    def __init__(self):
        self.__status: bool = False
        self.__volume: int = 0
        self.__canal: int = 0

    @property
    def status(self) -> bool:
        return self.__status

    @status.setter
    def status(self, status: bool) -> None:
        self.__status = status

    @property
    def volume(self) -> int:
        return self.__volume

    @volume.setter
    def volume(self, volume: int) -> None:
        self.__volume = volume

    @property
    def canal(self) -> int:
        return self.__canal

    @canal.setter
    def canal(self, canal: int) -> None:
        self.__canal = canal




    def ligar_desligar(self) -> None:
        self.status = not self.status

        if self.status:
            print('Status da TV: Ligada')
        else:
            print('Status da TV: Desligada')

    def aumentar_volume_som(self) -> None:
        self.__volume += 1
        print(f'Volume da Tv +: {self.__volume}')

    def diminuir_volume_som(self):
        self.__volume -= 1
        print(f'Volume da Tv +: {self.__volume}')

    def aumentar_canal(self) -> None:
        self.__canal += 1
        print(f'Canal da Tv +: {self.__canal}')

    def diminuir_canal(self):
        self.__canal -= 1
        print(f'Canal da Tv +: {self.__canal}')

    def mudar_canal(self, canal: int):
        self.__canal = canal
        print(f'Canal da Tv : {self.__canal}')



class ControleRemoto:

    def __init__(self, televisao: Televisao) -> None:
        self.__televisao: Televisao = televisao

    @property
    def televisao(self) -> Televisao:
        return self.__televisao

    def ligar_desligar(self) -> None:
        self.televisao.ligar_desligar()

    def aumentar_volume(self) -> None:
        self.televisao.aumentar_volume_som()

    def diminuir_volume(self) -> None:
        self.televisao.diminuir_volume_som()

    def aumentar_canal(self) -> None:
        self.televisao.aumentar_canal()

    def diminuir_canal(self) -> None:
        self.televisao.diminuir_canal()

    def mudar_canal(self, canal: int) -> None:
        self.televisao.mudar_canal(canal)
