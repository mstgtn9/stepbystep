sal = int(input('Digite o valor do seu salario: R$'))
if sal<=1250:
    reajuste = sal*15//100
    print('O valor do seu salário atualizado será de R${}'.format((sal)+(reajuste)))
else:
    reajuste= sal*10//100
    print('O valor do seu salário atualizado será de R${}'.format((sal)+(reajuste)))
