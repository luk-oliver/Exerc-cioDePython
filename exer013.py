salario = float(input('Qual o salário do funcionário? '))
reajuste = salario + (salario * 15)/100
print('O salário era R${:.2f} com 15% de reajuste passa ganhar R${:.2f}' .format(salario, reajuste))