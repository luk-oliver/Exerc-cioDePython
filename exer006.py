n = int(input('Digite um número '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('o dobro de',n, 'é {}' .format(d))
print('o triplo de',n, 'é {}' .format(t))
print('A raiz quadrada de',n, 'é {:.2f}'.format(pow(n, (1/2))))

print('O dobro de {} vale {}. \nO triplo de {} vale {}. \na raiz quadrada de {} vale {:.2f}'. format(n, d, n, t, n, r))
