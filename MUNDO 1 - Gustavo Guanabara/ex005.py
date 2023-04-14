n = int(input('Digite um número:'))
s = n + 1
a = n - 1
print('Analisando seu número digitado seu sucessor é',s, 'é o seu antecessor é', a)

# ou usando ".format"

num = int(input('Digite um número:'))
sc = num + 1
at = num - 1
print('Analisando o número digitado seu sucessor é {} é seu antecessor é {}'.format(num + 1, num - 1))
