from random import randint
from time import sleep
n1 = randint(1, 5)
print('=============================================')
print('A maquina acaba de gerar um numero de 1 até 5')
print('=============================================')
resp = int(input('Tente acertar qual foi esse numero: '))
print('LOADING...')
sleep(1.5)
if resp == n1:
    print == n1 ('Você acertou! O NUMERO GERADO FOI {'.format(n1))
else:
    print('Você errou! O numero gerado foi {}'.format(n1))
