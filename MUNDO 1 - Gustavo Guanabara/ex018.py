'''import math

angulo = float(input('Digite o angulo que: '))
seno = math.sin(math.radians(angulo))
print('O angulo de {:.2f} tem o SENO de {:.2f}'.format(angulo,seno))
cosseno = math.cos(math.radians(angulo))
print('O angulo de {:.2f} tem o COSSENO de {:.2f}'.format(angulo,cosseno))
tangente = math.tan(math.radians(angulo))
print('O angulo de {:.2f} tem o TANGENTE de {:.2f}'.format(angulo,tangente))'''




    #importando mais de um metodo especifico da biblioteca

from math import radians,sin,cos,tan

angulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(angulo))
print('O ângulo de {:.2f} tem o SENO de {:.2f}'.format(angulo,seno))
cosseno = cos(radians(angulo))
print('O ângulo de {:.2f} tem o COSSENO de {:.2f}'.format(angulo,cosseno))
tangente = tan(radians(angulo))
print('O ângulo de {:.2f} tem o TANGENTE de {:.2f}'.format(angulo,tangente))
