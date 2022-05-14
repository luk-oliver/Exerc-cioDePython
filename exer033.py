from calendar import isleap '''isleap que dizer 'ilha' '''
ano = int(input('Digite um ano: '))
if isleap(ano):
    print('O ano é Bissexto'.format(isleap(ano)))
else:
    print('O ano não é bissexto'.format(isleap(ano)))