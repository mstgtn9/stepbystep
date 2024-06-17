print('=-'*15)
print('CALCULE SEU IMC')
print('=-'*15)
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso // altura **2
if imc <= 18.5:
    print('Seu IMC é {}. Você esta abaixo do peso ideal.'.format(imc))
elif imc > 18.5 and imc < 25:
    print('Seu IMC é {}. Você está no peso ideal.'.format(imc))
elif imc >= 25 and imc < 30:
    print('Seu IMC é {}. Voce está com sobre peso.'.format(imc))
elif imc > 30 and imc < 40:
    print('Seu IMC é {}. Você está com obesidade.'.format(imc))
elif imc > 40:
    print('Seu IMC é {}. Você está com obesidade mórbida.'.format(imc))
