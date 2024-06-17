preço = float(input('Qual o preço das compras? R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] A VISTA DINHEIRO / CHEQUE
[ 2 ] A VISTA CARTÃO
[ 3 ] 2X NO CRÉDITO
[ 4 ] 3X OU MAIS NO CRÉDITO''')
opcao = int(input('DIGITE A FORMA DE PAGAMENTO: '))
if opcao == 1:
    np = preço - (preço*10//100)
    print('Sua compra no valor de R${} ficará R${}'.format(preço, np))
elif opcao == 2:
    np = preço - (preço*5//100)
    print('Sua compra no valor de R${} ficará R${}'.format(preço, np))
elif opcao == 3:
    print('Não há descontos disponiveis nessa forma de pagamento. \nSua compra ficou no valor de R$'.format(preço))
elif opcao == 4:
    parcela = int(input('Quantas vezes deseja parcelar? '))
    np = preço + (preço*20//100)
    parcelado = np // parcela
    print('Serão {} parcelas no valor de R${} totalizando R${}'.format(parcela, parcelado, np))