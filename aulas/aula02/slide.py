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

with slide("Exercicios"):
    text("A - A and B and Compilation Errors")
    code(open('aulas/aula02/exercicios/01.py').read(), width=500, size='20px')

with slide("Exercicios"):
    text("B - Snacktower")
    code("""
    from queue import PriorityQueue


    def get_na_fila(show_snack, maior):
        while True:
            if fila_preferencia.empty():
                break

            snack = -1*fila_preferencia.get()
            if snack == maior:
                show_snack.append(snack)
                maior -= 1
            else:
                fila_preferencia.put(-1*snack)
                break
        return maior
    """, width=500, size='20px')

with slide("Exercicios"):
    text("B - Snacktower")
    code("""
    maior = int(input())
    snacks = map(int, input().split())
    fila_preferencia, show_snack = PriorityQueue(), list()


    for snack in snacks:    
        if snack == maior:
            show_snack.append(snack)
            maior -= 1
            maior = get_na_fila(show_snack, maior)
            print(*show_snack)
            show_snack = list()
        else:
            fila_preferencia.put(-1*snack)
            print()
    """, width=500, size='20px')

with slide("Exercicios"):
    text("C - Sushi for Two")
    code(open('aulas/aula02/exercicios/03.py').read(), width=500, size='20px')

with slide("Exercicios"):
    text("D - Sport Mafia")
    code(open('aulas/aula02/exercicios/04.py').read(), width=500, size='20px')

with slide("Exercicios"):
    text("E - Planning The Expedition")
    code(open('aulas/aula02/exercicios/05.py').read(), width=500, size='20px')


save('aulas/aula02/slide.pdf')
