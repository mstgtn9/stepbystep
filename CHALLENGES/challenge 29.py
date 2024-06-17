kmc = int(input('Digite a sua velocidade: '))
if kmc <= 80:
    print('Você esta no limite de velocidade. Continue assim!')
else:
    mlt = (kmc - 80)*7
    print('Você ultrapassou o limite de velocidade, sua multa é de R${},00'.format(mlt))
