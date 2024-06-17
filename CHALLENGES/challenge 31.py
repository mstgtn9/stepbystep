nkm = int(input('Qual a distancia de sua viagem? '))
if nkm<=200:
    nkm1 = nkm*0.50
    print('Sua viagem custará R${}'.format(nkm1))
else:
    nkm2 = nkm*0.45
    print('Sua viagem custará R${}'.format(nkm2))