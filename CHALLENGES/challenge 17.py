import math
co = float(input('Informe o cateto oposto? '))
ca = float(input('Informe o cateto adjaente: '))
hip = math.hypot(co, ca)
print('O resultado da hipotenusa é: {:.2f} '.format(hip))
