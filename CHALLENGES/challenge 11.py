altura = float(input('Digite a altura dessa parede: '))
largura = float(input('Agora digite a largura da parede: '))
m2 = largura * altura
lt = m2 / 2
print('Sua parede tem a dimensão de {}x{} e sua area é de {}m²'.format(largura, altura, m2))
print('Você precisará de {:.1f} Litros de tinta para pintar a sua parede'.format(lt))