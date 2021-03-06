#!/usr/bin/env python
import networkx as nx
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node(32)
G.add_node(2)
G.add_node(7)
G.add_node(8)
G.add_node(10)
G.add_node(14)
G.add_node(16)
G.add_node(17)
G.add_node(20)
G.add_node(25)
G.add_node(26)
G.add_node(28)

G.add_edge(32,16)
G.add_edge(32,20)
G.add_edge(32,25)
G.add_edge(32,26)
G.add_edge(32,28)
G.add_edge(2,7)
G.add_edge(2,8)
G.add_edge(2,10)
G.add_edge(2,14)
G.add_edge(2,16)
G.add_edge(2,17)
G.add_edge(7,8)
G.add_edge(7,10)
G.add_edge(7,14)
G.add_edge(7,16)
G.add_edge(7,17)
G.add_edge(8,10)
G.add_edge(8,14)
G.add_edge(8,16)
G.add_edge(8,17)
G.add_edge(10,14)
G.add_edge(10,16)
G.add_edge(10,17)
G.add_edge(14,16)
G.add_edge(14,17)
G.add_edge(16,17)
G.add_edge(16,20)
G.add_edge(16,25)
G.add_edge(16,26)
G.add_edge(16,28)
G.add_edge(20,25)
G.add_edge(20,26)
G.add_edge(20,28)
G.add_edge(25,26)
G.add_edge(25,28)
G.add_edge(26,28)

print G.nodes()
print nx.fiedler_vector(G,method='lobpcg')

pos=nx.circular_layout(G,dim=50, scale=100)
plt.clf()
nx.draw(G,with_labels=True)
plt.savefig('C:/Users/Branko/Desktop/FPPNZSSZRUTDAP-UWFZAAFLSA-N_unoriented.png')
