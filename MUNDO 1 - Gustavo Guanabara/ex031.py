'''distancia = float(input('Qual é a distancia da sua viagem? '))
print('Você está prestes a começar sua viagem de {}Km.'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('E o preço da sua passagem será de {:.2f}'.format(preço))'''



        #Operador ternário (if) em uma linha

distancia = float(input('Qual é a distancia da sua viagem? '))
print('Você está prestes a começar sua viagem de {}Km.'.format(distancia))
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('E o preço da sua passagem será de {:.2f}'.format(preço))
