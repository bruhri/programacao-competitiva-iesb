fila = list()
qtd = int(input())
for _ in range(qtd):
    fila.append(int(input()))

fila = list(reversed(fila))
print(fila.pop())