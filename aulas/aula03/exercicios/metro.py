from collections import deque

def initialize(dist, graph, vertices):
    for i in range(vertices):
        dist[i] = -1

    for i in range(vertices):
        graph[i] = set()

def bfs(start, graph, dist):
    fila = deque()
    dist[start] = 0
    fila.append(start)
    while fila:
        v = fila.popleft()
        for w in graph[v]:
            if dist[w] == -1:
                dist[w] = dist[v] + 1
                fila.append(w)

graph, dist = dict(), dict()
vertices, final = map(int, input().split())
initialize(dist, graph, vertices)

# ida
estacoes = list(map(int, input().split()))
for i in range(vertices):
    for j in range(i+1, vertices):
        if estacoes[i] == 1 and estacoes[j] == 1:
            graph[i].add(j)

# volta
estacoes = list(map(int, input().split()))
for i in range(vertices-1, -1, -1):
    for j in range(i-1, -1, -1):
        if estacoes[i] == 1 and estacoes[j] == 1:
            graph[i].add(j)

bfs(0, graph, dist)
print('NO' if dist[final-1] == -1 else 'YES')
