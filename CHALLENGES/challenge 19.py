from random import choice
pa = str(input('PRIMEIRO ALUNO: '))
sa = str(input('SEGUNDO ALUNO: '))
ta = str(input('TERCEIRO ALUNO: '))
qa = str(input('QUARTO ALUNO: '))
lista = [pa, sa, ta, qa]
escolhido = choice(lista)
print('O escolhido é: {}'.format(escolhido))