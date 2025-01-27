import os
import csv
from tkinter.messagebox import showerror, showinfo
from typing import Optional


class SaveCsv:
    def __init__(self) -> None:
        self.__file_name = 'vendas.csv'
        if not os.path.exists(self.__file_name):
            self.__create_csv_file(self.__file_name)

    def insert_in_file(self, msg: str, value: str, date: str) -> None:
        if msg == '' or value == '':
            showerror('Campo em vazio', 'Digite um valor para os campos')
        else:
            with open(self.__file_name, 'a', newline='') as csv_file:
                writer = csv.writer(csv_file, delimiter=';')
                writer.writerow([msg, value, date])
                csv_file.close()
            showinfo('Sucesso', 'As informações foram gravadas com sucesso.')

    def select_by_date(self, date: str) -> bool:
        with open(self.__file_name, 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=';')

            reader.__next__()
            for row in reader:
                continue

            csv_file.close()
        return False

    def __create_csv_file(self, file_name: str) -> None:
        with open(file_name, 'x', newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=';')
            writer.writerow(['Mensagem', 'Valor', 'Data'])
            csv_file.close()

    def info_total(self, date: str, show_today_only: Optional[bool] = False) -> None:
        total = 0
        with open(self.__file_name, 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=';')
            reader.__next__()
            for item in reader:
                if show_today_only:
                    if item[2] == date:
                        total += float(item[1])
                else:
                    total += float(item[1])
            csv_file.close()

        if str(total)[-2] == ".":
            total = str(total).replace('.', ',')
            total = f'{total}0'

        showinfo('Valor total', f'O total lançado até o momento é R${total}')
