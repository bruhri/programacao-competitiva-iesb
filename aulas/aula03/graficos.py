import networkx as nx
import matplotlib.pyplot as plt

def grafo_simples():
    # plt.figure(figsize=(14, 8), dpi=500)
    G = nx.Graph()
    G.add_nodes_from([0,1,2,3,4])
    G.add_edges_from([(1, 2), (0, 3), (1, 4), (3, 4), (0, 2), (4, 2)])
    nx.draw(G, with_labels=True)
    plt.savefig('aulas/img/grafo_simples.png')
    plt.clf()