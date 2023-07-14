#Dissecando uma Variável

a = input('Digite algo:')
print('O tipo primitivo desse valor é:', type(a))
print('Só tem espaços?', a.isspace())
print('É um número?', a.isnumeric())
print('É alfabético?', a.isalpha())
print('É alfanúmerico?', a.isalnum())
print('Está em maiúsculas?', a.isupper())
print('Está em minúsculas?', a.islower())
print('Esta capitalizado?', a .istitle())
