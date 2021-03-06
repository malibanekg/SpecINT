#!/usr/bin/env python
import networkx as nx
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node(2)
G.add_node(4)
G.add_node(7)
G.add_node(10)
G.add_node(14)
G.add_node(15)
G.add_node(20)
G.add_node(21)
G.add_node(22)
G.add_node(23)
G.add_node(24)
G.add_node(27)
G.add_node(29)
G.add_node(35)
G.add_node(38)

G.add_edge(2,4)
G.add_edge(2,7)
G.add_edge(2,10)
G.add_edge(2,14)
G.add_edge(2,15)
G.add_edge(2,20)
G.add_edge(2,21)
G.add_edge(2,22)
G.add_edge(35,38)
G.add_edge(35,14)
G.add_edge(35,23)
G.add_edge(35,24)
G.add_edge(35,27)
G.add_edge(35,29)
G.add_edge(4,7)
G.add_edge(4,10)
G.add_edge(4,14)
G.add_edge(4,15)
G.add_edge(4,20)
G.add_edge(4,21)
G.add_edge(4,22)
G.add_edge(38,14)
G.add_edge(38,23)
G.add_edge(38,24)
G.add_edge(38,27)
G.add_edge(38,29)
G.add_edge(7,10)
G.add_edge(7,14)
G.add_edge(7,15)
G.add_edge(7,20)
G.add_edge(7,21)
G.add_edge(7,22)
G.add_edge(10,14)
G.add_edge(10,15)
G.add_edge(10,20)
G.add_edge(10,21)
G.add_edge(10,22)
G.add_edge(14,15)
G.add_edge(14,20)
G.add_edge(14,21)
G.add_edge(14,22)
G.add_edge(14,23)
G.add_edge(14,24)
G.add_edge(14,27)
G.add_edge(14,29)
G.add_edge(15,20)
G.add_edge(15,21)
G.add_edge(15,22)
G.add_edge(20,21)
G.add_edge(20,22)
G.add_edge(21,22)
G.add_edge(23,24)
G.add_edge(23,27)
G.add_edge(23,29)
G.add_edge(24,27)
G.add_edge(24,29)
G.add_edge(27,29)

print G.nodes()
print nx.fiedler_vector(G,method='lobpcg')

pos=nx.circular_layout(G,dim=50, scale=100)
plt.clf()
nx.draw(G,with_labels=True)
plt.savefig('C:/Users/Branko/Desktop/WZPBZJONDBGPKJ-VEHQQRBSSA-N_unoriented.png')
