lista = ['Joao', 'Fabio', 'julia', 1, 2, 3, 4, 5, 6, 8, 9, 10]
v1, v2, v3, *partenumerica = lista

print(v1, v2, v3, partenumerica)

v1, v2, v3, *partenumerica, ultimo = lista

print(v1, v2, v3, partenumerica, ultimo)
