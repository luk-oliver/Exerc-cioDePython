'''import random
a1 = str(input('Digite o primeiro aluno: '))
a2 = str(input('Digite o segundo aluno: '))
a3 = str(input('Digite o terceiro aluno: '))
a4 = str(input('Digite o terceiro aluno: '))
lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)
print('O escolhido foi {}'.format(escolhido))'''

'''forma simplificada pode ser'''

from random import choice
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
n4 = int(input('Digite o quarto número: '))
n5 = int(input('Digite o quinto número: '))
n6 = int(input('Digite o sexto número: '))
sorteio = [n1, n2, n3, n4, n5, n6]
numero = choice(sorteio)
print('O número escolhido do sorteio foi {}' .format(numero))
