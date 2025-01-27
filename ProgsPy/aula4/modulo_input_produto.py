from produtos import Produto
print('Digite o nome do produto')
nome = input()
print('Digite o valor do produto')
valor = float(input())
print('Digite o valor do desconto')
desc = int(input())
prod2 = Produto(nome, valor)
prod2.desconto(desc)
#print(f'Nome: {prod2.nome} Valor do desonto {prod2.valor}')
print(
    f'Nome do Produto: ​​​​​​{prod2.nome}​​​​​​ | Valor com Desconto: {prod2.valor}​​​​​​')
