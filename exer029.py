from random import choice
num = int(input('Digite um número de 0 a 5: '))
lista = [0, 1, 2, 3, 4, 5]
numero = choice(lista)
print('O número escolhido pelo computador foi {}'.format(numero))
if num == numero:
    print('PARABÉNS! você acertou')
else:
    print('VOCÊ ERROU!!! Tenta novamente')
