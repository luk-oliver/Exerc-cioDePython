n = input('Digite algo? ')
print('este tipo primitivo é do tipo ', type(n)) # verifica o tipo da variável se é 'str', 'int', 'boleano',
print('só tem espaços?', n.isspace())
print('É número?', n.isnumeric()) # n é numero3a
print('É alfabéticos? ', n.isalpha()) # n é alfabético
print('É alfanumerico? ', n.isalnum()) # é número e alfabético
print(' Está em maiusculo', n.isupper())
print('Está em minúsculos', n.islower())
print('Ele está capitalizada?', n.istitle())
