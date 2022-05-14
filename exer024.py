'''numero = input('Digite um número qualquer: ')
num = numero.split()
print('unidade:{}'.format(num[0][3]))
print('dezena:{}'.format(num[0][2]))
print('centena:{}'.format(num[0][1]))
print('milhar:{}'.format(num[0][0]))'''

numero = int(input('Digite um número qualquer: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
mi= numero // 10000 % 10
print('unidade:{}'.format(u))
print('dezena:{}'.format(d))
print('centena:{}'.format(c))
print('milhar:{}'.format(m))
print('milhoes:{}'.format(mi))
