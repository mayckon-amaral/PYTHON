largura = float(input('Digite a largura: '))
altura = float(input('Digite a altura: '))
area = largura * altura
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(largura, altura,area))
tinta = area / 2
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))
