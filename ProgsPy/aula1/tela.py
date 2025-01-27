from tkinter import *

# janela = Tk()  # crianeo um item do tipo janela

# janela.mainloop()
# -*- coding:utf-8 -*-


app = Tk()

show = ""  # variavel que vai mudar o texto

equation = StringVar()  # variavel que vai mostrar o texto

display = Label(app, textvariable=equation)  # labelpara o display do texto

equation.set("0")  # texto inicial no display

display.grid(columnspan=4)  # expandir o display em 4 espaços no grid


# Função que adiciona o valor do botao pressionado ao display
def btnPress(num):
    global show
    show = show + str(num)
    equation.set(show)

# função que faz o calculo da equação


def evaluate():
    global show
    total = str(eval(show))
    equation.set(total)
    show = ""

# Função que limpa o display


def clear():
    global show
    show = "0"
    equation.set(show)


# botoes numericos
one = Button(app, text="1", command=lambda: btnPress(1))
one.grid(row=1, column=0)

two = Button(app, text="2", command=lambda: btnPress(2))
two.grid(row=1, column=1)

three = Button(app, text="3", command=lambda: btnPress(3))
three.grid(row=1, column=2)

four = Button(app, text="4", command=lambda: btnPress(4))
four.grid(row=2, column=0)

five = Button(app, text="5", command=lambda: btnPress(5))
five.grid(row=2, column=1)

six = Button(app, text="6", command=lambda: btnPress(6))
six.grid(row=2, column=2)

seven = Button(app, text="7", command=lambda: btnPress(7))
seven.grid(row=3, column=0)

eight = Button(app, text="8", command=lambda: btnPress(8))
eight.grid(row=3, column=1)

nine = Button(app, text="9", command=lambda: btnPress(9))
nine.grid(row=3, column=2)

zero = Button(app, text="0", command=lambda: btnPress(0))
zero.grid(row=4, column=1)

# Botoes de operadores

plus = Button(app, text="+", command=lambda: btnPress("+"))
plus.grid(row=1, column=3)

minus = Button(app, text="-", command=lambda: btnPress("-"))
minus.grid(row=2, column=3)

div = Button(app, text="/", command=lambda: btnPress("/"))
div.grid(row=3, column=3)

mult = Button(app, text="x", command=lambda: btnPress("*"))
mult.grid(row=4, column=3)


equal = Button(app, text="=", command=evaluate)
equal.grid(row=4, column=2)

clear = Button(app, text="C", command=clear)
clear.grid(row=4, column=0)

app.mainloop()
