# criando um Classe
class Pessoa:  # definindo a Classe
    ano_atual = 2022  # definindo um atributo e colocando um valor inicial
    # self é um parametro padrão do python

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_nascimento(self):
        print(self.nome, "nasceu em ", self.ano_atual - self.idade)
