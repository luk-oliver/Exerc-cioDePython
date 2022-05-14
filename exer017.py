'''import math
co = float(input('Quanto medi o cateto oposto '))
ca = float(input('Quanto medi o catete adjacente '))
h = (co ** 2 + ca ** 2) ** (1/2)
print('O cumrimento da hipotenusa é {}'.format(h))'''

from math import hypot
co = float(input('Quanto medi o cateto oposto '))
ca = float(input('Quanto medi o catete adjacente '))
h = hypot(co, ca)
print('A hipotenusa medir {:.2f}'.format(h))

