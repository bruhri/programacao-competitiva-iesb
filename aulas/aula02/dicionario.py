cardapio = {
    '01':3.50, '03':7.90, '11':5.20
}
pedidos = input().split()
print(sum([cardapio.get(pedido, 0) for pedido in pedidos]))