from collections import deque

def initialize(dist, graph, verticies):
    for i in range(verticies):
        dist[i] = -1

    for i in range(verticies):
        graph[i] = set()

def populate(graph, arestas, bi=False):
    for _ in range(arestas):
        v, w = map(int, input().split())
        graph[v].add(w)
        if bi:
            graph[w].add(v)

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
verticies, arestas = map(int, input().split())
initialize(dist, graph, verticies)
populate(graph, arestas)


bfs(0)
print(dist)