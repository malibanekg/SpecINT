#!/usr/bin/env python
import networkx as nx
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node(1)
G.add_node(5)
G.add_node(6)
G.add_node(8)
G.add_node(10)
G.add_node(12)
G.add_node(17)
G.add_node(19)
G.add_node(23)
G.add_node(24)
G.add_node(26)
G.add_node(28)

G.add_edge(1,5)
G.add_edge(1,6)
G.add_edge(1,8)
G.add_edge(1,10)
G.add_edge(1,12)
G.add_edge(1,17)
G.add_edge(5,6)
G.add_edge(5,8)
G.add_edge(5,10)
G.add_edge(5,12)
G.add_edge(5,17)
G.add_edge(6,8)
G.add_edge(6,10)
G.add_edge(6,12)
G.add_edge(6,17)
G.add_edge(8,10)
G.add_edge(8,12)
G.add_edge(8,17)
G.add_edge(10,12)
G.add_edge(10,17)
G.add_edge(12,17)
G.add_edge(12,19)
G.add_edge(12,23)
G.add_edge(12,24)
G.add_edge(12,26)
G.add_edge(12,28)
G.add_edge(19,23)
G.add_edge(19,24)
G.add_edge(19,26)
G.add_edge(19,28)
G.add_edge(23,24)
G.add_edge(23,26)
G.add_edge(23,28)
G.add_edge(24,26)
G.add_edge(24,28)
G.add_edge(26,28)

print G.nodes()
print nx.fiedler_vector(G,method='lobpcg')

pos=nx.circular_layout(G,dim=50, scale=100)
plt.clf()
nx.draw(G,with_labels=True)
plt.savefig('C:/Users/Branko/Desktop/NJBFOOCLYDNZJN-UHFFFAOYSA-N_unoriented.png')
