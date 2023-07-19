nome = str(input('Digite seu nome completo: ')).strip()     # .strip() serve para eliminar espaços antes e depois
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))     # .count(' ') serve para contar espaços entre as palavras
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))        # .find(' ') serve para encontrar o primeiro espaço
separa = nome.split()  # .split() joga dentro de uma lista o nomes inteiros
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
