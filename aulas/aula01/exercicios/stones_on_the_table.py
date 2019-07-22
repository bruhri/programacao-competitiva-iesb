qtd, pedras = int(input()), input()
movimentos = 0
for index, pedra in enumerate(pedras):
    if index+1 < qtd and pedra == pedras[index+1]:
        movimentos+=1
print(movimentos)