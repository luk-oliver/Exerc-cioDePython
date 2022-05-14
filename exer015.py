dia = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Digite a KM rodada: '))
pago = (dia * 60) + (km * 0.15)
print('O aluguel de {} dia e a KM rodada {:.2f} custará R$ {:.2f} reais' .format(dia, km, pago))