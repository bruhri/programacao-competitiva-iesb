from collections import defaultdict, deque

def bfs(start, end, visitados):
    fila = deque()
    fila.append( (0, start) )
    while fila:
        apertos, vertice = fila.popleft()
        if vertice == end:
            return apertos
        if vertice in visitados:
            continue
        visitados.add(vertice)
        if vertice < end:
            fila.append( (apertos+1, vertice*2) )
        if vertice - 1 >= 1:
            fila.append( (apertos+1, vertice-1) )

graph, visitados = defaultdict(set), set()
start, end = map(int, input().split())
print(bfs(start, end, visitados))