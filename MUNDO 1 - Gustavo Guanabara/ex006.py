n =  int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('Analisando o número digitado, o seu dobro é' , d)
print('O seu triplo é ', t)
print('É sua raiz é ', r)

#ou usando \n é .format() para reduzir o codigo e criando uma nova linha a baixo na mesma linha

num = int(input('Digite um número:'))
print('Analisando o número digitado o seu dobro é {}. \nseu triplo {}. \ne sua raiz {:.2f}.'.format(num * 2, num * 3, (num **(1/2))))
