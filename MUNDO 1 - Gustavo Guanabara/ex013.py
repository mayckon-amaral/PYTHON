salário = float(input('Qual é o salário do Funcionário? R$'))
novo = salário + (salário * 15 / 100)
print('Um funcionário que recebia R${:.2f}, com 15% de aumento, passa receber R${:.2f}'.format(salário,novo))
