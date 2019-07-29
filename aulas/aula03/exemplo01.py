lista_adj = {
    0:[2, 3],
    1:[2, 4],
    2:[],
    3:[4],
    4:[2]
}

qtd_entradas = 0
vertice_buscado = int(input())
for vertice in lista_adj:
    if vertice_buscado in vertice:
        qtd_entradas += 1
print(qtd_entradas)