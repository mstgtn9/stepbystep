from random import shuffle
n1 = str(input('PRIMEIRO ALUNO: '))
n2 = str(input('SEGUNDO ALUNO: '))
n3 = str(input('TERCEIRO ALUNO: '))
n4 = str(input('QUARTO ALUNO: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print ('A ordem é: {}'.format(lista))
