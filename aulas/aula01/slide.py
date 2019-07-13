"""
ComplicatedBlue
===============
Redefine title page with new arguments and a page layout with add a progress
bar and slide numbers.
.. raw:: html
   <iframe src="../_static/theme_html_outputs/complicatedblue.html" width="100%" height="500px"></iframe>
"""

import sys

from beampy import *
from bokeh.plotting import figure as bokfig, show

doc = document(theme="maratonaiesb")

with slide():
    maketitle(lesson='Aula 01', author='Rodrigo G. Araújo',  date='24/07/2019')

with slide('Programação Competitiva 01/04'):
    with group(x='center', y='auto', width=400) as g1:
        text('Resolver problemas de Ciência da Computação conhecidos, o mais rápido possível.')
        text(r'Steven \& Felix Halim (2010)', y='+1cm', size=17, color='#F6B801')

with slide('Programação Competitiva 02/04'):
    with group(x=0.15, y='auto', width=400) as g2:
        itemize(['Todos os problemas contem souluções existentes',
            'A velocidade caracteriza a competição',
            'Formar profissionais capazes de produzir softwares de qualidade',
            'Trabalho em equipe'
            ], width=600)

with slide('Programação Competitiva 03/04'):
    with group(x='center', y='auto', width=400) as g1:
        text('''Competitive programming combines two topics: (1) the design of algorithms and 
                    (2) the implementation of algothms''')
        text(r'Antti Laaksonen (2018)', y='+1cm', size=17, color='#F6B801')
        
with slide('Programação Competitiva 04/04'):
    with group(x=0.15, y='auto', width=400) as g2:
        itemize(['Resolução de problemas e pensamento matemático',
            'Combinação de técnicas conhecidas',
            'Navas interpretações de técnicas',
            'Habilidade em programação',
            ], width=600)

with slide('Regras da Maratona 01/02'):
    with group(x='center', y='auto', width=400) as g1:
        text('ACM ICPC', size=40)

    with group(x=0.15, y='auto', width=400) as g2:
        itemize(['Sub-Regional (14/09 - Centro Universitário IESB)',
            'Regional (07/11 - Campina Grande)',
            'Mundial (TDB)',
            'Equipes de três alunos, um reserva e um coach',
            '8 a 14 problemas em 5 horas',
            ], width=600)

with slide('Regras da Maratona 02/02'):
    with group(x='center', y='auto', width=400) as g1:
        text('Critérios de Vitória', size=40)

    with group(x=0.15, y='auto', width=400) as g2:
        itemize(['Maior número de problemas',
            'Menor tempo total na subimissão de soluções',
            'O tempo de subimissão é o tempo transcorrido até o momento na competição',
            'Cada subimissão incorreta antes de acertar gera uma penalidade de 20 minutos',
            'O tempo total é a soma dos tempos de submissão acressido das penalidades',
            'Cada problema tem uma cor, e é entregue um balão ao acertar'
            ], width=600)

with slide('Campeões Mundiais'):
    times = ['USA', 'Russia', 'China', 'Polônia', 'Canadá', 'República Checha', 'Alemanha', 'Australia', 'Nova Zelândia']
    titulos = [17, 14, 4, 2, 2, 1, 1, 1, 1]
    grafico = bokfig(height=400, width=600, x_range=times)
    grafico.vbar(x=times, top=titulos, width=0.9)
    figure(grafico, width=600)
    text("Brasil conseguiu 13º lugar no mundial em 2005 com a USP")

with slide('Campeões Brasileiros'):
    times = ['UNICAMP', 'PUC-RJ', 'UFPE', 'FURG', 'USP', 'ITA']
    titulos = [3, 2, 9, 1, 5, 3]
    grafico = bokfig(height=400, width=600, x_range=times)
    grafico.vbar(x=times, top=titulos, width=0.9)
    figure(grafico, width=600)
    text('Brasília (UNB) conseguiu o 2º lugar em 1996')

with slide('IESB nas Maratonas'):
    itemize(['2016 - 11º Lugar - 3 Balões - Programação Orientada a Cebola',
            '2017 - 7º Lugar - 5 Balões - Programação Orientada a Cebola',
            '2018 - 9º Lugar - 3 Balões - DevLabs',
            ], width=600)
    text('UNB CIC e UNB FGA disputam a primeira posição todos os anos.')

with slide('Juizes Online 01/02'):
    text("URI - Iniciantes")
    figure('aulas/img/uri.png', width=300)
    text("Codeforces - Intermediário/Avançado")
    figure('aulas/img/codeforces.png', width=300)

with slide('Juizes Online 02/02'):
    text("Cada solução submetida ao juiz retornará um feedback sobre a solução")
    text("As linguagens aceitas na Maratona de Programação SBC são: C, C++, Java e Python")
    with group(x='auto', width=800) as g0:
        with group(width='50%', x=g0.left+0, y=g0.bottom+bottom(0)) as g1:
            figure('aulas/img/resposta_juiz_2.png', width=400)
        with group(width='50%', x=g1.right+0, y=g1.top+0) as g2:
            figure('aulas/img/resposta_juiz_1.png', width=400)
    text("Imagens obtidas de https://github.com/edsomjr/TEP/", size=10, x=document._height*0.8)

with slide('Entrada e Saída 01/05'):
    with group(x='center', y='auto', width=700) as g1:
        text("""A programação competitiva requer que os problemas sejam 
            solucionados lendo arquivos de entrada especificos e escrevendo a saída
            em um arquivo da forma solicitada. Os arquivos em sua maioria são
            obtivos pela entrada e sáida padrão.""")
        text("Os arquivos de entrada são divididos em quatro tipos:")
        itemize([
            'Um único caso do problema',
            'N casos do problema, com o valor de N informado na primeira linha',
            'N casos do problema, acabando com um valor informado',
            'M casos do problema, até que acabe o arquivo (EOF)'    
        ], item_style='number')

with slide('Entrada e Saída 02/05'):
    # text("Categoria 1: Um único caso do problema")
    # with group(x='auto', y='auto', height=300, width=300, background='#f0f0f5') as g2:
    #     with group(background='#b3b3cc', width=300, height=50, y=g2.top) as g21:
    #         text("Arquivo de Entrada")
    #     with group(background='#f0f0f5') as g22:
    #         text("X Y", x=g2.left, y=g2.top+60)

    # with group(x='auto', y=g2.top+0, height=300, width=300) as g3:
    code("""
    from pylab import *

    n = range(10)

    plot(n, n*random.rand(), 'ko')

    for i in range(10):
        print(i)

    """, width=500)

save('aulas/aula01/slide.html')
# save('aulas/aula01/slide.pdf')
