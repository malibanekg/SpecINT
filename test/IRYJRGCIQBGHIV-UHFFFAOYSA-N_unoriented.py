#!/usr/bin/env python
import networkx as nx
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node(0)
G.add_node(1)
G.add_node(15)
G.add_node(16)
G.add_node(21)
G.add_node(22)
G.add_node(24)
G.add_node(26)
G.add_node(27)
G.add_node(28)
G.add_node(42)
G.add_node(48)
G.add_node(50)

G.add_edge(0,1)
G.add_edge(0,15)
G.add_edge(0,16)
G.add_edge(0,21)
G.add_edge(0,22)
G.add_edge(0,24)
G.add_edge(0,26)
G.add_edge(1,15)
G.add_edge(1,16)
G.add_edge(1,21)
G.add_edge(1,22)
G.add_edge(1,24)
G.add_edge(1,26)
G.add_edge(48,42)
G.add_edge(48,16)
G.add_edge(48,50)
G.add_edge(48,27)
G.add_edge(48,28)
G.add_edge(42,16)
G.add_edge(42,50)
G.add_edge(42,27)
G.add_edge(42,28)
G.add_edge(15,16)
G.add_edge(15,21)
G.add_edge(15,22)
G.add_edge(15,24)
G.add_edge(15,26)
G.add_edge(16,50)
G.add_edge(16,21)
G.add_edge(16,22)
G.add_edge(16,24)
G.add_edge(16,26)
G.add_edge(16,27)
G.add_edge(16,28)
G.add_edge(50,27)
G.add_edge(50,28)
G.add_edge(21,22)
G.add_edge(21,24)
G.add_edge(21,26)
G.add_edge(22,24)
G.add_edge(22,26)
G.add_edge(24,26)
G.add_edge(27,28)

print G.nodes()
print nx.fiedler_vector(G,method='lobpcg')

pos=nx.circular_layout(G,dim=50, scale=100)
plt.clf()
nx.draw(G,with_labels=True)
plt.savefig('C:/Users/Branko/Desktop/IRYJRGCIQBGHIV-UHFFFAOYSA-N_unoriented.png')
