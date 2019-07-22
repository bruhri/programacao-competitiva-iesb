import sys

from beampy import *
from graficos import campeoes_brasileiros

doc = document(theme="maratonaiesb")

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
            'Menor tempo total na subimissão de soluções',
            'O tempo de subimissão é o tempo transcorrido até o momento na competição',
            'Cada subimissão incorreta antes de acertar gera uma penalidade de 20 minutos',
            'O tempo total é a soma dos tempos de submissão acressido das penalidades',
            'Cada problema tem uma cor, e é entregue um balão ao acertar'
            ], width=600)

with slide('Campeões Mundiais'):
    figure('aulas/img/campeoes_mundiais.png', width=700)
    text("Brasil conseguiu 13º lugar no mundial em 2005 com a USP")

with slide('Campeões Brasileiros'):
    figure('aulas/img/campeoes_brasileiros.png', width=600)
    text('Brasília (UNB) conseguiu o 2º lugar em 1996')

with slide('IESB nas Maratonas'):
    itemize(['2016 - 11º Lugar - 3 Balões - Programação Orientada a Cebola',
            '2017 - 7º Lugar - 5 Balões - Programação Orientada a Cebola',
            '2018 - 9º Lugar - 3 Balões - DevLabs',
            ], width=600)
    text('UNB CIC e UNB FGA disputam a primeira posição todos os anos.')

with slide('Juizes Online'):
    text("URI - Iniciantes")
    figure('aulas/img/uri.png', width=300)
    text("Codeforces - Intermediário/Avançado")
    figure('aulas/img/codeforces.png', width=300)

with slide('Juizes Online'):
    text("Cada solução submetida ao juiz retornará um feedback sobre a solução")
    text("As linguagens aceitas na Maratona de Programação SBC são: C, C++, Java e Python")
    with group(x='auto', width=800) as g0:
        with group(width='50%', x=g0.left+0, y=g0.bottom+bottom(0)) as g1:
            figure('aulas/img/resposta_juiz_2.png', width=400)
        with group(width='50%', x=g1.right+0, y=g1.top+0) as g2:
            figure('aulas/img/resposta_juiz_1.png', width=400)
    text("Imagens obtidas de https://github.com/edsomjr/TEP/", size=10, x=document._height*0.8)

with slide('Entrada e Saída'):
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

with slide('Entrada e Saída'):
    text("Categoria 1: Um único caso do problema")
    with group(x='auto', y='auto', height=300, width=300, background='#f0f0f5') as g2:
        with group(background='#b3b3cc', width=300, height=50, y=g2.top) as g21:
            text("Arquivo de Entrada")
        with group(background='#f0f0f5') as g22:
            text("X Y", x=g2.left, y=g2.top+60)

    with group(x='auto', y=g2.top+0, height=300, width=300) as g3:
        code(open('aulas/aula01/entrada_tipo_1.py').read(), width=300)


with slide('Entrada e Saída'):
    text("Categoria 2: Varios casos informados no inicio.")
    with group(x='auto', y='auto', height=300, width=300, background='#f0f0f5') as g2:
        with group(background='#b3b3cc', width=300, height=50, y=g2.top) as g21:
            text("Arquivo de Entrada")
        with group(background='#f0f0f5') as g22:
            text("QTD", x=g2.left, y=g2.top+60)
            text("X Y", x=g2.left, y=g2.top+100)

    with group(x='auto', y=g2.top+0, height=300, width=300) as g3:
        code(open('aulas/aula01/entrada_tipo_2.py').read(), width=300)


with slide('Entrada e Saída'):
    text("Categoria 2: Varios casos acabando com um valor.")
    with group(x='auto', y='auto', height=300, width=300, background='#f0f0f5') as g2:
        with group(background='#b3b3cc', width=300, height=50, y=g2.top) as g21:
            text("Arquivo de Entrada")
        with group(background='#f0f0f5') as g22:
            text("X Y", x=g2.left, y=g2.top+40)
            text("X Y", x=g2.left, y=g2.top+80)
            text("X Y", x=g2.left, y=g2.top+120)
            text("-1 -1", x=g2.left, y=g2.top+160)

    with group(x='auto', y=g2.top+0, height=300, width=300) as g3:
        code(open('aulas/aula01/entrada_tipo_3.py').read(), width=300)


with slide('Entrada e Saída'):
    text("Categoria 2: Varios casos até o fim de arquivo.")
    with group(x='auto', y='auto', height=300, width=300, background='#f0f0f5') as g2:
        with group(background='#b3b3cc', width=300, height=50, y=g2.top) as g21:
            text("Arquivo de Entrada")
        with group(background='#f0f0f5') as g22:
            text("X Y", x=g2.left, y=g2.top+40)
            text("X Y", x=g2.left, y=g2.top+80)
            text("X Y", x=g2.left, y=g2.top+120)
            text("X Y", x=g2.left, y=g2.top+160)

    with group(x='auto', y=g2.top+0, height=300, width=300) as g3:
        code(open('aulas/aula01/entrada_tipo_4.py').read(), width=300)


with slide("Categorização de problemas"):
    itemize(
        ['Ad-Hoc', 'Busca Completa', 'Dividir e Conquista', 'Gulosos', 'Prorgramação Dinâmica',
        'Grafos', 'Matemática', 'Geometrica Computacional', 'Estrutura de Dados']
    )

with slide("Classificação Pessoal"):
    itemize([
        'A - Já resolvi um parecido e posso resolver de novo rapidamente',
        'B - Já vi um parecido e sei que não consigo resolver',
        'C - Nunca vi'
    ])
    text("Divida a classificação entre a equipe, deixe somente um, no máximo dois no computador")

with slide("Execicios"):
    text("https://codeforces.com/group/uZDbxesr6A/contests")

with slide("Exercicios"):
    text("A - Bit++")
    code(open('aulas/aula01/exercicios/bit++.py').read(), width=500, size='20px')

with slide("Exercicios"):
    text("B - Beautiful Matrix")
    code(open('aulas/aula01/exercicios/beautiful_matrix.py').read(), width=500, size='20px')

with slide("Exercicios"):
    text("C - Stones on the Table")
    code(open('aulas/aula01/exercicios/stones_on_the_table.py').read(), width=500, size='20px')

with slide("Exercicios"):
    text("D - Word")
    code(open('aulas/aula01/exercicios/word.py').read(), width=500, size='20px')

with slide("Exercicios"):
    text("E - Fox And Snake")
    code(open('aulas/aula01/exercicios/fox_and_snake.py').read(), width=500, size='20px')


save('aulas/aula01/slide.pdf')
