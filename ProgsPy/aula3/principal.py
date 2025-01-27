from dados import produtos, clientes


def filtrando(produto):
    if produto['preco'] > 30:
        return True


nova_lista = filter(filtrando, produtos)

for produto in nova_lista:
    print(produto)
