Km = float(input('Digite a quilometragem da sua viajem: '))
curto = Km * 0.50
longa = Km * 0.45
if(Km <= 200):
    print('Sua viagem até 200 Km custará R$ {} reais'.format(curto))
else:
    print('Sua viagem acima de 200 Km custará R$ {} reais'.format(longa))
