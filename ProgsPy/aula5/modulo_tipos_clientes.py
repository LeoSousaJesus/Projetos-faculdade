from classes import Aluno, ClienteVip, Pessoa, Cliente
# criando o modulo e linkando do a Classe

""" objeto_clie1 = Cliente('Joao', 48)  # crinado um objeto do tipo cliente
print(objeto_clie1.nome, ' - ', objeto_clie1.reclamar())


objeto_clie2 = Aluno('Julia', 19)  # crinado um objeto do tipo cliente
print(objeto_clie2.nome, objeto_clie2.idade, ' ', objeto_clie2.estudar())

objeto_clie3 = Pessoa('Pedro', 30)  # crinado um objeto do tipo cliente
print(objeto_clie3.idade, ' ', objeto_clie3.fofocar())
"""
objeto_cli1 = Cliente('Joao', 48)  # crinado um objeto do tipo cliente
objeto_cli1.reclamar()

print()

objeto_clivip = ClienteVip('Denise', 22, 'Souza')
objeto_clivip.reclamar()
