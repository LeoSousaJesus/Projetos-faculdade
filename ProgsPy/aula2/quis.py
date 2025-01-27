perguntas = {
    'Pergunta 1': {
        'pergunta': 'Qual a melhor Linguagem?',
        'respostas': {'a': 'Java', 'b': 'Python', 'c': 'Angular', },
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Qual o Professor mais legal?',
        'respostas': {'a': 'Joao', 'b': 'Pedro', 'c': 'Maria', },
        'resposta_certa': 'a',
    }
}
print()
# indice_p indice da pergunta, indice_op indice da opçao
for indice_p, txtpergunta in perguntas.items():
    print(f'{indice_p}: {txtpergunta["pergunta"]}')

    print('respostas: ')
    for indice_r, valor_r in txtpergunta['respostas'].items():
        print(f'[{indice_r}]: {valor_r}')
# verificando as respostas do usuario
    resposta_usuario = input('escolha a opcao ')

    if resposta_usuario == txtpergunta['resposta_certa']:
        print('acertou')
    else:
        print('errou')
        print()
