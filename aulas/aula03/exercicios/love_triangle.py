vertices = int(input())
avioes = list(map(lambda x: int(x)-1, input().split()))
for vertice in range(vertices):
    if avioes[avioes[avioes[vertice]]] == vertice:
        print('YES')
        exit(0)
print('NO')

