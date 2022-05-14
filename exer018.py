import math
ângulo = float(input('Digite o ângulo: '))
seno = math.sin(math.radians(ângulo))
print('o seno do ângulo {} é {:.2f}' .format(ângulo, seno))
cosseno = math.cos(math.radians(ângulo))
print('O cosseno do ângulo {} é {:.2f}'.format(ângulo, cosseno))
tangente = math.tan(math.radians(ângulo))
print('A tangente do ângulo {} é {:.2f}'.format(ângulo, tangente))
