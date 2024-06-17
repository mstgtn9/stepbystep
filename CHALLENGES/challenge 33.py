n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))
if n1 < n2:
    if n1 < n3:
        menor = n1
    else:
        menor = n3
else:
    if n2 < n3:
        menor = n2
    else:
        menor = n3
print('O menor numero digitado foi {}'.format(menor))
if n1 > n2 :
    if n1 > n3:
        maior = n1
    else:
        maior = n3
else:
    if n2>n3:
        maior = n2
    else:
        maior= n3
print('O maior numero digitado foi {}'.format(maior))

