class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    def desconto(self, percentual):
        self.valor = self.valor - (self.valor * (percentual / 100))
