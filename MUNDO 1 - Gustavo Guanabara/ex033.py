'''a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

#Verificando quem é o menor

if a < b and a < c:
    menor = a
if b < c and b < a:
    menor = b
if c < a and c < b:
    menor = c

#Verificando quem é o maior

if a > b and a > c:
    maior = a
if b > c and b > a:
    maior = b
if c > a and c > b:
    maior = c
print('O número menor foi {}'.format(menor))
print('O número maior foi {}'.format(maior))'''



        #Simplificando o código eliminando um if

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

#Verificando quem é o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

#Verificando quem é o maior
maior = a
if b > a and b >c:
    maior = b
if c > a and c > b:
    maior = c

print('O número menor foi {}'.format(menor))
print('O número maior foi {}'.format(maior))
