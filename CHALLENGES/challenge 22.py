frase = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maisculo fica: {} ' .format(frase.upper()))
print('Seu nome em minusculo fica: {} '.format(frase.lower()))
print('Seu numero possui {} caracteres'.format(len(frase)-frase.count(' ')))
dividido = frase.split()
print('Seu primeiro nome é: {} e tem {} caracteres'.format(dividido[0], len(dividido[0])))
