pedido1 = [125, 132, 98, 10]
pedido2 = [25, 28, 102, 35, 50, 65]

# maneira peba
lista_soma = []
for i in range(len(pedido1)):
    lista_soma.append(pedido1[i]+pedido2[i])
print(lista_soma)


lista_soma_pro = [x+y for x, y in zip(pedido2, pedido1)]
print(lista_soma_pro)
