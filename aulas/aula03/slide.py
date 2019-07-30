import sys

from beampy import *

doc = document(theme="maratonaiesb")

with slide():
    maketitle(lesson='Aula 03', author='Rodrigo G. Araújo',  date='29/07/2019')

with slide("Introdução a Teoria dos Grafos"):
    figure('aulas/img/grafo_simples.png', width=700)

with slide("Lista de Adjacência"):
    code(open("aulas/aula03/listadj.py").read(), width=400, size='20px')

with slide("Matriz de Adjacência"):
    code(open("aulas/aula03/matadj.py").read(), width=400, size='20px')

with slide("Grafo Direcionado"):
    figure('aulas/img/grafo_direcionado.png', width=700)

with slide("Problema Simples"):
    code(open("aulas/aula03/exemplo01.py").read(), width=400, size='20px')

with slide("BFS"):
    figure('aulas/img/grafo_simples.png', width=700)

with slide("BFS"):
    code("""
    from collections import deque

    def initialize(dist, graph):
        for i in range(verticies):
            dist[i] = -1

        for i in range(verticies):
            graph[i] = set()
    """, width=500, size='5px')

with slide("BFS"):
    code("""
    def populate(graph, arestas, bi=False):
        for _ in range(arestas):
            v, w = map(int, input().split())
            graph[v].add(w)
            if bi:
                graph[w].add(v)
    """, width=500, size='5px')

with slide("BFS"):
    code("""
    def bfs(start, graph, dist):
	fila = deque()
	dist[start] = 0
	fila.append(start)
	while fila:
		v = fila.popleft()
		for w in graph[v]:
			if dist[i] == -1:
				dist[w] = dist[v] + 1
				fila.append(w)
    """, width=500, size='5px')

with slide("BFS"):
    code("""
    graph, dist = dict(), dict()
    initialize(dist, graph)
    verticies, arestas = map(int, input().split())
    populate(graph, arestas)

    bfs(0)
    print(dist)
    """, width=500, size='5px')

with slide("Exercicios"):
    text("A - Maximum in Table")
    code(open("aulas/aula03/exercicios/maximum_in_table.py").read(), width=400, size='20px')

with slide("Exercicios"):
    text("B - Prison Transfer")
    code(open("aulas/aula03/exercicios/prison_transfer.py").read(), width=400, size='20px')

with slide("Exercicios"):
    text("C - Metro")
    code("""
    from collections import deque

    def initialize(dist, graph, vertices):
        for i in range(vertices):
            dist[i] = -1

        for i in range(vertices):
            graph[i] = set()
    """, width=500, size='20px')


with slide("Exercicios"):
    text("C - Metro")
    code("""
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
    """, width=500, size='20px')


with slide("Exercicios"):
    text("C - Metro")
    code("""
    graph, dist = dict(), dict()
    vertices, final = map(int, input().split())
    initialize(dist, graph, vertices)

    # ida
    estacoes = list(map(int, input().split()))
    for i in range(vertices):
        for j in range(i+1, vertices):
            if estacoes[i] == 1 and estacoes[j] == 1:
                graph[i].add(j)
    """, width=500, size='20px')


with slide("Exercicios"):
    text("C - Metro")
    code("""
    # volta
    estacoes = list(map(int, input().split()))
    for i in range(vertices-1, -1, -1):
        for j in range(i-1, -1, -1):
            if estacoes[i] == 1 and estacoes[j] == 1:
                graph[i].add(j)

    bfs(0, graph, dist)
    print('NO' if dist[final-1] == -1 else 'YES')
    """, width=500, size='20px')


with slide("Exercicios"):
    text("D - Love Triangle")
    code(open("aulas/aula03/exercicios/love_triangle.py").read(), width=400, size='20px')

with slide("Exercicios"):
    text("E - Two Buttons")
    code(open("aulas/aula03/exercicios/two_buttons.py").read(), width=400, size='20px')


save('aulas/aula03/slide.pdf')
