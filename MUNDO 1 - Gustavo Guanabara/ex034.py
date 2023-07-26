salario = float(input('Qual é o salário do funcioanário? R$ '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava R${:.2f} passa a receber R${:.2f}'.format(salario, novo))
