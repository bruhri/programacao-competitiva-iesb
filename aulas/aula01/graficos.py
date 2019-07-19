import matplotlib.pyplot as plt


def campeoes_brasileiros():
    plt.figure(figsize=(10, 8), dpi=500)
    times = ['UNICAMP', 'PUC-RJ', 'UFPE', 'FURG', 'USP', 'ITA']
    titulos = [3, 2, 9, 1, 5, 3]
    plt.bar(x=times, height=titulos, width=0.9)
    plt.savefig('aulas/img/campeoes_brasileiros.png')
    plt.clf()

def campeoes_mudiais():
    plt.figure(figsize=(14, 8), dpi=500)
    times = ['USA', 'Russia', 'China', 'Polônia', 'Canadá', 'República Checha', 'Alemanha', 'Australia', 'Nova Zelândia']
    titulos = [17, 14, 4, 2, 2, 1, 1, 1, 1]
    plt.bar(x=times, height=titulos, width=0.9)
    plt.savefig('aulas/img/campeoes_mundiais.png')
    plt.clf()
