#!/usr/bin/env python
import networkx as nx
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node(0)
G.add_node(1)
G.add_node(4)
G.add_node(44)
G.add_node(12)
G.add_node(20)
G.add_node(22)
G.add_node(23)
G.add_node(24)
G.add_node(25)
G.add_node(28)

G.add_edge(0,1)
G.add_edge(0,4)
G.add_edge(0,12)
G.add_edge(0,20)
G.add_edge(0,22)
G.add_edge(0,23)
G.add_edge(1,4)
G.add_edge(1,12)
G.add_edge(1,20)
G.add_edge(1,22)
G.add_edge(1,23)
G.add_edge(4,12)
G.add_edge(4,20)
G.add_edge(4,22)
G.add_edge(4,23)
G.add_edge(44,24)
G.add_edge(44,25)
G.add_edge(44,28)
G.add_edge(44,12)
G.add_edge(12,20)
G.add_edge(12,22)
G.add_edge(12,23)
G.add_edge(12,24)
G.add_edge(12,25)
G.add_edge(12,28)
G.add_edge(20,22)
G.add_edge(20,23)
G.add_edge(22,23)
G.add_edge(24,28)
G.add_edge(24,25)
G.add_edge(25,28)

print G.nodes()
print nx.fiedler_vector(G,method='lobpcg')

pos=nx.circular_layout(G,dim=50, scale=100)
plt.clf()
nx.draw(G,with_labels=True)
plt.savefig('/home/marija/Desktop/IHUNBGSDBOWDMA-AQFIFDHZSA-N_unoriented.png')
