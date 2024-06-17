r1 = int(input('Digite o valor da primeira reta: '))
r2 = int(input('Digite o valor da segunda reta: '))
r3 = int(input('Digite o valor da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('AS RETAS FORMAM UM TRIANGULO')
    if r1 == r2 and r2 == r3:
        print('EQUILATERO')
    elif r1 == r2 or r1 == r3 or r3 == r2:
        print('ISOSCELES')
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print('ESCALENO')
else:
    print('AS RETAS NÃO FORMAM UM TRIANGULO')