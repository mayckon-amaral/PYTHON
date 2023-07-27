        # Trabalhando com cores (escape sequence ANSI) no terminal
# style
print('----Style----')
print('\033[0mOlá, Mundo!\033[m')                # \033[0m = Normal
print('\033[1mOlá, Mundo!\033[m')                # \033[1m = Negrito
print('\033[4mOlá, Mundo!\033[m')                # \033[4m = Sublinhado
print('\033[7mOlá, Mundo!\033[m')                # \033[7m = Inversão de cor(cor de fonte para cor de fundo)
print()

# text
print('----Text----')               
print('\033[30mPreto\033[m')
print('\033[1;31mVermelho\033[m')
print('\033[1;32mVerde\033[m')
print('\033[1;33mAmarelo\033[m')
print('\033[1;34mAzul\033[m')
print('\033[1;35mMagenta\033[m')
print('\033[1;36mCiano\033[m')
print('\033[1;37mCinza\033[m')

print()
# background
print('----Back----')
print('\033[1;40m Preto\033[m')            
print('\033[1;41mVermelho!\033[m')         
print('\033[1;42mVerde\033[m')            
print('\033[1;43mAmarelo\033[m')           
print('\033[1;44mAzul\033[m')              
print('\033[1;45mMagenta\033[m')           
print('\033[1;46mCiano\033[m')             
print('\033[1;47mCinza\033[m')             
print()

        # exemplos:

print('-----Exemplo 1----')

a = 3
b = 5
print('Os valores são \033[1;33m{}\033[m e \033[1;34m{}\033[m'.format(a,b))         # \033[m  serve para fechar a cor
print()


print('-----Exemplo 2----')
nome = 'Mayckon'
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[1;32m', nome, '\033[m'))
print()


print('-----Exemplo 3----')

        #   criando sistema de cores com dicionário

nome = 'Mayckon'
cores = {'limpa':'\033[m',
         'preto': '\033[30m',
         'vermelho':'\033[31m',
         'verde':'\033[32m'}

print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['vermelho'], nome, cores['limpa']))      # Chamando as cores do dicionário
