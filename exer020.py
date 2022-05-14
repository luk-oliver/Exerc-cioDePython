'''import random
aluno1 = str(input('Digite o primeiro aluno: '))
aluno2 = str(input('Digite o segundo aluno: '))
aluno3 = str(input('Digite o terceiro aluno: '))
aluno4 = str(input('Digite o quarto aluno: '))
listas = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(listas)
print('O nome sorteado foi ')
print(listas)'''

'''o simplificado '''

from random import shuffle
aluno1 = str(input('Digite o primeiro aluno: '))
aluno2 = str(input('Digite o segundo aluno: '))
aluno3 = str(input('Digite o terceiro aluno: '))
aluno4 = str(input('Digite o quarto aluno: '))
listas = [aluno1, aluno2, aluno3, aluno4]
shuffle(listas)
print('A ordem foi sorteado foi ')
print(listas)