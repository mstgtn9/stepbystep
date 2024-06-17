from random import randint
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('''SUAS OPÇÕES
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Digite sua escolha: '))
print('=-'*11)
print('O computador escolheu {}'.format(itens[computador]))
print('O jogador escolheu {}'.format(itens[jogador]))
print('=-'*11)
if computador == 0: #computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMUTADOR VENCE')
    else:
        print('JOGADA INVALIDA')
elif computador == 1: #computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVALIDA')
elif computador == 2: #computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA')