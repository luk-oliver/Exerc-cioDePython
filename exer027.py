frase = input('Digite uma frase: ').upper().strip()
print('A letra a aparece na frase {} vezes ' .format(frase.count('A'))) #mostrar quantas vezes aparece na frase
print('A letra a aparece na posição {} na primeira vez '.format(frase.find('A')+1)) # mostra a posição da letra na frase
print('A letra a aparece na posição {} na ultima vez' .format(frase.rfind('A')+1))