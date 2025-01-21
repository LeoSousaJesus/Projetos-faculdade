# -*- coding: utf-8 -*-
"""ExerciciosAdionais2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XDpNZiyA5czJ9KsxNkRgtsxK06LHB9Kh

# Exercício 1

Escreva um programa que receba um número inteiro positivo na entrada e verifique se é primo. Se o número for primo, imprima "primo". Caso contrário, imprima "não primo".

Exemplos:

Digite um número inteiro: 13

primo

Digite um número inteiro: 12

não primo
"""

numero = int(input("Digite um número: "))

s_primo = True

if numero <= 1:
    s_primo = False
else:
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            s_primo = False
            break

if s_primo:
    print("primo")
else:
    print("não primo")

"""# Exercício 2 - Desafio do vídeo "Repetição com while"

Escreva um programa que receba um número inteiro na entrada e verifique se o número recebido possui ao menos um dígito com um dígito adjacente igual a ele. Caso exista, imprima "sim"; se não existir, imprima "não".

Exemplos:

Digite um número inteiro: 12345

não

Digite um número inteiro: 1011

sim
"""

numero = input("Digite um número: ")

com_adjacente = False

for i in range(len(numero) - 1):
    if numero[i] == numero[i + 1]:
        com_adjacente = True
        break

if com_adjacente:
    print("sim")
else:
    print("não")