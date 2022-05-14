preco = int(input('Digite o preço do produto '))
desc = preco - preco * 5/100
print('O preço do produto custava R${} na promoção com desconto de 5% custa R${}' .format(preco, desc))