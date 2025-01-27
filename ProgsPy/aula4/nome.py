nome = str(input('Qual seu nome: '))
if nome == 'Fábio':
    print('Que nome lindo...')
elif nome in 'João Fabricio Nicolas':
    print('Seu nome é muito comum {}'.format(nome))
print('Bom dia, {}'.format(nome))
