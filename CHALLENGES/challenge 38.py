from time import sleep
print('=-'*15)
print('ANALISADOR DE NUMEROS')
print('=-'*15)
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
print('...')
sleep(0.5)
print('PROCESSANDO')
sleep(0.5)
print('...')
sleep(0.5)
if n1 > n2:
    print('=-'*15)
    print('O primeiro numero {} é maior que o segundo {} digitado'.format(n1, n2))
elif n2 > n1:
    print('=-'*15)
    print('O segundo numero {} é maior que o primeiro {} digitado'.format(n1, n2))
else:
    print('=-'*30)
    print('VOCE ESTA TENTANDO ME ENGANAR? OS DOIS NUMEROS SÃO IGUAIS!!!')
    print('=-'*30)
