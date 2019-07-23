import sys

from beampy import *

doc = document(theme="maratonaiesb")

with slide():
    maketitle(lesson='Aula 02', author='Rodrigo G. Araújo',  date='25/07/2019')

with slide('Big O'):
    with group(x='center', y='auto', width=500) as g1:
        text("""No pior caso da execução deste algoritmo, o número de operações realizado será 
            proporcional a N, e por simplicidade, eliminamos constantes e fatores não dominantes.""")
        text("""A quantidade de operações por segundo que podem ser executadas em um problema de maratona
            está por volta de $10^8$ e a memória maxima $10^6$""")
    
with slide("O(1)"):
    with group(x='center', y='auto', width=500) as g1:
        code(open('aulas/aula02/o_1.py').read(), width=500, size='20px')

with slide("$O(N)$ e $O(N^2)$"):
    with group(x='center', y='auto', width=500) as g1:
        code(open('aulas/aula02/o_n.py').read(), width=500, size='20px')

with slide("Busca Binária"):
    with group(x='center', y='auto', width=500) as g1:
        text("$O(log N)$")
        code(open('aulas/aula02/busca_binaria.py').read(), width=500, size='20px')

with slide("Pilha"):
    with group(x='center', y='auto', width=500) as g1:
        code(open('aulas/aula02/pilha.py').read(), width=500, size='20px')

with slide("Fila"):
    with group(x='center', y='auto', width=500) as g1:
        code(open('aulas/aula02/fila.py').read(), width=500, size='20px')

with slide("Dicionário"):
    with group(x='center', y='auto', width=500) as g1:
        code(open('aulas/aula02/dicionario.py').read(), width=500, size='20px')


save('aulas/aula02/slide.pdf')
