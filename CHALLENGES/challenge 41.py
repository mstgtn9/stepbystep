ano = int(input('Em que ano voc nasceu? '))
idade = 2024 - ano
if idade <= 9:
    print('Você tem {} anos. Sua categoria é MIRIM.'.format(idade))
elif idade >= 9 and idade <= 14:
    print('Você tem {} anos. Sua categoria é INFANTIL.'.format(idade))
elif idade >= 15 and idade <=19:
    print('Você tem {} anos. Sua categoria é JUNIOR.'.format(idade))
elif idade == 20:
    print('Você tem {} anos. Sua categoria é SENIOR.'.format(idade))
elif idade >= 21:
    print('Você tem {} anos. Sua categoria é MASTER'.format(idade))