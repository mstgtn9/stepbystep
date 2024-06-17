print('=-'*15)
print('MEDIDOR DE BURRICE')
print('=-'*15)
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2) // 2
if media >=7 :
    print('=-'*15)
    print('PARABÉNS!\nPARABÉNS!\nPARABÉNS!\nPARABÉNS!\nPARABÉNS!\n')
    print('=-'*15)
    print('Sua média foi {} APROVADO!'.format(media))
elif media >=5 and media <=6.9:
    print('-='*15)
    print('Sua média foi {} RECUPERAÇÃO'.format(media))
elif media <=4.9:
    print('=-'*15)
    print('Sua media foi {} REPROVADO'.format(media))