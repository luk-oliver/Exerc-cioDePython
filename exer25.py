'''country = input('Digite o nome de uma cidade: ')
city = country.split()
print('A cidade começa com Santos? a resposta é: {}'.format('Santos' in city[0]))'''

cid = str(input('Digite a cidade que você nasceu: ')).strip()
print(cid[:5].upper() == 'SANTO')