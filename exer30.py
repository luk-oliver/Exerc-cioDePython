vel = float(input('Digite a velocidade do carro: '))
multa = (vel - 80) * 7
if vel > 80:
    print('Você ultrapassou o limite de Velocidade, Você está MULTADO! em R$ {} reais'.format(multa))
else:
    print('Você está dentro do limite de velocidade, USE CINTO DE SEGURANÇA!')

