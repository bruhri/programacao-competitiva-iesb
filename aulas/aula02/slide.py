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
    




save('aulas/aula02/slide.pdf')
