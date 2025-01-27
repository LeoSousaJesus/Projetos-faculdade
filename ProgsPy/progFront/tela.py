from tkinter import *
from tkinter import ttk
from tkinter import StringVar
from tkinter.messagebox import showinfo


def tela():
    # Instancia do tkinter e ajuste da tela
    info = Tk()
    info.geometry('300x100')
    frm = ttk.Frame(info)
    frm.grid()
    mensagem = StringVar()
    ttk.Label(frm, text="Digite uma mensagem: ").grid(
        {'column': 0, 'row': 0}
    )
    ttk.Entry(frm, textvariable=mensagem).grid(
        {'column': 1, 'row': 0}
    )
    ttk.Button(frm, text='Enviar', command=lambda: result(mensagem.get()))\
        .grid({'column': 1, 'row': 1})
    info.mainloop()


def result(mensagem: str) -> None:
    showinfo('Resultado', f'{mensagem}')


if __name__ == '__main__':
    tela()
