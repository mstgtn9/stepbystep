dc = int(input('Quantos dias alugados? '))
km = int(input('Quantos km rodados? '))
pdc = dc * 60
pkm = km * 0.15
pf = pdc + pkm
print('O valor a ser pago é: R${}'.format(pf))
