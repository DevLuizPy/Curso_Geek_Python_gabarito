"""
1. Crie a classe Veiculo, contendo marca e modelo. Crie as propriedades getters e setters para os atributos e
um método para imprimir os dados de um veículo. Crie também o construtor da classe.
"""


class Veiculo:

    def __init__(self, marca: str, modelo: str) -> None:
        self.__marca: str = marca
        self.__modelo: str = modelo

    @property
    def marca(self) -> str:
        return self.__marca

    @marca.setter
    def marca(self, nova_marca: str) -> None:
        self.__marca = nova_marca

    @property
    def modelo(self) -> str:
        return self.__modelo

    @modelo.setter
    def modelo(self, novo_modelo: str) -> None:
        self.__modelo = novo_modelo

    def dados(self):
        print(f'Esses são os dados do veículo, marca: {self.__marca}, modelo: {self.__modelo}')


"""
2. Crie a classe Carro que herda a classe Veiculo e possui o atributo portas. Crie as propriedades getters e
setters para o atributo. Crie também o construtor da classe. Sobrescreva o método de imprimir os dados do
veículo de forma a apresentar também a quantidade de portas do carro.
"""


class Carro(Veiculo):

    def __init__(self, marca: str, modelo: str, portas: int) -> None:
        super().__init__(marca, modelo)
        self.__portas: int = portas

    @property
    def portas(self) -> int:
        return self.__portas

    @portas.setter
    def portas(self, nova_portas: int) -> None:
        self.__portas = nova_portas

    def dados(self):
        print(f'Esses são os dados do veículo, marca: {self.marca}, modelo: {self.modelo},'
              f' Portas: {self.__portas}')


"""
3. Crie um programa, instancie um objeto da classe Carro e teste o seu médodo.
"""

carro_1 = Carro('Honda', 'Civic', 4)

carro_1.dados()
