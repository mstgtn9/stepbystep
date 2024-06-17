print('=-'*15)
print('ALISTE-SE PARA O EXECITO BRASILEIRO')
print('=-'*15)
ano = int(input('Digite o ano você nasceu? '))
idade = 2024 - ano
tempo = ano - 2006
if idade <= 17:
    print('Você tem {} anos. \nFalta(m) {} ano(s) para se alistar \nVolte quando completar 18 anos.'.format(idade , tempo))
elif idade == 18:
    print('Parabens! Você já tem 18 anos completos.\nVá a uma junta militar para dar inico ao alistamento.')
else:
    print('Você tem {} anos.\nJa devia ter se apresentado\nVá a uma junta militar para regulaziar sua situação.'.format(idade))
