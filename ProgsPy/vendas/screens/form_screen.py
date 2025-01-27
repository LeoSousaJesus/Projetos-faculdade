from tkinter import *
from tkinter import ttk
from controller.save_csv import SaveCsv
from datetime import datetime


class FormScreen:
    def __init__(self) -> None:
        self.__save = SaveCsv()
        self.__now = datetime.now().strftime('%d/%m/%Y')

        self.root = Tk()
        self.root.geometry("300x150")
        frm = ttk.Frame(self.root)
        frm.grid()
        # Label e input text
        ttk.Label(frm, text="Mensagem:").grid(column=0, row=0)
        self._msg_value = StringVar()  # Variável responsável por resgatar o texto digitado
        msg = ttk.Entry(frm, textvariable=self._msg_value)  # Campo de input referenciando a variável de resgate
        msg.grid(column=1, row=0)  # Posicionando o campo de acordo com o grid
        # Label e input text
        ttk.Label(frm, text="Valor do dia:").grid(column=0, row=1)
        self._total = StringVar()  # Variável responsável por resgatar o texto digitado
        valor = ttk.Entry(frm, textvariable=self._total)  # Campo de input referenciando a variável de resgate
        valor.grid(column=1, row=1)  # Posicionando o campo de acordo com o grid

        ttk.Button(frm, text="Salvar",
                   command=lambda: self.save_information(self._msg_value.get(), self._total.get())) \
            .grid(column=0, row=2)
        ttk.Button(frm, text="Total lançado",
                   command=lambda: self.__save.info_total(date=self.__now))\
            .grid(column=1, row=2)
        ttk.Button(frm, text="Total do dia",
                   command=lambda: self.__save.info_total(date=self.__now, show_today_only=True))\
            .grid(column=2, row=2)
        self.root.mainloop()

    def save_information(self, msg: str, total: str) -> None:
        now = datetime.now().strftime('%d/%m/%Y')

        self.__save.insert_in_file(msg=msg, value=total, date=now)
        self._msg_value = ''
        self._total = ''
