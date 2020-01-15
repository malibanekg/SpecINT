#!/usr/bin/env python
import networkx as nx
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node(0)
G.add_node(49)
G.add_node(10)
G.add_node(44)
G.add_node(17)
G.add_node(50)
G.add_node(22)
G.add_node(23)
G.add_node(24)
G.add_node(25)
G.add_node(26)
G.add_node(27)

G.add_edge(0,10)
G.add_edge(0,17)
G.add_edge(0,22)
G.add_edge(0,23)
G.add_edge(0,24)
G.add_edge(0,25)
G.add_edge(0,26)
G.add_edge(49,50)
G.add_edge(49,27)
G.add_edge(49,44)
G.add_edge(49,10)
G.add_edge(10,44)
G.add_edge(10,17)
G.add_edge(10,50)
G.add_edge(10,22)
G.add_edge(10,23)
G.add_edge(10,24)
G.add_edge(10,25)
G.add_edge(10,26)
G.add_edge(10,27)
G.add_edge(44,50)
G.add_edge(44,27)
G.add_edge(17,22)
G.add_edge(17,23)
G.add_edge(17,24)
G.add_edge(17,25)
G.add_edge(17,26)
G.add_edge(50,27)
G.add_edge(22,23)
G.add_edge(22,24)
G.add_edge(22,25)
G.add_edge(22,26)
G.add_edge(23,24)
G.add_edge(23,25)
G.add_edge(23,26)
G.add_edge(24,25)
G.add_edge(24,26)
G.add_edge(25,26)

print G.nodes()
print nx.fiedler_vector(G,method='lobpcg')

pos=nx.circular_layout(G,dim=50, scale=100)
plt.clf()
nx.draw(G,with_labels=True)
plt.savefig('C:/Users/Branko/Desktop/PMATZTZNYRCHOR-CGLBZJNRSA-N_unoriented.png')
