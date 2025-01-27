from mercado import Carrinho, ProdutoDisponivel
meucarrinho = Carrinho()
# print(meucarrinho)
produto1 = ProdutoDisponivel('Mouse', 35)
produto2 = ProdutoDisponivel('Teclado', 50)
produto3 = ProdutoDisponivel('HD', 500)

meucarrinho.inserir_produto(produto1)
meucarrinho.inserir_produto(produto2)
meucarrinho.inserir_produto(produto3)
meucarrinho.inserir_produto(produto3)
meucarrinho.lista_produto()
print("Total do Carrinho R$: ", meucarrinho.soma_total())
