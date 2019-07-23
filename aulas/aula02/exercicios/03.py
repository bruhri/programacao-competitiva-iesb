from collections import defaultdict
qtd = int(input())
sushi = list(map(int, input().split()))
sushi.append(0)
pecas, atual, sequencia = list(), sushi[0], 0

for peca in sushi:
    if atual != peca:
        pecas.append(sequencia)
        atual = peca
        sequencia = 0
    sequencia += 1

res = 0
for i in range(1, len(pecas)):
    valor = 2*min(pecas[i-1], pecas[i])
    if valor > res:
        res = valor

print(res)