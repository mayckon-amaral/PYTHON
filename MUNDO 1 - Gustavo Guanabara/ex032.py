  # Analisando o ano atual
from datetime import date
ano = int(input('Que ano quer analisar: Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year     #data atual do dia e ano
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))



'''ano = int(input('Que ano quer analisar: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))'''
