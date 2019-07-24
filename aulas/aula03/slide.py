import sys

from beampy import *

doc = document(theme="maratonaiesb")

with slide():
    maketitle(lesson='Aula 03', author='Rodrigo G. Araújo',  date='26/07/2019')

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

# with slide("BFS"):
#     code(open().read(), width=600)

# with slide("Problema Simples"): É POSSIVEL CHEGAR DE Y A Z?
#     code(open().read(), width=600)

# with slide("Dijkstra"):
#     code(open().read(), width=600)

# with slide("Problema Simples"): QUAL MENOR DISTÂNCIA DE Y A Z?
#     code(open().read(), width=600)


# with slide("Exercicios"):
#     text("A - A and B and Compilation Errors")
#     code(open('aulas/aula02/exercicios/01.py').read(), width=500, size='20px')



save('aulas/aula03/slide.pdf')
