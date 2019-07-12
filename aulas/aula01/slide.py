"""
ComplicatedBlue
===============
Redefine title page with new arguments and a page layout with add a progress
bar and slide numbers.
.. raw:: html
   <iframe src="../_static/theme_html_outputs/complicatedblue.html" width="100%" height="500px"></iframe>
"""

import sys

from beampy import slide, document, maketitle, text, save, box, itemize, group, bottom, figure
from bokeh.plotting import figure as bokfig, show

doc = document(theme="maratonaiesb", quiet=True)

#TODO add citation pattern to maratonaiesb theme

with slide():
    maketitle(lesson='Aula 01', author='Rodrigo G. Araújo',  date='24/07/2019')

with slide('Programação Competitiva'):
    with group(x='center', y='auto', width=400) as g1:
        text('Resolver problemas de Ciência da Computação conhecidos, o mais rápido possível.')
        text(r'Steven \& Felix Halim (2010)', y='+1cm', size=17, color='#F6B801')

with slide('Programação Competitiva'):
    with group(x=0.15, y='auto', width=400) as g2:
        itemize(['Todos os problemas contem souluções existentes',
            'A velocidade caracteriza a competição',
            'Formar profissionais capazes de produzir softwares de qualidade',
            'Trabalho em equipe'
            ], width=600)

with slide('Programação Competitiva'):
    with group(x='center', y='auto', width=400) as g1:
        text('''Competitive programming combines two topics: (1) the design of algorithms and 
                    (2) the implementation of algothms''')
        text(r'Antti Laaksonen (2018)', y='+1cm', size=17, color='#F6B801')
        
with slide('Programação Competitiva'):
    with group(x=0.15, y='auto', width=400) as g2:
        itemize(['Resolução de problemas e pensamento matemático',
            'Combinação de técnicas conhecidas',
            'Navas interpretações de técnicas',
            'Habilidade em programação',
            ], width=600)

with slide('Regras da Maratona'):
    with group(x='center', y='auto', width=400) as g1:
        text('ACM ICPC', size=40)

    with group(x=0.15, y='auto', width=400) as g2:
        itemize(['Sub-Regional (14/09 - Centro Universitário IESB)',
            'Regional (07/11 - Campina Grande)',
            'Mundial (TDB)',
            'Equipes de três alunos, um reserva e um coach',
            '8 a 14 problemas em 5 horas',
            ], width=600)

with slide('Regras da Maratona'):
    with group(x='center', y='auto', width=400) as g1:
        text('Critérios de Vitória', size=40)

    with group(x=0.15, y='auto', width=400) as g2:
        itemize(['Maior número de problemas',
            'Menot tempo total na subimissão de soluções',
            'O tempo de subimissão é o tempo transcorrido até o momento na competição',
            'Cada subimissão incorreta antes de acertar gera uma penalidade de 20 minutos',
            'O tempo total é a soma dos tempos de submissão acressido das penalidades',
            ], width=600)

with slide('Campeões Mundiais'):
    times = ['USA', 'Russia', 'China', 'Polônia', 'Canadá', 'República Checha', 'Alemanha', 'Australia', 'Nova Zelândia']
    titulos = [17, 14, 4, 2, 2, 1, 1, 1, 1]
    grafico = bokfig(height=400, width=600, x_range=times)
    grafico.vbar(x=times, top=titulos, width=0.9)
    figure(grafico, width=600)
    text("Brasil conseguiu 13º lugar no mundial em 2005 com a USP")

with slide('Campeões Brasileiros'):
    text('Gráfico com campeões brasiliros')
    text('Brasília conseguiu o 2º lugar em 1996')

with slide('Campeões no DF'):
    text('Gráfico com campeões DF')
    text('IESB conseguiu o 5º lugar em 2017')

with slide('Referências'):
    with group(x=0.05, y='auto', width=400) as g2:
        itemize([
                r'https://pt.wikipedia.org/wiki/ACM\_International\_Collegiate\_Programming\_Contest',
                r'http://maratona.ime.usp.br/',
                'https://icpc.baylor.edu/',
                'https://github.com/edsomjr/TEP/',
                "Laaksonen, Antti. Competitive Programmer's Handbook, 2018",
                "Halim, Felix; Halim, Steve. Competitive Programming 3, 2010",
                ], width=700)

save('aulas/aula01/slide.html')
save('aulas/aula01/slide.pdf')
