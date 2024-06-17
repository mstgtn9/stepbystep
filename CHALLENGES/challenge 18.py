from math import sin, cos, tan,radians
ang = float(input('Digite o angulo que voce deseja: '))
sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print('O seno é: {:.2f}'.format(sen))
print('O coseno é: {:.2f}'.format(cos))
print('A tangente é: {:.2f}'.format(tan))
