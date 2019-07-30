import sys

from beampy import *

doc = document(theme="maratonaiesb")

with slide():
    maketitle(lesson='Aula 03', author='Rodrigo G. Araújo',  date='30/07/2019')

with slide("Two Pointers"):
    pass

with slide("Two Pointers"):
    pass

with slide("Soma de Prefixo 1D"):
    pass

with slide("Soma de Prefixo 1D"):
    pass


# with slide("Exercicios"):
#     text("A - Maximum in Table")
#     code(open("aulas/aula03/exercicios/maximum_in_table.py").read(), width=400, size='20px')

save('aulas/aula04/slide.pdf')
