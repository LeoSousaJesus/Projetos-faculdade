#import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import StringVar
from tkinter.messagebox import showerror, showinfo


def tela():
    # Instancia do tkinter e ajuste da tela
    soma = Tk()
    soma.geometry('300x150')
    frm = ttk.Frame(soma)
    frm.grid()
    # Declaração das variáveis para a recuperação do valor digitado no input
    numero1 = StringVar()
    numero2 = StringVar()
    # Declaração do input e label
    ttk.Label(frm, text="Digite o primeiro número: ").grid(
        {'column': 0, 'row': 0})
    ttk.Entry(frm, textvariable=numero1).grid({'column': 1, 'row': 0})
    # Declaração do input e label
    ttk.Label(frm, text="Digite o segundo número: ").grid(
        {'column': 0, 'row': 1})
    ttk.Entry(frm, textvariable=numero2).grid({'column': 1, 'row': 1})
    # Declaração do botão
    ttk.Button(frm, text='Somar', command=lambda: operacao(numero1.get(), numero2.get(), "+"))\
        .grid({'column': 1, 'row': 2})
    ttk.Button(frm, text='Subtrair', command=lambda: operacao(numero1.get(), numero2.get(), "-"))\
        .grid({'column': 1, 'row': 3})
    ttk.Button(frm, text='Multiplicar', command=lambda: operacao(numero1.get(), numero2.get(), "*"))\
        .grid({'column': 1, 'row': 4})
    ttk.Button(frm, text='Dividir', command=lambda: operacao(numero1.get(), numero2.get(), "/"))\
        .grid({'column': 1, 'row': 5})
    soma.mainloop()

# se os valores forem possiveis de transformar em numeros converte
# se nao mostra a mensagem de erro


def valida_numeros(n1: str, n2: str) -> bool:
    if n1.isnumeric() and n2.isnumeric():
        return True

    showerror('Valor inválido', 'Por favor, digite apenas números.')
    return False


def operacao(n1: str, n2: str, sinal: str) -> None:
    if valida_numeros(n1, n2):
        n1 = float(n1)
        n2 = float(n2)
        if sinal == "+":
            showinfo('Resultado', f'A soma dos valores digitados é {n1 + n2}')
        elif sinal == "-":
            showinfo(
                'Resultado', f'A subtração dos valores digitados é {n1 - n2}')
        elif sinal == "*":
            showinfo(
                'Resultado', f'A multiplicação dos valores digitados é {n1 * n2}')
        else:
            showinfo(
                'Resultado', f'A divisão dos valores digitados é {n1 / n2}')


if __name__ == '__main__':
    tela()
